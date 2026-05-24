"""MCP stdio client demo —— 真正走 MCP 协议验证 server.py。"""
from __future__ import annotations
import asyncio
import json
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    params = StdioServerParameters(command=sys.executable, args=["server.py"])
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            print(f"✓ 发现 {len(tools.tools)} 个 tool:")
            for t in tools.tools:
                print(f"  - {t.name}: {t.description.splitlines()[0] if t.description else ''}")
            print("\n--- 调用 rag_health ---")
            res = await session.call_tool("rag_health", {})
            print(json.dumps(res.structuredContent, ensure_ascii=False, indent=2))
            print("\n--- 调用 rag_list_collections ---")
            res = await session.call_tool("rag_list_collections", {})
            data = res.structuredContent.get("result", [])
            print(f"共 {len(data)} 个 collection: {[x['name'] for x in data]}")


if __name__ == "__main__":
    asyncio.run(main())
