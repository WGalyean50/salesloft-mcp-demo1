"""Transcript loading and parsing utilities."""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import frontmatter

logger = logging.getLogger(__name__)


@dataclass
class Transcript:
    """Represents a loaded call transcript."""

    call_id: str
    date: str
    duration_seconds: int
    rep_name: str
    prospect_name: str
    prospect_company: str
    prospect_title: str = ""
    deal_stage: str = "Discovery"
    deal_value: int | None = None
    disposition: str = ""
    tags: list[str] = field(default_factory=list)
    key_themes: list[str] = field(default_factory=list)
    content: str = ""
    file_path: str = ""

    def to_summary(self) -> dict[str, Any]:
        """Return summary dict for list_calls responses."""
        return {
            "call_id": self.call_id,
            "date": self.date,
            "duration_seconds": self.duration_seconds,
            "rep_name": self.rep_name,
            "prospect_name": self.prospect_name,
            "prospect_company": self.prospect_company,
            "deal_stage": self.deal_stage,
            "deal_value": self.deal_value,
            "disposition": self.disposition,
            "tags": self.tags,
        }

    def to_full(self) -> dict[str, Any]:
        """Return full transcript dict for get_call responses."""
        return {
            "call_id": self.call_id,
            "date": self.date,
            "duration_seconds": self.duration_seconds,
            "rep_name": self.rep_name,
            "prospect_name": self.prospect_name,
            "prospect_company": self.prospect_company,
            "prospect_title": self.prospect_title,
            "deal_stage": self.deal_stage,
            "deal_value": self.deal_value,
            "disposition": self.disposition,
            "tags": self.tags,
            "key_themes": self.key_themes,
            "content": self.content,
        }


def _generate_call_id(file_path: Path) -> str:
    """Generate call_id from filename."""
    # Remove .md extension and convert to lowercase
    return file_path.stem.lower().replace(" ", "_")


def _parse_duration(duration_str: str) -> int:
    """Parse duration string to seconds.

    Handles formats like:
    - "30 minutes"
    - "1 hour 30 minutes"
    - "32 min"
    - "1:30:00"
    - "45:00"
    """
    if not duration_str:
        return 0

    duration_str = duration_str.lower().strip()

    # Try HH:MM:SS or MM:SS format
    if ":" in duration_str:
        parts = duration_str.split(":")
        if len(parts) == 3:
            hours, mins, secs = map(int, parts)
            return hours * 3600 + mins * 60 + secs
        elif len(parts) == 2:
            mins, secs = map(int, parts)
            return mins * 60 + secs

    # Try "X minutes" or "X min" format
    minutes_match = re.search(r"(\d+)\s*(?:minutes?|mins?)", duration_str)
    hours_match = re.search(r"(\d+)\s*(?:hours?|hrs?)", duration_str)

    total_seconds = 0
    if hours_match:
        total_seconds += int(hours_match.group(1)) * 3600
    if minutes_match:
        total_seconds += int(minutes_match.group(1)) * 60

    return total_seconds


def _parse_date(date_str: str) -> str:
    """Parse date string to ISO format or return as-is if already formatted."""
    if not date_str:
        return ""

    # If already in ISO format, return as-is
    if "T" in date_str and "Z" in date_str:
        return date_str

    # Common date formats to try to normalize
    # For now, just clean up and return - could add dateutil.parser later
    return date_str.strip()


def _extract_metadata_from_markdown(content: str) -> dict[str, Any]:
    """Extract metadata from markdown content when no YAML frontmatter exists.

    Looks for patterns like:
    - **Date:** January 2, 2026
    - **Duration:** 30 minutes
    - **Participants:** or **Interviewer:**/**Interviewee:**
    - Company names in headers or metadata
    """
    metadata: dict[str, Any] = {}

    # Extract date
    date_match = re.search(r"\*\*Date:\*\*\s*(.+?)(?:\n|$)", content)
    if date_match:
        metadata["date"] = _parse_date(date_match.group(1).strip())

    # Extract duration
    duration_match = re.search(r"\*\*Duration:\*\*\s*(.+?)(?:\n|$)", content)
    if duration_match:
        metadata["duration_seconds"] = _parse_duration(duration_match.group(1))

    # Extract interviewer/rep (multiple patterns)
    rep_patterns = [
        r"\*\*Interviewer:\*\*\s*(.+?)(?:,|$|\n)",
        r"-\s*(.+?),\s*(?:Enterprise|Senior|Sales|VP|Director)",
        r"\[SALESLOFT REP\]",  # Placeholder, will use from participants
    ]

    for pattern in rep_patterns:
        match = re.search(pattern, content)
        if match and pattern != r"\[SALESLOFT REP\]":
            # Extract just the name part
            rep_name = match.group(1).strip()
            # Remove titles and company info
            rep_name = re.sub(r",.*$", "", rep_name).strip()
            metadata["rep_name"] = rep_name
            break

    if "rep_name" not in metadata:
        # Try to find rep in Participants section
        participants_match = re.search(
            r"\*\*Participants:\*\*\s*((?:.*\n)*?)(?:\n\n|\*\*|---)", content
        )
        if participants_match:
            participants_text = participants_match.group(1)
            # Look for Salesloft mentions
            salesloft_match = re.search(
                r"-\s*(.+?),\s*(?:.*?Salesloft|Enterprise.*?Director)",
                participants_text,
            )
            if salesloft_match:
                metadata["rep_name"] = salesloft_match.group(1).strip()

    # Extract interviewee/prospect
    interviewee_patterns = [
        r"\*\*Interviewee:\*\*\s*(.+?)(?:,|\(|$|\n)",
        r"#.*?Interview.*?:\s*(.+?)(?:,|-|\n|$)",
        r"#.*?Customer Interview:\s*(.+?)(?:,|\n|$)",
    ]

    for pattern in interviewee_patterns:
        match = re.search(pattern, content)
        if match:
            prospect_name = match.group(1).strip()
            # Clean up the name
            prospect_name = re.sub(r"\s*[,\-].*$", "", prospect_name).strip()
            metadata["prospect_name"] = prospect_name
            break

    # Try to extract prospect title
    title_match = re.search(
        r"(?:Interviewee|" + re.escape(metadata.get("prospect_name", "")) + r").*?(?:,\s*)(.+?)(?:\n|$)",
        content,
    )
    if title_match:
        title = title_match.group(1).strip()
        # Extract title - look for CRO, VP, Director, etc.
        title_type_match = re.search(
            r"(CRO|Chief Revenue Officer|VP\s+\w+|Vice President.*?|Director.*?)(?:,|$|\()",
            title,
            re.IGNORECASE,
        )
        if title_type_match:
            metadata["prospect_title"] = title_type_match.group(1).strip()

    # Extract company name
    company_patterns = [
        r"\*\*Interviewee:\*\*.*?,\s*(?:VP\s+\w+|CRO|Director.*?),\s*(.+?)(?:\n|\(|$)",
        r"\*\*Company.*?:\*\*\s*(.+?)(?:\n|$)",
        r"#.*?Interview.*?:\s*.+?\s*[-–]\s*(.+?)(?:\n|$)",
        r"\(\$?\d+M?\s*ARR.*?(?:,|\)|\n)",  # Look for ARR mentions
    ]

    for pattern in company_patterns:
        match = re.search(pattern, content)
        if match:
            company = match.group(1).strip() if match.lastindex else ""
            # Clean up company name
            company = re.sub(r"\s*\(.*\).*$", "", company).strip()
            company = re.sub(r"\s*,.*$", "", company).strip()
            if company and len(company) > 2:
                metadata["prospect_company"] = company
                break

    # Extract from header format: "# Customer Interview: Name, Title"
    header_match = re.search(
        r"#\s*(?:Customer\s+)?Interview:\s*(.+?),\s*(CRO|VP.*?|Chief.*?)(?:\n|$)",
        content,
    )
    if header_match:
        if "prospect_name" not in metadata:
            metadata["prospect_name"] = header_match.group(1).strip()
        if "prospect_title" not in metadata:
            metadata["prospect_title"] = header_match.group(2).strip()

    # Look for company in subheader
    subheader_match = re.search(r"##\s*(.+?)(?:Scaling|Challenges|Growth|Interview)", content)
    if subheader_match and "prospect_company" not in metadata:
        company_hint = subheader_match.group(1).strip()
        if company_hint and "Interview" not in company_hint:
            metadata["prospect_company"] = company_hint

    # Extract tags from content analysis (simple keyword extraction)
    tag_keywords = {
        "enterprise": ["enterprise", "fortune 500"],
        "mid-market": ["mid-market", "midmarket"],
        "pipeline": ["pipeline", "forecast"],
        "procurement": ["procurement", "rfp"],
        "competitive": ["competitor", "competing"],
        "pricing": ["pricing", "discount", "negotiation"],
        "integration": ["integration", "api", "connect"],
        "security": ["security", "compliance", "gdpr"],
    }

    content_lower = content.lower()
    tags = []
    for tag, keywords in tag_keywords.items():
        if any(kw in content_lower for kw in keywords):
            tags.append(tag)
    if tags:
        metadata["tags"] = tags

    return metadata


def load_transcript(file_path: Path) -> Transcript | None:
    """Load and parse a single transcript file.

    Args:
        file_path: Path to the markdown file

    Returns:
        Transcript object if successful, None if file is malformed
    """
    try:
        # Read file and parse frontmatter
        post = frontmatter.load(file_path)

        # Get metadata from frontmatter or extract from content
        if post.metadata:
            metadata = dict(post.metadata)
        else:
            metadata = _extract_metadata_from_markdown(post.content)

        # Generate call_id if not present
        call_id = metadata.get("call_id") or _generate_call_id(file_path)

        # Build transcript object
        transcript = Transcript(
            call_id=call_id,
            date=str(metadata.get("date", "")),
            duration_seconds=metadata.get("duration_seconds", 0)
            if isinstance(metadata.get("duration_seconds"), int)
            else _parse_duration(str(metadata.get("duration", ""))),
            rep_name=str(metadata.get("rep_name", "")),
            prospect_name=str(metadata.get("prospect_name", "")),
            prospect_company=str(metadata.get("prospect_company", "")),
            prospect_title=str(metadata.get("prospect_title", "")),
            deal_stage=str(metadata.get("deal_stage", "Discovery")),
            deal_value=metadata.get("deal_value"),
            disposition=str(metadata.get("disposition", "")),
            tags=metadata.get("tags", []) if isinstance(metadata.get("tags"), list) else [],
            key_themes=metadata.get("key_themes", [])
            if isinstance(metadata.get("key_themes"), list)
            else [],
            content=post.content,
            file_path=str(file_path),
        )

        return transcript

    except Exception as e:
        logger.warning(f"Failed to load transcript {file_path}: {e}")
        return None


def load_all_transcripts(transcripts_dir: Path | None = None) -> list[Transcript]:
    """Load all transcripts from the transcripts directory.

    Args:
        transcripts_dir: Path to transcripts directory. Defaults to ./transcripts/

    Returns:
        List of successfully loaded Transcript objects
    """
    if transcripts_dir is None:
        transcripts_dir = Path.cwd() / "transcripts"

    if not transcripts_dir.exists():
        logger.warning(f"Transcripts directory not found: {transcripts_dir}")
        return []

    transcripts = []
    for md_file in sorted(transcripts_dir.glob("*.md")):
        transcript = load_transcript(md_file)
        if transcript:
            transcripts.append(transcript)

    logger.info(f"Loaded {len(transcripts)} transcripts from {transcripts_dir}")
    return transcripts


def get_transcript_by_id(
    call_id: str, transcripts_dir: Path | None = None
) -> Transcript | None:
    """Get a specific transcript by call_id.

    Args:
        call_id: The unique identifier for the call
        transcripts_dir: Path to transcripts directory

    Returns:
        Transcript if found, None otherwise
    """
    transcripts = load_all_transcripts(transcripts_dir)
    for transcript in transcripts:
        if transcript.call_id == call_id:
            return transcript
    return None
