# stock-data-mcp

MCP Server for stock and crypto data with multi-source failover.

Thin wrapper over [open-stock-data](https://github.com/openstockdata/open-stock-data) — registers 47 tool functions as MCP tools via FastMCP.

## Install

```bash
pip install stock-data-mcp
```

## Usage

```bash
# stdio mode (default)
stock-data-mcp

# HTTP mode
stock-data-mcp --http --host 0.0.0.0 --port 8808

# Add to Claude Code
claude mcp add stock-data -- uvx stock-data-mcp
```
