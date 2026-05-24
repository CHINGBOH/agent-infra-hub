# MCP Tool 型 Skill（第二类技能）

## Skill 类型总览

Claude Code 的"技能"不只有 SKILL.md 一种形式。完整分类：

| 类型 | 机制 | 激活方式 | 典型例子 |
|------|------|----------|---------|
| **A. SKILL.md 型** | Markdown 文本注入 context | Claude 读 description 自动判断 | brainstorming、TDD、debugging |
| **B. MCP Tool 型** | 软件工具，Claude 调用新工具 | 工具始终可用，Claude 按需调用 | code-review-graph、GitHub MCP |
| **C. Plugin 包型** | A+B+Hook+Command 的组合包 | 安装插件后自动生效 | superpowers、frontend-design |
| **D. Hook 型** | 事件驱动的 shell 命令 | 特定事件自动触发 | security-guidance、hookify |

## MCP Tool 型 Skill 的特点

与 SKILL.md 型 skill 的本质区别：

- **不消耗 context window**（工具调用结果按需返回）
- **有持久状态**（数据库/索引，跨对话保留）
- **可编程能力**（执行真实计算，不只是引导文本）
- **需要安装和配置**（pip install + MCP 注册）

## 本目录内容

- [code-review-graph/](code-review-graph/) — 知识图谱型代码分析工具（已安装 v2.3.3）

## 注册方式

MCP Tool 型 Skill 通过 `~/.mcp.json`（用户级）或项目 `.mcp.json` 注册：

```json
{
  "mcpServers": {
    "tool-name": {
      "command": "uvx",
      "args": ["package-name", "serve"],
      "cwd": "/path/to/repo",
      "type": "stdio"
    }
  }
}
```
