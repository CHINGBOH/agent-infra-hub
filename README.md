# agent-infra-hub

围绕 LLM 的微型 OS — Skills / Agent 框架 / 基础设施四大支柱的完整参考库。

**~630 MB | 31 个仓库 | 9 个分类**

```
LLM（CPU）
  ├── Skills（行为注入）          01-06
  ├── Agent 设计（进程架构）       07
  └── 基础设施（微型 OS 四支柱）   08
       ├── Hooks          中断系统
       ├── Context Window 内存管理
       ├── Tool Use / MCP 系统调用
       └── Subagent       进程隔离
```

---

## 快速索引（按使用场景）

| 我需要… | 用这个 | 路径 |
|---------|--------|------|
| 数据分析管道 agent（中文） | claude-data-analysis-ultra | [→](#1-data-analysis-数据分析管道) |
| Quarto 报告生成 | posit-dev-skills/quarto | [→](#2-r-quarto-r--quarto-工具链) |
| 写/执行 R 统计代码 | agentic-skills/writing-r-code | [→](#2-r-quarto-r--quarto-工具链) |
| R 统计结果核验（反幻觉） | ClaudeR | [→](#2-r-quarto-r--quarto-工具链) |
| Jupyter EDA 集成 | notebook-intelligence | [→](#3-jupyter-jupyter-集成) |
| 学术报告撰写与审阅 | academic-research-skills | [→](#4-research-学术研究管道) |
| 数据分析 subagent 分工 | VoltAgent 05-data-ai | [→](#5-subagents-专项-subagent-分工) |
| 搜索更多 skills | 06-catalogs | [→](#6-catalogs-skills-目录-发现) |
| 理解 Claude Code Agent 底层架构 | Dive-into-Claude-Code | [→](#7-agent-design-agent-架构设计) |
| 多阶段工作流 + 质量门控设计 | metaswarm | [→](#7-agent-design-agent-架构设计) |
| Agent 团队角色分工（lead/impl/review） | wshobson-agents | [→](#7-agent-design-agent-架构设计) |
| 所有 Workflow 模式速查 | ultimate-guide | [→](#7-agent-design-agent-架构设计) |
| 20-50 Agent 并行 + 锁协调 | agent-farm | [→](#7-agent-design-agent-架构设计) |
| **Hooks 13个生命周期事件实现** | claude-code-hooks-mastery | [→](#8-infrastructure-基础设施四大支柱) |
| **Context 压缩 + Ghost Token 检测** | token-optimizer | [→](#8-infrastructure-基础设施四大支柱) |
| **Claude Code 作为 MCP Server** | claude-code-mcp | [→](#8-infrastructure-基础设施四大支柱) |
| **Boomerang 任务拆分 MCP 模式** | claude-code-mcp-enhanced | [→](#8-infrastructure-基础设施四大支柱) |
| **Agent Harness 完整系统（82k★）** | ECC | [→](#8-infrastructure-基础设施四大支柱) |
| **Hub-and-Spoke 上下文隔离架构** | sub-agent-collective | [→](#8-infrastructure-基础设施四大支柱) |
| **更多 Agent 架构基础设施候选仓库** | 09-agent-infra-catalog | [→](#9-agent-infra-catalog-候选库) |
| **统计分析 Agent 组装路径** | use-cases/statistical-analysis-agent.md | [→](use-cases/statistical-analysis-agent.md) |
| **建筑造价知识库 Agent 组装路径** | use-cases/construction-cost-knowledge-base-agent.md | [→](use-cases/construction-cost-knowledge-base-agent.md) |
| **Agent 查询可用性审计** | docs/audits/agent-query-readiness.md | [→](docs/audits/agent-query-readiness.md) |
| **本地知识库 CLI** | tools/agent_kb.py | [→](docs/cli/agent-kb-cli.md) |
| **Agent KB CLI 架构与 skill 选择** | docs/architecture/agent-kb-cli-agent-skill-selection.md | [→](docs/architecture/agent-kb-cli-agent-skill-selection.md) |

---

## 目录结构

```
agent-infra-hub/
├── 01-data-analysis/          数据分析管道
│   ├── claude-data-analysis/          liangdabiao — 数据分析 Agent
│   └── claude-data-analysis-ultra/    liangdabiao — 进阶 12 技能版
│
├── 02-r-quarto/               R + Quarto 工具链
│   ├── posit-dev-skills/              Posit 官方 skills (quarto/tidyverse/shiny...)
│   ├── agentic-skills/                wolf5996 — R 科学分析 skills
│   └── ClaudeR/                       IMNMV — R MCP + 统计核验
│
├── 03-jupyter/                Jupyter 集成
│   └── notebook-intelligence/         JupyterLab + Claude Code 扩展
│
├── 04-research/               学术研究管道
│   └── academic-research-skills/      Imbad0202 — 研究→写作→审阅→定稿
│
├── 05-subagents/              专项 Subagent 分工
│   └── awesome-claude-code-subagents/ VoltAgent — 100+ 专项 subagents
│
├── 06-catalogs/               Skills 目录（发现更多）
│   ├── awesome-claude-code/           hesreallyhim — 权威 curated list
│   ├── alirezarezvani-claude-skills/  313+ skills (研究/工程/商业)
│   ├── awesome-claude-code-toolkit/   rohitg00 — agents+commands+hooks
│   ├── composio-awesome-claude-skills/ Composio — 文档/文件/工作流
│   ├── travisvn-awesome-claude-skills/ travisvn — 精选列表
│   └── mingrath-awesome-claude-skills/ mingrath — 开发/数据/DevOps
│
├── 07-agent-design/           Agent 架构设计
│   ├── Dive-into-Claude-Code/         VILA-Lab — 学术级架构逆向分析
│   ├── metaswarm/                     dsifry — 9 阶段工作流 + 质量门控
│   ├── wshobson-agents/               wshobson — 81 插件 + 4 角色团队
│   ├── ultimate-guide/                FlorianBruniaux — 20+ 工作流模式
│   ├── agent-farm/                    Dicklesworthstone — 并行 20-50 agents
│   ├── ccswarm/                       nwiizo — Git Worktree 隔离
│   ├── claude-swarm/                  affaan-m — 任务依赖图 DAG
│   ├── agent-orchestrator/            ComposioHQ — CI/PR 全自动化
│   └── ruflo/                         ruvnet — 企业级 Swarm + RAG
│
├── 08-infrastructure/         基础设施四大支柱（★ 新增）
│   ├── hooks/                         中断系统
│   │   ├── claude-code-hooks-mastery/ disler — 13 事件完整实现 + TTS + 安全
│   │   ├── claude-code-hooks-multi-agent-observability/ disler — 多 Agent 监控
│   │   └── claude-code-hooks/         karanb192 — 即用 hooks 集合
│   ├── context-window/                内存管理
│   │   └── token-optimizer/           alexgreensh — Ghost Token + 5层压缩
│   ├── tool-use-mcp/                  系统调用层
│   │   ├── claude-code-mcp/           steipete — agent-in-agent MCP
│   │   ├── claude-code-mcp-enhanced/  grahama1970 — Boomerang 模式
│   │   └── claude-code-everything/    wesammustafa — 全栈实战手册
│   └── subagent-isolation/            进程隔离
│       ├── ECC/                       affaan-m — 82k★ Agent Harness
│       └── claude-code-sub-agent-collective/ vanzan01 — Hub-and-Spoke
│
└── 09-agent-infra-catalog/    Agent 架构基础设施候选库
    ├── catalog.yaml                   awesome / 编排 / 路由 / 门控 / 观测 / skills 清单
    └── README.md                      分类法与导入策略
```

---

## 本地知识库 CLI

本仓库提供零依赖本地检索入口：

```bash
./tools/agent_kb.py build
./tools/agent_kb.py ask "我要做建筑造价知识库 agent，需要哪些资料？" --json
./tools/agent_kb.py search "Milvus knowledge graph construction cost"
```

详细说明见 [docs/cli/agent-kb-cli.md](docs/cli/agent-kb-cli.md)。架构与 agent/skill 选择见 [docs/architecture/agent-kb-cli-agent-skill-selection.md](docs/architecture/agent-kb-cli-agent-skill-selection.md)。

---

## 1. data-analysis — 数据分析管道

> 适用场景：CSV/Excel 上传 → 自动分析 → 报告

### claude-data-analysis（基础版）

```
路径：01-data-analysis/claude-data-analysis/
原仓：https://github.com/liangdabiao/claude-data-analysis
语言：中文
```

**核心命令：**
- `/do-all` — 常规数据分析（描述统计、可视化、相关性）
- 数据放入 `data_storage/`，Claude 自动分析

**结构参考价值（survey-analysis-platform）：**
- `.claude/` 目录 — subagent 配置方式
- slash command 定义格式
- 数据→分析→报告管道组织

---

### claude-data-analysis-ultra（进阶 12 技能版）

```
路径：01-data-analysis/claude-data-analysis-ultra/
原仓：https://github.com/liangdabiao/claude-data-analysis-ultra
语言：中文
```

**12 个专项 skills（skills.md）：**

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
| 数据质量报告 | 缺失值/异常/分布 |
| 自动化报告 | Markdown 报告生成 |

**最佳参考：** `SKILLS_USAGE.md`（skills 调用规范）

---

## 2. r-quarto — R + Quarto 工具链

> 适用场景：R 脚本开发、Quarto 报告、统计结果核验

### posit-dev-skills（Posit 官方，最高权威）

```
路径：02-r-quarto/posit-dev-skills/
原仓：https://github.com/posit-dev/skills
安装：npx skills add posit-dev/skills/<skill-name>
```

**Skills 清单：**

| Skill 目录 | 功能 | survey-platform 用途 |
|-----------|------|---------------------|
| `quarto/` | Quarto 文档创作、R Markdown 迁移、cross-refs、callouts | **04-report/ 直接使用** |
| `tidyverse/` | dplyr/ggplot2/purrr 最佳实践 | 02-analyze/ 模块开发 |
| `r-lib/` | R 包开发、usethis、devtools | lib/ 函数库管理 |
| `shiny/` | bslib 现代 Dashboard | 可替换 Streamlit UI |
| `brand-yml/` | Quarto 统一样式配置 | 报告品牌一致性 |
| `ggsql/` | ggplot2 + SQL 集成 | 数据可视化 |
| `alt-text/` | 图表无障碍描述 | 报告可访问性 |

**重点阅读：** `quarto/README.md`、`tidyverse/SKILL.md`

---

### agentic-skills（R 科学分析）

```
路径：02-r-quarto/agentic-skills/
原仓：https://github.com/wolf5996/agentic-skills
```

**Skills 清单：**

| Skill 目录 | 功能 | survey-platform 用途 |
|-----------|------|---------------------|
| `writing-r-code/` | R 代码生成规范 | **02-analyze/ 模块生成** |
| `writing-qmd-scientific/` | 科学 QMD 文档写作 | **04-report/ 模板** |
| `creating-analysis-projects/` | 分析项目脚手架 | 新项目初始化 |
| `developing-r-packages/` | R 包开发流程 | lib/ 模块化 |
| `git-hygiene/` | Git 规范 | 版本管理 |
| `md-format/` | Markdown 格式化 | 报告文档规范 |

---

### ClaudeR（R MCP + 统计核验）

```
路径：02-r-quarto/ClaudeR/
原仓：https://github.com/imnmv/clauder
类型：MCP Server + R 包
```

**核心功能：**
- RStudio ↔ Claude Code 双向集成（via MCP）
- **手稿审计协议**：逐块读取统计报告 → 提取所有统计声明到注册表 → 与 R 代码逐一核实 → 标记不一致

**survey-platform 用途：**
- 报告数字核验（反幻觉关键机制）
- `clauder-mcp/` — MCP 配置参考
- `inst/` — 审计协议实现参考

**安装：** `llms-install.md`

---

## 3. jupyter — Jupyter 集成

### notebook-intelligence

```
路径：03-jupyter/notebook-intelligence/
原仓：https://github.com/notebook-intelligence/notebook-intelligence
类型：JupyterLab 扩展
```

**功能：**
- Claude Code 驱动 Jupyter notebook agent
- inline edit、auto-complete、chat in notebook
- MCP 支持、skills 加载
- 支持 Claude Code CLI / Ollama / OpenAI-compatible

**survey-platform 用途：**
- `00-explore/explore.ipynb` 的 LLM 集成
- EDA 自动化（数据分布、缺失值、变量关系）

**安装：**
```bash
pip install notebook-intelligence
# 详见 README.md
```

---

## 4. research — 学术研究管道

### academic-research-skills

```
路径：04-research/academic-research-skills/
原仓：https://github.com/Imbad0202/academic-research-skills
语言：多语言（含中文 README）
```

**Skills 清单：**

| Skill / 目录 | 功能 | survey-platform 对应 |
|-------------|------|---------------------|
| `academic-pipeline/` | 研究→写作→审阅→修改→定稿完整流程 | 需求采集→分析→报告全流程 |
| `academic-paper/` | 学术论文写作 skill | 报告撰写规范 |
| `academic-paper-reviewer/` | 论文审阅 skill | 报告质量审核 |
| `deep-research/` | 深度研究 skill | 文献/需求深度调研 |
| `commands/` | slash command 定义 | 命令设计参考 |
| `agents/` | 研究 agent 配置 | multi-agent 设计参考 |
| `hooks/` | 钩子配置 | 自动化触发参考 |

**重点阅读：** `QUICKSTART.md`、`README.zh-CN.md`

---

## 5. subagents — 专项 Subagent 分工

### awesome-claude-code-subagents（VoltAgent）

```
路径：05-subagents/awesome-claude-code-subagents/
原仓：https://github.com/VoltAgent/awesome-claude-code-subagents
安装：bash install-agents.sh
```

**data-ai 类（最相关）：**

| 文件 | Subagent 职能 | survey-platform 用途 |
|------|-------------|---------------------|
| `05-data-ai/data-analyst.md` | SQL查询、统计分析、可视化 | 数据分析主 agent |
| `05-data-ai/data-scientist.md` | 假设检验、预测建模 | 高级分析 agent |
| `05-data-ai/data-engineer.md` | 数据管道、SQLite管理 | 数据清洗 agent |
| `05-data-ai/database-optimizer.md` | 数据库优化 | SQLite schema |
| `10-research-analysis/data-researcher.md` | 数据研究 | 需求调研 agent |
| `08-business-product/business-analyst.md` | 需求分析 | 用户需求采集 |

**完整分类：**
```
categories/
├── 01-core-development/     核心开发
├── 02-language-specialists/ 语言专家
├── 03-infrastructure/       基础设施
├── 04-quality-security/     质量安全
├── 05-data-ai/             数据 + AI ← 最相关
├── 06-developer-experience/ 开发体验
├── 07-specialized-domains/  专项领域
├── 08-business-product/    商业产品 ← 需求采集
├── 09-meta-orchestration/  编排协调 ← 管道调度
└── 10-research-analysis/   研究分析 ← 报告生成
```

---

## 6. catalogs — Skills 目录（发现更多）

### awesome-claude-code（hesreallyhim — 最权威）

```
路径：06-catalogs/awesome-claude-code/
原仓：https://github.com/hesreallyhim/awesome-claude-code
特点：结构化数据（THE_RESOURCES_TABLE.csv）+ 分类索引
```

搜索方法：
```bash
grep -i "data\|analysis\|R\|statistics" \
  06-catalogs/awesome-claude-code/THE_RESOURCES_TABLE.csv
```

---

### alirezarezvani-claude-skills（313+ skills）

```
路径：06-catalogs/alirezarezvani-claude-skills/
原仓：https://github.com/alirezarezvani/claude-skills
```

**与本项目相关的分类：**

| 目录 | 内容 |
|------|------|
| `research/` | dossier、litreview、grants、patent、pulse、notebooklm |
| `engineering/` | data-quality-auditor、chaos-engineering、code-tour、docker、feature-flags、karpathy-coder |
| `productivity/` | 日常生产力工具 |
| `orchestration/` | 多 agent 编排 |

---

### awesome-claude-code-toolkit（rohitg00）

```
路径：06-catalogs/awesome-claude-code-toolkit/
特点：agents + commands + hooks + rules + skills + templates + mcp-configs 全套
```

**重点目录：**
- `agents/data-ai/` — data-scientist.md
- `skills/` — 精选 35 skills
- `hooks/` — 20 个自动化 hooks
- `mcp-configs/` — 14 个 MCP 配置

---

### composio-awesome-claude-skills

```
路径：06-catalogs/composio-awesome-claude-skills/
特点：文档处理（docx/pdf/xlsx）、工作流自动化
```

**相关 skills：**
- `developer-growth-analysis/` — 开发者数据增长分析
- `meeting-insights-analyzer/` — 会议洞察分析
- `document-skills/` — Word/PDF/Excel 文档处理

---

## 安装指南

### 方式一：npx 安装（posit-dev 推荐方式）

```bash
# 安装到项目 .claude/skills/
npx skills add posit-dev/skills/quarto
npx skills add posit-dev/skills/tidyverse
```

### 方式二：复制 skill 目录到项目

```bash
# 复制单个 skill 到 survey-analysis-platform
cp -r 02-r-quarto/agentic-skills/writing-r-code \
      ~/projects/survey-analysis-platform/.claude/skills/

cp -r 02-r-quarto/agentic-skills/writing-qmd-scientific \
      ~/projects/survey-analysis-platform/.claude/skills/
```

### 方式三：复制到全局 skills 目录

```bash
# 所有项目均可使用
cp -r 02-r-quarto/posit-dev-skills/quarto ~/.claude/skills/
cp -r 05-subagents/awesome-claude-code-subagents/categories/05-data-ai/data-analyst.md \
      ~/.claude/skills/data-analyst/
```

### 方式四：subagents 批量安装（VoltAgent）

```bash
cd 05-subagents/awesome-claude-code-subagents
bash install-agents.sh
```

---

## 更新仓库

```bash
# 更新单个仓库
cd 02-r-quarto/posit-dev-skills && git pull

# 批量更新所有仓库
find /home/l/projects/agent-infra-hub -name ".git" -maxdepth 3 \
  -exec sh -c 'cd "$(dirname "{}")" && git pull --ff-only 2>&1 | grep -v "Already"' \;
```

---

## 7. agent-design — Agent 架构设计

> 详细导航见 [07-agent-design/README.md](07-agent-design/README.md)

| 仓库 | 定位 | 核心价值 |
|------|------|---------|
| `Dive-into-Claude-Code/` | 学术级架构分析 | 理解 Agent 底层（1.6% AI + 98.4% 基础设施） |
| `metaswarm/` | 9 阶段工作流框架 | 质量门控设计、ORCHESTRATION.md |
| `wshobson-agents/` | 81 插件生产系统 | 4 角色团队（lead/implementer/reviewer/debugger） |
| `ultimate-guide/` | 完整文档 + 速查 | 20+ 工作流模式、41 架构图、cheatsheet |
| `agent-farm/` | 大规模并行框架 | 20-50 Agent 并行、文件锁协调 |
| `ccswarm/` | Rust 并行实现 | Git Worktree 隔离方案 |
| `claude-swarm/` | SDK 示范项目 | 任务依赖图（DAG）驱动并行 |
| `agent-orchestrator/` | CI 全自动化 | Plan→Spawn→自动修复 CI/PR |
| `ruflo/` | 企业级平台 | Swarm 智能 + RAG 集成 |

**推荐阅读顺序：**
```
Dive-into-Claude-Code/README_zh.md（10 min）
→ ultimate-guide/guide/cheatsheet.md（10 min）
→ metaswarm/ORCHESTRATION.md（20 min）
→ wshobson-agents/plugins/agent-teams/README.md（10 min）
```

---

## 8. infrastructure — 基础设施四大支柱

> 详细导航见 [08-infrastructure/README.md](08-infrastructure/README.md)

| 支柱 | 计算机类比 | 核心仓库 | 关键价值 |
|------|-----------|---------|---------|
| Hooks | 中断处理 | `hooks/claude-code-hooks-mastery` | 13 个生命周期事件，pre_tool_use 可阻断 |
| Context Window | 内存管理 | `context-window/token-optimizer` | Ghost Token 检测，5层 Compaction 策略 |
| Tool Use / MCP | 系统调用 | `tool-use-mcp/claude-code-mcp-enhanced` | Boomerang 拆任务，agent-in-agent 递归 |
| Subagent Isolation | 进程隔离 | `subagent-isolation/ECC` | 82k★ Harness 系统，NanoClaw 编排引擎 |

---


## 9. agent-infra-catalog — 候选库

> 详细清单见 [09-agent-infra-catalog/catalog.yaml](09-agent-infra-catalog/catalog.yaml)

用于继续扩展本仓库的 GitHub 候选清单，采用 **metadata first** 策略：先结构化记录仓库 URL、分类、能力、优先级和导入模式，再决定是否 clone 源码。

**覆盖分类：**

| 分类 | 典型内容 |
|------|----------|
| `awesome-indexes` | agent / skills / governance / Claude Code 索引 |
| `orchestrators` | 多 Agent 编排、DAG、worker pool、workflow runtime |
| `routing-gateways` | LLM gateway、模型路由、fallback、MCP/A2A proxy |
| `governance-guardrails` | policy enforcement、sandbox、audit、quality gate |
| `observability-hud` | dashboard、HUD、statusline、hook telemetry |
| `skill-systems` | skills、plugin、capability routing、runtime projection |

**优先候选：**

| 仓库 | 方向 |
|------|------|
| `Agent-Analytics/awesome-multi-agent-orchestrators` | 多 Agent 编排索引 |
| `microsoft/agent-governance-toolkit` | Runtime governance / policy / sandbox |
| `agentgateway/agentgateway` | MCP/A2A agentic proxy |
| `inngest/agent-kit` | TypeScript deterministic routing |
| `open-multi-agent/open-multi-agent` | goal → task DAG |
| `jscraik/Agent-Skills` | skills capability control plane |
| `ek33450505/claude-code-dashboard` | hooks + sessions + SQLite 观测 |
| `scalarian/oh-my-codex` | Codex skills / hooks / HUD / MCP |

---

## 与 survey-analysis-platform 的完整对应关系

```
survey-analysis-platform 模块      Skills                Agent 设计参考
────────────────────────────────────────────────────────────────────────
00-explore/ (Jupyter EDA)      ← notebook-intelligence
01-clean/   (数据清洗)          ← data-engineer subagent  + team-implementer
02-analyze/ (R 统计分析)        ← writing-r-code           + metaswarm/orchestrated-execution
03-integrate/ (结果整合)        ← data-scientist subagent  + team-reviewer
04-report/  (Quarto 报告)       ← posit-dev-skills/quarto  + wshobson-agents/agent-teams
app/agent   (主循环设计)        ←                            Dive-into-Claude-Code/architecture
app/agent   (需求采集对话)      ← academic-pipeline         + ultimate-guide/agent-teams.md
app/agent   (工作流模式)        ←                            metaswarm/9阶段工作流
app/tools   (工具设计)          ←                            Dive-into-Claude-Code/build-your-own-agent
app/tools   (反幻觉核验)        ← ClaudeR 审计协议           + metaswarm/design-review-gate
管道质量门控                    ← Pydantic schema            + metaswarm/skills/plan-review-gate
并行分析模块                    ←                            agent-farm/文件锁设计
任务依赖顺序                    ←                            claude-swarm/DAG 设计
```

---

## 批量更新所有仓库

```bash
find /home/l/projects/agent-infra-hub -maxdepth 3 -name ".git" -type d \
  | while read g; do
      d=$(dirname "$g")
      echo "=== $(basename $d) ==="
      git -C "$d" pull --ff-only 2>&1 | head -1
    done
```

---

*最后更新：2026-05-22 | 21 仓库 | 维护：survey-analysis-platform 项目组*
