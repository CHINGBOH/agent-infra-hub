# 09-agent-infra-catalog — Agent 架构基础设施候选库

本目录用于收集还未下载到本仓库的 GitHub 候选项目，覆盖 awesome 索引、skills 系统、Agent 编排、路由网关、门控治理、HUD/观测等方向。

当前策略是 **metadata first**：先维护结构化清单，再按优先级下载源码。这样可以避免仓库快速膨胀，同时让后续 SQLite / FTS / MCP 查询层有稳定输入。

## 文件

```
09-agent-infra-catalog/
├── README.md
├── catalog.yaml
├── BEST-OF-STACK.md                          ← 🌟 22 模块最优 Agent 拼装蓝图
└── 2026-05-25-three-new-repos-analysis.md    ← agentmemory + scientific-skills + OMC 三仓库分析
```

## 🌟 BEST-OF-STACK.md

跨 17 个仓库（5 个 agent_research champions + 12 个 agent-infra-hub）拆成 **4 层 22 个模块**，
每个模块都有 🥇主选 + 🥈备选 + ⛔反面，附确切文件路径。是"做 agent 应该抄谁哪个文件"的单一可信源。

涵盖：
- A. 核心运行时 9 模块（loop / memory / tools / MCP / hooks / provider / streaming / sandbox / prompt）
- B. 技能层 3 模块（skill-registry / skill-content / skill-discovery）
- C. 编排层 5 模块（planner / team-swarm / subagent / worktree / hand-off-protocol）
- D. 开发运维 5 模块（replay / eval / observability / CLI / setup）

附 3 套现成拼装姿势：极简（500 行）/ 生产单 agent（5k 行）/ Multi-agent（10k+ 行）。

## 分类

| 分类 | 说明 |
|------|------|
| `awesome-indexes` | awesome/curated 索引仓库，用于发现更多项目 |
| `orchestrators` | 多 Agent 编排、DAG、worker pool、workflow runtime |
| `routing-gateways` | LLM/Agent gateway、模型路由、fallback、MCP/A2A proxy |
| `governance-guardrails` | policy enforcement、sandbox、audit、quality gate |
| `observability-hud` | dashboard、HUD、statusline、hook telemetry |
| `skill-systems` | skills、plugin、capability routing、runtime projection |

## 使用建议

1. 先读取 `catalog.yaml`，按 `priority: high` 过滤。
2. 对 `import_mode: metadata_first` 的仓库只进入数据库索引，不下载源码。
3. 对 `import_mode: clone_candidate` 的仓库可批量 clone 到对应分类目录。
4. 后续 SQLite 表可以直接映射 `category`、`artifact_types`、`agent_layers`、`capabilities`、`source_url`。


## 本地浅克隆源码

以下仓库已按分类浅克隆到本地工作区，用于人工审阅和资料抽取。公开主仓只提交 `catalog.yaml` 等元数据，不 vendor 这些第三方仓库源码；分类目录已由 `.gitignore` 忽略。

| 分类 | 本地路径 |
|------|----------|
| `awesome-indexes` | `awesome-indexes/awesome-multi-agent-orchestrators` |
| `awesome-indexes` | `awesome-indexes/awesome-ai-agent-governance` |
| `orchestrators` | `orchestrators/agent-kit` |
| `orchestrators` | `orchestrators/open-multi-agent` |
| `routing-gateways` | `routing-gateways/portkey-gateway` |
| `routing-gateways` | `routing-gateways/agentgateway` |
| `governance-guardrails` | `governance-guardrails/agent-governance-toolkit` |
| `observability-hud` | `observability-hud/claude-code-dashboard` |
| `skill-systems` | `skill-systems/agent-skills` |
| `skill-systems` | `skill-systems/oh-my-codex` |

## 优先导入顺序

```
1. Agent-Analytics/awesome-multi-agent-orchestrators
2. microsoft/agent-governance-toolkit
3. agentgateway/agentgateway
4. inngest/agent-kit
5. open-multi-agent/open-multi-agent
6. jscraik/Agent-Skills
7. ek33450505/claude-code-dashboard
8. scalarian/oh-my-codex
```
