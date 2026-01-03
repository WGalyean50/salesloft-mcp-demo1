# Salesloft MCP Demo Server

An MCP (Model Context Protocol) server that exposes sales call transcripts to Claude, enabling AI-powered analysis of customer conversations.

## What This Demo Shows

This demo illustrates how AI can transform raw sales call data into actionable intelligence. Instead of manually reviewing hours of call recordings, sales leaders can ask natural language questions and get instant answers.

**Example queries you can ask Claude:**

- "What calls do we have available?"
- "Show me all discovery calls"
- "What are the common objections we're hearing?"
- "Find mentions of procurement or budget delays"
- "Summarize the TeleCom Nexus interview"
- "Which companies are concerned about migration?"

## Quick Start

### Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) package manager
- Claude Code or Claude Desktop with MCP support

### Installation

1. Clone or download this repository:

```bash
cd salesloft_mcp_demo
```

2. Install dependencies:

```bash
uv sync
```

3. Verify installation:

```bash
uv run salesloft-mcp --help
```

### Configure Claude Code

Add to your Claude Code settings (`.claude/settings.local.json`):

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

Replace `/path/to/salesloft_mcp_demo` with the actual path to this directory.

### Run the Demo

1. Restart Claude Code to load the MCP server
2. Ask Claude about your call data:
   - "What calls do we have?"
   - "Search for mentions of pricing"
   - "Tell me about the TeleCom Nexus call"

## Available Tools

### `list_calls`

List available call transcripts with optional filtering.

**Parameters:**
- `company` (optional): Filter by company name (partial match)
- `deal_stage` (optional): Filter by stage (Discovery, Demo, Negotiation)
- `limit` (optional): Max results to return (default: 50)

### `get_call`

Get the full transcript content for a specific call.

**Parameters:**
- `call_id` (required): The unique identifier for the call

### `search_calls`

Search for keywords across all transcripts.

**Parameters:**
- `query` (required): Search terms
- `limit` (optional): Max excerpts to return (default: 10)

## Available Resources

- `transcripts://list` - Get all call metadata
- `transcripts://call/{call_id}` - Get full transcript content

## Sample Transcripts

The demo includes 40+ sample interview transcripts covering:

- **Telecom**: Pipeline visibility, 5G budget competition
- **Legal Tech**: Law firm adoption, procurement complexity
- **E-commerce**: Shopify competition, migration concerns
- **HR Tech**: Multi-stakeholder buying committees
- **And more...**

## Testing

Run the test suite:

```bash
uv run pytest tests/ -v
```

## Project Structure

```
salesloft_mcp_demo/
├── src/salesloft_mcp/
│   ├── server.py           # MCP server with tools/resources
│   ├── transcript_loader.py # File parsing utilities
│   └── search.py           # Search functionality
├── transcripts/            # Call transcript files
├── tests/                  # Test suite
├── docs/                   # Documentation
└── .claude/               # Claude Code configuration
```

## Troubleshooting

### Server not appearing in Claude Code

1. Check that the path in `settings.local.json` is correct
2. Ensure `uv` is in your PATH
3. Restart Claude Code

### No transcripts loading

1. Verify the `transcripts/` directory exists
2. Check that `.md` files are present
3. Run `uv run python -c "from salesloft_mcp.transcript_loader import load_all_transcripts; print(len(load_all_transcripts()))"` to verify

### Import errors

Run `uv sync` to ensure all dependencies are installed.

## Future Enhancements

This MVP demonstrates core value. Future versions could add:

- Real SalesLoft API integration
- Sentiment analysis per speaker
- Objection detection and categorization
- Deal health scoring based on call signals
- Competitive intelligence extraction
