# 21-memory — Agent 记忆明星仓库

> Agent 记忆专题。从短期对话窗到长期事实图谱，覆盖 4 套主流方案。

| 仓库 | 星 | 体量 | 抄什么 |
|---|---|---|---|
| 🥇 **[mem0](./mem0/)** | 30k★ | 47M / 360 py | 自动事实抽取+冲突合并；ships `skills/` 目录 + AGENTS.md + CLAUDE.md + `openmemory/` MCP 服务 |
| 🥈 **[letta](./letta/)** | 15k★ | 25M / 878 py | 前 MemGPT；分层记忆（core/recall/archival）+ 持久 agent state |
| **[zep](./zep/)** | 3k★ | 190M / 129 py | Go 实现，Knowledge Graph 记忆服务（已转型 ZepCloud） |
| **[cognee](./cognee/)** | 5k★ | 76M / 1524 py | 知识图谱式记忆；ECL 管线；AGENTS.md+CLAUDE.md |

## 抄作业重点
- **mem0/openmemory/** — 自家 MCP 记忆服务参考（最热门方案）
- **mem0/skills/** + AGENTS.md — 记忆产品的 agent-friendly 范本
- **letta/letta/agent.py** — MemGPT 的 core+archival 分层结构
- **cognee/cognee/modules/cognify/** — ECL（Extract-Cognify-Load）知识图谱管线
