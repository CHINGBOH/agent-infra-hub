# 三仓库分析：agentmemory · scientific-agent-skills · oh-my-claudecode

> 调研日期 2026-05-25 · 三个仓库分属 **三个不同层** 的 agent 基础设施，互不重叠，可拼装

---

## 📊 一句话定位

| 仓库 | 层 | 体量 | 主语言 | 一句话 |
|---|---|---|---|---|
| **agentmemory** | 记忆基础设施（横切） | 57k LOC | TypeScript | 给所有 MCP 客户端通用的**持久化记忆 + 混合检索** server |
| **scientific-agent-skills** | 技能内容库 | 138 skills / 267k MD | Markdown + Py | 138 个**科学领域 SKILL.md**，符合开放 Agent Skills 标准 |
| **oh-my-claudecode (OMC)** | 编排框架 | 221k LOC | TypeScript | Claude Code 上的**多智能体 team/swarm 编排插件** |

> 这三者**正交**：agentmemory 给 OMC 当记忆后端，OMC 跑 scientific-skills 的某个 skill —— 完美的三层夹心。

---

## 1. agentmemory — 持久化记忆 + 混合检索

**位置**：`08-infrastructure/agentmemory/`  (14M, 309 TS files)

### 卖点
- 53 个 MCP 工具 · 12 个自动 hooks · 0 外部 DB · 950+ 测试
- R@5 = 95.2%，token 用量 ↓ 92%（号称）
- 兼容 Claude Code / Cursor / Gemini CLI / Codex / Hermes / OpenClaw / pi / OpenCode 等几乎所有 MCP 客户端

### 架构（src/ 子模块）
| 模块 | 职责 | 关键文件 |
|---|---|---|
| `state/` | **存储+检索引擎** | `hybrid-search.ts`（324 行）、`vector-index.ts`、`search-index.ts`（BM25?）、`reranker.ts`、`stemmer.ts`、`cjk-segmenter.ts`（中文分词！）、`synonyms.ts` |
| `mcp/` | MCP server | `server.ts` 1730 行集中注册 53 tools，`standalone.ts` |
| `hooks/` | Claude Code 12 个 hooks | `pre-tool-use.ts`, `post-tool-use.ts`, `session-{start,end}.ts`, `subagent-{start,stop}.ts`, `task-completed.ts`, `post-commit.ts`, `pre-compact.ts`, `stop.ts`, `notification.ts`, `prompt-submit.ts`, `post-tool-failure.ts`, `sdk-guard.ts` |
| `viewer/` | 实时网页查看器（:3111） | `server.ts`, `document.ts` |
| `eval/` | 自评估 + 自纠错 | `metrics-store.ts`, `quality.ts`, `self-correct.ts` |
| `replay/` | 会话回放 | `jsonl-parser.ts` |
| `integrations/` | 适配器 | `hermes/`, `openclaw/`, `pi/`, `filesystem-watcher/` |

### 设计文档
仓库根目录有 **`DESIGN.md`** —— 但坑爹的是内容是 **Lamborghini 视觉设计系统**（黑+金配色），疑似 paste 错文件 ⚠️。要看真设计文档去 [Karpathy LLM Wiki gist](https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2)（README 提到的 1200⭐ gist）。

### 抄哪些？
- 🥇 **`state/hybrid-search.ts`** — BM25 + 向量 + rerank 的混合检索三明治，324 行可拆出来
- 🥇 **`state/cjk-segmenter.ts`** — 中文分词集成（rag-dashboard 可能用得上）
- 🥇 **`hooks/*.ts`** — 12 个 hooks 模板齐全，Claude Code hooks 教科书
- 🥈 **`mcp/server.ts`** — 53 tools 的注册范本（1730 行单文件，但工具列表完整）

### 避坑
- **`DESIGN.md` 是 Lamborghini 跑车广告文案，不是设计文档**（很可能 LLM 生成 README/DESIGN 混乱）
- 单文件 `mcp/server.ts` 1730 行，应拆成模块

---

## 2. scientific-agent-skills — 138 个开放标准 SKILL.md

**位置**：`07-agent-design/scientific-agent-skills/`  (13M, 893 .md files)

### 卖点
- **138 skills** 覆盖 17 个科学领域（基因组、药物发现、临床、医学影像、地理空间、材料、物理天文、实验室自动化…）
- 符合开放 [Agent Skills 标准](https://agentskills.io/)（不仅限 Claude Code）
- 兼容 Cursor / Claude Code / Codex 等
- 配套 [K-Dense BYOK](https://github.com/K-Dense-AI/k-dense-byok) 桌面 AI 共同科学家

### 结构
```
scientific-skills/
├── biopython/           ← 每个目录 = 1 skill
│   └── SKILL.md         ← YAML frontmatter (name/description/license/metadata) + 正文
├── astropy/
├── deepchem/
├── diffdock/
├── ... (139 个目录)
```

每个 `SKILL.md` 都有标准 frontmatter：
```yaml
---
name: biopython
description: Comprehensive molecular biology toolkit. Use for ...
license: Unknown
metadata:
    skill-author: K-Dense Inc.
---
```

### 工具
- `scan_skills.py` — 扫描器
- `scan_pr_skills.py` — PR 审查用扫描
- `pyproject.toml` + `uv.lock` — 用 uv 管依赖

### 抄哪些？
- 🥇 **整个 `scientific-skills/` 目录** —— 138 个高质量 SKILL.md 是现成的领域知识库，可直接 link 到 `~/.copilot/skills/` 或 Claude Code skills 目录
- 🥇 **`scan_skills.py`** — 看 K-Dense 怎么做 skill 索引/校验
- 🥈 **SKILL.md frontmatter schema** —— 与你 `~/.copilot/skills/lsp-usage/SKILL.md` 的 schema 比对，看是否一致

### 用法
对学术研究类任务（rag-dashboard 论文流程、academic-pipeline）非常对口 —— 比如做生物医学 RAG，可以直接挂 biopython/cellxgene/diffdock 等 skill。

---

## 3. oh-my-claudecode (OMC) — Claude Code 多智能体编排

**位置**：`07-agent-design/oh-my-claudecode/`  (6.9M, 1076 TS files / 221 MD files)

### 卖点
- "**零学习曲线**" 的 Claude Code 编排：`autopilot: build a REST API for managing tasks`
- Team 模式（v4.1.7+）= 标准编排方式，swarm / ultrapilot 都是 Team 的语法糖
- 配套姊妹项目：[oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex)（OpenAI Codex CLI 版）
- 支持 7 种语言 README（中/英/韩/日/西/越/葡）

### 关键目录
| 目录 | 文件数 | 内容 |
|---|--:|---|
| `agents/` | 19 | 角色 agent：analyst / architect / critic / debugger / designer / executor / explore / git-master / planner / qa-tester / scientist / security-reviewer / test-engineer / tracer / verifier / writer / code-reviewer / code-simplifier / document-specialist |
| `commands/` | 27 | slash commands：`/deep-interview`, `/deep-dive`, `/autoresearch`, `/skillify`, `/skill`, `/remember`, `/release`, `/ccg`, `/hud`, `/wiki`, `/learner`, `/sciomc` (scientific OMC) … |
| `skills/` | 45 | 内置 skills |
| `bridge/` | 8 | MCP/Team 桥接：`mcp-server.cjs`, `team-bridge.cjs`, `team-mcp.cjs`, `gyoshu_bridge.py`, `cli.cjs`, `runtime-cli.cjs` |
| `missions/` | 8 | "任务" 模板：optimize-omc, prove-reliability-by-finding-and-fixing-flaky-tests, enhance-omc-performance |
| `hooks/` | 1 | Claude Code hook |

### 关键概念
- **autopilot**：自然语言一句话 → 自动跑完编排
- **deep-interview**：苏格拉底式提问澄清模糊需求（加权维度衡量清晰度）
- **Team 模式**：v4.1.7 后的标准入口
- **skillify** 命令：把工作流转成可复用 skill
- **sciomc** 命令：与 scientific-skills 集成？（命名暗示）

### 抄哪些？
- 🥇 **`agents/` 19 个角色定义** — 与 wshobson-agents 对比，看哪个抽象更好
- 🥇 **`commands/deep-interview.md`** — 苏格拉底澄清流程，academic-pipeline 用得上
- 🥇 **`commands/skillify.md`** — 工作流 → skill 的自动化（你的痛点）
- 🥈 **`bridge/team-bridge.cjs`** + **`team-mcp.cjs`** — Team 编排底层
- 🥈 **`missions/`** — 看"任务"作为一级抽象怎么落地

### 避坑
- `bridge/mcp-server.cjs` 是 esbuild 单文件打包（不是源码），改不动 → 看 `team.js` 才是入口
- 整个 OMC 是 plugin，不是 lib，集成需要 Claude Code 的 `/plugin install`

---

## 🔗 三者拼装姿势

```
┌─────────────────────────────────────────┐
│  oh-my-claudecode (编排)                 │  ← 用户层
│    autopilot / team / deep-interview     │
└────────┬─────────────────────────┬──────┘
         │ 选 skill                │ 调 hook / MCP
         ▼                         ▼
┌────────────────────┐    ┌────────────────────┐
│ scientific-skills  │    │   agentmemory      │
│  138 SKILL.md     │    │  53 MCP + 12 hooks │
│  (内容)           │    │  混合检索 + 持久化  │
└────────────────────┘    └────────────────────┘
```

**实操**：
1. 用 OMC 的 `/omc-setup` 配置 team 模式
2. 在 `~/.copilot/skills/` symlink 进来 scientific-skills 中需要的目录
3. 装 agentmemory：`npm i -g @agentmemory/agentmemory && agentmemory`
4. Claude Code 自动同时具备：编排能力（OMC）+ 领域技能（K-Dense）+ 长期记忆（agentmemory）

---

## 📌 与 agent-infra-hub 已有内容的关系

| 已有 | 与新仓库的关系 |
|---|---|
| `07-agent-design/wshobson-agents/` | 与 OMC 的 `agents/` 比较：哪个角色抽象更完整？OMC 的 explore/scientist/tracer/document-specialist 是新角色 |
| `07-agent-design/metaswarm/` | 与 OMC 的 Team/Swarm 模式比较：协调机制差异 |
| `08-infrastructure/context-window/` | 与 agentmemory 的 `state/` 比较：上下文压缩 vs 持久化记忆 |
| `08-infrastructure/hooks/` | agentmemory 的 12 个 hooks 是**最完整**的 Claude Code hooks 教科书，应该提升为参考实现 |
| `06-catalogs/` 各 skill 目录 | scientific-skills 是**领域内容**层，不是工程层 skill，按学科归档 |

---

## ⏭️ 建议后续动作

1. **agentmemory 抽出可复用模块**：把 `state/hybrid-search.ts` + `state/cjk-segmenter.ts` 拆给 rag-dashboard 用
2. **scientific-skills symlink 化**：在 `06-catalogs/scientific-skills-INDEX.md` 列出 138 个 skill 名 + 一句话描述，方便快速查
3. **OMC vs metaswarm 对比文档**：写一个 `07-agent-design/orchestration-comparison.md`
4. **agent-infra-hub 主 README 更新**：把这三个加入 catalog
