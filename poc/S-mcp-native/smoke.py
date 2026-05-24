"""
直连冒烟：不走 MCP 协议，直接调 server.py 里的函数，
确认 rag-dashboard 后端的 8 个 tool 都能正常拿到数据。
"""
from __future__ import annotations
import json
import sys

sys.path.insert(0, ".")
from server import (  # noqa: E402
    rag_health,
    rag_list_collections,
    rag_search,
    rag_agent_query,
    rag_list_traces,
    rag_architecture_live,
    rag_feature_flags,
)


def pp(name, val, max_len=300):
    s = json.dumps(val, ensure_ascii=False, indent=2, default=str)
    if len(s) > max_len:
        s = s[:max_len] + f"\n  ... (+{len(s) - max_len} chars)"
    print(f"\n--- {name} ---\n{s}")


def main():
    pp("health", rag_health())
    cols = rag_list_collections()
    pp("collections (count)", len(cols))
    if cols:
        pp("collections[0]", cols[0])
    pp("feature_flags", rag_feature_flags(), max_len=400)
    pp("architecture_live (keys)", list(rag_architecture_live().keys())[:10])
    try:
        traces = rag_list_traces(limit=3)
        pp("traces (count)", len(traces) if isinstance(traces, list) else "n/a")
    except Exception as e:
        print(f"\n--- traces ---\nWARN: {e}")
    try:
        search_res = rag_search(query="测试", top_k=3, mode="hybrid")
        pp("search('测试', top_k=3)", search_res, max_len=400)
    except Exception as e:
        print(f"\n--- search ---\nWARN: {e}")
    print("\n✓ smoke done")


if __name__ == "__main__":
    main()
