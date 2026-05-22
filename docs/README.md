# `docs/` — agent-infra-hub Technical Documentation

> **AI agent 入口：** [/MANIFEST.md](../MANIFEST.md)
> **本目录：** 给人和 agent 看的深度技术文档（架构、参考、操作指南、审计）。

---

## 目录结构

```
docs/
├── README.md                ← 你在这里
├── architecture/            ← 设计文档 / 系统不变量
├── reference/               ← 精确 API/格式参考（部分自动生成）
├── cli/                     ← CLI 用户手册（高层叙述）
├── guides/                  ← 操作指南、选型手册、集成手册
├── audits/                  ← 一次性 / 持续审计报告
└── _generated/              ← 自动生成产物（勿手改）
```

## 入口索引

### 架构 — [architecture/](architecture/)

| 文档 | 说明 |
|------|------|
| [architecture/README.md](architecture/README.md) | 架构总览 + 模块边界 |
| [architecture/repo-layout.md](architecture/repo-layout.md) | 仓库一级目录布局与不变量 |
| [architecture/documentation-system.md](architecture/documentation-system.md) | **本套活文档系统的设计**（代码↔文档穿透） |
| [architecture/agent-kb-cli-agent-skill-selection.md](architecture/agent-kb-cli-agent-skill-selection.md) | `agent_kb.py` 用于 agent skill 选型的设计 |

### 参考 — [reference/](reference/)

| 文档 | 来源 | 性质 |
|------|------|------|
| [reference/agent_kb_cli.md](reference/agent_kb_cli.md) | `tools/agent_kb.py` argparse | 🤖 自动生成 |
| [reference/catalog-schema.md](reference/catalog-schema.md) | `catalog.json` 结构 | 手写 |
| [reference/manifest-structure.md](reference/manifest-structure.md) | `MANIFEST.md` 章节约定 | 手写 |

### CLI — [cli/](cli/)

| 文档 | 说明 |
|------|------|
| [cli/agent-kb-cli.md](cli/agent-kb-cli.md) | `agent_kb.py` 高层用户指南（任务驱动） |

### 操作指南 — [guides/](guides/)

| 文档 | 场景 |
|------|------|
| [guides/cross-module-composition.md](guides/cross-module-composition.md) | 如何把 07 (agent pattern) × 08 (infra) × 09 (governance) 组合成完整 agent |
| [guides/wshobson-plugin-selection.md](guides/wshobson-plugin-selection.md) | wshobson 81 个 plugin 的选型决策树 |
| [guides/experimental-apis.md](guides/experimental-apis.md) | 实验性 Claude Code API 的引入策略 |
| [guides/adding-new-content.md](guides/adding-new-content.md) | 向仓库新增 skill / pattern / 候选库的流程 |

### 审计 — [audits/](audits/)

| 文档 | 性质 |
|------|------|
| [audits/agent-query-readiness.md](audits/agent-query-readiness.md) | 一次性：agent 可查询性评估 |
| [_generated/link-report.md](_generated/link-report.md) | 🤖 自动：跨文档链接审计 |
| [_generated/catalog-fs-report.md](_generated/catalog-fs-report.md) | 🤖 自动：catalog 与文件系统一致性 |

### 自动生成 — [_generated/](_generated/)

| 文件 | 真值源 | 重生成命令 |
|------|--------|------------|
| `cli-help.md` | `tools/agent_kb.py` argparse | `make docs-cli` |
| `cli-signatures.json` | 同上（机器可读） | `make docs-cli` |
| `link-report.md` | 所有 `*.md` 文件 | `make docs-links` |
| `catalog-fs-report.md` | `catalog.json` + `09-agent-infra-catalog/catalog.yaml` | `make docs-catalog` |

⚠️ `_generated/` 下任何文件都 **不要手改**。改源码后 `make docs` 一次性重生成。

---

## 文档↔代码穿透原则

本仓库的"活文档"靠三个机制保持新鲜：

1. **真值单源（Single Source of Truth）**
   - CLI 签名的真值是 `tools/agent_kb.py` 的 argparse。文档由 `docs_gen.py` 反射生成。
   - 仓库资源的真值是 `catalog.json` 和 `09-agent-infra-catalog/catalog.yaml`。文档由审计脚本对照文件系统。

2. **生成器 + 校验器（[tools/docs_gen.py](../tools/docs_gen.py)）**
   - `make docs` — 全量重生成派生文档。
   - `make docs-check` — CI 门控；若派生文档与提交版不一致，退出非零。

3. **链接审计（broken-link gate）**
   - 每次 `make docs` 都会扫全部我们维护的 `*.md`，把死链汇总到 `_generated/link-report.md`。
   - 当前基线：**0 broken** 在 73 个文件 / 205 条链接中。

完整设计：[architecture/documentation-system.md](architecture/documentation-system.md)

---

## 我该读哪个？

| 我是… | 从这里开始 |
|-------|-----------|
| AI agent 找轮子 | [/MANIFEST.md](../MANIFEST.md) |
| 用 `agent_kb.py` 检索 | [cli/agent-kb-cli.md](cli/agent-kb-cli.md) → [reference/agent_kb_cli.md](reference/agent_kb_cli.md) |
| 设计多 agent 系统 | [guides/cross-module-composition.md](guides/cross-module-composition.md) |
| 选 wshobson plugin | [guides/wshobson-plugin-selection.md](guides/wshobson-plugin-selection.md) |
| 改动代码并保持文档同步 | [architecture/documentation-system.md](architecture/documentation-system.md) |
| 给仓库加新内容 | [guides/adding-new-content.md](guides/adding-new-content.md) |
| 评估仓库当前状态 | [audits/](audits/) + [_generated/](_generated/) |
