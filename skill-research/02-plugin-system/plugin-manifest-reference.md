# Plugin Manifest（plugin.json）完整参考

每个插件必须在 `.claude-plugin/plugin.json` 中包含清单文件。

## 最小格式

```json
{
  "name": "my-plugin"
}
```

## 完整格式

```json
{
  "name": "plugin-name",
  "version": "1.0.0",
  "description": "插件用途的简短说明",
  "author": {
    "name": "作者名",
    "email": "email@example.com",
    "url": "https://example.com"
  },
  "homepage": "https://docs.example.com",
  "repository": "https://github.com/user/plugin-name",
  "license": "MIT",
  "keywords": ["testing", "automation", "ci-cd"],
  "commands": "./custom-commands",
  "agents": ["./agents", "./specialized-agents"],
  "hooks": "./config/hooks.json",
  "mcpServers": "./.mcp.json"
}
```

## 字段说明

| 字段 | 必需 | 格式 | 说明 |
|------|------|------|------|
| `name` | ✅ | kebab-case | 唯一标识符，小写+连字符 |
| `version` | | SemVer | 语义化版本 |
| `description` | | string | 插件描述 |
| `author` | | object | 作者信息 |
| `homepage` | | URL | 文档地址 |
| `repository` | | URL | 代码仓库 |
| `license` | | string | 许可证类型 |
| `keywords` | | string[] | 插件发现标签 |
| `commands` | | path/path[] | 自定义命令路径（补充默认 commands/ 目录） |
| `agents` | | path/path[] | 自定义 agent 路径 |
| `hooks` | | path | 自定义 hooks.json 路径 |
| `mcpServers` | | path | 自定义 .mcp.json 路径 |

**注意**：自定义路径是**补充**默认路径，不是替换。默认路径下的组件也会加载。

## 自动发现规则

Claude Code 按以下顺序自动发现组件：

1. 读取 `.claude-plugin/plugin.json`
2. 扫描 `commands/` 目录下所有 `.md` 文件 → 注册为斜杠命令
3. 扫描 `agents/` 目录下所有 `.md` 文件 → 注册为 agent
4. 扫描 `skills/` 目录下各子目录的 `SKILL.md` → 注册为 skill
5. 加载 `hooks/hooks.json` → 注册事件 hook
6. 加载 `.mcp.json` → 启动 MCP server

## 路径变量

在 hooks 和 MCP server 配置中使用 `${CLAUDE_PLUGIN_ROOT}` 引用插件根目录：

```json
{
  "command": "bash ${CLAUDE_PLUGIN_ROOT}/scripts/run.sh"
}
```

**永远不要**使用硬编码的绝对路径。

## 真实案例：Superpowers 插件

```json
{
  "name": "superpowers",
  "description": "Core skills library for Claude Code: TDD, debugging, collaboration patterns",
  "version": "5.1.0",
  "author": {
    "name": "Jesse Vincent",
    "email": "jesse@fsck.com"
  },
  "homepage": "https://github.com/obra/superpowers",
  "repository": "https://github.com/obra/superpowers",
  "license": "MIT",
  "keywords": ["skills", "tdd", "debugging", "collaboration", "best-practices", "workflows"]
}
```

## 真实案例：Example Plugin（最小化）

```json
{
  "name": "example-plugin",
  "description": "A comprehensive example plugin demonstrating all Claude Code extension options",
  "author": {
    "name": "Anthropic",
    "email": "support@anthropic.com"
  }
}
```
