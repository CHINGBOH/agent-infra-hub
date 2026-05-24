# Hook 系统参考

Hooks 是 Claude Code 的事件驱动扩展机制，在特定事件发生时自动执行 shell 命令。

## hooks.json 格式

```json
{
  "hooks": {
    "EventName": [
      {
        "matcher": "pattern",
        "hooks": [
          {
            "type": "command",
            "command": "bash ${CLAUDE_PLUGIN_ROOT}/hooks/script.sh",
            "async": false,
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

## 可用事件类型

| 事件 | 触发时机 |
|------|----------|
| `PreToolUse` | Claude 调用工具之前 |
| `PostToolUse` | Claude 调用工具之后 |
| `Stop` | Claude 完成响应时 |
| `SubagentStop` | 子 Agent 完成时 |
| `SessionStart` | 会话开始时（包括 startup/clear/compact） |
| `SessionEnd` | 会话结束时 |
| `UserPromptSubmit` | 用户提交 prompt 时 |
| `PreCompact` | 上下文压缩前 |
| `Notification` | Claude 发送通知时 |

## Superpowers 的 SessionStart Hook（实际案例）

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|clear|compact",
        "hooks": [
          {
            "type": "command",
            "command": "\"${CLAUDE_PLUGIN_ROOT}/hooks/run-hook.cmd\" session-start",
            "async": false
          }
        ]
      }
    ]
  }
}
```

这个 hook 在每次会话开始时运行，注入 superpowers 的系统上下文（可用 skill 列表等）。

## ${CLAUDE_PLUGIN_ROOT} 变量

在 hook command 中，`${CLAUDE_PLUGIN_ROOT}` 会被替换为插件的实际安装路径。这是编写可移植 hook 的关键——不要用硬编码路径。

## Hook 位置

- **Plugin hook**：`<plugin>/hooks/hooks.json`
- **全局 hook**：`~/.claude/settings.json` 的 `hooks` 字段
- **项目 hook**：`.claude/settings.json` 的 `hooks` 字段

## 匹配器（matcher）

`matcher` 是正则表达式，用于过滤事件。例如：
- `"Write|Edit"` — 仅在 Write 或 Edit 工具调用时触发
- `"startup|clear|compact"` — 仅在会话启动/清理/压缩时触发
- `""` 或省略 — 所有同类事件都触发
