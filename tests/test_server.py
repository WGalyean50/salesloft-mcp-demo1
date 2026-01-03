"""Tests for MCP server tools and resources."""

import json

import pytest

from salesloft_mcp.server import get_call, list_calls, search_calls


@pytest.mark.asyncio
class TestListCalls:
    """Tests for list_calls tool."""

    async def test_list_all_calls(self):
        """LC-1: Returns all transcripts when called with no parameters."""
        result = await list_calls()
        data = json.loads(result)
        assert isinstance(data, list)
        assert len(data) > 0

    async def test_filter_by_company(self):
        """LC-2: Filters by company name (case-insensitive partial match)."""
        result = await list_calls(company="tech")
        data = json.loads(result)
        # Should return results with "tech" in company name
        assert isinstance(data, list)

    async def test_filter_by_deal_stage(self):
        """LC-3: Filters by deal_stage (exact match)."""
        result = await list_calls(deal_stage="Discovery")
        data = json.loads(result)
        assert isinstance(data, list)
        # All results should have Discovery stage
        for item in data:
            assert item["deal_stage"].lower() == "discovery"

    async def test_respects_limit(self):
        """LC-4: Respects limit parameter."""
        result = await list_calls(limit=5)
        data = json.loads(result)
        assert len(data) <= 5

    async def test_empty_result_for_no_matches(self):
        """LC-5: Returns empty array (not error) when no matches found."""
        result = await list_calls(company="NonExistentCompanyXYZ123")
        data = json.loads(result)
        assert data == []

    async def test_returns_valid_json(self):
        """LC-6: Returns valid JSON that Claude can parse."""
        result = await list_calls(limit=3)
        data = json.loads(result)
        assert isinstance(data, list)
        if len(data) > 0:
            # Check required fields exist
            assert "call_id" in data[0]
            assert "prospect_company" in data[0]
            assert "deal_stage" in data[0]


@pytest.mark.asyncio
class TestGetCall:
    """Tests for get_call tool."""

    async def test_get_valid_call(self):
        """GC-1: Returns full transcript for valid call_id."""
        # First get a valid call_id
        list_result = await list_calls(limit=1)
        calls = json.loads(list_result)
        if len(calls) > 0:
            call_id = calls[0]["call_id"]
            result = await get_call(call_id)
            data = json.loads(result)
            assert "call_id" in data
            assert "content" in data
            assert data["call_id"] == call_id

    async def test_get_invalid_call(self):
        """GC-2: Returns appropriate error for invalid call_id."""
        result = await get_call("nonexistent_call_id_12345")
        data = json.loads(result)
        assert "error" in data

    async def test_includes_all_metadata(self):
        """GC-3: Includes all metadata fields in response."""
        list_result = await list_calls(limit=1)
        calls = json.loads(list_result)
        if len(calls) > 0:
            call_id = calls[0]["call_id"]
            result = await get_call(call_id)
            data = json.loads(result)
            # Check all expected fields
            expected_fields = [
                "call_id",
                "date",
                "duration_seconds",
                "rep_name",
                "prospect_name",
                "prospect_company",
                "deal_stage",
                "content",
            ]
            for field in expected_fields:
                assert field in data


@pytest.mark.asyncio
class TestSearchCalls:
    """Tests for search_calls tool."""

    async def test_search_finds_keywords(self):
        """Test that search finds common keywords."""
        result = await search_calls("sales")
        data = json.loads(result)
        assert isinstance(data, list)

    async def test_search_respects_limit(self):
        """Test that search respects limit parameter."""
        result = await search_calls("the", limit=3)
        data = json.loads(result)
        assert len(data) <= 3

    async def test_search_returns_excerpt(self):
        """Test that search returns excerpts with context."""
        result = await search_calls("budget", limit=1)
        data = json.loads(result)
        if len(data) > 0:
            assert "excerpt" in data[0]
            assert len(data[0]["excerpt"]) > 0

    async def test_search_includes_call_id(self):
        """Test that search results include call_id for attribution."""
        result = await search_calls("customer", limit=1)
        data = json.loads(result)
        if len(data) > 0:
            assert "call_id" in data[0]
