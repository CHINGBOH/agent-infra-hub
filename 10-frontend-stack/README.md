# 10-frontend-stack — 前端层"抄作业"参考

> 2026-05-25 浅克隆 7 个前端明星仓库，给 agent 系统补齐前端层（dashboard / chat UI / dev server / BFF / LLM SDK / 工具链）。详细分析见 [../09-agent-infra-catalog/2026-05-25-frontend-stack-analysis.md](../09-agent-infra-catalog/2026-05-25-frontend-stack-analysis.md)。

## 仓库清单

| 仓库 | Star | 大小 | 模块 | 抄什么 |
|---|---|---|---|---|
| [vite/](vite/) | 70k+ | 44M | 构建/dev server | `packages/vite/src/node/` 插件协议 + HMR |
| [shadcn-ui/](shadcn-ui/) | 80k+ | 29M | 组件库 | `apps/v4/registry/new-york-v4/ui/` + 官方 SKILL.md |
| [tanstack-query/](tanstack-query/) | 45k+ | 54M | 异步状态 | `packages/query-core/src/` 框架无关核心 |
| [hono/](hono/) | 22k+ | 7.2M | BFF / edge | `src/hono-base.ts` + `context.ts` |
| [vercel-ai/](vercel-ai/) | 11k+ | 24M | LLM SDK | `packages/ai/src/` + 58 个 provider |
| [assistant-ui/](assistant-ui/) | 4k+ | 22M | Chat UI | `packages/core/` + 6 个 Python 包 |
| [biome/](biome/) | 17k+ | 52M | fmt+lint | 工具链设计参考（不直接搬代码） |

合计 ~232 MB。

## 推荐组合

### Agent Dashboard（rag-dashboard 类）
```
vite + shadcn-ui (apps/v4 组件) + tanstack-query + biome
```

### Agent Chat UI
```
assistant-ui + vercel-ai + hono BFF + tanstack-query
```

### MCP server / Agent 后端
```
hono + vercel-ai (只用 provider 包) + biome
```

## ⭐ 重大发现：shadcn 官方 SKILL.md 演进

[shadcn-ui/skills/shadcn/SKILL.md](shadcn-ui/skills/shadcn/SKILL.md) 给标准 SKILL.md schema 新增了两个权限字段：

```yaml
user-invocable: false
allowed-tools: Bash(npx shadcn@latest *), Bash(pnpm dlx shadcn@latest *)
```

这是 agentskills.io 标准之外的官方扩展，建议后续重写 138 个 scientific-skills 时跟进。

## 接入示例

```bash
# 抄 shadcn 组件到 rag-dashboard
cp -r /home/l/projects/agent-infra-hub/10-frontend-stack/shadcn-ui/apps/v4/registry/new-york-v4/ui/button.tsx \
      /home/l/projects/rag-dashboard/src/frontend/web/src/components/ui/

# 浏览 hono 单一源文件
glow /home/l/projects/agent-infra-hub/10-frontend-stack/hono/src/hono-base.ts
```
