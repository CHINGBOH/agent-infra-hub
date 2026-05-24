"""
rag-dashboard MCP server (PoC S — MCP-native)

把 rag-dashboard 的 REST API 包装成 MCP tools，让 Claude Code / 任何 MCP client
可以直接调用本地 RAG 检索 + agent 推理。

Run:
  stdio (Claude Code 标配):
    python server.py
  HTTP (调试):
    python server.py --http --port 8765
"""
from __future__ import annotations

import os
import sys
import httpx
from mcp.server.fastmcp import FastMCP

RAG_API = os.environ.get("RAG_API", "http://127.0.0.1:8002")
TIMEOUT = float(os.environ.get("RAG_TIMEOUT", "60"))

mcp = FastMCP("rag-dashboard")


def _client() -> httpx.Client:
    # rag-dashboard 在本机 127.0.0.1，必须绕过环境代理
    return httpx.Client(base_url=RAG_API, timeout=TIMEOUT, trust_env=False)


@mcp.tool()
def rag_health() -> dict:
    """检查 rag-dashboard 后端 + 数据库 + qdrant + cache 健康状态。"""
    with _client() as c:
        r = c.get("/health")
        r.raise_for_status()
        return r.json()


@mcp.tool()
def rag_list_collections() -> list[dict]:
    """列出 qdrant 中所有 collection（名称 / 向量数 / 状态）。"""
    with _client() as c:
        r = c.get("/api/v1/collections")
        r.raise_for_status()
        return r.json().get("collections", [])


@mcp.tool()
def rag_search(
    query: str,
    top_k: int = 10,
    mode: str = "hybrid",
    filters: dict | None = None,
    session_id: str | None = None,
) -> dict:
    """对 rag-dashboard 做一次纯检索（不经过 agent 推理）。

    Args:
        query: 检索文本
        top_k: 返回 top-k 命中（1-100）
        mode: vector / keyword / graph / hybrid
        filters: 元数据过滤，如 {"doc_type": "lecture"}
        session_id: 复用会话上下文（可选）
    """
    payload = {"query": query, "top_k": top_k, "mode": mode}
    if filters:
        payload["filters"] = filters
    if session_id:
        payload["session_id"] = session_id
    with _client() as c:
        r = c.post("/api/search", json=payload)
        r.raise_for_status()
        return r.json()


@mcp.tool()
def rag_agent_query(
    query: str,
    session_id: str | None = None,
    max_iterations: int = 3,
    llm_route: str = "deepseek",
) -> dict:
    """提交问题给 rag-dashboard Nexus agent（带工具调用 + 多轮推理）。

    Args:
        query: 用户问题
        session_id: 会话 id（不传会自动新建）
        max_iterations: agent 最大迭代轮数
        llm_route: deepseek / openai / ollama 等路由 key
    """
    payload = {
        "query": query,
        "max_iterations": max_iterations,
        "llm_route": llm_route,
    }
    if session_id:
        payload["session_id"] = session_id
    with _client() as c:
        r = c.post("/api/v1/agent", json=payload)
        r.raise_for_status()
        return r.json()


@mcp.tool()
def rag_get_trace(trace_id: str) -> dict:
    """根据 trace_id 取回某次 agent 执行的完整 trace（每步工具调用 + 时延）。"""
    with _client() as c:
        r = c.get(f"/api/v1/agent/trace/{trace_id}")
        r.raise_for_status()
        return r.json()


@mcp.tool()
def rag_list_traces(limit: int = 20) -> list[dict]:
    """列出最近 N 个 agent trace 摘要（看跑了什么、有没有错）。"""
    with _client() as c:
        r = c.get("/api/v1/agent/traces", params={"limit": limit})
        r.raise_for_status()
        data = r.json()
        if isinstance(data, dict):
            return data.get("traces", [])
        return data


@mcp.tool()
def rag_architecture_live() -> dict:
    """实时仓库架构（自家文档/服务/工具的拓扑图，用于 self-introspection）。"""
    with _client() as c:
        r = c.get("/api/v1/architecture/live")
        r.raise_for_status()
        return r.json()


@mcp.tool()
def rag_feature_flags() -> dict:
    """读取 runtime feature flag 状态。"""
    with _client() as c:
        r = c.get("/api/v1/feature-flags/")
        r.raise_for_status()
        return r.json()


def main():
    if "--http" in sys.argv:
        port = 8765
        if "--port" in sys.argv:
            port = int(sys.argv[sys.argv.index("--port") + 1])
        mcp.settings.host = "127.0.0.1"
        mcp.settings.port = port
        mcp.run(transport="streamable-http")
    else:
        mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
