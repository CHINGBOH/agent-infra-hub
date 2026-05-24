# 12-go-backend — Go 后端"抄作业"参考

> 2026-05-25 浅克隆 6 个 Go 后端明星仓库（合计 ~110 MB）。详细分析见 [../09-agent-infra-catalog/2026-05-25-backend-stack-analysis.md](../09-agent-infra-catalog/2026-05-25-backend-stack-analysis.md)。

## 仓库清单

| 仓库 | Star | 大小 | 模块 | 抄什么 |
|---|---|---|---|---|
| [ollama/](ollama/) | 100k+ | 15M | 本地 LLM serving | `server/` + 🔥 `anthropic/anthropic.go`（双协议） |
| [eino/](eino/) | 3k+ | 14M | LLM 框架 | `adk/turn_loop.go` + `flow/{agent,indexer,retriever}/` |
| [langchaingo/](langchaingo/) | 5k+ | 20M | LangChain Go 端口 | 迁移场景；新项目优先 eino |
| [weaviate/](weaviate/) | 12k+ | 49M | 向量 DB（生产级） | `adapters/` + `modules/` |
| [mcp-go/](mcp-go/) | 4k+ | 3.6M | MCP server SDK | `server/hooks.go` + `server/elicitation.go` + `otel/` |
| [gptscript/](gptscript/) | 3k+ | 9.8M | 声明式 LLM 脚本 | `pkg/runner/` + `pkg/tools/` |

## 推荐组合

**完整 Go agent**：`ollama + eino + weaviate + mcp-go + gptscript`  
→ 单一 Go 运行时栈，适合 Hermes/BeautyOS 这种已有 Go 基础设施的项目。

## ⭐ 看点

- **ollama 自带 Anthropic 兼容层**（`anthropic/anthropic.go`）— Claude Code 可直接指向 ollama
- **eino > langchaingo**：ByteDance spawn，agent loop / interrupt / cancel / failover 齐全；新项目首选
- **weaviate 自带 CLAUDE.md** — 含强硬 "No bug is ever out of scope" 工程文化，是给 agent 协作的范本
- **mcp-go 已支持 elicitation** — MCP 最新双向交互能力
