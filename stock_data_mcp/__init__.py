"""
Stock Data MCP Server

薄壳项目：将 open-stock-data 的工具函数注册为 MCP tool。
"""

import os
import argparse
from starlette.middleware.cors import CORSMiddleware

from ._version import __version__
from .server import mcp


def main():
    """MCP 服务器入口"""
    port = int(os.getenv("PORT", 0)) or 80
    parser = argparse.ArgumentParser(description="Stock Data MCP Server")
    parser.add_argument("--http", action="store_true", help="Use streamable HTTP mode instead of stdio")
    parser.add_argument("--host", default="0.0.0.0", help="Host to bind to (default: 0.0.0.0)")
    parser.add_argument("--port", type=int, default=port, help=f"Port to listen on (default: {port})")

    args = parser.parse_args()
    mode = os.getenv("TRANSPORT") or ("http" if args.http else None)
    if mode in ["http", "sse"]:
        app = mcp.http_app(transport=mode)
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["GET", "POST", "OPTIONS"],
            allow_headers=["*"],
            expose_headers=["mcp-session-id", "mcp-protocol-version"],
            max_age=86400,
        )
        mcp.run(transport=mode, host=args.host, port=args.port)
    else:
        mcp.run()


if __name__ == "__main__":
    main()
