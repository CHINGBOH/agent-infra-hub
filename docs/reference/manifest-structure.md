# `MANIFEST.md` — 结构约定

> AI agent 主入口的章节布局契约。修改 MANIFEST 前先读这个，确保不破坏导航不变量。

---

## 顶层章节顺序（不可重排）

```
1. 一句话定位
2. 快速定位（按意图）       ← 意图→路径主表
3. Skills                   ← 按子类罗列 SKILL.md 组件
4. Agent Patterns           ← 链入 07-agent-design/_INDEX.md
5. Infrastructure           ← 链入 08-infrastructure/_INDEX.md
6. Knowledge Graphs         ← code-review-graph 已索引仓库
7. Tools                    ← 本仓库可执行工具
8. Catalogs                 ← 06/05/09 三块社区索引
9. 跨模块组合速查 {#cross-refs}      ← pattern × infra × governance 组合
10. Experimental APIs {#experimental-apis}  ← 实验性依赖警告
11. Use Cases               ← 组装示例
12. 分层导航路径            ← ASCII 树
```

## 锚点合约

| 锚点 | 提供给谁引用 |
|------|--------------|
| `#cross-refs` | 07/08/wshobson `_INDEX.md` 顶部"跨模块组合"链接 |
| `#experimental-apis` | wshobson `_INDEX.md` 实验性 plugin 段，任何引用实验性 flag 的文档 |
| `#skills`, `#agent-patterns`, `#infrastructure`, `#knowledge-graphs`, `#tools`, `#catalogs` | 由 markdown 标题自动生成（GFM slug） |

破坏锚点会触发 `docs/_generated/link-report.md` 的 broken 计数上升——CI 失败。

## 表格列规范

### 「快速定位」表
- 列：`我需要…` / `路径`
- 路径必须是相对链接，目标须能解析。

### 「Skills」分子节表
- 列至少含：`Skill` / `触发场景` 或 `功能`
- 每行的 `[→]` 链接指向 SKILL.md 或子 README。

### 「Agent Patterns」表
- 列：`模式` / `来源` / `核心机制` / `适用场景`
- wshobson 行**必须**带二级路由链接：`wshobson-agents（81 plugins，[二级路由 →](07-agent-design/wshobson-agents-INDEX.md)）`。

### 「跨模块组合速查」表
- 列：`你的 Agent 模式` / `应该搭配的 Hooks` / `Context 策略` / `隔离方式` / `治理 / 观测`
- 每个单元格至少 1 个可点击的相对链接。

### 「Experimental APIs」表
- 列：`Flag / API` / `启用方式` / `影响的组件` / `稳定性`
- 每条影响组件需可点击。

## 维护规则

1. **任何新增的一级目录** → 在「分层导航路径」ASCII 树里加一行。
2. **任何新增的 use-case** → 在「Use Cases」表加一行，并在 `catalog.json` 加对应资源。
3. **任何新增的实验性 flag** → 加入「Experimental APIs」表，并在使用它的文档里链回 `#experimental-apis`。
4. **修改章节顺序** → 同步更新本文件 + `docs/architecture/documentation-system.md`。
5. 提交前 `make docs-links` 必须 0 broken。

## 校验

```bash
make docs-links     # 检查所有相对链接
grep -n '^## ' MANIFEST.md   # 比对章节顺序
```
