# stock-data-mcp

MCP Server for stock and crypto data with multi-source failover.

### Multi-Source Data Provider

The `data_provider` module implements automatic failover across multiple data sources:

**Global Priority:**

| Priority | Fetcher | Condition | Markets |
|----------|---------|-----------|---------|
| 0 | TushareFetcher | Has TUSHARE_TOKEN | A-shares |
| 1 | EfinanceFetcher | Default | A-shares, ETF |
| 2 | AkshareFetcher | Default | A-shares, ETF, HK |
| 3 | BaostockFetcher | Default | A-shares |
| 4 | AlphaVantageFetcher | Has API key | US stocks |
| 5 | YfinanceFetcher | Default | Global |

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
claude mcp add stock-data \
    -e TUSHARE_TOKEN=your_token \
    -e ALPHA_VANTAGE_API_KEY=your_key \
    -e OKX_BASE_URL=https://okx.4url.cn\
    -e BINANCE_BASE_URL=https://bian.4url.cn \
    -- uvx stock-data-mcp
```
<details>
<summary>Environment Variables (Optional)</summary>

| Variable | Description |
|----------|-------------|
| `TUSHARE_TOKEN` | Tushare Pro API Token (high-priority A-share data source) |
| `ALPHA_VANTAGE_API_KEY` | Alpha Vantage API Key (enhanced US data, falls back to yfinance if not set) |
| `OKX_BASE_URL` | OKX API proxy URL |
| `BINANCE_BASE_URL` | Binance API proxy URL |
| `NEWSNOW_CHANNELS` | NewsNow financial news channel list (default: `wallstreetcn-quick,cls-telegraph,jin10`) |

</details>
