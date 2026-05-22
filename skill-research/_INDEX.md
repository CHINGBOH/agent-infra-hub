# skill-research — Skill 系统完整索引

> 本仓库 Skill 研究的导航中心。涵盖 Skill 原理研究、官方 Personal Skills 文档、工程 Skills 实例、第三方知识图谱。

---

## Skill 系统速查

### Skill 类型一览

| 类型 | 机制 | 激活方式 | 代表 |
|------|------|---------|------|
| **A. SKILL.md 型** | Markdown 注入 context | Claude 自动根据 description 判断 | brainstorming、TDD |
| **B. MCP Tool 型** | 软件工具，Claude 调用新工具 | 工具始终可用 | code-review-graph |
| **C. Plugin 包型** | A+B+Hook+Command 组合 | 安装后自动生效 | superpowers |
| **D. Hook 型** | 事件驱动 shell 命令 | 特定事件自动触发 | hookify |

### 触发机制

```
description 字段 → Claude 读取所有 skill 的 name + description
                 → 根据任务自主决定是否调用
```

description 是**唯一触发机制**，写法决定 skill 能否被正确激活。

---

## 一、如何写 Skill（Writing Guide）

| 目录 | 内容 | 优先读 |
|------|------|--------|
| [04-writing-guide/anthropic-best-practices.md](04-writing-guide/anthropic-best-practices.md) | Anthropic 官方最佳实践 | ★★★ |
| [04-writing-guide/skill-development-official.md](04-writing-guide/skill-development-official.md) | superpowers TDD 方法论 | ★★★ |
| [03-skill-files/](03-skill-files/) | SKILL.md 写法规范、Progressive Disclosure | ★★ |
| [01-skill-anatomy/](01-skill-anatomy/) | Skill 文件格式、frontmatter 字段详解 | ★★ |

### SKILL.md Frontmatter 速查

```yaml
---
name: skill-identifier           # 必需，kebab-case
description: Use when...         # 必需，触发条件（<=1024字符）
version: 1.0.0                   # 可选
argument-hint: <arg>             # 可选
allowed-tools: [Read, Bash]      # 可选，预授权工具
model: haiku                     # 可选，覆盖模型
---
```

### Progressive Disclosure（三层加载）

```
Level 1: metadata (name + description)   → 每次对话加载 (~100词)
Level 2: SKILL.md body                   → skill 触发时加载 (<500行)
Level 3: references/ scripts/ assets/   → 按需加载 (无限制)
```

---

## 二、Skill 实例（Examples）

### Superpowers 工程级 Skills

路径：[05-examples/superpowers-skills/](05-examples/superpowers-skills/)

包含 brainstorming、TDD、debugging 等核心工程 skills 完整 SKILL.md 原文 — 学习官方工程质量 skill 写法的最佳样本。

### 最小示例

- [05-examples/example-skill.md](05-examples/example-skill.md) — 最简 skill 格式
- [05-examples/example-command.md](05-examples/example-command.md) — slash command 示例

---

## 三、Anthropic 官方 Personal Skills（9个）

路径：[11-anthropic-personal-skills/](11-anthropic-personal-skills/)  
总览：[11-anthropic-personal-skills/README.md](11-anthropic-personal-skills/README.md)  
来源：爬取自 claude.ai/customize/skills（2026-05-23）

| Skill | 核心模式 | 完整程度 |
|-------|---------|---------|
| [algorithmic-art](11-anthropic-personal-skills/algorithmic-art/README.md) | 两阶段：哲学 → p5.js | 完整 |
| [canvas-design](11-anthropic-personal-skills/canvas-design/README.md) | 两阶段：哲学 → 画布 | 完整 |
| [doc-coauthoring](11-anthropic-personal-skills/doc-coauthoring/README.md) | 三阶段：情境→精炼→读者测试 | 完整 |
| [internal-comms](11-anthropic-personal-skills/internal-comms/README.md) | 路由分发：类型识别→模板→执行 | 完整 |
| [mcp-builder](11-anthropic-personal-skills/mcp-builder/README.md) | 四阶段：研究→实现→测试→评估 | 完整 |
| [skill-creator](11-anthropic-personal-skills/skill-creator/README.md) | eval 循环：with-skill vs baseline | 完整 |
| [slack-gif-creator](11-anthropic-personal-skills/slack-gif-creator/README.md) | GIFBuilder + PIL | 完整 |
| [theme-factory](11-anthropic-personal-skills/theme-factory/README.md) | Artifact 主题样式 | 占位（待补充） |
| [web-artifacts-builder](11-anthropic-personal-skills/web-artifacts-builder/README.md) | 多组件 HTML Artifact | 占位（待补充） |

### 设计模式提炼

从 9 个官方 skill 中归纳出的可复用模式：

1. **两阶段创作**（algorithmic-art, canvas-design）：先创作意图文档 → 再执行技术实现
2. **结构化工作流**（doc-coauthoring, mcp-builder）：明确阶段划分，每阶段有验收标准
3. **路由分发**（internal-comms）：identify_type → load_template → execute
4. **Eval 循环**（skill-creator）：with-skill vs baseline subagent → grade → feedback → improve
5. **资源引用**（所有 skill）：SKILL.md body 引用 references/ 中的详细资料

---

## 四、MCP 构建专项 Skills（3套）

| 套件 | 路径 | 内容 |
|------|------|------|
| build-mcp-server | [build-mcp-server/](build-mcp-server/) | 完整 MCP Server 开发流程 + SDK 参考原文 |
| build-mcp-app | [build-mcp-app/](build-mcp-app/) | MCP App UI Widget 组件 + 6个模板 |
| build-mcpb | [build-mcpb/](build-mcpb/) | MCPB 捆绑包 + manifest schema + 安全指南 |

---

## 五、Plugin 系统（Plugin System）

| 目录 | 内容 |
|------|------|
| [02-plugin-system/](02-plugin-system/) | Plugin 目录结构、plugin.json 格式、自动发现机制 |
| [07-plugin-inventory/](07-plugin-inventory/) | 本机已安装所有插件清单 |
| [08-personal-skills/](08-personal-skills/) | 用户个人 skills（~/.claude/skills/） |
| [09-skill-creator/](09-skill-creator/) | Anthropic 官方 skill 创建工具完整代码 |

### Plugin 目录结构速查

```
my-plugin/
├── .claude-plugin/plugin.json   ← 插件清单（必需）
├── commands/                    ← slash commands (.md)
├── agents/                      ← 子 Agent 定义 (.md)
├── skills/skill-name/SKILL.md   ← Skill 定义
├── hooks/hooks.json             ← 事件钩子
└── .mcp.json                    ← MCP server 定义
```

---

## 六、Hooks 系统研究

路径：[06-hooks/](06-hooks/)  
内容：Hook 事件类型、hooks.json 格式详解  
实例在：[../08-infrastructure/hooks/](../08-infrastructure/hooks/)

---

## 七、MCP Tool 型 Skill（B型）

路径：[10-mcp-tool-skills/](10-mcp-tool-skills/)  
内容：B型 Skill 类型说明 + code-review-graph 完整工具文档

---

## 八、知识图谱（外部仓库索引）

路径：[12-third-party-repos/README.md](12-third-party-repos/README.md)

已索引的 7 个外部仓库（通过 code-review-graph MCP 查询）：

| 仓库 | repo_root |
|------|-----------|
| yt-dlp | `/home/l/projects/03_third-party-sources/yt-dlp` |
| FinceptTerminal | `/home/l/projects/03_third-party-sources/FinceptTerminal` |
| the-book-of-secret-knowledge | `/home/l/projects/03_third-party-sources/the-book-of-secret-knowledge` |
| odoo | `/home/l/projects/03_third-party-sources/odoo` |
| chrome-devtools-mcp | `/home/l/projects/03_third-party-sources/chrome-devtools-mcp` |
| ai-engineering-from-scratch | `/home/l/projects/03_third-party-sources/ai-engineering-from-scratch` |
| codegraph | `/home/l/projects/03_third-party-sources/codegraph` |

---

## 研究路线建议

```
入门: 05-examples/example-skill.md
  ↓
理解机制: 02-plugin-system/
  ↓
学写法: 04-writing-guide/anthropic-best-practices.md
  ↓
看工程实践: 04-writing-guide/skill-development-official.md
  ↓
看真实例子: 05-examples/superpowers-skills/
  ↓
官方 skill 深读: 11-anthropic-personal-skills/
  ↓
创建工具: 09-skill-creator/
```
