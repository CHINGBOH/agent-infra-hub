# 2026-05-25 — 前端栈深度调研（7 个明星仓库）

> 目的：给 agent-infra-hub 补齐前端层"抄作业"参考。Agent 系统通常需要 dashboard / chat UI / dev server / 数据获取层，这 7 个仓库覆盖全部前端模块。

## 一、阵容速览

| 仓库 | Star | 规模 | 角色 |
|---|---|---|---|
| [vitejs/vite](../10-frontend-stack/vite/) | 70k+ | 545 TS | 🥇 构建工具 / dev server |
| [shadcn-ui/ui](../10-frontend-stack/shadcn-ui/) | 80k+ | 3119 TSX | 🥇 组件库（拷贝式） |
| [TanStack/query](../10-frontend-stack/tanstack-query/) | 45k+ | 614 TS / 321 TSX | 🥇 异步状态管理 |
| [honojs/hono](../10-frontend-stack/hono/) | 22k+ | 329 TS | 🥇 BFF / edge web framework |
| [vercel/ai](../10-frontend-stack/vercel-ai/) | 11k+ | 3945 TS / 58 providers | 🥇 LLM SDK + chat stream |
| [assistant-ui/assistant-ui](../10-frontend-stack/assistant-ui/) | 4k+ | 879 TSX | 🥇 Chat UI 组件 |
| [biomejs/biome](../10-frontend-stack/biome/) | 17k+ | 4217 Rust | 🥇 fmt + lint 工具链 |

合计约 178MB（浅克隆）。

## 二、每个仓库的"抄什么"

### 1️⃣ vitejs/vite — 构建/dev server 标杆

**热点文件**：
- `packages/vite/src/node/server/` — dev server (HMR / middleware / WS)
- `packages/vite/src/node/plugin.ts` + `plugins/` — Rollup-style 插件接口
- `packages/vite/src/node/optimizer/` — esbuild 预构建
- `packages/vite/src/node/config.ts` — 配置合并 / 多环境 (environment API 新特性)

**抄走**：
- 插件钩子设计（`resolveId / load / transform / handleHotUpdate`）
- HMR 协议（client/server WS）
- 自定义环境模型 (v6+, `environment API`)

**避坑**：插件顺序 `enforce: 'pre' | 'post'` 一旦写错排序很难调；先看 `server/pluginContainer.ts`。

---

### 2️⃣ shadcn-ui/ui — 拷贝式组件 + 🆕 官方 SKILL.md

**重大发现**：shadcn 自家在 `skills/shadcn/SKILL.md` 公开了**符合 [agentskills.io](https://agentskills.io/) 标准的 skill**，并扩展了字段：

```yaml
---
name: shadcn
description: Manages shadcn components and projects...
user-invocable: false                           # 🆕 新字段
allowed-tools: Bash(npx shadcn@latest *), ...   # 🆕 新字段，权限白名单
---
```

> 这是 SKILL.md 标准的**官方演进**：从纯描述 → 加入权限模型。值得同步到 `06-catalogs/README.md` schema 段落。

**热点目录**：
- `apps/v4/` — Tailwind v4 官方组件库源码（**真正要抄的地方**，不是 packages/）
- `packages/shadcn/` — CLI（registry 拉取逻辑）

**抄走**：
- `apps/v4/registry/new-york-v4/ui/` 所有组件（拷贝式 = 不依赖 npm）
- `components.json` 配置范式
- CLI 的 registry 协议（远程组件分发）

---

### 3️⃣ TanStack/query — 异步状态金标准

**热点文件**：
- `packages/query-core/src/` — 框架无关核心（QueryClient / Query / Mutation）
- `packages/query-core/src/queryObserver.ts` — 订阅模型
- `packages/react-query/src/useQuery.ts` — React 适配层（极薄）

**抄走**：
- `staleTime / gcTime` 双缓存策略
- query key 序列化 → 自动 dedup
- 离线 + retry + 焦点重连默认行为

**避坑**：直接抄 React 版会绑死 React；先抄 `query-core` 做框架无关层。

---

### 4️⃣ honojs/hono — 优雅极致的 web framework

**特点**：329 个 TS 文件，单一 `src/` 目录，**`hono.ts` 只有 34 行**，核心逻辑在 `hono-base.ts` (545) + `context.ts` (780)。

**抄走**：
- Context API 设计 (`c.json() / c.req / c.var`)
- 5 种 router 并存可选（`trie-router / reg-exp-router / linear-router / pattern-router / smart-router`），运行时切换
- 类型推导（中间件链 → 路由 → 响应类型全自动）

**适用场景**：Agent 的 BFF / MCP server / RAG retrieval API。比 Express / Fastify 更轻，比 Next.js API routes 更可控。

---

### 5️⃣ vercel/ai — LLM SDK 多 provider 冠军

**规模**：`packages/` 下 **58 个独立 provider 包**（OpenAI / Anthropic / Bedrock / Azure / Mistral / Gemini / Groq / xAI / DeepSeek / Cohere / ...）。这是当前最完整的 provider adapter 集合。

**热点目录**：
- `packages/ai/src/generate-text/` — text 生成统一接口
- `packages/ai/src/agent/` — 🆕 Agent loop 原语（v5）
- `packages/ai/src/generate-object/` — 结构化输出
- `packages/ai/src/embed/` + `generate-image/` + `generate-speech/` — 多模态

**抄走**：
- Provider 接口契约 (`LanguageModelV2`) — 比 LangChain 优雅
- 流式 chat 协议 (`@ai-sdk/ui-utils`)
- 工具调用统一抽象

**对照**：`hermes-agent` 的 provider 层 vs vercel-ai 的差距明显，可直接换。

---

### 6️⃣ assistant-ui — Chat UI 组件（含 Python 后端）

**结构**：
- `packages/core/` — 状态管理 + adapter
- `packages/react/` + `packages/react-markdown/` — React 组件
- `packages/assistant-stream/` — TS 流协议
- `python/` — **6 个 Python 包**：
  - `assistant-transport-backend` + `assistant-transport-backend-langgraph` — LangGraph 接入
  - `assistant-ui-sync-server-api` — 状态同步

**抄走**：
- 消息列表虚拟滚动 + 流式渲染策略
- Thread / Branching / Edit 范式
- 工具调用 UI 渲染（`ToolUI`）

**适用**：直接做 rag-dashboard 的 chat 界面。比自己写省 3 周。

---

### 7️⃣ biomejs/biome — Rust 工具链

**规模**：4217 个 Rust 文件，`crates/biome_*` 模块化分层。

**抄走**（仅设计参考，不直接搬代码）：
- 单 binary 解决 fmt + lint + import-sort + a11y
- 增量 parser（rome 衍生）速度比 ESLint 快 10-100x

**避坑**：Rust 工具链对小项目过重，**Node 项目建议直接用 `npx @biomejs/biome`**，不必读源码。

## 三、推荐组合（按场景）

### 场景 A：Agent Dashboard（rag-dashboard 类）
```
vite + shadcn-ui (apps/v4 组件) + tanstack-query + biome
```
→ 直接拷贝 shadcn 组件，TanStack Query 调后端 API，biome 一把刷格式。

### 场景 B：Agent Chat UI（assistant 类）
```
assistant-ui + vercel-ai + hono BFF + tanstack-query
```
→ assistant-ui 出 UI 壳，vercel-ai 接模型，hono 做 BFF / MCP server。

### 场景 C：MCP server / Agent 后端
```
hono + vercel-ai (provider adapters only) + biome
```
→ 不要前端，纯 API。Hono 路由 + vercel-ai 拆出来用的 provider 包。

## 四、与现有 BEST-OF-STACK 的对接

新增 **Layer E: 前端 / UI / SDK**，补 7 个模块到 `BEST-OF-STACK.md`（详见该文件 §E）。

## 五、SKILL.md schema 演进记录

shadcn 引入两个新字段，建议同步到 `06-catalogs/README.md` 文档段落：

| 字段 | 取值 | 用途 |
|---|---|---|
| `user-invocable` | `true` / `false` | 该 skill 是否允许用户直接 `/skill <name>` 触发 |
| `allowed-tools` | `Bash(cmd *), Read(*.ts), ...` | 权限白名单（精确到 glob） |

agentskills.io 标准之外的扩展，但 Anthropic 自家 Claude Code 已支持。后续 138 scientific-skills 重写时建议加上。
