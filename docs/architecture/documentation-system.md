# Documentation System — 文档↔代码穿透设计

> **核心目标：** 代码（CLI 签名、文件路径、catalog 条目、函数参数）一旦变化，文档**自动**反映到位；CI 阻止漂移。
>
> **核心机制：** 真值单源 + 反射生成 + 链接审计 + Make 编排 + CI 门控。

---

## 设计原则

### 1. Single Source of Truth（真值单源）

每一类信息只有**一个权威源头**。所有派生展示都从源头反射出来，不能与之相互独立维护。

| 信息类别 | 权威源 | 派生产物 |
|----------|--------|----------|
| CLI 命令与参数 | [tools/agent_kb.py](../../tools/agent_kb.py) 的 argparse 树 | [docs/reference/agent_kb_cli.md](../reference/agent_kb_cli.md), [docs/_generated/cli-help.md](../_generated/cli-help.md), [docs/_generated/cli-signatures.json](../_generated/cli-signatures.json) |
| 仓库内资源条目 | [catalog.json](../../catalog.json) | [docs/_generated/catalog-fs-report.md](../_generated/catalog-fs-report.md)（一致性审计） |
| 候选引入仓库 | [09-agent-infra-catalog/catalog.yaml](../../09-agent-infra-catalog/catalog.yaml) | 同上（catalog ↔ filesystem diff） |
| 所有 markdown 链接的连通性 | 文件系统真实路径 | [docs/_generated/link-report.md](../_generated/link-report.md) |

**禁止：** 在派生产物里加入只有该产物才有的事实——任何这种事实都必须先回写到权威源。

### 2. Reflective Generation（反射生成）

生成器**直接读取**权威源的结构，而非靠手工列表跟踪。

- CLI 文档：动态 import `tools/agent_kb.py`，monkey-patch `ArgumentParser.parse_args` 截获 parser 实例，遍历 `_actions`/`_choices_actions` 提取参数、类型、默认值、帮助文本。新增一个 subcommand 后只需 `make docs`，文档自动出现。
- 资源审计：解析 `catalog.json`，对每个 `resources[].path` 做 `(REPO_ROOT/path).exists()`。
- 候选库审计：扫 `catalog.yaml` 的 `repositories[].name`，在 `09-agent-infra-catalog/*/` 下找同名子目录。

代码实现：[tools/docs_gen.py](../../tools/docs_gen.py)。

### 3. Auto-Skipping Vendored Code（自动跳过 vendored）

链接审计要扫**我们维护的文档**，不扫第三方克隆。规则：

- 任何含 `.git` 子目录的目录被视作 vendored，整体跳过。
- 明确的 verbatim 上游文档（如 `skill-research/04-writing-guide/anthropic-best-practices.md`）通过 `SKIP_PATH_PREFIXES` 跳过。
- 标准排除：`node_modules/`、`data/`、`__pycache__/`、`09-agent-infra-catalog/`（候选库本就在 `.gitignore`）。

当前扫描面：**73 个 markdown 文件 / 205 条内部链接**。

### 4. CI Gate（漂移门控）

`make docs-check` 把所有生成器跑到临时目录，与已提交版本逐字节比较。任何差异 → 退出码非零。

CI 调用：
```yaml
- run: make docs-check
```

本地修了 CLI 但忘了 `make docs`？CI 立刻拦下，错误信息指明哪几个 `docs/_generated/*` 或 `docs/reference/*` 文件过时。

---

## 数据流

```
                              修改 tools/agent_kb.py（加 subcommand / 改参数）
                                            │
                                            ▼
                              ┌─────────────────────────────┐
                              │  python tools/docs_gen.py   │
                              │           all               │
                              └────────────┬────────────────┘
                                           │
              ┌────────────────────────────┼─────────────────────────────┐
              │                            │                             │
              ▼                            ▼                             ▼
    ┌───────────────────┐      ┌─────────────────────┐      ┌────────────────────┐
    │ argparse 反射      │      │ catalog.json 校验    │      │ markdown 链接扫描   │
    │ → cli-help.md      │      │ → catalog-fs-       │      │ → link-report.md    │
    │ → cli-signatures   │      │   report.md          │      │                    │
    │ → agent_kb_cli.md  │      └─────────────────────┘      └────────────────────┘
    └───────────────────┘
              │
              ▼
   git diff 显示派生文档更新；提交后 CI 通过
```

---

## 生成器命令

| Make 目标 | 等价命令 | 输出 |
|-----------|----------|------|
| `make docs` | `python3 tools/docs_gen.py all` | 全部派生文档 |
| `make docs-cli` | `python3 tools/docs_gen.py cli` | 仅 CLI 文档 |
| `make docs-links` | `python3 tools/docs_gen.py links` | 仅链接审计 |
| `make docs-catalog` | `python3 tools/docs_gen.py catalog` | 仅 catalog 审计 |
| `make docs-check` | `python3 tools/docs_gen.py check` | CI 门控 |

完整 Makefile：[../../Makefile](../../Makefile)。

---

## 扩展：添加新的派生文档

若需要新增一种"派生自代码"的文档（例如：为 `tools/某个新脚本.py` 生成参考），步骤：

1. **明确真值源** — 一段代码、一个 JSON、一个目录结构。
2. **写生成函数** — 在 `tools/docs_gen.py` 加一个 `generate_xxx()` 函数，输出到 `docs/_generated/` 或 `docs/reference/`。
3. **挂到 task switch** — 在 `main()` 的 `choices` 与 `if args.task in (...)` 分支里加入。
4. **挂到 Makefile** — 加一个 `docs-xxx` target 并加入 `make docs`。
5. **更新本仓库的 docs/README.md** — 在表格里登记新文件 + 真值源。
6. **更新 `docs/_generated/README.md`** 自动登记表（`_ensure_generated_readme()` 函数里）。

---

## 不变量（违反就视为 bug）

1. `docs/_generated/**` 内任何文件**不能手改**。
2. `docs/reference/agent_kb_cli.md` **不能手改**——它是 `tools/agent_kb.py` argparse 的镜像。
3. 任何 `**/_INDEX.md`、`MANIFEST.md`、`docs/**.md` 里的相对链接必须能通过 `make docs-links` 校验。
4. `tools/docs_gen.py` **仅使用 Python 标准库**——保证 fresh clone 上 `make docs` 立即工作。
5. CI 必须运行 `make docs-check`；本地提交前也应运行一次。

---

## 已知限制 / 待办

- 链接审计当前**不验证 anchor**（`#section`）。可扩展：parse 目标文档的 heading 集合做匹配。
- 未对 `catalog.yaml` 做完整 schema 校验，仅检查 `name → directory` 一致性。后续可引入 `jsonschema`（需要外部依赖，需评估）。
- 第三方克隆的 README 表述变化不会触发任何告警——这是有意为之，我们不维护它们的内部链接。
