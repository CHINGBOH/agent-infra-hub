# 08-infrastructure — 基础设施组件索引

> Claude Code Agent 的四大基础设施支柱：Hooks / Context Window / Tool Use MCP / Subagent Isolation。

---

## 四支柱概览

```
LLM（CPU）
├── Hooks         中断系统   — 在特定生命周期事件注入行为
├── Context Window 内存管理  — 压缩、优化、Ghost Token 检测
├── Tool Use/MCP  系统调用层 — 外部工具、agent-in-agent 模式
└── Subagent      进程隔离   — Hub-and-Spoke，独立上下文
```

---

## 一、Hooks（中断系统）

> 在 Claude Code 的 13 个生命周期事件上注入自定义 shell 命令。

### 生命周期事件

```
PreToolUse       → 工具调用前
PostToolUse      → 工具调用后
PreCompact       → 上下文压缩前
Stop             → Agent 停止时
Notification     → 通知事件
UserPromptSubmit → 用户提交消息时
...共 13 个
```

### 组件

| 组件 | 内容 | 路径 |
|------|------|------|
| **claude-code-hooks-mastery** | 13个事件完整实现，TTS朗读，安全文件检查，git自动提交 | [hooks/claude-code-hooks-mastery/](hooks/claude-code-hooks-mastery/) |
| **claude-code-hooks-multi-agent-observability** | 多 Agent 场景监控 hooks，事件溯源 | [hooks/claude-code-hooks-multi-agent-observability/](hooks/claude-code-hooks-multi-agent-observability/) |
| **claude-code-hooks** | 即用 hooks 集合（karanb192 整理） | [hooks/claude-code-hooks/](hooks/claude-code-hooks/) |

### hooks.json 格式速查

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "command": "echo 'About to run Bash'"
      }]
    }]
  }
}
```

Hooks 系统原理文档：[../skill-research/06-hooks/](../skill-research/06-hooks/)

---

## 二、Context Window（内存管理）

> 管理有限上下文窗口，避免 Ghost Token，实现多层压缩。

### token-optimizer

```
路径: context-window/token-optimizer/
来源: alexgreensh
```

**核心功能：**

| 功能 | 说明 |
|------|------|
| Ghost Token 检测 | 识别上下文中残留的过期/无效内容 |
| 5层压缩策略 | 从最轻到最激进的分级压缩方案 |
| 上下文优先级管理 | 保留高价值内容，淘汰低价值内容 |
| 压缩触发时机 | 在 PreCompact hook 中自动触发 |

**使用场景：** 长对话任务，大型代码库分析，多轮迭代开发。

---

## 三、Tool Use / MCP（系统调用层）

> 通过 MCP 协议将外部工具和能力接入 Claude Code。

### claude-code-mcp（Agent-in-Agent）

```
路径: tool-use-mcp/claude-code-mcp/
来源: steipete
核心: 将 Claude Code 本身暴露为 MCP Server
```

**关键模式：** 外层 Claude → MCP 调用 → 内层 Claude Code  
适用场景：需要嵌套 agent 执行、隔离子任务执行环境。

---

### claude-code-mcp-enhanced（Boomerang 模式）

```
路径: tool-use-mcp/claude-code-mcp-enhanced/
来源: grahama1970
核心: Boomerang 任务拆分模式
```

**Boomerang 模式：**
```
主 Agent 发出任务 → 子 Agent 执行 → 结果返回主 Agent
       ↑_________________________________↓
                   (循环优化)
```

适用场景：复杂任务需要拆分后由专项 agent 处理，结果聚合回主线。

---

### claude-code-everything（全栈实战）

```
路径: tool-use-mcp/claude-code-everything/
来源: wesammustafa
```

全栈开发实战手册，涵盖 Tool Use 在实际项目中的完整用法。

---

## 四、Subagent Isolation（进程隔离）

> 子 agent 运行在独立上下文中，防止污染主 agent 状态。

### ECC（Engineering Command Center）

```
路径: subagent-isolation/ECC/
来源: affaan-m
规模: 82,000+ GitHub Stars
```

**完整 Agent Harness 系统，提供：**
- 子 agent 生命周期管理
- 上下文隔离边界
- 结果聚合和错误处理
- 监控和可观测性

---

### claude-code-sub-agent-collective

```
路径: subagent-isolation/claude-code-sub-agent-collective/
来源: vanzan01
核心: Hub-and-Spoke 上下文隔离
```

**Hub-and-Spoke 架构：**
```
             Hub Agent（协调/状态）
           /           |           \
   Spoke-1         Spoke-2         Spoke-3
  (独立上下文)    (独立上下文)    (独立上下文)
```

**关键特性：**
- 每个 Spoke 只获得完成任务必要的最小上下文
- Hub 维护全局状态，Spoke 无需知道彼此
- 防止上下文污染和信息泄漏

---

## 组合使用模式

### 生产级 Agent 系统推荐配置

```
基础层（必选）:
  + Hooks: claude-code-hooks-mastery  (生命周期管控)
  + Context: token-optimizer           (内存管理)

扩展层（按需）:
  + MCP: claude-code-mcp              (子 agent 嵌套)
  + Isolation: sub-agent-collective   (任务隔离)

监控层（可选）:
  + Hooks: hooks-multi-agent-observability (可观测性)
```

### 安全敏感场景

```
claude-code-hooks-mastery  (安全文件检查 hook)
  + ECC                    (进程级隔离)
  + token-optimizer        (防 ghost token 信息泄漏)
```

### 高并发处理场景

```
agent-farm (../07-agent-design/)  (20-50并行)
  + ccswarm (../07-agent-design/) (worktree隔离)
  + claude-code-mcp-enhanced      (Boomerang聚合)
```

---

## 相关资源

- Hooks 原理研究：[../skill-research/06-hooks/](../skill-research/06-hooks/)
- MCP Tool 型 Skill：[../skill-research/10-mcp-tool-skills/](../skill-research/10-mcp-tool-skills/)
- Agent 设计模式：[../07-agent-design/_INDEX.md](../07-agent-design/_INDEX.md)
- 候选基础设施库：[../09-agent-infra-catalog/README.md](../09-agent-infra-catalog/README.md)
