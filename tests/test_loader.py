"""Tests for transcript loader module."""

import tempfile
from pathlib import Path

import pytest

from salesloft_mcp.transcript_loader import (
    Transcript,
    _generate_call_id,
    _parse_duration,
    load_all_transcripts,
    load_transcript,
)


class TestParseDuration:
    """Tests for duration parsing."""

    def test_minutes_format(self):
        assert _parse_duration("30 minutes") == 1800
        assert _parse_duration("30 min") == 1800
        assert _parse_duration("45 mins") == 2700

    def test_hours_and_minutes(self):
        assert _parse_duration("1 hour 30 minutes") == 5400
        assert _parse_duration("2 hours") == 7200

    def test_colon_format(self):
        assert _parse_duration("30:00") == 1800
        assert _parse_duration("1:30:00") == 5400
        assert _parse_duration("45:30") == 2730

    def test_empty_string(self):
        assert _parse_duration("") == 0


class TestGenerateCallId:
    """Tests for call ID generation from filenames."""

    def test_simple_filename(self):
        assert _generate_call_id(Path("interview_acme.md")) == "interview_acme"

    def test_filename_with_spaces(self):
        assert _generate_call_id(Path("Interview File.md")) == "interview_file"

    def test_uppercase_filename(self):
        assert _generate_call_id(Path("INTERVIEW_TEST.md")) == "interview_test"


class TestLoadTranscript:
    """Tests for loading individual transcripts."""

    def test_load_with_yaml_frontmatter(self):
        """Test loading a file with YAML frontmatter."""
        content = '''---
call_id: "test_call_001"
date: "2025-01-15T14:30:00Z"
duration_seconds: 1800
rep_name: "Sarah Johnson"
prospect_name: "John Smith"
prospect_company: "Acme Corp"
deal_stage: "Discovery"
tags: ["enterprise", "telecom"]
---

# Call Transcript

**[00:00:15] Sarah Johnson:**
Hello, John. Thanks for joining.

**[00:00:25] John Smith:**
Thanks for having me.
'''
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".md", delete=False
        ) as f:
            f.write(content)
            f.flush()

            transcript = load_transcript(Path(f.name))

            assert transcript is not None
            assert transcript.call_id == "test_call_001"
            assert transcript.duration_seconds == 1800
            assert transcript.rep_name == "Sarah Johnson"
            assert transcript.prospect_name == "John Smith"
            assert transcript.prospect_company == "Acme Corp"
            assert transcript.deal_stage == "Discovery"
            assert "enterprise" in transcript.tags

    def test_load_without_frontmatter(self):
        """Test loading a file without YAML frontmatter."""
        content = '''# Customer Interview: Jane Doe, VP Sales

**Date:** January 10, 2025
**Duration:** 45 minutes
**Participants:**
- Sarah Chen, Enterprise Sales Director, Salesloft
- Jane Doe, VP Sales, TechCorp

## Transcript

**Sarah:** Thanks for your time today.
'''
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".md", delete=False
        ) as f:
            f.write(content)
            f.flush()

            transcript = load_transcript(Path(f.name))

            assert transcript is not None
            # Should generate call_id from filename
            assert transcript.call_id is not None
            assert transcript.duration_seconds == 2700  # 45 minutes


class TestLoadAllTranscripts:
    """Tests for loading multiple transcripts."""

    def test_load_from_directory(self):
        """Test loading all transcripts from a directory."""
        # Use the actual transcripts directory
        transcripts_dir = Path(__file__).parent.parent / "transcripts"
        if transcripts_dir.exists():
            transcripts = load_all_transcripts(transcripts_dir)
            assert len(transcripts) > 0
            assert all(isinstance(t, Transcript) for t in transcripts)

    def test_empty_directory(self):
        """Test loading from an empty directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            transcripts = load_all_transcripts(Path(tmpdir))
            assert transcripts == []

    def test_nonexistent_directory(self):
        """Test loading from a nonexistent directory."""
        transcripts = load_all_transcripts(Path("/nonexistent/path"))
        assert transcripts == []


class TestTranscriptMethods:
    """Tests for Transcript dataclass methods."""

    def test_to_summary(self):
        """Test summary generation."""
        transcript = Transcript(
            call_id="test_001",
            date="2025-01-15",
            duration_seconds=1800,
            rep_name="Sarah",
            prospect_name="John",
            prospect_company="Acme",
            deal_stage="Discovery",
            tags=["enterprise"],
        )

        summary = transcript.to_summary()

        assert summary["call_id"] == "test_001"
        assert summary["prospect_company"] == "Acme"
        assert "content" not in summary  # Content not in summary

    def test_to_full(self):
        """Test full transcript generation."""
        transcript = Transcript(
            call_id="test_001",
            date="2025-01-15",
            duration_seconds=1800,
            rep_name="Sarah",
            prospect_name="John",
            prospect_company="Acme",
            deal_stage="Discovery",
            content="Full transcript text here",
        )

        full = transcript.to_full()

        assert full["call_id"] == "test_001"
        assert full["content"] == "Full transcript text here"
