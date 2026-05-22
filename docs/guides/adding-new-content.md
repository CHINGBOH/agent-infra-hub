# 向 agent-infra-hub 添加新内容

> 把新 skill/pattern/候选库塞进仓库的标准流程。保证导航不变量不被破坏。

---

## 0. 决策：你要加的是什么？

参考 [../architecture/repo-layout.md](../architecture/repo-layout.md) §「添加新组件时的去向决策表」决定目录。

---

## 1. 添加一个新 Skill

### 1.1 选目录

- 数据分析 → `01-data-analysis/<skill-name>/`
- R/Quarto → `02-r-quarto/<skill-name>/`
- Jupyter → `03-jupyter/<skill-name>/`
- 学术研究 → `04-research/<skill-name>/`
- 通用/不属于以上 → 先开 issue 讨论

### 1.2 文件结构

```
<skill-name>/
├── SKILL.md          # YAML frontmatter: name, description, triggers
├── README.md         # 给人看
└── <额外 references>/
```

### 1.3 登记

1. 在 `catalog.json` `resources[]` 加一条（schema 见 [../reference/catalog-schema.md](../reference/catalog-schema.md)）。
2. 在 `MANIFEST.md` 对应 Skills 子节加一行表。
3. 跑 `make docs` 验证。

---

## 2. 添加一个新 Agent Pattern

### 2.1 目录

`07-agent-design/<pattern-name>/` — 通常是 vendored clone（带 `.git`）。`.gitignore` 已通配。

### 2.2 登记

1. 在 [`07-agent-design/_INDEX.md`](../../07-agent-design/_INDEX.md) 顶部「模式选型速查」表加一行。
2. 在 `MANIFEST.md` 「Agent Patterns」表加一行。
3. 如果是企业级 / 实验性，在 [跨模块组合](cross-module-composition.md) 加一个场景。
4. 在 `catalog.json` 加 resource 条目，`type: agent_pattern`。

---

## 3. 添加一个 Infrastructure 组件

### 3.1 目录

按支柱归入：

```
08-infrastructure/{hooks,context-window,tool-use-mcp,subagent-isolation}/<component>/
```

### 3.2 登记

1. 在 [`08-infrastructure/_INDEX.md`](../../08-infrastructure/_INDEX.md) 对应支柱小节加表行。
2. 在 `MANIFEST.md` 「Infrastructure」对应小节加行。
3. 在 [跨模块组合](cross-module-composition.md) 至少一个场景里出现。
4. `catalog.json` 加 resource，`type: infrastructure`。

---

## 4. 添加一个候选引入仓库（09）

### 4.1 仅元数据（推荐起步）

编辑 [`09-agent-infra-catalog/catalog.yaml`](../../09-agent-infra-catalog/catalog.yaml)：

```yaml
- name: org/repo
  url: https://github.com/org/repo
  category: orchestrators   # 或其他 taxonomy 内值
  artifact_types: [orchestrator]
  agent_layers: [orchestration]
  capabilities: [...]
  import_mode: metadata_first
  priority: medium
```

### 4.2 浅克隆候选

如果 `priority: high` 且需本地审阅：

```bash
cd 09-agent-infra-catalog/<category>/
git clone --depth=1 <url>
```

然后在 [`09-agent-infra-catalog/README.md`](../../09-agent-infra-catalog/README.md) §「本地浅克隆源码」加一行。

### 4.3 验证

```bash
make docs-catalog
```

报告里 `Not yet cloned locally` 计数应反映你的预期（metadata-only 应该列在那里；clone 不应该）。

---

## 5. 添加一个新 Use Case

1. 在 `use-cases/<scenario-name>.md` 写场景：必须列出用到的本仓库组件清单 + 每个的可点链接。
2. 在 `MANIFEST.md` 「Use Cases」表加行。
3. `catalog.json` 加 resource，`type: use_case`。

---

## 6. 添加一个新工具（`tools/<name>.py`）

### 6.1 约束

- **仅标准库**（参考现有 `agent_kb.py` / `docs_gen.py`）
- 顶部 docstring 描述用途与示例命令
- 用 `argparse`（不要用 click/typer）——保持反射生成可用
- 在 `Makefile` 加 target

### 6.2 如果工具有 CLI 也需要文档？

按 [架构文档](../architecture/documentation-system.md) §「扩展：添加新的派生文档」步骤，在 `tools/docs_gen.py` 加一个反射生成函数。

---

## 7. 提交前自检

```bash
make docs          # 重生成所有派生文档
make docs-check    # 应该输出 ✅
grep "Broken: \*\*0\*\*" docs/_generated/link-report.md   # 死链为 0
grep "Missing on disk: \*\*0\*\*" docs/_generated/catalog-fs-report.md   # catalog 一致
```

全部通过再 commit。

---

## 8. 常见错误

| 症状 | 原因 | 修复 |
|------|------|------|
| `make docs-check` 报漂移 | 改了 `agent_kb.py` 但忘了 `make docs` | 跑 `make docs` 再提交 |
| link-report 报 broken | MANIFEST 或 _INDEX 写了错误相对路径 | 修路径，重跑 `make docs-links` |
| catalog-fs 报 Missing on disk | `catalog.json` 写了不存在的 path | 修 path 或先 commit 文件 |
| MANIFEST 的锚点链接失效 | 改了章节标题但锚点未同步 | 参考 [../reference/manifest-structure.md](../reference/manifest-structure.md) 锚点合约 |
