# agent-infra-hub — AI 写代码轮子库

> **AI Agent 导航入口。** 本文档是仓库导航中枢，AI agent 直接读此文件以定位所需组件。  
> 机器可读索引：[catalog.json](catalog.json) | 人类文档：[README.md](README.md)

---

## 一句话定位

本仓库是 **AI 写代码的基础配置轮子库**：预装了可直接取用的 Skills、Agent 架构模式、基础设施组件、外部库知识图谱。目标消费者是 AI agent，来此 **取件** 而非阅读文档。

---

## 快速定位（按意图）

| 我需要… | 路径 |
|---------|------|
| **找一个现成 Skill** 来注入 Claude 的能力 | → [Skills 目录](#skills) |
| **设计多 Agent 协作架构** | → [Agent 设计模式](#agent-patterns) |
| **配置 Hooks / Context / MCP / Isolation** | → [基础设施组件](#infrastructure) |
| **查询外部库的代码结构**（yt-dlp、odoo 等） | → [知识图谱](#knowledge-graphs) |
| **本地语义检索**仓库内容 | → [工具](#tools) |
| **发现更多社区 skills/agents** | → [社区 Catalogs](#catalogs) |
| **Skill 系统原理深入研究** | → [skill-research/README.md](skill-research/README.md) |
| **Agent 基础设施候选库（待引入）** | → [09-agent-infra-catalog/README.md](09-agent-infra-catalog/README.md) |

---

## Skills

> 可直接注入 Claude 能力的 SKILL.md 型组件。按领域分组。

### Anthropic 官方 Personal Skills（9个）

完整文档：[skill-research/11-anthropic-personal-skills/README.md](skill-research/11-anthropic-personal-skills/README.md)

| Skill | 触发场景 | 关键能力 | 详情 |
|-------|---------|---------|------|
| `algorithmic-art` | 生成算法艺术/生成艺术 | 哲学创作(.md) → p5.js 实现(.html+.js)，两阶段工作流 | [→](skill-research/11-anthropic-personal-skills/algorithmic-art/README.md) |
| `canvas-design` | 设计海报/视觉创意作品 | 哲学构思(.md) → 画布创作(.pdf/.png)，museum quality | [→](skill-research/11-anthropic-personal-skills/canvas-design/README.md) |
| `doc-coauthoring` | 联合撰写复杂文档 | 3阶段：情境收集→结构精炼→读者测试，支持子 Agent | [→](skill-research/11-anthropic-personal-skills/doc-coauthoring/README.md) |
| `internal-comms` | 企业内部通讯/公告 | 路由分发模式：识别类型→加载模板→执行 | [→](skill-research/11-anthropic-personal-skills/internal-comms/README.md) |
| `mcp-builder` | 构建 MCP Server | 4阶段：研究→实现→审查测试→评估(10题XML) | [→](skill-research/11-anthropic-personal-skills/mcp-builder/README.md) |
| `skill-creator` | 创建 Claude Code Skill | eval 循环：with-skill vs baseline 子 agent 对比 | [→](skill-research/11-anthropic-personal-skills/skill-creator/README.md) |
| `slack-gif-creator` | 创建 Slack GIF 表情/消息 | GIFBuilder + PIL，Emoji GIF 128×128，消息 480×480 | [→](skill-research/11-anthropic-personal-skills/slack-gif-creator/README.md) |
| `theme-factory` | 为 Artifacts 应用主题样式 | 占位（SKILL.md 内容待补充） | [→](skill-research/11-anthropic-personal-skills/theme-factory/README.md) |
| `web-artifacts-builder` | 构建复杂多组件 HTML Artifact | 占位（SKILL.md 内容待补充） | [→](skill-research/11-anthropic-personal-skills/web-artifacts-builder/README.md) |

### MCP 构建专项 Skills（3套）

| Skill 套件 | 侧重 | 关键文件 |
|-----------|------|---------|
| `build-mcp-server` | MCP Server 完整开发流程，含 SDK 参考 | [skill-research/build-mcp-server/](skill-research/build-mcp-server/) |
| `build-mcp-app` | MCP App 交互 UI 组件，6个 widget 模板 | [skill-research/build-mcp-app/](skill-research/build-mcp-app/) |
| `build-mcpb` | MCPB 本地捆绑包，manifest schema + 安全指南 | [skill-research/build-mcpb/](skill-research/build-mcpb/) |

### 数据分析 Skills（12个，中文）

来源：[01-data-analysis/claude-data-analysis-ultra/](01-data-analysis/claude-data-analysis-ultra/)  
关键文件：`SKILLS_USAGE.md`（调用规范）

| Skill | 功能 |
|-------|------|
| RFM 客户分群 | Recency/Frequency/Monetary 聚类 |
| LTV 预测器 | 用户生命周期价值建模 |
| 留存分析 | 队列留存率矩阵 |
| 漏斗分析 | 转化漏斗 + 流失定位 |
| A/B Test | 显著性检验 + 效应量 |
| 增长模型 | 用户增长拟合 |
| 回归分析建模 | 多元线性/Logistic |
| 异常检测 | 统计异常值识别 |
| 时序分析 | 趋势/季节性分解 |
| 用户画像 | 聚类 + 标签生成 |
| 数据质量报告 | 缺失值/异常/分布检测 |
| 自动化报告 | Markdown 报告生成 |

### R / Quarto Skills

| 来源 | Skills | 路径 |
|------|--------|------|
| Posit 官方 | quarto, tidyverse, r-lib, shiny, brand-yml, ggsql, alt-text | [02-r-quarto/posit-dev-skills/](02-r-quarto/posit-dev-skills/) |
| wolf5996/agentic-skills | writing-r-code, writing-qmd-scientific, creating-analysis-projects, developing-r-packages, git-hygiene, md-format | [02-r-quarto/agentic-skills/](02-r-quarto/agentic-skills/) |
| ClaudeR | R MCP + 统计核验（反幻觉手稿审计协议） | [02-r-quarto/ClaudeR/](02-r-quarto/ClaudeR/) |

### 学术研究 Skills

路径：[04-research/academic-research-skills/](04-research/academic-research-skills/)  
流程：研究 → 写作 → 审阅 → 定稿

### Superpowers 插件 Skills（深度研究）

路径：[skill-research/05-examples/superpowers-skills/](skill-research/05-examples/superpowers-skills/)  
包含：brainstorming、TDD、debugging 等核心工程 skills 完整 SKILL.md 原文

### Skill 系统研究资料（如何写 Skill）

详见 [skill-research/_INDEX.md](skill-research/_INDEX.md)  
关键：[skill-research/04-writing-guide/](skill-research/04-writing-guide/) — Anthropic 最佳实践 + 工程方法论

---

## Agent Patterns

> 多 Agent 协作架构模式，可直接参考或组合使用。

完整文档：[07-agent-design/_INDEX.md](07-agent-design/_INDEX.md)

| 模式 | 来源 | 核心机制 | 适用场景 |
|------|------|---------|---------|
| **DAG 任务依赖** | claude-swarm | 任务依赖图，有向无环图调度 | 有依赖的多步骤任务 |
| **并行 Swarm (20-50)** | agent-farm | 分布式 agent + 锁协调 | 大规模并行任务 |
| **9阶段质量门控** | metaswarm | 分阶段工作流 + 评估门控 | 高质量输出需求 |
| **团队角色分工** | wshobson-agents | Lead/Impl/Review 三角色 | 代码开发团队模拟 |
| **Git Worktree 隔离** | ccswarm | 每个 agent 独立 worktree | 并行代码修改无冲突 |
| **CI/PR 全自动化** | agent-orchestrator | PR 评审 + 代码修复循环 | DevOps 自动化 |
| **企业级 RAG+Swarm** | ruflo | Swarm + 向量检索 + 企业安全 | 知识密集型企业任务 |
| **Hub-and-Spoke 隔离** | ECC + sub-agent-collective | 中心节点分发，子 agent 隔离 | 安全敏感的子任务 |
| **架构参考（学术级）** | Dive-into-Claude-Code | Claude Code 内部机制逆向分析 | 深入理解平台 |
| **20+ 模式速查** | ultimate-guide | 所有 workflow 模式分类索引 | 模式选型参考 |

---

## Infrastructure

> Hooks / Context / MCP / Isolation 四大基础设施支柱。

完整文档：[08-infrastructure/_INDEX.md](08-infrastructure/_INDEX.md)

### Hooks（事件驱动中断系统）

| 组件 | 功能 | 路径 |
|------|------|------|
| claude-code-hooks-mastery | **13 个生命周期事件** 完整实现，含 TTS + 安全检查 | [08-infrastructure/hooks/claude-code-hooks-mastery/](08-infrastructure/hooks/claude-code-hooks-mastery/) |
| claude-code-hooks-multi-agent-observability | 多 Agent 监控 hooks | [08-infrastructure/hooks/claude-code-hooks-multi-agent-observability/](08-infrastructure/hooks/claude-code-hooks-multi-agent-observability/) |
| claude-code-hooks | 即用 hooks 集合（karanb192） | [08-infrastructure/hooks/claude-code-hooks/](08-infrastructure/hooks/claude-code-hooks/) |

Hooks 系统原理：[skill-research/06-hooks/](skill-research/06-hooks/)

### Context Window（内存管理）

| 组件 | 功能 | 路径 |
|------|------|------|
| token-optimizer | Ghost Token 检测 + 5层压缩策略 | [08-infrastructure/context-window/token-optimizer/](08-infrastructure/context-window/token-optimizer/) |

### Tool Use / MCP（系统调用层）

| 组件 | 功能 | 路径 |
|------|------|------|
| claude-code-mcp | Claude Code 作为 MCP Server（agent-in-agent 模式） | [08-infrastructure/tool-use-mcp/claude-code-mcp/](08-infrastructure/tool-use-mcp/claude-code-mcp/) |
| claude-code-mcp-enhanced | Boomerang 任务拆分 MCP 模式 | [08-infrastructure/tool-use-mcp/claude-code-mcp-enhanced/](08-infrastructure/tool-use-mcp/claude-code-mcp-enhanced/) |
| claude-code-everything | 全栈实战手册 | [08-infrastructure/tool-use-mcp/claude-code-everything/](08-infrastructure/tool-use-mcp/claude-code-everything/) |

### Subagent Isolation（进程隔离）

| 组件 | 功能 | 路径 |
|------|------|------|
| ECC | 82k★ Agent Harness 完整系统 | [08-infrastructure/subagent-isolation/ECC/](08-infrastructure/subagent-isolation/ECC/) |
| sub-agent-collective | Hub-and-Spoke 上下文隔离架构 | [08-infrastructure/subagent-isolation/claude-code-sub-agent-collective/](08-infrastructure/subagent-isolation/claude-code-sub-agent-collective/) |

---

## Knowledge Graphs

> 已建立 code-review-graph 索引的外部仓库。通过 MCP tool `mcp__code-review-graph__*` + `repo_root` 参数查询。

完整文档：[skill-research/12-third-party-repos/README.md](skill-research/12-third-party-repos/README.md)

| 仓库 | 领域 | repo_root 路径 | 查询用途 |
|------|------|---------------|---------|
| **yt-dlp** | 视频下载，网络请求，格式处理 | `/home/l/projects/03_third-party-sources/yt-dlp` | Extractor 架构、PostProcessor 设计 |
| **FinceptTerminal** | 金融终端，TUI，实时数据 | `/home/l/projects/03_third-party-sources/FinceptTerminal` | Textual TUI 设计，金融数据 API |
| **the-book-of-secret-knowledge** | DevOps/安全/网络工具集合 | `/home/l/projects/03_third-party-sources/the-book-of-secret-knowledge` | 工具选型参考（纯 Markdown） |
| **odoo** | ERP，多模块，ORM，前端框架 | `/home/l/projects/03_third-party-sources/odoo` | ORM 设计、前后端分离、权限系统 |
| **chrome-devtools-mcp** | MCP Server，Chrome DevTools 协议 | `/home/l/projects/03_third-party-sources/chrome-devtools-mcp` | MCP Server 实现参考，CDP 集成 |
| **ai-engineering-from-scratch** | AI 工程，RAG，向量库，Agent | `/home/l/projects/03_third-party-sources/ai-engineering-from-scratch` | AI 应用工程模式 |
| **codegraph** | 代码图谱，AST，依赖分析 | `/home/l/projects/03_third-party-sources/codegraph` | 代码结构分析工具 |

**查询示例：**
```
# 语义搜索节点
mcp__code-review-graph__semantic_search_nodes_tool(query="extractor plugin", repo_root="/home/l/projects/03_third-party-sources/yt-dlp")

# 架构概览
mcp__code-review-graph__get_architecture_overview_tool(repo_root="/home/l/projects/03_third-party-sources/odoo")

# 查找函数调用关系
mcp__code-review-graph__query_graph_tool(pattern="callers_of", node_id="<node>", repo_root="...")
```

---

## Tools

> 本仓库提供的可执行工具。

### agent_kb.py — 本地知识库 CLI

```bash
python tools/agent_kb.py build                        # 建立索引
python tools/agent_kb.py ask "问题" --json            # 语义检索
python tools/agent_kb.py answer "问题"                # DeepSeek 合成答案
python tools/agent_kb.py search "关键词"              # 全文检索
python tools/agent_kb.py repl                         # 交互 shell
```

文档：[docs/cli/agent-kb-cli.md](docs/cli/agent-kb-cli.md)  
架构：[docs/architecture/agent-kb-cli-agent-skill-selection.md](docs/architecture/agent-kb-cli-agent-skill-selection.md)

---

## Catalogs

> 社区 curated 资源列表，用于发现更多 skills/agents/tools。

### 06-catalogs/（社区资源目录）

| 目录 | 内容 | 规模 |
|------|------|------|
| awesome-claude-code | hesreallyhim 权威 curated list | 高质量精选 |
| alirezarezvani-claude-skills | 研究/工程/商业 skills | 313+ skills |
| awesome-claude-code-toolkit | agents + commands + hooks | rohitg00 |
| composio-awesome-claude-skills | 文档/文件/工作流 | Composio |
| travisvn-awesome-claude-skills | 精选列表 | travisvn |
| mingrath-awesome-claude-skills | 开发/数据/DevOps | mingrath |

### 05-subagents/（专项 Subagent）

[awesome-claude-code-subagents/](05-subagents/awesome-claude-code-subagents/) — VoltAgent，100+ 专项 subagents

### 09-agent-infra-catalog/（候选引入库）

[09-agent-infra-catalog/README.md](09-agent-infra-catalog/README.md) — 按编排/路由/观测/门控/skills 分类的候选仓库清单

---

## Use Cases（组装示例）

> 展示如何从本库组合轮子搭建完整 agent。

| 场景 | 文档 |
|------|------|
| 统计分析 Agent | [use-cases/statistical-analysis-agent.md](use-cases/statistical-analysis-agent.md) |
| 建筑造价知识库 Agent | [use-cases/construction-cost-knowledge-base-agent.md](use-cases/construction-cost-knowledge-base-agent.md) |

---

## 分层导航路径

```
MANIFEST.md                          ← 你在这里（AI 入口）
├── catalog.json                     ← 机器可读全量索引
├── README.md                        ← 人类文档
│
├── skill-research/
│   ├── _INDEX.md                    ← Skill 系统完整索引
│   ├── 11-anthropic-personal-skills/ ← 官方 9个 skill 完整文档
│   ├── 05-examples/superpowers-skills/ ← 工程级 skill 实例
│   ├── 04-writing-guide/            ← 如何写 Skill
│   └── 12-third-party-repos/        ← 知识图谱仓库文档
│
├── 07-agent-design/
│   └── _INDEX.md                    ← Agent 架构模式索引
│
├── 08-infrastructure/
│   └── _INDEX.md                    ← 基础设施组件索引
│
├── 09-agent-infra-catalog/
│   └── catalog.yaml                 ← 候选库结构化清单
│
├── 01-data-analysis/                ← 数据分析 skills + agents
├── 02-r-quarto/                     ← R/Quarto 工具链
├── 03-jupyter/                      ← Jupyter 集成
├── 04-research/                     ← 学术研究 skills
├── 05-subagents/                    ← 100+ 专项 subagents
├── 06-catalogs/                     ← 社区资源目录
│
├── tools/agent_kb.py               ← 本地检索 CLI
├── data/agent-kb/                  ← 知识库数据
└── docs/                           ← 架构文档 + CLI 文档
```
