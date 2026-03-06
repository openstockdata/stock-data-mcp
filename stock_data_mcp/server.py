"""
MCP 服务器模块

将 open-stock-data 的工具函数批量注册为 MCP tool。
"""

from fastmcp import FastMCP
from open_stock_data.tools import TOOL_REGISTRY

from ._version import __version__

mcp = FastMCP(name="stock-data-mcp", version=__version__)

# 批量注册所有工具
for _name, (_fn, _title, _desc) in TOOL_REGISTRY.items():
    mcp.tool(title=_title, description=_desc)(_fn)
