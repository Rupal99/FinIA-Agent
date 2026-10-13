# AI-Powered Investment Research & Analysis Agent

## Architecture

The system uses LangGraph to orchestrate a multi-agent investment research workflow. A Supervisor Agent coordinates the research process, gathers insights from specialized research subgraphs, and passes the results through sequential financial analysis stages to generate a final investment report.

### Agent Workflow

```text
                         USER
                           |
                           v
                      SUPERVISOR
                           |
              +------------+------------+
              |                         |
              v                         v
      FINANCIAL RESEARCH         MARKET/NEWS RESEARCH
          SUBGRAPH                   SUBGRAPH
              |                         |
              +------------+------------+
                           |
                           v
                    VALUATION AGENT
                           |
                           v
                       RISK AGENT
                           |
                           v
                 INVESTMENT COMMITTEE
                           |
                           v
                      FINAL REPORT
```

### Workflow Components

1. **Supervisor Agent**
   - Receives the user's investment research query.
   - Orchestrates the research workflow.
   - Coordinates the Financial Research and Market/News Research subgraphs.
   - Aggregates research outputs and passes them to the downstream analysis agents.

2. **Financial Research Subgraph**
   - Analyzes a company's financial performance.
   - Examines financial statements, revenue, profitability, and other relevant financial metrics.
   - Provides financial insights to support investment decisions.

3. **Market/News Research Subgraph**
   - Researches relevant market developments and financial news.
   - Identifies industry trends, company announcements, and market-moving events.
   - Provides contextual insights that may influence investment decisions.

4. **Valuation Agent**
   - Evaluates the company's valuation using available financial data and research findings.
   - Assesses relevant valuation metrics and investment opportunities.
   - Produces a valuation assessment for the next stage.

5. **Risk Agent**
   - Identifies potential financial, business, and market risks.
   - Evaluates risks associated with the investment opportunity.
   - Produces a risk assessment for the Investment Committee.

6. **Investment Committee**
   - Reviews the financial research, market insights, valuation, and risk assessment.
   - Synthesizes the findings into an investment recommendation.
   - Evaluates the overall investment opportunity based on the available evidence.

7. **Final Report**
   - Consolidates the outputs from the research and analysis stages.
   - Presents the investment thesis, valuation insights, key risks, and final recommendation.
   - Delivers a structured report in response to the user's query.

## MCP Usage

The system uses the Model Context Protocol (MCP) to connect LangGraph agents to external tools and data sources.

```text
                      LANGGRAPH
                           |
                           v
                       MCP CLIENTS
                           |
              +------------+------------+
              |            |            |
              v            v            v
       FINANCIAL MCP   SEARCH MCP   MARKET MCP
              |            |            |
              v            v            v
       FINANCIAL DATA  WEB SOURCES  MARKET DATA
```

### MCP Components

- **Financial MCP:** Provides access to financial data and relevant financial information.
- **Search MCP:** Enables web search and retrieval of relevant research sources.
- **Market MCP:** Provides access to market data and related information.

MCP clients allow the LangGraph workflow to interact with external data sources through standardized tool interfaces.

## Planned Future Enhancement

### Industry & Competitor Research Subgraph

An Industry & Competitor Research Subgraph will be introduced in a future iteration.

This subgraph will focus on:

- Industry analysis and market positioning.
- Competitor identification and comparison.
- Competitive advantages and business differentiation.
- Industry trends and growth opportunities.

It will be integrated into the Supervisor's research workflow alongside the existing Financial Research and Market/News Research subgraphs.

For the current implementation, the workflow consists of only two research subgraphs: Financial Research and Market/News Research.

## Technology Stack

- **Python:** Core implementation language.
- **LangGraph:** Multi-agent orchestration and workflow management.
- **MCP (Model Context Protocol):** Standardized integration with external tools and data sources.
- **Financial Data Sources:** Financial metrics and company information.
- **Web Search:** Market news and relevant research sources.

## Project Goal

Build a modular, multi-agent investment research system that combines financial analysis, market intelligence, valuation, and risk assessment to produce structured, evidence-based investment reports.