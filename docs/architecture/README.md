# Architecture — 总览

> 本目录收录 agent-infra-hub 的系统级设计文档。每一篇都描述一个**不变量**（invariant）：随代码演进必须维持的约束。

---

## 文档清单

| 文档 | 描述的不变量 |
|------|--------------|
| [repo-layout.md](repo-layout.md) | 一级目录契约：每个 `0X-*/` 编号目录的职责边界 |
| [documentation-system.md](documentation-system.md) | 文档↔代码穿透机制：派生文档必须能从真值源 100% 重生成 |
| [agent-kb-cli-agent-skill-selection.md](agent-kb-cli-agent-skill-selection.md) | `agent_kb.py recommend` 为 agent 做 skill 选型的检索语义 |

---

## 系统视图

```
┌────────────────────────────────────────────────────────────────┐
│                       AI Agent (consumer)                       │
│                                                                 │
│   读 MANIFEST.md → 走二级路由 (_INDEX.md) → 拿组件路径          │
└─────────────────────────────┬──────────────────────────────────┘
                              │
              ┌───────────────┴────────────────┐
              ▼                                ▼
   ┌─────────────────────┐         ┌──────────────────────┐
   │  Navigation Surface │         │ Source-of-Truth Data │
   │ ─────────────────── │         │ ──────────────────── │
   │  MANIFEST.md        │         │  tools/agent_kb.py   │
   │  *_INDEX.md         │         │  catalog.json        │
   │  README.md          │         │  catalog.yaml        │
   │  docs/**.md         │         │  filesystem reality  │
   └─────────────────────┘         └──────────┬───────────┘
              ▲                                │
              │      tools/docs_gen.py         │
              └────────── (regenerates) ───────┘
```

**核心契约：** Navigation Surface 的派生部分（CLI 参考、链接报告、catalog 审计）**必须**能从 Source-of-Truth Data 通过 `tools/docs_gen.py` 完整重生成。CI 用 `make docs-check` 强制。

---

## 模块边界

| 编号 | 目录 | 职责 | 不可越界做的事 |
|------|------|------|----------------|
| 01 | `01-data-analysis/` | 数据分析 skill 套件 | 不放 agent 编排逻辑 |
| 02 | `02-r-quarto/` | R/Quarto 工具链 skills | 不放 Python skills |
| 03 | `03-jupyter/` | Jupyter 集成 | 不放纯 markdown skills |
| 04 | `04-research/` | 学术研究 skills | 不放工程类 skills |
| 05 | `05-subagents/` | 专项 subagent 集合 | 不放完整 agent pattern |
| 06 | `06-catalogs/` | 社区精选索引 | 不 vendor 实际 skill 源码 |
| 07 | `07-agent-design/` | 多 agent 协作模式 | 不放基础设施 |
| 08 | `08-infrastructure/` | hooks / context / MCP / 隔离 | 不放业务 skill |
| 09 | `09-agent-infra-catalog/` | 候选引入库元数据 + 浅克隆 | 不把克隆产物入主仓 |
| — | `skill-research/` | Skill 系统研究材料 + 第三方仓库索引 | 不放可执行 skill |
| — | `tools/` | 仓库自有工具 | 仅 Python 标准库依赖 |
| — | `docs/` | 给人/agent 的深度文档 | 不放可执行代码 |
| — | `use-cases/` | 组装示例 | 必须引用本仓库已有组件 |

完整布局见 [repo-layout.md](repo-layout.md)。
