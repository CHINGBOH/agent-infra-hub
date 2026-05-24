# Superpowers Skill 集合

来源：`~/.claude/plugins/cache/claude-plugins-official/superpowers/5.1.0/skills/`
版本：5.1.0（作者：Jesse Vincent，MIT 协议）

## 包含的 Skills

| 文件 | Skill 名 | 功能 |
|------|----------|------|
| [using-superpowers.md](using-superpowers.md) | using-superpowers | 会话启动时注入，建立 skill 使用规则（每次对话都激活） |
| [brainstorming.md](brainstorming.md) | brainstorming | 创意工作前的需求探索和设计流程 |
| [writing-skills.md](writing-skills.md) | writing-skills | 创建/编辑 skill 的完整方法论（TDD 应用于文档） |
| [systematic-debugging.md](systematic-debugging.md) | systematic-debugging | 4阶段根因定位调试流程 |
| [test-driven-development.md](test-driven-development.md) | test-driven-development | RED-GREEN-REFACTOR 严格 TDD 循环 |
| [subagent-driven-development.md](subagent-driven-development.md) | subagent-driven-development | 子 Agent 驱动开发（并行任务执行+两阶段审查） |
| [verification-before-completion.md](verification-before-completion.md) | verification-before-completion | 声称完成前的强制验证流程 |

## Superpowers 的设计哲学

Superpowers 是一套**完整的软件开发方法论**，通过 skill 系统实现：

1. **brainstorming** → 需求探索，生成设计文档
2. **using-git-worktrees** → 隔离工作空间
3. **writing-plans** → 分解为精确的实现任务
4. **subagent-driven-development** → 子 Agent 并行执行
5. **test-driven-development** → 严格 TDD
6. **requesting-code-review** → 任务间代码审查
7. **finishing-a-development-branch** → 合并/PR 决策

## 关键设计特征

### using-superpowers 的 EXTREMELY-IMPORTANT 模式

`using-superpowers` skill 使用了极强的触发规则：

```
如果有哪怕 1% 的可能性某个 skill 适用，你就必须调用它。
这不是可商量的。这不是可选的。
```

这种写法用于克服 AI 的"理性化"倾向——AI 会找借口跳过 skill。

### HARD-GATE 模式

`brainstorming` skill 使用了 HARD-GATE 标签：

```
<HARD-GATE>
在展示设计并获得用户批准之前，
绝对不能写任何代码或执行任何实现操作。
</HARD-GATE>
```

用于强制执行不可跳过的流程节点。

### 理性化拦截表格

`writing-skills` 和其他 discipline skill 都包含：

| 借口 | 现实 |
|------|------|
| "这个太简单不需要测试" | 简单代码也会出错。测试只需 30 秒。 |
| "我已经手动测了" | 等同于无测试。 |

这种模式用于主动封堵 AI 的借口。
