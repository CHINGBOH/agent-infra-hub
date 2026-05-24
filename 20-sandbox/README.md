# 20-sandbox — 代码执行 · 沙箱明星仓库

| 仓库 | 星 | 体量 | 抄什么 |
|---|---|---|---|
| 🥇 **[e2b](./e2b/)** | 7k★ | 8.5M / 387 py | LLM 代码沙箱 SaaS + 开源 SDK；CLAUDE.md；agent 标配 |
| 🥈 **[daytona](./daytona/)** | 14k★ | 98M / 794 py | Dev environment 平台；含 agent workspace；AGENTS.md |
| **[open-interpreter](./open-interpreter/)** | 60k★ | 17M / 144 py | 本地代码解释器（早期开山之作） |
| **[pyodide](./pyodide/)** | 13k★ | 7.2M / 168 py | Python in browser via WASM；浏览器侧 agent 沙箱基石；AGENTS.md |

## 抄作业重点
- **e2b/packages/python-sdk** 是 LLM 沙箱客户端的事实接口
- **pyodide** = 完全前端 agent 解决方案（无后端依赖）
- **daytona** workspaces 模式适用于多 agent 隔离
