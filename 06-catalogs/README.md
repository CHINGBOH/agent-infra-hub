# 06-catalogs — Skill 目录与发现入口

本目录收集 awesome-style skill 列表 + 自研索引，是"找一个现成 skill"的第一站。

## 🌟 索引文件

| 文件 | 内容 | 大小 |
|---|---|---|
| **[scientific-skills-INDEX.md](scientific-skills-INDEX.md)** | **138 个科学领域 skills** 中文索引（按 17 学科分类） | 83K |
| [scientific-skills.tsv](scientific-skills.tsv) | 上述索引的机器可读版（`name / category / lines / chars / desc / path`） | 66K |

## 📦 收录的 awesome 列表（gitlinks）

| 仓库 | Skill 数量 | 一句话 |
|---|---|---|
| [alirezarezvani-claude-skills](alirezarezvani-claude-skills/) | 313+ | 大杂烩 |
| [awesome-claude-code](awesome-claude-code/) | — | hesreallyhim 维护，最权威总索引 |
| [awesome-claude-code-toolkit](awesome-claude-code-toolkit/) | — | rohitg00 toolkit 系列 |
| [composio-awesome-claude-skills](composio-awesome-claude-skills/) | — | Composio 出品 |
| [mingrath-awesome-claude-skills](mingrath-awesome-claude-skills/) | — | mingrath 维护 |
| [travisvn-awesome-claude-skills](travisvn-awesome-claude-skills/) | — | travisvn 维护 |

## 📚 实际 skill 内容仓库（在 07-agent-design/）

- [scientific-agent-skills/](../07-agent-design/scientific-agent-skills/) — 138 个 SKILL.md 实体（K-Dense 出品，符合 [agentskills.io](https://agentskills.io/) 开放标准）

## 🔧 快速接入示例

```bash
# 给 Claude Code 接入 138 个科学 skill
ln -s /home/l/projects/agent-infra-hub/07-agent-design/scientific-agent-skills/scientific-skills/* ~/.claude/skills/

# 选择性接入（RAG / 学术研究常用 7 个）
for s in biopython rdkit scanpy paper-lookup literature-review database-lookup citation-management; do
  ln -s /home/l/projects/agent-infra-hub/07-agent-design/scientific-agent-skills/scientific-skills/$s ~/.claude/skills/
done

# 一行验证
ls ~/.claude/skills/ | wc -l
```

## 📐 SKILL.md 开放标准

所有收录 skill 遵循 [agentskills.io](https://agentskills.io/) 标准（跨 Cursor / Claude Code / Codex CLI 通用）：

```yaml
---
name: <skill-name>
description: <When to use this skill...>
license: <optional>
metadata:
    skill-author: <author>
---

# Skill Title
## Overview
## When to Use This Skill
## Examples
```
