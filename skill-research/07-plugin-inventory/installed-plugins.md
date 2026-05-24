# 本机已安装插件清单

数据来源：`~/.claude/plugins/marketplaces/claude-plugins-official/`

## 官方插件（plugins/）

| 插件名 | 描述 |
|--------|------|
| agent-sdk-dev | Claude Agent SDK 开发插件 |
| claude-code-setup | 分析代码库，推荐 hooks/skills/MCP/subagents 配置 |
| claude-md-management | 维护和改进 CLAUDE.md 文件的工具集 |
| code-modernization | 遗留代码现代化（COBOL、Java/C++、单体 Web 应用）工作流 |
| code-review | 多专业 agent 的 PR 自动化代码审查 |
| code-simplifier | 简化和优化代码以提升可读性和可维护性 |
| commit-commands | 简化 git commit/push/PR 工作流的命令集 |
| cwc-makers | Code-with-Claude Makers Cardputer 的无缝接入工具 |
| example-plugin | 展示所有 Claude Code 扩展能力的参考插件 |
| explanatory-output-style | 为代码实现添加教育性解释（模拟已废弃的 Explanatory 输出风格） |
| feature-dev | 功能开发工作流，含代码库探索、架构设计、质量审查 agent |
| frontend-design | 前端 UI/UX 实现技巧 |
| hookify | 通过分析对话模式轻松创建 hooks 阻止不当行为 |
| learning-output-style | 在决策点请求有意义代码贡献的交互学习模式 |
| math-olympiad | 竞赛数学求解（IMO/Putnam/USAMO），含对抗性验证 |
| mcp-server-dev | 设计和构建 MCP server 的技能（部署模型、工具设计、认证） |
| mcp-tunnels | 通过 Anthropic MCP tunnel 连接私有 MCP server |
| playground | 创建交互式 HTML playground（单文件、可视化控制、实时预览） |
| plugin-dev | 插件开发工具集（agents/commands/hooks/MCP/plugin 结构指南） |
| pr-review-toolkit | 专注于注释/测试/错误处理/类型设计/代码质量的 PR 审查 agent |
| ralph-loop | 持续自引用 AI 循环，用于迭代开发（Ralph Wiggum 技术） |
| security-guidance | 编辑文件时警告潜在安全问题的 hook |
| skill-creator | 创建/改进/评估 skill 的完整工具链 |

## 外部插件（external_plugins/）

| 插件名 | 描述 |
|--------|------|
| asana | Asana 项目管理集成 |
| context7 | Upstash Context7 MCP server（版本化文档查找） |
| discord | Discord 频道桥接，含访问控制 |
| fakechat | 本地 iMessage 风格 Web 聊天测试界面 |
| firebase | Google Firebase MCP 集成（Firestore/Auth/Functions/Hosting） |
| github | 官方 GitHub MCP server（issue/PR/代码搜索） |
| gitlab | GitLab DevOps 集成（MR/CI/CD/issue/wiki） |
| greptile | AI 代码审查 agent（GitHub/GitLab PR 注释） |
| imessage | iMessage 频道桥接，含访问控制 |
| laravel-boost | Laravel 开发工具包 MCP server |
| linear | Linear issue 跟踪集成 |
| playwright | Microsoft 浏览器自动化和 E2E 测试 MCP server |
| serena | 语义代码分析 MCP server（LSP 集成） |
| telegram | Telegram 频道桥接，含访问控制 |
| terraform | Terraform MCP server（IaC 开发） |

## 已缓存（已安装）插件

位于 `~/.claude/plugins/cache/claude-plugins-official/`：

| 插件 | 版本 |
|------|------|
| chrome-devtools-mcp | latest |
| code-review | latest |
| code-simplifier | latest |
| context7 | latest |
| deploy-on-aws | 1.2.0 |
| frontend-design | latest |
| github | latest |
| pyright-lsp | latest |
| superpowers | 5.1.0 |
| typescript-lsp | latest |

## 用户个人 Skills（~/.claude/skills/）

| skill | 功能 |
|-------|------|
| debug-issue | 使用知识图谱系统化调试问题 |
| explore-codebase | 用图工具探索代码库结构 |
| review-changes | 审查代码变更 |
| refactor-safely | 安全重构代码 |
