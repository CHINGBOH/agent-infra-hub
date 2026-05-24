# PoC S — MCP-native（rag-dashboard 当 MCP server）

把 `/home/l/projects/rag-dashboard` 的 REST 后端包成 **MCP server**，
Claude Code / Cursor / 任何 MCP client 都能直接调用本地 RAG + Nexus agent。

> 组合 S 的意思：**S**ingle-process，stdio MCP，零中间件。
> 14 种组合中最轻量的"接入姿势"PoC。

## 它能做什么

8 个 MCP tool 一对一映射 rag-dashboard 的常用接口：

| Tool | 后端 endpoint | 用途 |
| --- | --- | --- |
| `rag_health` | `GET /health` | 体检（pg / qdrant / cache） |
| `rag_list_collections` | `GET /api/v1/collections` | 看向量库里有哪些 collection |
| `rag_search` | `POST /api/search` | 纯检索（hybrid / vector / keyword / graph） |
| `rag_agent_query` | `POST /api/v1/agent` | 走 Nexus agent（多轮 + 工具调用） |
| `rag_get_trace` | `GET /api/v1/agent/trace/{id}` | 取回某次 agent 的完整 trace |
| `rag_list_traces` | `GET /api/v1/agent/traces` | 最近 N 个 trace 摘要 |
| `rag_architecture_live` | `GET /api/v1/architecture/live` | 自家服务/文档拓扑 |
| `rag_feature_flags` | `GET /api/v1/feature-flags/` | runtime flag 状态 |

## 前置条件

- rag-dashboard 后端在 `http://127.0.0.1:8002` 跑着
  （`cd ~/projects/rag-dashboard/src/backend/retrieval-service && uvicorn main:app --port 8002`）
- Python ≥ 3.10
- `pip install -r requirements.txt`

## 三步跑通

```bash
# 1) 装依赖
pip install -r requirements.txt

# 2) 直连冒烟（不走 MCP 协议，直接调函数确认后端通）
python smoke.py

# 3) MCP stdio 客户端 demo（真正走 JSON-RPC）
python client_demo.py
```

`client_demo.py` 预期输出：
```
✓ 发现 8 个 tool: ...
共 9 个 collection: ['agent_lecture_kb', 'yanmei_skincare_kb', ...]
```

## 注册到 Claude Code

把下面写进 `~/.config/claude/mcp.json`（或 Claude Desktop 等价文件）：

```json
{
  "mcpServers": {
    "rag-dashboard": {
      "command": "python",
      "args": ["/home/l/projects/agent-infra-hub/poc/S-mcp-native/server.py"],
      "env": {
        "RAG_API": "http://127.0.0.1:8002"
      }
    }
  }
}
```

Cursor / Continue 等也是同一格式。重启客户端后 `/mcp` 应看到 `rag-dashboard` 8 个 tool。

## HTTP 模式（调试 / 多客户端共享）

```bash
python server.py --http --port 8765
# 客户端连 http://127.0.0.1:8765/mcp
```

## 环境变量

| Var | 默认 | 说明 |
| --- | --- | --- |
| `RAG_API` | `http://127.0.0.1:8002` | rag-dashboard 后端地址 |
| `RAG_TIMEOUT` | `60` | httpx 超时（秒）|

## 设计要点（抄作业用）

1. **`trust_env=False`** —— 必须！本机 socks 代理会让 httpx 报 `Unknown scheme for proxy URL`。
2. **FastMCP 而非 `MCPServer`** —— 仓库 `examples/mcpserver/` 里的 `from mcp.server.mcpserver import MCPServer` 在 v1.23.3 已不存在；用 `from mcp.server.fastmcp import FastMCP`。
3. **stdio 当默认**，HTTP 走 `--http` —— Claude Code 标准是 stdio，开发调试时 HTTP 更方便看包。
4. **类型注解 = schema** —— `query: str, top_k: int = 10` 这种签名直接被 FastMCP 转成 JSON-Schema 给 client。
5. **structuredContent 取数** —— FastMCP 1.20+ 把返回值放在 `result.structuredContent`，不要去拼 `content[i].text`，否则数组会被拆成 N 个 text 项。

## 下一步（其它组合 PoC 排期）

- **P · 记忆持久化**（mem0 + rag-dashboard）
- **O · 沙箱执行**（e2b/daytona 跑 agent 生成的代码）
- **R · 实时语音**（livekit-agents 包同一份 tool）
- **Q · MCP 网关**（多个 MCP server 聚合）

详见 `09-agent-infra-catalog/BEST-OF-STACK.md` 第 18 层矩阵。
