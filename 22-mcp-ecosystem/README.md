# 22-mcp-ecosystem — Model Context Protocol 生态

| 仓库 | 星 | 体量 | 抄什么 |
|---|---|---|---|
| 🥇 **[mcp-servers](./mcp-servers/)** | 60k★ | 2.1M | **官方参考服务器**：everything / fetch / filesystem / git / memory / sequentialthinking / time；CLAUDE.md |
| 🥇 **[mcp-python-sdk](./mcp-python-sdk/)** | 16k★ | 4.8M / 356 py | **官方 Python SDK**；AGENTS.md+CLAUDE.md |
| 🥈 **[mcp-agent](./mcp-agent/)** | 8k★ | 50M / 596 py | lastmile-ai；用 MCP 写 agent，含 workflow + orchestrator |
| **[awesome-mcp-servers](./awesome-mcp-servers/)** | 60k★ | 1.7M | punkpeye 维护的索引（社区 MCP server 列表） |

## 抄作业重点
- **mcp-servers/src/{fetch,filesystem,git,memory,time}/** — 写 MCP server 的 7 个官方范本
- **mcp-python-sdk/src/mcp/server/fastmcp.py** — FastMCP 装饰器 API（写 server 的最简方式）
- **mcp-agent/src/mcp_agent/workflows/** — 在 MCP 上编排 agent 的模式

## 自家项目对接（rag-dashboard / hermes-agent）
- 抄 `mcp-servers/src/memory/` 实现自家 memory MCP
- 抄 `mcp-python-sdk` 的 FastMCP 模式重构现有 tool 接口
