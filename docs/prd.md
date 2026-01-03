# Product Requirements Document: Salesloft MCP Demo Server

**Version:** 1.0
**Date:** January 2026
**Author:** Product Team
**Status:** Draft

---

## Table of Contents

1. [Product Vision and Goals](#1-product-vision-and-goals)
2. [User Personas and Use Cases](#2-user-personas-and-use-cases)
3. [Core Requirements and Features](#3-core-requirements-and-features)
4. [User Flows](#4-user-flows)
5. [Technical Requirements](#5-technical-requirements)
6. [Acceptance Criteria](#6-acceptance-criteria)
7. [Out of Scope (MVP)](#7-out-of-scope-mvp)
8. [Open Questions and Risks](#8-open-questions-and-risks)

---

## 1. Product Vision and Goals

### 1.1 Problem Statement

Sales leaders and revenue operations teams are drowning in call data. They have hundreds of customer discovery calls, prospect interviews, and sales conversations stored in various systems, but extracting meaningful insights requires manual review of lengthy transcripts. Key patterns, competitive intelligence, customer pain points, and deal health signals remain buried in unstructured text.

The current state:
- **Time-intensive analysis**: A 30-minute call transcript takes 15-20 minutes to read and synthesize
- **Lost institutional knowledge**: Insights from calls leave when reps leave
- **No systematic pattern recognition**: Cross-call themes and competitive intelligence require manual correlation
- **Reactive decision-making**: Deal risks are discovered too late because call signals are not surfaced proactively

### 1.2 Solution Overview

Build an MCP (Model Context Protocol) server that exposes sales call transcripts to Claude, enabling AI-powered analysis of customer conversations. This MVP demonstrates how Salesloft call data could be made accessible to Claude for intelligent querying, pattern recognition, and insight extraction.

The MCP server acts as a bridge between local transcript files (simulating a SalesLoft API integration) and Claude, allowing users to ask natural language questions about their call data and receive contextually relevant answers.

### 1.3 Target User

**Primary:** Salesloft + Clari sales team members and sales engineers who need to demonstrate the value of AI-powered call analysis to prospects and customers.

**Secondary:** Revenue operations leaders, CROs, and VPs of Sales who want to explore how AI could help them extract value from their existing call recordings and transcripts.

### 1.4 Core Value Proposition

Enable sales teams to query their entire call history using natural language, transforming raw transcripts into actionable intelligence without manual review.

**Key value drivers:**
- **Speed**: Get answers about call content in seconds instead of hours of manual review
- **Pattern recognition**: Surface themes across multiple calls that would be invisible in isolation
- **Accessibility**: Make call insights available to anyone on the team, not just those who attended
- **Demonstration value**: Show prospects what AI-powered revenue intelligence could look like

### 1.5 Success Metrics for the Demo

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Demo completion rate | Users can complete 3 core queries successfully | Manual testing |
| Query response time | < 5 seconds for list/search operations | Timing measurement |
| Transcript retrieval accuracy | 100% of stored transcripts accessible | Test coverage |
| Search relevance | Relevant excerpts returned for keyword queries | Qualitative assessment |

---

## 2. User Personas and Use Cases

### 2.1 Primary Personas

#### Persona 1: Sales Engineer (Demo User)

**Name:** Alex, Senior Sales Engineer at Salesloft + Clari
**Role:** Technical pre-sales, responsible for demonstrating Salesloft + Clari capabilities
**Goals:**
- Show prospects how AI can transform their sales call data into intelligence
- Demonstrate the MCP integration pattern for Claude users
- Create compelling "wow moments" in discovery calls

**Pain Points:**
- Generic demos do not resonate with specific industry verticals
- Difficult to show the "so what" of call recording features
- Prospects skeptical about actual AI capabilities

**Use Case:** Alex uses the MCP server during prospect demos to show how Claude can answer questions like "What were the main objections raised in our telecom calls?" or "Summarize the competitive mentions across all discovery calls."

#### Persona 2: VP of Sales (Prospect)

**Name:** Jennifer, VP Sales at a $75M ARR E-commerce Platform
**Role:** Revenue leader responsible for sales team performance and forecasting
**Goals:**
- Improve forecast accuracy from current 65% to 90%+
- Understand why deals are won/lost across segments
- Scale institutional knowledge beyond individual reps

**Pain Points:**
- Spends 30% of time trying to get clean pipeline data
- Surprised by deal slips because call signals are not surfaced
- Reps who leave take relationship context with them

**Use Case:** Jennifer explores the MCP demo to understand how she could ask Claude "Which enterprise deals show declining engagement based on call patterns?" or "What pricing objections are we hearing most frequently?"

#### Persona 3: Revenue Operations Leader

**Name:** Marcus, CRO at a $500M ARR Enterprise SaaS Company
**Role:** Chief Revenue Officer overseeing 180 reps across 12 regions
**Goals:**
- Create unified visibility across fragmented tools
- Enable data-driven coaching at scale
- Reduce 10-15% surprise deal slips to under 5%

**Pain Points:**
- 8 different tools create data silos
- Regional VPs each forecast differently
- When reps leave, 6-18 months of ramp time is lost

**Use Case:** Marcus wants to see how AI could help with questions like "What deal health signals should I be tracking across my regions?" or "Show me calls where the champion expressed timeline concerns."

### 2.2 Key Use Cases

#### Use Case 1: Call Discovery and Navigation
**As a** sales leader
**I want to** list and filter available call transcripts
**So that** I can quickly find relevant conversations to analyze

**Scenarios:**
- View all calls with a specific company
- Filter calls by deal stage (Discovery, Demo, Negotiation, etc.)
- See most recent calls across the entire team

#### Use Case 2: Deep Dive on Specific Calls
**As a** sales rep or manager
**I want to** retrieve the full transcript of a specific call
**So that** I can understand exactly what was discussed

**Scenarios:**
- Review a call before a follow-up meeting
- Prepare for a deal review by reading key conversations
- Understand context for a deal handoff

#### Use Case 3: Cross-Call Pattern Search
**As a** revenue operations leader
**I want to** search for keywords or themes across all calls
**So that** I can identify patterns and competitive intelligence

**Scenarios:**
- Find all mentions of competitor products
- Search for pricing objections
- Identify calls where procurement was mentioned as a blocker

### 2.3 Example Questions Users Will Ask Claude

**Call Discovery:**
- "What calls do we have with TeleCom Nexus?"
- "Show me all discovery calls from last week"
- "Which calls are in the negotiation stage?"

**Single Call Analysis:**
- "Summarize the key points from the Jeffrey Moore interview"
- "What objections did the prospect raise in that call?"
- "Who were the stakeholders mentioned in the Acme Corp call?"

**Cross-Call Intelligence:**
- "What are the common pain points across all our healthcare tech interviews?"
- "Find any mentions of budget or pricing concerns"
- "What competitive products are prospects evaluating?"
- "Which calls mention integration requirements?"

**Strategic Insights:**
- "What patterns do you see in deals that involve IT and Network stakeholder misalignment?"
- "Summarize the key themes from our telecom vertical calls"
- "What are the most common objections we are hearing?"

---

## 3. Core Requirements and Features

### 3.1 MVP Tools

The MCP server will expose three tools that Claude can invoke to interact with transcript data.

#### Tool 1: `list_calls`

**Purpose:** List available call transcripts with optional filtering

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `company` | string | No | Filter by company name (partial match, case-insensitive) |
| `deal_stage` | string | No | Filter by deal stage (Discovery, Demo, Negotiation, Committed, etc.) |
| `limit` | integer | No | Maximum results to return (default: 50, max: 100) |

**Returns:** JSON array of call summaries containing:
- `call_id`: Unique identifier
- `date`: Call date and time (ISO 8601)
- `duration_seconds`: Call length
- `rep_name`: Sales rep who conducted the call
- `prospect_name`: Primary prospect contact
- `prospect_company`: Company name
- `deal_stage`: Current deal stage
- `deal_value`: Estimated deal value (if known)
- `disposition`: Call outcome (e.g., "Follow-up Scheduled", "Needs Champion")
- `tags`: Array of relevant tags

**Example invocation:**
```
list_calls(company="TeleCom", deal_stage="Discovery", limit=10)
```

#### Tool 2: `get_call`

**Purpose:** Retrieve the full transcript content for a specific call

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `call_id` | string | Yes | The unique identifier for the call |

**Returns:** Full transcript content including:
- Complete metadata (all fields from list_calls)
- Full transcript text with speaker labels and timestamps
- Any additional notes or tags

**Example invocation:**
```
get_call(call_id="interview_jeffrey_moore_20250115")
```

#### Tool 3: `search_calls`

**Purpose:** Search for keywords or phrases across all transcripts

**Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Search terms (supports multiple words) |
| `limit` | integer | No | Maximum excerpts to return (default: 10, max: 50) |

**Returns:** JSON array of matching excerpts containing:
- `call_id`: Which call the excerpt is from
- `call_summary`: Brief context about the call
- `excerpt`: The matching text passage (with surrounding context)
- `speaker`: Who said the matching text
- `timestamp`: When in the call this occurred (if available)

**Example invocation:**
```
search_calls(query="procurement delay", limit=5)
```

### 3.2 MVP Resources

The MCP server will expose two resources that provide direct data access.

#### Resource 1: `transcripts://list`

**Purpose:** Provide a machine-readable index of all available transcripts

**Returns:** JSON array of all call metadata (same structure as `list_calls` with no filters)

**Use case:** Allows Claude to understand the full scope of available data before making targeted queries

#### Resource 2: `transcripts://call/{call_id}`

**Purpose:** Direct access to a specific transcript's content

**Returns:** Full transcript content for the specified call ID

**Use case:** Efficient retrieval when the call_id is already known

### 3.3 Data Format Requirements

#### Transcript File Format

All transcripts must be stored as Markdown files with YAML frontmatter.

**Location:** `transcripts/` directory in the project root

**Filename convention:** `{type}_{company_slug}_{date}.md`
- Example: `interview_telecom_nexus_20250115.md`
- Example: `discovery_acme_corp_20250118.md`

**Required frontmatter fields:**
```yaml
---
call_id: "unique-identifier-string"
date: "2025-01-15T14:30:00Z"  # ISO 8601 format
duration_seconds: 1920
rep_name: "Mitchell Chen"
prospect_name: "Jeffrey Moore"
prospect_company: "TeleCom Nexus"
prospect_title: "Chief Revenue Officer"
deal_stage: "Discovery"
deal_value: 500000  # Optional, in USD
disposition: "Follow-up Scheduled"
tags: ["enterprise", "telecom", "pipeline-visibility"]
---
```

**Transcript body format:**
```markdown
# Call Transcript: TeleCom Nexus Discovery Call

## Participants
- **Mitchell Chen** - VP Sales, Salesloft + Clari
- **Jeffrey Moore** - CRO, TeleCom Nexus

## Transcript

**[00:00:15] Mitchell Chen:**
Thanks for taking the time today, Jeffrey...

**[00:00:32] Jeffrey Moore:**
Of course. We have been looking at solutions for...
```

### 3.4 Sample Transcripts to Include

The MVP should include 4-6 sample transcripts demonstrating variety in:

| Transcript | Company | Stage | Duration | Key Themes |
|------------|---------|-------|----------|------------|
| TeleCom Nexus Interview | TeleCom Nexus | Discovery | 32 min | Pipeline visibility, 5G budget competition, stakeholder misalignment |
| Marcus Chen Interview | Enterprise SaaS | Discovery | 32 min | Forecast accuracy, rep productivity, tool sprawl |
| Sandra Mitchell Interview | Legal Tech | Discovery | 32 min | Law firm adoption, procurement complexity, change management |
| Jennifer Adams Interview | E-commerce Platform | Discovery | 32 min | Shopify competition, SI partnerships, migration risk |
| Angela White Interview | Staffing Tech | Discovery | 30 min | Cyclicality, platform competition, portfolio diversification |

---

## 4. User Flows

### 4.1 Flow 1: Initial Call Discovery

**Scenario:** A user wants to explore what call data is available

**Steps:**
1. User asks Claude: "What calls do we have available?"
2. Claude invokes `list_calls()` with no filters
3. MCP server reads all transcript files from `transcripts/` directory
4. Server parses frontmatter from each file
5. Server returns JSON array of call summaries
6. Claude presents a formatted list to the user

**Expected Claude behavior:**
- Present calls in a scannable format (table or bulleted list)
- Include key details: company, date, stage, rep
- Offer to dive deeper into specific calls

**Example Claude response:**
```
I found 5 call transcripts available. Here's an overview:

| Company | Contact | Stage | Date | Rep |
|---------|---------|-------|------|-----|
| TeleCom Nexus | Jeffrey Moore (CRO) | Discovery | Jan 15 | Mitchell Chen |
| Enterprise SaaS | Marcus Chen (CRO) | Discovery | Jan 14 | Sarah Zhang |
| Legal Tech Solutions | Sandra Mitchell (CRO) | Discovery | Jan 2 | Marcus Chen |
| CommerceFlow | Jennifer Adams (VP Sales) | Discovery | Jan 15 | Marcus Chen |
| TalentFlow Solutions | Angela White (CRO) | Discovery | Jan 2 | Marcus Chen |

Would you like me to summarize any of these calls or search for specific topics across them?
```

### 4.2 Flow 2: Filtered Call Search

**Scenario:** A user wants to find calls with a specific company

**Steps:**
1. User asks: "Show me all calls with telecom companies"
2. Claude invokes `list_calls(company="telecom")`
3. MCP server filters transcripts where company contains "telecom" (case-insensitive)
4. Server returns filtered results
5. Claude presents the filtered list

**Expected Claude behavior:**
- Apply appropriate filters based on user intent
- Explain what filter was applied
- Handle zero results gracefully

### 4.3 Flow 3: Deep Dive on a Single Call

**Scenario:** A user wants to understand a specific call in detail

**Steps:**
1. User asks: "Tell me about the Jeffrey Moore interview"
2. Claude invokes `get_call(call_id="interview_telecom_nexus_20250115")`
3. MCP server reads the full transcript file
4. Server returns complete content including metadata and transcript
5. Claude analyzes the content and provides a summary

**Expected Claude behavior:**
- Provide a structured summary (key points, objections, next steps)
- Offer to answer specific questions about the call
- Identify notable quotes or insights

**Example Claude response:**
```
Here's a summary of the Jeffrey Moore interview from January 15, 2025:

## Call Overview
- **Duration:** 32 minutes
- **Participants:** Mitchell Chen (Salesloft) with Jeffrey Moore (CRO) and Sophia Rodriguez (Director Sales Ops) from TeleCom Nexus

## Key Themes

**1. Pipeline Visibility Gap**
Jeffrey described their pipeline as "full but not actually full" because deals move slowly through carrier procurement. They cannot tell which deals are genuinely progressing vs. stalled.

**2. 5G Budget Competition**
Software budgets are being crowded out by infrastructure investments. Jeffrey noted: "When we come in with a software platform that costs $500K to $2M a year, the conversation is basically: 'Why would we spend that when we should be spending it on 5G optimization?'"

**3. Stakeholder Misalignment**
Network and IT teams often have conflicting priorities, and TeleCom Nexus has no visibility into these internal dynamics. Jeffrey admitted: "We're flying blind."

## Notable Quotes
- "Our pipeline looks full, but in reality, we're not actually controlling anything"
- "Forecasting - don't get me started on forecasting" (on their 75-80% accuracy rate)

## Identified Pain Points
- 240-day deal cycles (vs. expected 60 days)
- 10-15% of deals slip with no early warning
- Champions become bottlenecks for internal selling

Would you like me to elaborate on any of these themes or search for similar patterns in other calls?
```

### 4.4 Flow 4: Cross-Call Pattern Search

**Scenario:** A user wants to find mentions of a specific topic across all calls

**Steps:**
1. User asks: "Find any mentions of procurement or budget delays"
2. Claude invokes `search_calls(query="procurement budget delay")`
3. MCP server searches all transcripts for matching terms
4. Server returns excerpts with context
5. Claude synthesizes findings across calls

**Expected Claude behavior:**
- Present excerpts with proper attribution
- Identify patterns across multiple calls
- Highlight most relevant matches first

**Example Claude response:**
```
I found mentions of procurement and budget delays in 3 calls. Here are the key excerpts:

**TeleCom Nexus (Jeffrey Moore):**
> "Our carrier procurement cycles are crushing our forecasting accuracy. We'll have a deal that looks solid and then their procurement process drags it from a 60-day close to 240 days."

**Legal Tech Solutions (Sandra Mitchell):**
> "Five years ago, procurement didn't even exist in these conversations. Now, every firm with more than $100 million in revenue has a formal procurement process."

**CommerceFlow (Jennifer Adams):**
> "The IT buyer is often equally important, sometimes more important. They care about infrastructure, security, compliance, integration with enterprise systems."

## Pattern Analysis
Across these calls, procurement emerges as a consistent deal blocker with several common characteristics:
1. **Timeline extension:** Deals extend 3-4x beyond initial estimates
2. **Multiple stakeholders:** Procurement adds 3-6 new decision makers mid-cycle
3. **Security/compliance focus:** Risk assessment often outweighs cost considerations

Would you like me to search for specific strategies mentioned for handling procurement delays?
```

---

## 5. Technical Requirements

### 5.1 Technology Stack

| Component | Choice | Rationale |
|-----------|--------|-----------|
| **Language** | Python 3.11+ | Strong MCP SDK support, team familiarity |
| **MCP SDK** | `mcp` (FastMCP) | Official SDK, simplest integration path |
| **Transport** | STDIO | Standard for Claude Code integration |
| **Frontmatter Parsing** | `python-frontmatter` | Well-maintained, handles YAML frontmatter reliably |
| **File Format** | Markdown with YAML | Human-readable, easy to create samples |

### 5.2 Project Structure

```
salesloft_mcp_demo/
├── transcripts/                    # Call transcript markdown files
│   ├── interview_telecom_nexus_20250115.md
│   ├── interview_marcus_chen_20250114.md
│   ├── interview_sandra_mitchell_20250102.md
│   ├── interview_jennifer_adams_20250115.md
│   └── interview_angela_white_20250102.md
├── src/
│   └── salesloft_mcp/
│       ├── __init__.py
│       ├── server.py               # MCP server implementation
│       ├── transcript_loader.py    # File parsing utilities
│       └── search.py               # Search functionality
├── tests/
│   ├── test_server.py
│   ├── test_loader.py
│   └── test_search.py
├── docs/
│   ├── prd.md                      # This document
│   ├── mcp_spec.md                 # Technical specification
│   └── transcript.md               # Sample transcript reference
├── pyproject.toml
├── README.md
└── CLAUDE.md
```

### 5.3 Dependencies

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

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-asyncio>=0.21.0",
]
```

### 5.4 Configuration

**Claude Code Settings** (`.claude/settings.local.json`):
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

### 5.5 Data Handling Requirements

**Privacy and Security:**
- All transcript data is local (no external API calls)
- No sensitive data should be included in sample transcripts
- Transcripts directory should be configurable via environment variable

**Performance:**
- Server should start in under 2 seconds
- List operations should complete in under 1 second
- Search operations should complete in under 3 seconds for typical query

**Error Handling:**
- Graceful handling of malformed frontmatter
- Clear error messages for missing call_id
- Fallback behavior if transcripts directory is empty

---

## 6. Acceptance Criteria

### 6.1 Tool: `list_calls`

| ID | Criterion | Test Method |
|----|-----------|-------------|
| LC-1 | Returns all transcripts when called with no parameters | Unit test |
| LC-2 | Filters by company name (case-insensitive partial match) | Unit test |
| LC-3 | Filters by deal_stage (exact match) | Unit test |
| LC-4 | Respects limit parameter | Unit test |
| LC-5 | Returns empty array (not error) when no matches found | Unit test |
| LC-6 | Returns valid JSON that Claude can parse | Integration test |

### 6.2 Tool: `get_call`

| ID | Criterion | Test Method |
|----|-----------|-------------|
| GC-1 | Returns full transcript for valid call_id | Unit test |
| GC-2 | Returns appropriate error for invalid call_id | Unit test |
| GC-3 | Includes all metadata fields in response | Unit test |
| GC-4 | Preserves transcript formatting (speaker labels, timestamps) | Manual verification |

### 6.3 Tool: `search_calls`

| ID | Criterion | Test Method |
|----|-----------|-------------|
| SC-1 | Finds exact keyword matches | Unit test |
| SC-2 | Finds partial word matches | Unit test |
| SC-3 | Returns relevant context around matches (50-100 words) | Unit test |
| SC-4 | Attributes excerpts to correct call_id | Unit test |
| SC-5 | Respects limit parameter | Unit test |
| SC-6 | Case-insensitive search | Unit test |

### 6.4 Resources

| ID | Criterion | Test Method |
|----|-----------|-------------|
| R-1 | `transcripts://list` returns valid JSON array | Unit test |
| R-2 | `transcripts://call/{id}` returns correct transcript | Unit test |
| R-3 | Invalid resource URI returns appropriate error | Unit test |

### 6.5 Integration Criteria

| ID | Criterion | Test Method |
|----|-----------|-------------|
| INT-1 | MCP server starts successfully via configured command | Manual test |
| INT-2 | Claude can invoke list_calls and receive results | Manual test |
| INT-3 | Claude can invoke get_call and receive results | Manual test |
| INT-4 | Claude can invoke search_calls and receive results | Manual test |
| INT-5 | Full demo flow completes without errors | Manual test |

### 6.6 Definition of Done

The MVP is complete when:

1. **All tools implemented:** Three tools (`list_calls`, `get_call`, `search_calls`) are functional
2. **All resources implemented:** Two resources (`transcripts://list`, `transcripts://call/{id}`) are accessible
3. **Sample data created:** 4-6 representative transcripts based on existing documentation
4. **Tests passing:** All acceptance criteria have passing tests
5. **Documentation complete:** README with setup instructions and usage examples
6. **Demo verified:** A non-technical user can follow instructions to run a demo

---

## 7. Out of Scope (MVP)

### 7.1 Explicitly Not Building

| Feature | Rationale | Future Consideration |
|---------|-----------|---------------------|
| **Real SalesLoft API integration** | MVP uses local files; API requires auth, rate limiting, error handling | Phase 2 |
| **Sentiment analysis tool** | Adds complexity without core value demonstration | Phase 2 |
| **Competitive intelligence extraction** | Requires NLP beyond basic search | Phase 2 |
| **Objection categorization** | Would need trained model or complex heuristics | Phase 2 |
| **Deal health scoring** | Requires integration with CRM data | Phase 2 |
| **Prompt templates** | MCP prompts feature is less critical for demo | Phase 2 |
| **Statistics/aggregation resources** | Nice-to-have analytics | Phase 2 |
| **Multi-user authentication** | Local demo does not require auth | Phase 2 |
| **Transcript upload/creation** | Read-only for MVP | Phase 2 |
| **Real-time call processing** | Would require streaming integration | Future |

### 7.2 Future Enhancement Roadmap

**Phase 2: Enhanced Analysis**
- Sentiment analysis per speaker
- Objection detection and categorization
- Competitive mention extraction
- Topic modeling across calls

**Phase 3: Integration**
- Real SalesLoft Conversations API integration
- Clari deal stage correlation
- CRM sync for deal context

**Phase 4: Intelligence**
- Deal health scoring based on call signals
- Recommended follow-up actions
- Coaching suggestions for reps

---

## 8. Open Questions and Risks

### 8.1 Open Questions

| Question | Impact | Owner | Target Resolution |
|----------|--------|-------|-------------------|
| What frontmatter fields are required vs. optional? | Data model design | Product | Before development |
| Should search support boolean operators (AND/OR)? | Search complexity | Engineering | Sprint planning |
| How should we handle very long transcripts (60+ min calls)? | Performance, UX | Engineering | During development |
| Should excerpts include speaker attribution in search results? | User experience | Product | During development |

### 8.2 Assumptions

| Assumption | Risk if Wrong | Mitigation |
|------------|---------------|------------|
| Users have Claude Code installed and configured | Demo fails | Provide setup instructions |
| Sample transcripts are representative enough | Demo lacks impact | Base on real interview patterns |
| STDIO transport is sufficient | Integration issues | Test early with Claude Desktop |
| Python 3.11+ is available | Environment issues | Document requirements clearly |

### 8.3 Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| **MCP SDK changes** | Low | High | Pin SDK version, monitor releases |
| **Transcript parsing edge cases** | Medium | Medium | Robust error handling, validation |
| **Search performance on many transcripts** | Low | Low | MVP has few files; optimize later |
| **Demo requires technical setup** | High | Medium | Clear README, video walkthrough |
| **Claude misinterprets tool results** | Medium | Medium | Well-structured JSON responses, clear field names |

### 8.4 Dependencies

| Dependency | Type | Risk Level | Contingency |
|------------|------|------------|-------------|
| MCP Python SDK (`mcp>=1.2.0`) | External library | Low | Well-maintained by Anthropic |
| `python-frontmatter` | External library | Low | Mature, stable library |
| Claude Code | Runtime environment | Low | Primary supported environment |
| Python 3.11+ | Runtime | Low | Widely available |

---

## Appendix A: Sample Transcript Structure

Based on the existing documentation, sample transcripts should follow this pattern:

```markdown
---
call_id: "interview_telecom_nexus_20250115"
date: "2025-01-15T14:30:00Z"
duration_seconds: 1920
rep_name: "Mitchell Chen"
prospect_name: "Jeffrey Moore"
prospect_company: "TeleCom Nexus"
prospect_title: "Chief Revenue Officer"
additional_attendees:
  - name: "Sophia Rodriguez"
    title: "Director of Sales Operations"
deal_stage: "Discovery"
deal_value: 500000
disposition: "Follow-up Scheduled"
tags: ["enterprise", "telecom", "pipeline-visibility", "5g", "stakeholder-alignment"]
key_themes:
  - "Pipeline visibility gap"
  - "5G budget competition"
  - "Network/IT misalignment"
---

# Customer Interview: TeleCom Nexus

## Interview Summary

Jeffrey Moore is the CRO of TeleCom Nexus, a telecom software company at $125M ARR. The conversation explored challenges around carrier procurement cycles, 5G investment competition, and organizational stakeholder dynamics.

## Full Transcript

**[00:00:15] Mitchell Chen:**
Jeffrey, Sophia - thanks so much for taking the time today...

[Transcript continues...]

## Key Takeaways

1. **Pipeline Visibility Gap**: Deals stall in procurement with no visibility
2. **5G Budget Competition**: Infrastructure investment crowding out software
3. **Stakeholder Misalignment**: Network and IT teams have conflicting priorities
```

---

## Appendix B: Common Pain Points from Research

Based on the 50 personas and interviews analyzed, these are the most common themes that should be searchable in sample transcripts:

**Forecast and Pipeline:**
- Forecast accuracy issues
- Deal slippage surprises
- Pipeline visibility gaps
- Stage definition inconsistency

**Sales Productivity:**
- Admin burden reducing selling time
- Tool sprawl and context switching
- CRM hygiene problems
- Activity logging resistance

**Stakeholder Management:**
- Multi-threaded deal complexity
- Champion dependency risk
- Procurement bottlenecks
- IT vs. Business buyer dynamics

**Competitive:**
- Price pressure
- Platform bundling threats
- Speed-to-respond challenges
- Feature parity commoditization

**Knowledge and Enablement:**
- Rep turnover knowledge loss
- Playbook gaps
- Onboarding ramp time
- Coaching scalability

---

*End of Product Requirements Document*
