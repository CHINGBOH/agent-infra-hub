# `catalog.json` — Schema 参考

> 仓库的机器可读资源清单。被 `tools/agent_kb.py` 读取建索引，被 `tools/docs_gen.py catalog` 验证路径连通。

---

## 顶层结构

```json
{
  "meta": { ... },
  "categories": [...],
  "resources": [...]
}
```

## `meta`

| 字段 | 类型 | 描述 |
|------|------|------|
| `name` | string | 仓库名 |
| `description` | string | 一句话定位 |
| `version` | string | 语义化版本 |
| `updated` | string (YYYY-MM-DD) | 上次更新日期 |
| `entry_point` | string | AI agent 入口文件路径 |
| `human_docs` | string | 人类入口文件路径 |

## `categories`

字符串数组。当前枚举：

```
skill | agent_pattern | infrastructure | knowledge_graph | tool | catalog | use_case | research
```

新增分类需同步更新 [docs/architecture/repo-layout.md](../architecture/repo-layout.md)。

## `resources[]`

| 字段 | 类型 | 必需 | 描述 |
|------|------|------|------|
| `id` | string | ✅ | 全仓唯一标识符（kebab-case） |
| `name` | string | ✅ | 展示名 |
| `type` | enum (`categories`) | ✅ | 大类 |
| `subtype` | string | — | 细分（如 `anthropic_personal`、`community_curated`） |
| `source` | string | — | 来源出处（"Anthropic official"、GitHub org 等） |
| `path` | string | ✅ | 相对仓库根的路径，必须存在 |
| `trigger` | string | — | 触发场景描述（给 agent 选型用） |
| `tags` | string[] | — | 检索标签 |
| `key_pattern` | string | — | 简短描述工作流模式 |

## 完整性校验

`make docs-catalog` 会输出 [docs/_generated/catalog-fs-report.md](../_generated/catalog-fs-report.md)，列出：

- 声明的 resources 总数
- `path` 在文件系统不存在的条目（应为 0）

## 添加新资源

```jsonc
{
  "id": "my-new-skill",
  "name": "my-new-skill",
  "type": "skill",
  "subtype": "domain-specific",
  "source": "你的来源",
  "path": "01-data-analysis/my-new-skill/SKILL.md",
  "trigger": "什么场景触发",
  "tags": ["tag1", "tag2"],
  "key_pattern": "stage_a -> stage_b"
}
```

之后跑 `make docs-catalog` 应显示 Missing on disk: 0。
