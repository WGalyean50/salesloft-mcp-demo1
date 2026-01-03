"""MCP Server for Salesloft call transcript analysis."""

from __future__ import annotations

import json
import logging
import os
from pathlib import Path

from mcp.server.fastmcp import FastMCP

from .search import search_transcripts
from .transcript_loader import Transcript, get_transcript_by_id, load_all_transcripts

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP("salesloft-transcripts")

# Cache for transcripts (loaded once at startup)
_transcripts_cache: list[Transcript] | None = None


def _get_transcripts_dir() -> Path:
    """Get the transcripts directory path."""
    # Check environment variable first
    env_path = os.environ.get("SALESLOFT_TRANSCRIPTS_DIR")
    if env_path:
        return Path(env_path)

    # Default to ./transcripts relative to current working directory
    return Path.cwd() / "transcripts"


def _get_transcripts() -> list[Transcript]:
    """Get cached transcripts, loading if necessary."""
    global _transcripts_cache
    if _transcripts_cache is None:
        _transcripts_cache = load_all_transcripts(_get_transcripts_dir())
        logger.info(f"Loaded {len(_transcripts_cache)} transcripts")
    return _transcripts_cache


# =============================================================================
# MCP Tools
# =============================================================================


@mcp.tool()
async def list_calls(
    company: str | None = None,
    deal_stage: str | None = None,
    limit: int = 50,
) -> str:
    """List available call transcripts with optional filtering.

    Args:
        company: Filter by company name (partial match, case-insensitive)
        deal_stage: Filter by deal stage (Discovery, Demo, Negotiation, etc.)
        limit: Maximum results to return (default: 50, max: 100)

    Returns:
        JSON array of call summaries with metadata
    """
    # Enforce limit bounds
    limit = min(max(1, limit), 100)

    transcripts = _get_transcripts()
    results = []

    for transcript in transcripts:
        # Apply company filter (case-insensitive partial match)
        if company:
            company_lower = company.lower()
            if (
                company_lower not in transcript.prospect_company.lower()
                and company_lower not in transcript.prospect_name.lower()
            ):
                continue

        # Apply deal_stage filter (case-insensitive exact match)
        if deal_stage:
            if transcript.deal_stage.lower() != deal_stage.lower():
                continue

        results.append(transcript.to_summary())

        if len(results) >= limit:
            break

    return json.dumps(results, indent=2)


@mcp.tool()
async def get_call(call_id: str) -> str:
    """Get the full transcript content for a specific call.

    Args:
        call_id: The unique identifier for the call

    Returns:
        Full transcript content including metadata and transcript text
    """
    transcripts = _get_transcripts()

    for transcript in transcripts:
        if transcript.call_id == call_id:
            return json.dumps(transcript.to_full(), indent=2)

    return json.dumps({"error": f"Call not found: {call_id}"})


@mcp.tool()
async def search_calls(query: str, limit: int = 10) -> str:
    """Search for keywords across all call transcripts.

    Args:
        query: Search terms (case-insensitive, searches all transcript content)
        limit: Maximum excerpts to return (default: 10, max: 50)

    Returns:
        JSON array of matching excerpts with call context
    """
    # Enforce limit bounds
    limit = min(max(1, limit), 50)

    transcripts = _get_transcripts()
    results = search_transcripts(transcripts, query, limit)

    return json.dumps([r.to_dict() for r in results], indent=2)


# =============================================================================
# MCP Resources
# =============================================================================


@mcp.resource("transcripts://list")
async def list_all_transcripts() -> str:
    """Get a complete list of all available call transcripts.

    Returns:
        JSON array of all call metadata
    """
    transcripts = _get_transcripts()
    return json.dumps([t.to_summary() for t in transcripts], indent=2)


@mcp.resource("transcripts://call/{call_id}")
async def get_transcript_resource(call_id: str) -> str:
    """Get the full content of a specific transcript.

    Args:
        call_id: The unique identifier for the call

    Returns:
        Full transcript content
    """
    transcripts = _get_transcripts()

    for transcript in transcripts:
        if transcript.call_id == call_id:
            return transcript.content

    return f"Error: Call not found: {call_id}"


# =============================================================================
# Entry Point
# =============================================================================


def main():
    """Entry point for the MCP server."""
    logger.info("Starting Salesloft MCP server...")
    mcp.run()


if __name__ == "__main__":
    main()
