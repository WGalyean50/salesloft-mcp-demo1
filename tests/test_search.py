"""Tests for search functionality."""

import pytest

from salesloft_mcp.search import SearchResult, search_transcripts
from salesloft_mcp.transcript_loader import Transcript


class TestSearchResult:
    """Tests for SearchResult dataclass."""

    def test_to_dict(self):
        result = SearchResult(
            call_id="test_001",
            call_summary="John @ Acme",
            excerpt="This is a test excerpt with context.",
            speaker="John Smith",
            timestamp="00:05:30",
        )

        d = result.to_dict()

        assert d["call_id"] == "test_001"
        assert d["call_summary"] == "John @ Acme"
        assert d["excerpt"] == "This is a test excerpt with context."
        assert d["speaker"] == "John Smith"
        assert d["timestamp"] == "00:05:30"


class TestSearchTranscripts:
    """Tests for transcript search functionality."""

    @pytest.fixture
    def sample_transcripts(self) -> list[Transcript]:
        return [
            Transcript(
                call_id="call_001",
                date="2025-01-15",
                duration_seconds=1800,
                rep_name="Sarah",
                prospect_name="John",
                prospect_company="Acme Corp",
                content="""
**[00:05:30] John Smith:**
We are dealing with serious procurement delays. The budget approval
process takes forever and we need a solution.

**[00:06:15] Sarah:**
I understand. Many of our customers face similar procurement challenges.
""",
            ),
            Transcript(
                call_id="call_002",
                date="2025-01-16",
                duration_seconds=2400,
                rep_name="Mike",
                prospect_name="Jane",
                prospect_company="Beta Inc",
                content="""
**[00:10:00] Jane Doe:**
Our main concern is the competitive landscape. We are evaluating
several vendors including your competitors.

**[00:10:30] Mike:**
Let me explain what differentiates us from the competition.
""",
            ),
        ]

    def test_search_finds_exact_match(self, sample_transcripts):
        """SC-1: Finds exact keyword matches."""
        results = search_transcripts(sample_transcripts, "procurement")
        assert len(results) >= 1
        assert any("procurement" in r.excerpt.lower() for r in results)

    def test_search_finds_partial_match(self, sample_transcripts):
        """SC-2: Finds partial word matches."""
        results = search_transcripts(sample_transcripts, "compet")
        assert len(results) >= 1
        # Should find "competitive" or "competition"
        assert any(
            "compet" in r.excerpt.lower() for r in results
        )

    def test_search_returns_context(self, sample_transcripts):
        """SC-3: Returns relevant context around matches."""
        results = search_transcripts(sample_transcripts, "budget")
        assert len(results) >= 1
        # Excerpt should have surrounding context
        assert len(results[0].excerpt) > 20

    def test_search_attributes_to_correct_call(self, sample_transcripts):
        """SC-4: Attributes excerpts to correct call_id."""
        results = search_transcripts(sample_transcripts, "procurement")
        assert len(results) >= 1
        assert results[0].call_id == "call_001"

    def test_search_respects_limit(self, sample_transcripts):
        """SC-5: Respects limit parameter."""
        results = search_transcripts(sample_transcripts, "the", limit=2)
        assert len(results) <= 2

    def test_search_case_insensitive(self, sample_transcripts):
        """SC-6: Case-insensitive search."""
        results_lower = search_transcripts(sample_transcripts, "procurement")
        results_upper = search_transcripts(sample_transcripts, "PROCUREMENT")
        assert len(results_lower) == len(results_upper)

    def test_search_empty_query(self, sample_transcripts):
        """Test empty query returns no results."""
        results = search_transcripts(sample_transcripts, "")
        assert len(results) == 0

    def test_search_no_matches(self, sample_transcripts):
        """Test query with no matches."""
        results = search_transcripts(sample_transcripts, "xyznonexistent123")
        assert len(results) == 0
