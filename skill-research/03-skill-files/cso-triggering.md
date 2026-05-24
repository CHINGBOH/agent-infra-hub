# Claude Search Optimization（CSO）：让 Skill 被正确触发

CSO 是 skill 写作中最关键的工程问题：如何让 Claude 在正确的场景下找到并调用你的 skill。

## 触发机制原理

Claude 的 skill 列表以 `name + description` 的形式注入到 system prompt。Claude 读取这个列表，根据当前任务决定是否调用某个 skill（通过 `Skill` 工具）。

**关键洞察**：Claude 只有在任务需要时才会调用 skill。简单的一步操作（"读这个文件"）通常不会触发 skill，即使 description 完全匹配。复杂、多步骤、专业化的任务才是 skill 触发的主场。

## Description 的唯一性

Description 是触发的**唯一机制**——这意味着：

1. Description 必须清楚说明**何时使用**（触发条件）
2. Description **绝对不能**描述 skill 如何工作（workflow 摘要）
3. Description 越精准，触发越准确

### 为什么不能放 workflow 摘要

**实测发现的问题**：当 description 包含 workflow 摘要时，Claude 会用 description 替代阅读完整的 SKILL.md。

例如：
```yaml
# ❌ 问题：description 摘要了 workflow
description: Use when executing plans - dispatches subagent per task with code review between tasks
```

结果：Claude 只做一次代码审查（按 description 的理解），而 SKILL.md 中的流程图明确要求两次审查。

```yaml
# ✅ 修复：只描述触发条件
description: Use when executing implementation plans with independent tasks in the current session
```

结果：Claude 正确读取 SKILL.md，执行两次审查流程。

## 高质量 Description 的特征

### 格式
```yaml
description: Use when [具体触发条件和症状]
```

### 内容要素
- **具体触发词**：用户可能说的确切短语
- **症状描述**：问题的表现（不是语言特定的症状）
- **技术无关**：除非 skill 本身是技术特定的
- **第三人称**：因为会被注入到 system prompt

### 好的例子

```yaml
# 触发词明确
description: Use when the user asks to "create a hook", "add a PreToolUse hook", "validate tool use", or mentions hook events.

# 症状描述（技术无关）
description: Use when tests have race conditions, timing dependencies, or pass/fail inconsistently.

# 技术特定（明确说明）
description: Use when using React Router and handling authentication redirects.
```

### 差的例子

```yaml
# 太模糊
description: For async testing

# 第一人称
description: I can help you with async tests when they're flaky

# 包含技术但 skill 不是技术特定的
description: Use when tests use setTimeout/sleep and are flaky

# Workflow 摘要（陷阱！）
description: Use when debugging - analyze logs, find root cause, write fix
```

## 关键词覆盖

在 skill **body** 中使用 Claude 可能搜索的词汇：
- 错误消息原文：`"Hook timed out"`, `"ENOTEMPTY"`, `"race condition"`
- 症状词：`"flaky"`, `"hanging"`, `"zombie"`, `"pollution"`
- 同义词：timeout/hang/freeze, cleanup/teardown/afterEach
- 工具名：具体命令、库名、文件类型

## 命名规范

**动词开头，清晰描述动作**：
- ✅ `condition-based-waiting` — 描述做的事
- ✅ `root-cause-tracing` — 动词+名词
- ❌ `async-test-helpers` — 太模糊
- ❌ `debugging-techniques` — 太宽泛

**动名词（-ing）适合流程类 skill**：
- `creating-skills`, `testing-skills`, `debugging-with-logs`

## Token 效率

Skill metadata 在**每次对话**都会加载到上下文，必须保持精简：

| Skill 类型 | 词数目标 |
|------------|---------|
| 每次对话都激活的启动 skill | <150词 |
| 高频调用 skill | <200词 |
| 普通 skill | <500词 |

**技巧**：
- 细节放到 `references/` 而非 SKILL.md
- 用 `--help` 引用工具文档而非重复描述
- 交叉引用其他 skill 而非重复内容
