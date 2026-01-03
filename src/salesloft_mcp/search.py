"""Search functionality for transcripts."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from .transcript_loader import Transcript


@dataclass
class SearchResult:
    """A single search result with context."""

    call_id: str
    call_summary: str
    excerpt: str
    speaker: str
    timestamp: str

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            "call_id": self.call_id,
            "call_summary": self.call_summary,
            "excerpt": self.excerpt,
            "speaker": self.speaker,
            "timestamp": self.timestamp,
        }


def _extract_speaker(text: str, match_start: int) -> str:
    """Try to extract the speaker for a given text position."""
    # Look backwards for speaker patterns
    # Pattern 1: **[timestamp] Speaker:**
    # Pattern 2: [SPEAKER]
    # Pattern 3: **Speaker:**

    # Get text before match
    before_text = text[max(0, match_start - 200) : match_start]

    # Try pattern: **[timestamp] Name:**
    speaker_match = re.search(
        r"\*\*\[\d+:\d+(?::\d+)?\]\s*([^*]+?):\*\*",
        before_text,
    )
    if speaker_match:
        return speaker_match.group(1).strip()

    # Try pattern: [SPEAKER NAME]
    speaker_match = re.search(r"\[([A-Z][A-Z\s]+)\]", before_text)
    if speaker_match:
        return speaker_match.group(1).strip()

    # Try pattern: **Name:**
    speaker_match = re.search(r"\*\*([^*\[\]]+?):\*\*", before_text)
    if speaker_match:
        return speaker_match.group(1).strip()

    return ""


def _extract_timestamp(text: str, match_start: int) -> str:
    """Try to extract the timestamp for a given text position."""
    # Look backwards for timestamp patterns
    before_text = text[max(0, match_start - 200) : match_start]

    # Pattern: **[0:00]** or **[00:00:00]**
    ts_match = re.search(r"\*\*\[(\d+:\d+(?::\d+)?)\]\*\*", before_text)
    if ts_match:
        return ts_match.group(1)

    # Pattern: [timestamp] in speaker label
    ts_match = re.search(r"\*\*\[(\d+:\d+(?::\d+)?)\]", before_text)
    if ts_match:
        return ts_match.group(1)

    return ""


def _get_context(text: str, match_start: int, match_end: int, context_words: int = 75) -> str:
    """Extract context around a match (approximately context_words before and after)."""
    # Find word boundaries
    # Look backwards for context
    before_start = match_start
    word_count = 0
    while before_start > 0 and word_count < context_words:
        before_start -= 1
        if text[before_start] in " \n\t":
            word_count += 1

    # Look forwards for context
    after_end = match_end
    word_count = 0
    while after_end < len(text) and word_count < context_words:
        after_end += 1
        if after_end < len(text) and text[after_end] in " \n\t":
            word_count += 1

    # Extract and clean up
    excerpt = text[before_start:after_end].strip()

    # Clean up markdown formatting for readability
    excerpt = re.sub(r"\*\*\[[\d:]+\]\*\*\s*", "", excerpt)  # Remove timestamp markers
    excerpt = re.sub(r"\*\*([^*]+):\*\*", r"\1:", excerpt)  # Clean speaker labels
    excerpt = re.sub(r"\s+", " ", excerpt)  # Normalize whitespace

    return excerpt


def search_transcripts(
    transcripts: list[Transcript],
    query: str,
    limit: int = 10,
) -> list[SearchResult]:
    """Search transcripts for matching keywords.

    Args:
        transcripts: List of transcripts to search
        query: Search query (case-insensitive)
        limit: Maximum number of results to return

    Returns:
        List of SearchResult objects with context
    """
    results: list[SearchResult] = []

    # Build regex pattern for case-insensitive search
    # Split query into words and search for any of them
    words = query.lower().split()
    if not words:
        return results

    # Create pattern that matches any word (partial matches allowed)
    pattern = "|".join(re.escape(word) for word in words)

    for transcript in transcripts:
        content = transcript.content
        content_lower = content.lower()

        # Find all matches
        for match in re.finditer(pattern, content_lower):
            match_start = match.start()
            match_end = match.end()

            # Build result
            result = SearchResult(
                call_id=transcript.call_id,
                call_summary=f"{transcript.prospect_name} @ {transcript.prospect_company}",
                excerpt=_get_context(content, match_start, match_end),
                speaker=_extract_speaker(content, match_start),
                timestamp=_extract_timestamp(content, match_start),
            )
            results.append(result)

            if len(results) >= limit:
                return results

    return results
