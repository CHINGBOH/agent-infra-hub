# skills-hub

Claude Code Skills & Subagents 本地仓库 — 按需调用，服务 survey-analysis-platform 及通用项目。

**290 MB | 12 个仓库 | 6 个分类 | ~350+ 可用 Skills**

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

---

## 目录结构

```
skills-hub/
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
└── 06-catalogs/               Skills 目录（发现更多）
    ├── awesome-claude-code/           hesreallyhim — 权威 curated list
    ├── alirezarezvani-claude-skills/  313+ skills (研究/工程/商业)
    ├── awesome-claude-code-toolkit/   rohitg00 — agents+commands+hooks
    ├── composio-awesome-claude-skills/ Composio — 文档/文件/工作流
    ├── travisvn-awesome-claude-skills/ travisvn — 精选列表
    └── mingrath-awesome-claude-skills/ mingrath — 开发/数据/DevOps
```

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
find /home/l/projects/skills-hub -name ".git" -maxdepth 3 \
  -exec sh -c 'cd "$(dirname "{}")" && git pull --ff-only 2>&1 | grep -v "Already"' \;
```

---

## 与 survey-analysis-platform 的对应关系

```
survey-analysis-platform 模块          推荐 Skill
─────────────────────────────────────────────────────
00-explore/ (Jupyter EDA)          ← notebook-intelligence
01-clean/   (数据清洗)              ← data-engineer subagent
02-analyze/ (R 统计分析)            ← writing-r-code + data-analyst
03-integrate/ (结果整合)            ← data-scientist subagent
04-report/  (Quarto 报告)           ← posit-dev-skills/quarto + writing-qmd-scientific
app/agent   (需求采集对话)           ← academic-pipeline + business-analyst
app/tools   (反幻觉核验)             ← ClaudeR 审计协议
```

---

*最后更新：2026-05-22 | 维护：survey-analysis-platform 项目组*
