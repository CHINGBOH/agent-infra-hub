# Claude Code Skill 深度研究

本目录收录了 Claude Code Plugin/Skill 系统的完整原始资料，用于深入研究其工作机制。

## Skill 类型分类

Claude Code 中的"技能"不止一种形态，共四类：

| 类型 | 机制 | 激活方式 | 例子 |
|------|------|----------|------|
| **A. SKILL.md 型** | Markdown 文本注入 context | Claude 读 description 自动判断 | brainstorming、TDD、debugging |
| **B. MCP Tool 型** | 软件工具，Claude 调用新工具 | 工具始终可用，Claude 按需调用 | code-review-graph、GitHub MCP |
| **C. Plugin 包型** | A+B+Hook+Command 组合包 | 安装插件后自动生效 | superpowers、frontend-design |
| **D. Hook 型** | 事件驱动 shell 命令 | 特定事件自动触发 | security-guidance、hookify |

**本研究目录主要覆盖 A 型（01-09）和 B 型（10）。**

---

## 什么是 SKILL.md 型 Skill（A型）？

让 Claude 在特定任务场景下自动激活的"上下文指导文档"。

- **不是命令**（用户手动调用）
- **不是 Agent**（Claude 派生的子进程）
- **是**：Claude 根据任务上下文自动调用的上下文指导文档

---

## 目录结构

| 目录 | 内容 |
|------|------|
| [01-skill-anatomy/](01-skill-anatomy/) | Skill 的解剖结构：文件格式、frontmatter、加载机制 |
| [02-plugin-system/](02-plugin-system/) | Plugin 目录结构、plugin.json 格式、自动发现机制 |
| [03-skill-files/](03-skill-files/) | SKILL.md 写法规范、Progressive Disclosure 设计 |
| [04-writing-guide/](04-writing-guide/) | 官方写作指南（Anthropic 最佳实践 + superpowers 方法论） |
| [05-examples/](05-examples/) | 真实 skill 文件（example-plugin + 全套 superpowers skills） |
| [06-hooks/](06-hooks/) | Hook 系统：事件类型、hooks.json 格式 |
| [07-plugin-inventory/](07-plugin-inventory/) | 本机已安装所有插件的清单 |
| [08-personal-skills/](08-personal-skills/) | 用户个人 skill（~/.claude/skills/） |
| [09-skill-creator/](09-skill-creator/) | Anthropic 官方 skill 创建工具（完整代码+分析） |
| [build-mcp-server/](build-mcp-server/) | MCP Server 开发技能集（3个 skill + 所有 references 原文） |
| [build-mcpb/](build-mcpb/) | MCPB 本地捆绑包 skill（含 manifest schema、安全指南） |
| [build-mcp-app/](build-mcp-app/) | MCP App 交互 UI 组件 skill（含 widget 模板等6个 references） |
| [10-mcp-tool-skills/](10-mcp-tool-skills/) | **B型 MCP Tool 型 Skill**：类型说明 + code-review-graph 完整文档 |
| [11-anthropic-personal-skills/](11-anthropic-personal-skills/) | **Anthropic 官方 Personal Skills**：从 claude.ai/customize/skills 爬取的 9 个官方技能完整文档 |
| [12-third-party-repos/](12-third-party-repos/) | **第三方仓库知识索引**：7 个已安装并建立 code-review-graph 索引的外部仓库（yt-dlp/Fincept/odoo/chrome-devtools-mcp 等） |

---

## 关键概念速查

### Skill 的三层加载（Progressive Disclosure）

```
Level 1: metadata (name + description)   → 每次对话都加载 (~100 词)
Level 2: SKILL.md body                   → skill 触发时加载 (<500 行)
Level 3: references/ scripts/ assets/   → 按需加载 (无限制)
```

### Plugin 目录结构

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json          ← 插件清单（必需）
├── commands/                ← 斜杠命令 (.md 文件)
├── agents/                  ← 子 Agent 定义 (.md 文件)
├── skills/                  ← Skills（每个子目录一个 skill）
│   └── skill-name/
│       └── SKILL.md         ← skill 定义（必需）
├── hooks/
│   └── hooks.json           ← 事件钩子配置
└── .mcp.json                ← MCP server 定义
```

### SKILL.md frontmatter 格式

```yaml
---
name: skill-identifier           # 必需，kebab-case
description: Use when...         # 必需，触发条件描述（<=1024字符）
version: 1.0.0                   # 可选
argument-hint: <arg>             # 可选，用于命令型 skill
allowed-tools: [Read, Bash]      # 可选，预授权工具
model: haiku                     # 可选，覆盖模型
---
```

### 触发机制

Claude 读取所有已安装 skill 的 `name + description`，根据用户任务自主决定是否调用。  
**description 是触发的唯一机制**——它决定了 Claude 在什么场景下会 invoke 这个 skill。

---

## 本机 Plugin 位置

| 路径 | 说明 |
|------|------|
| `~/.claude/plugins/marketplaces/claude-plugins-official/` | 官方 marketplace 镜像（所有可用插件） |
| `~/.claude/plugins/cache/claude-plugins-official/` | 已安装插件的缓存（含完整文件） |
| `~/.claude/skills/` | 用户个人 skills（不通过插件） |
| `~/.claude/settings.json` | Claude Code 配置（含已启用插件） |

---

## 研究路线建议

1. **入门**：先读 [05-examples/example-skill.md](05-examples/example-skill.md) 了解最小 skill 格式
2. **理解机制**：读 [02-plugin-system/plugin-structure-skill.md](02-plugin-system/plugin-structure-skill.md)
3. **学写法**：读 [04-writing-guide/anthropic-best-practices.md](04-writing-guide/anthropic-best-practices.md)
4. **看工程实践**：读 [04-writing-guide/skill-development-official.md](04-writing-guide/skill-development-official.md)（superpowers 的 TDD 方法论）
5. **看真实例子**：浏览 [05-examples/superpowers-skills/](05-examples/superpowers-skills/) 下的所有 skill
6. **了解创建工具**：读 [09-skill-creator/skill-creator.md](09-skill-creator/skill-creator.md)
