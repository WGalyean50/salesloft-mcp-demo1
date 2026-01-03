# MCP Server Specification: Call Transcript Insights (MVP)

## Overview

An MCP server that exposes sales call transcripts from a local `transcripts/` directory, enabling Claude to read and analyze call data. This MVP demonstrates the MCP pattern for a SalesLoft-like integration.

```
┌────────────────────────────────────────┐
│      Claude Code / Claude Desktop      │
└───────────────────┬────────────────────┘
                    │ STDIO
                    ▼
┌────────────────────────────────────────┐
│     salesloft-transcripts MCP Server   │
│                                        │
│  Tools:           Resources:           │
│  • list_calls     • transcripts://list │
│  • get_call       • transcripts://{id} │
│  • search_calls                        │
└───────────────────┬────────────────────┘
                    │
                    ▼
┌────────────────────────────────────────┐
│         transcripts/ directory         │
│   (markdown files with frontmatter)    │
└────────────────────────────────────────┘
```

---

## Data Format

### Transcript Files

Location: `transcripts/`

Filename pattern: `call_{date}_{company}_{type}.md`

```markdown
---
call_id: "uuid-here"
date: "2024-01-15T14:30:00Z"
duration_seconds: 1847
rep_name: "Sarah Johnson"
prospect_name: "John Smith"
prospect_company: "Acme Corp"
deal_stage: "Discovery"
deal_value: 150000
disposition: "Follow-up Scheduled"
tags: ["technical-deep-dive", "budget-approved"]
---

# Call Transcript: Acme Corp Discovery Call

**[00:00:15] Sarah Johnson:**
Hi John, thanks for taking the time...

**[00:00:32] John Smith:**
Yes, absolutely. We've been struggling with...
```

---

## Tech Stack

| Component | Choice |
|-----------|--------|
| Language | Python 3.11+ |
| SDK | `mcp` (FastMCP) |
| Transport | STDIO |
| Parsing | `python-frontmatter` |

### Project Structure

```
salesloft_mcp_demo/
├── transcripts/           # Call transcript markdown files
├── src/
│   └── salesloft_mcp/
│       ├── __init__.py
│       └── server.py      # MCP server implementation
├── pyproject.toml
└── docs/
    └── mcp_spec.md
```

### Dependencies

```toml
[project]
name = "salesloft-mcp"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "mcp>=1.2.0",
    "python-frontmatter>=1.0.0",
]

[project.scripts]
salesloft-mcp = "salesloft_mcp.server:main"
```

---

## MVP Tools (3 total)

### 1. `list_calls`

List all transcripts with basic filtering.

```python
@mcp.tool()
async def list_calls(
    company: str | None = None,
    deal_stage: str | None = None,
    limit: int = 50
) -> str:
    """
    List available call transcripts.

    Args:
        company: Filter by company name (partial match)
        deal_stage: Filter by stage (Discovery, Demo, Negotiation, etc.)
        limit: Max results to return

    Returns:
        JSON array of call summaries
    """
```

### 2. `get_call`

Get full transcript content.

```python
@mcp.tool()
async def get_call(call_id: str) -> str:
    """
    Get full transcript for a specific call.

    Args:
        call_id: The call's unique identifier

    Returns:
        Full transcript content with metadata
    """
```

### 3. `search_calls`

Simple keyword search across transcripts.

```python
@mcp.tool()
async def search_calls(query: str, limit: int = 10) -> str:
    """
    Search transcripts for keywords.

    Args:
        query: Search terms
        limit: Max excerpts to return

    Returns:
        Matching excerpts with call context
    """
```

---

## MVP Resources (2 total)

### `transcripts://list`

Returns JSON array of all call metadata.

### `transcripts://call/{call_id}`

Returns full transcript content for a specific call.

```python
@mcp.resource("transcripts://list")
async def list_all() -> str:
    """List all transcripts."""
    return json.dumps([t.metadata for t in load_all()])

@mcp.resource("transcripts://call/{call_id}")
async def read_call(uri: str) -> str:
    """Read specific transcript."""
    call_id = uri.split("/")[-1]
    return load_transcript(call_id).content
```

---

## Configuration

Add to Claude Code settings (`.claude/settings.local.json`):

```json
{
  "mcpServers": {
    "salesloft": {
      "type": "stdio",
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/salesloft_mcp_demo",
        "run",
        "salesloft-mcp"
      ]
    }
  }
}
```

---

## Example Usage

**User:** "What calls do we have with Acme Corp?"

Claude calls: `list_calls(company="Acme Corp")`

**User:** "Show me the full transcript from that discovery call"

Claude calls: `get_call(call_id="a1b2c3...")`

**User:** "Find any mentions of pricing concerns"

Claude calls: `search_calls(query="pricing")`

---

## Sample Transcripts to Create

| File | Company | Stage | Theme |
|------|---------|-------|-------|
| call_2024_01_15_acme_corp_discovery.md | Acme Corp | Discovery | Technical needs |
| call_2024_01_18_beta_inc_demo.md | Beta Inc | Demo | Strong interest |
| call_2024_01_22_gamma_llc_negotiation.md | Gamma LLC | Negotiation | Pricing discussion |
| call_2024_01_25_delta_co_discovery.md | Delta Co | Discovery | Lost to competitor |

---

## Testing

Use the MCP Inspector to verify tools work:

```bash
npx @modelcontextprotocol/inspector
```

---

## Future Enhancements (Post-MVP)

- Additional analysis tools (objections, competitive intel, sentiment)
- Prompt templates for structured analysis
- Stats/aggregation resources
- Real SalesLoft API integration
