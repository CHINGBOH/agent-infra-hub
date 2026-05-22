# Repo Layout — 一级目录契约

> 本文档定义每个一级目录的**职责边界**与**不变量**。修改目录前先读这个，避免污染分层。

---

## 一级目录

### 编号目录（01–09）

| 目录 | 内容 | 入口 | 不变量 |
|------|------|------|--------|
| `01-data-analysis/` | 中文数据分析 skill 套件（RFM、漏斗、A/B 等 12 个） | `01-data-analysis/claude-data-analysis-ultra/SKILLS_USAGE.md` | 所有 skill 必须有 `SKILL.md` 头部，遵循 progressive disclosure |
| `02-r-quarto/` | R/Quarto 工具链 skills（Posit 官方 + agentic-skills + ClaudeR） | 各 vendored 子目录 README | 仅放 R/Quarto 相关 skills |
| `03-jupyter/` | Jupyter 集成（notebook-intelligence） | `03-jupyter/notebook-intelligence/` | 仅 Jupyter Lab/Notebook 扩展 |
| `04-research/` | 学术研究流水线 skills（写作/审阅/定稿） | `04-research/academic-research-skills/` | 不混合工程 skills |
| `05-subagents/` | 100+ 专项 subagent（VoltAgent 收集） | `05-subagents/awesome-claude-code-subagents/` | 每个 subagent 单文件，不带 orchestrator |
| `06-catalogs/` | 6 个社区 curated 列表（awesome-claude-*） | `06-catalogs/*/README.md` | 仅索引，不 vendor skill 源码 |
| `07-agent-design/` | 多 agent 协作模式（10 种：DAG、swarm、9 阶段、wshobson、ccswarm…） | [07-agent-design/_INDEX.md](../../07-agent-design/_INDEX.md) | 仅放 agent **架构**，不放基础设施 |
| `08-infrastructure/` | 四大支柱：hooks / context-window / tool-use-mcp / subagent-isolation | [08-infrastructure/_INDEX.md](../../08-infrastructure/_INDEX.md) | 仅放基础设施组件，不放业务 skill |
| `09-agent-infra-catalog/` | 候选引入库 metadata + 已浅克隆源码 | [09-agent-infra-catalog/README.md](../../09-agent-infra-catalog/README.md) | metadata-first；浅克隆走 `.gitignore`，主仓只跟 `catalog.yaml` |

### 非编号目录

| 目录 | 用途 | 不变量 |
|------|------|--------|
| `skill-research/` | Skill 系统研究材料 + 第三方仓库知识图谱索引 | 不放可执行 skill；可放原文档抄录 |
| `tools/` | 仓库自有工具（`agent_kb.py`、`docs_gen.py`） | **仅 Python 标准库**，零外部依赖 |
| `docs/` | 给人和 agent 看的深度文档 | 不放可执行代码；派生文档走 `_generated/` |
| `use-cases/` | 组装示例 | 必须引用本仓库已有组件，路径可点开 |
| `data/` | 本地数据（SQLite 索引等） | `.gitignore` 屏蔽，不入仓 |

---

## 顶层文件

| 文件 | 角色 | 真值地位 |
|------|------|----------|
| `MANIFEST.md` | AI agent 主入口 | ✅ Single source of truth — navigation |
| `catalog.json` | 机器可读资源清单 | ✅ Single source of truth — resources |
| `README.md` | 人类入口 | 与 MANIFEST 协同；不能与之矛盾 |
| `claudecode.md` | Claude Code 平台说明 | 参考材料 |
| `Makefile` | 维护命令 | 必须包含 `docs`/`docs-check` |
| `.gitignore` | 排除 vendored 克隆源码、`data/`、`__pycache__` | 同步 9 目录 README 表述 |

---

## 添加新组件时的去向决策表

| 我要加的是… | 放哪里 |
|-------------|--------|
| 一个新 SKILL.md | 按领域归入 01-04；非传统领域开新目录前先开 issue |
| 一种新 agent 协作模式 | `07-agent-design/<pattern-name>/`，并在 `_INDEX.md` 加表 |
| 一个新 hook / context 组件 | `08-infrastructure/<pillar>/<component>/` |
| 一个候选 GitHub 仓库 | 在 `09-agent-infra-catalog/catalog.yaml` 加 entry；按 priority 决定是否浅克隆 |
| 一个组装示例 | `use-cases/<scenario-name>.md`，并在 `MANIFEST.md` Use Cases 表加行 |
| 一个新工具 | `tools/<name>.py`（仅 stdlib），并在 `Makefile` 加 target |
| 一篇深度文档 | `docs/{architecture,guides,reference}/<name>.md`，从 `docs/README.md` 索引 |

详细工作流见 [../guides/adding-new-content.md](../guides/adding-new-content.md)。

---

## 自动化保障

| 不变量 | 由谁强制 |
|--------|----------|
| MANIFEST 链接均可达 | `make docs-links` → `docs/_generated/link-report.md` |
| `catalog.json` 引用路径都存在 | `make docs-catalog` → `docs/_generated/catalog-fs-report.md` |
| CLI 文档与代码同步 | `make docs-cli` 反射 argparse |
| 派生文档不漂移 | `make docs-check`（CI 门控） |
