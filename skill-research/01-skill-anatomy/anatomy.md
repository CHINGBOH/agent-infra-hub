# Skill 解剖结构

## Skill 是什么

Skill 是一种**模型自动调用的上下文指导文档**，区别于其他 Claude Code 扩展机制：

| 类型 | 调用方式 | 用途 |
|------|----------|------|
| **Command** | 用户手动输入 `/command` | 用户主动触发的工作流 |
| **Agent** | Claude 主动派生子进程 | 执行独立任务的子进程 |
| **Skill** | Claude 根据任务上下文自动激活 | 特定场景下的知识/流程指导 |
| **Hook** | 事件驱动（PreToolUse、SessionStart 等） | 自动化行为拦截与增强 |

---

## Skill 文件结构

### 最小结构（只需 SKILL.md）

```
skill-name/
└── SKILL.md
```

### 完整结构

```
skill-name/
├── SKILL.md              ← 主定义文件（必需）
├── references/           ← 详细参考文档（按需加载）
│   └── detailed.md
├── examples/             ← 可运行示例
│   └── example.sh
├── scripts/              ← 工具脚本（可不加载到上下文直接执行）
│   └── helper.py
└── assets/               ← 输出用素材（模板、图标等）
    └── template.html
```

---

## SKILL.md 格式

```markdown
---
name: skill-name                    # 必需：唯一标识符，kebab-case
description: Use when...            # 必需：触发条件，<=1024字符
version: 1.0.0                      # 可选
argument-hint: <required> [opt]     # 可选：命令型skill的参数提示
allowed-tools: [Read, Bash, Edit]   # 可选：预授权工具列表
model: haiku                        # 可选：覆盖模型（haiku/sonnet/opus）
---

# Skill 标题

## 概述
核心概念 1-2 句话。

## 使用时机
[可选：决策流程图，仅在决策不明显时使用]

触发场景列表。
不适用场景列表。

## 核心模式
代码示例或步骤。

## 快速参考
表格或要点。

## 常见错误
常见问题及解决方案。
```

---

## 三层加载机制（Progressive Disclosure）

这是 skill 系统最重要的设计原则：

```
┌─────────────────────────────────────────┐
│  Level 1: metadata                      │
│  name + description                     │ ← 始终在上下文中（~100词）
│  用途：Claude 决定是否调用此 skill      │
└─────────────────────────────────────────┘
           ↓ skill 触发时
┌─────────────────────────────────────────┐
│  Level 2: SKILL.md body                 │
│  核心指导内容                           │ ← skill 触发时加载（目标 <500行）
│  用途：提供具体操作指导                 │
└─────────────────────────────────────────┘
           ↓ Claude 判断需要时
┌─────────────────────────────────────────┐
│  Level 3: references/ examples/         │
│  scripts/ assets/                       │ ← 按需加载（无限制）
│  用途：详细文档、工具、素材             │
└─────────────────────────────────────────┘
```

**为什么这么设计**：防止大量 skill 同时加载导致 context 爆炸。metadata 很小，只有真正需要的 skill 才会展开完整内容。

---

## Skill 的两种类型

### 1. 模型自动调用型（大多数 skill）

Claude 读取 description，自主决定是否 invoke。用于流程指导、最佳实践等。

```yaml
description: Use when implementing any feature or bugfix, before writing code
```

### 2. 用户调用型（命令型 skill）

用户通过 `/command` 手动触发，skill 接收 `$ARGUMENTS` 参数。

```yaml
---
name: my-command
description: Short description shown in /help
argument-hint: <required-arg> [optional-arg]
allowed-tools: [Read, Bash]
---

User called with: $ARGUMENTS
```

---

## description 字段设计原则

**description 是触发的唯一机制**，至关重要：

```yaml
# ❌ 错：描述 skill 做什么（workflow 摘要）
description: Use when debugging - analyze logs, trace calls, write fix

# ❌ 错：太模糊
description: For debugging help

# ✅ 对：只描述触发条件
description: Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes

# ✅ 对：包含具体触发场景
description: Use when the user asks to "create a hook", "add a PreToolUse hook", "validate tool use"
```

**关键规则**：description 只描述**何时使用**，不描述**如何工作**。如果 description 包含 workflow 摘要，Claude 会用 description 替代真正读取 SKILL.md，导致 skill 被绕过。

---

## 词数目标

| skill 类型 | SKILL.md 目标词数 |
|------------|-------------------|
| 启动流程 skill（每次对话都加载）| <150词 |
| 高频 skill | <200词 |
| 普通 skill | <500词 |
| 带 references 的复杂 skill | SKILL.md <2000词，details 移到 references/ |
