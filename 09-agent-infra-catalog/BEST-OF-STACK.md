# Best-of Agent Stack — 拆模块 + 选最优实现

> 2026-05-25 · 跨 17 个仓库（5 个 agent_research champions + 12 个 agent-infra-hub 仓库）  
> 把"做一个 agent 需要的所有模块"拆开，每个模块挑 **🥇主选 + 🥈备选**，给出确切文件路径。  
> 目标：照着这张表搭一套自己的 agent，每一块都用最优实现，不用从零造轮子。

---

## 🏗️ 全栈分 5 层 29 个模块

```
┌──────────────────────────────────────────────────────────────────┐
│  E. 前端 / UI    dev-server · component · chat-ui · BFF · …       │  🆕 2026-05-25
├──────────────────────────────────────────────────────────────────┤
│  D. 开发与运维   replay · eval · observability                    │
├──────────────────────────────────────────────────────────────────┤
│  C. 编排层      planner · team/swarm · subagent · worktree        │
├──────────────────────────────────────────────────────────────────┤
│  B. 技能层      skill-registry · skill-content · skill-discovery  │
├──────────────────────────────────────────────────────────────────┤
│  A. 核心运行时   loop · memory · tools · hooks · provider · …      │
└──────────────────────────────────────────────────────────────────┘
```

---

## 🔧 A. 核心运行时（9 个模块）

### A1. Tool-Call Loop（agent 主循环）

| | 仓库 | 文件 | 行数 | 理由 |
|---|---|---|---|---|
| 🥇 主选 | **cline** | `src/core/task/ToolExecutor.ts` | 659 | 生产级 MCP + 权限 + loop-detect 集成；类型完备 |
| 🥈 备选 | **aider** | `aider/coders/base_coder.py` | 2485 | Python 单文件最完整：内含 error-repair 反馈循环 |
| ⛔ 反面 | hermes | `agent/conversation_loop.py` | — | CCN 707 单函数，技术债典型 |

**抄哪段**：cline 的 `executeToolCall()` + `assertToolApproval()` 两个方法，60 行可独立。

---

### A2. Memory（记忆系统）

#### A2a. 短期：对话上下文压缩
| | 仓库 | 文件 | 卖点 |
|---|---|---|---|
| 🥇 | **cline** | `src/core/context/ContextManager.ts` (1295 行) | 滑动窗口 + 关键信息 anchor |
| 🥈 | hermes | `agent/context_compressor.py` + `conversation_compression.py` | Python 版双层压缩 |
| 🥈 | token-optimizer | `08-infrastructure/context-window/token-optimizer/` | 系统性压缩 configs/skills/prompts 等 75-85% 上下文（非 IO 输出） |

#### A2b. 长期：持久化 + 检索
| | 仓库 | 文件 | 卖点 |
|---|---|---|---|
| 🥇 | **agentmemory** | `src/state/hybrid-search.ts` (324 行) | BM25 + 向量 + rerank 三明治 · R@5=95.2% · 0 外部 DB |
| 🥇 | agentmemory | `src/state/cjk-segmenter.ts` | **唯一**内置中文分词的方案 |
| 🥇 | agentmemory | `src/state/{vector-index,search-index,reranker,stemmer,synonyms}.ts` | 完整检索栈 6 个模块 |
| 🥈 | aider | `aider/history.py` | 简单文件历史，单机用够 |

**拼装姿势**：cline ContextManager 做短期 + agentmemory hybrid-search 做长期，cjk-segmenter 接到 rag-dashboard。

---

### A3. Tool Registry（工具注册表）

| | 仓库 | 文件 | 卖点 |
|---|---|---|---|
| 🥇 | **agentmemory** | `src/mcp/server.ts` (1730 行) | 53 个 MCP tools 注册范本；MCP 标准 |
| 🥈 | cline | `src/services/mcp/McpHub.ts` | 客户端侧 MCP 集成 |
| 🥈 | langchain | `libs/core/langchain_core/tools/base.py` | `BaseTool` 抽象接口标杆 |
| 🥈 | hermes | `agent/tool_executor.py` + `tool_dispatch_helpers.py` | 分发器拆分清晰 |

**避坑**：agentmemory 单文件 1730 行注册 53 工具，**可读但难改** — 抄时拆成 `tools/<name>.ts` 一文件一工具。

---

### A4. MCP Server / Client

| | 仓库 | 文件 | 卖点 |
|---|---|---|---|
| 🥇 服务端 | **claude-code-mcp-enhanced** | `08-infrastructure/tool-use-mcp/claude-code-mcp-enhanced/` | one-shot 模式 + 权限自动 bypass + 任务编排 |
| 🥇 客户端 | cline | `src/services/mcp/McpHub.ts` | 生产客户端，支持 stdio+SSE |
| 🥈 极简 | tool-use-mcp/claude-code-mcp | — | 最小可运行参考 |

---

### A5. Hooks（生命周期事件）

| | 仓库 | 文件/数量 | 卖点 |
|---|---|---|---|
| 🥇 完整 | **agentmemory** | `src/hooks/*.ts` × **12** | 工业级：pre/post-tool-use, session-{start,end}, subagent-{start,stop}, task-completed, post-commit, pre-compact, stop, notification, prompt-submit, post-tool-failure, sdk-guard |
| 🥇 教学 | claude-code-hooks-mastery | `08-infrastructure/hooks/claude-code-hooks-mastery/` | 全网最系统化的 hooks 教程 |
| 🥇 观测 | claude-code-hooks-multi-agent-observability | 同 | 用 hooks 做实时多 agent 监控 |

**结论**：agentmemory 是**生产可用**的 hooks 实现，hooks-mastery 是**学习材料**，两者搭配。

---

### A6. Provider Adapters（多模型适配）

| | 仓库 | 文件 | 卖点 |
|---|---|---|---|
| 🥇 | **hermes-agent** | `agent/{anthropic,bedrock,codex_responses}_adapter.py` | 多厂适配最干净 |
| 🥈 | aider | `aider/llm.py` | 单文件多 provider 经典实现 |
| 🥈 | cline | `src/api/providers/*.ts` | TS 版多 provider，类型最全 |

---

### A7. Streaming（增量解析）

| | 仓库 | 文件 | 卖点 |
|---|---|---|---|
| 🥇 | **cline** | `src/core/assistant-message/parse-assistant-message.ts` | 边收边解析的流式 XML/JSON 解析器 |
| 🥈 | hermes | `agent/chat_completion_helpers.py` | Python 版工具调用 stream |

---

### A8. Sandbox / Permissions（权限控制）

| | 仓库 | 文件 | 卖点 |
|---|---|---|---|
| 🥇 | **cline** | `src/core/task/CommandPermissionController.ts` | 命令白名单/黑名单 + 用户确认 |
| 🥈 | aider | `aider/editor.py` | 编辑器边界（git 仓库内） |

---

### A9. Prompt Templates

| | 仓库 | 文件 | 卖点 |
|---|---|---|---|
| 🥇 | **cline** | `src/core/prompts/` (system prompt + tool docs) | 模板与代码解耦 |
| 🥈 | aider | `aider/coders/base_prompts.py` | 各 coder 模式独立 prompt 类 |
| 🥈 | langchain | `libs/core/langchain_core/prompts/` | `PromptTemplate`/`ChatPromptTemplate` 抽象 |

---

## 📚 B. 技能层（3 个模块）

### B1. Skill Registry（SKILL.md 标准 + 发现机制）

| | 仓库 | 文件 | 卖点 |
|---|---|---|---|
| 🥇 标准 | [agentskills.io](https://agentskills.io/) | `SKILL.md` frontmatter（name/description/license/metadata） | 跨 agent 开放标准（Cursor/Claude Code/Codex 都支持） |
| 🥇 实现 | **scientific-agent-skills** | `scan_skills.py` + 138 SKILL.md | 大规模实现样本 |
| 🥈 本地 | `~/.copilot/skills/` | `SKILL.md` (frontmatter: name/description) | 自动发现机制 |

---

### B2. Skill Content Library（领域技能内容）

| | 仓库 | 数量 | 适用 |
|---|---|---|---|
| 🥇 科研 | **scientific-agent-skills** | **138** skills 跨 17 领域 | 生物/化学/医学/天文/材料/地理空间/统计/写作… |
| 🥇 通用 | **wshobson-agents** | **185** specialist agents + 16 workflow orchestrators | 通用软件开发 |
| 🥈 索引 | composio-awesome-claude-skills / mingrath / travisvn / alirezarezvani 等 | — | 06-catalogs/ 下多个 awesome 列表 |

**完整索引**：`06-catalogs/scientific-skills-INDEX.md`（按 17 领域分组）  
**接入方式**：`ln -s .../scientific-skills/<name> ~/.claude/skills/`

---

### B3. Skill Auto-Discovery（工作流→skill 自动化）

| | 仓库 | 文件 | 卖点 |
|---|---|---|---|
| 🥇 | **scientific-agent-skills/autoskill** | `scientific-skills/autoskill/SKILL.md` | screenpipe 监视屏幕 → 识别重复流程 → 自动转 skill |
| 🥇 | **oh-my-claudecode** | `commands/skillify.md` | `/skillify` 把当前对话转成可复用 skill |

---

## 🎭 C. 编排层（5 个模块）

### C1. Single-Agent Planner

| | 仓库 | 文件 | 卖点 |
|---|---|---|---|
| 🥇 | **aider** | `aider/coders/architect_coder.py` | architect → implementer 两段式（先规划后执行）|
| 🥈 | langchain | `libs/langchain/langchain/agents/agent_types.py` | `ReAct`/`Plan-and-Execute`/`Self-Ask` 类型枚举参考 |
| 🥈 | oh-my-claudecode | `agents/architect.md` + `agents/planner.md` | 角色化 planner |

---

### C2. Multi-Agent Team / Swarm

| | 仓库 | 文件 | 卖点 |
|---|---|---|---|
| 🥇 标准 | **oh-my-claudecode** | `bridge/team-bridge.cjs` + `team-mcp.cjs` | Team 模式：autopilot/swarm 都路由到 Team |
| 🥈 经典 | repo-crewai | `crew.py` (`src/crewai/crew.py`) | 最干净的 multi-agent 抽象（Role-Goal-Backstory） |
| 🥈 Rust | ccswarm | `07-agent-design/ccswarm/` | Rust 实现，自我演进 |
| 🥈 大规模 | ruflo | `07-agent-design/ruflo/` | **100+ agent** 跨机器/团队/信任域协调 |
| 🥈 自演进 | metaswarm | `07-agent-design/metaswarm/` | self-improving orchestration |

**选型建议**：3 个以下 agent → crewai；3-20 个 → OMC Team；50+ → ruflo。

---

### C3. Subagent Isolation（子 agent 隔离）

| | 仓库 | 文件 | 卖点 |
|---|---|---|---|
| 🥇 测试驱动 | **claude-code-sub-agent-collective** | `08-infrastructure/subagent-isolation/claude-code-sub-agent-collective/` | TDD + 快速原型，子 agent 各司其职 |
| 🥇 生产级 | **ECC** | `08-infrastructure/subagent-isolation/ECC/` | 完整体系：skills+instincts+memory+continuous learning+security+research-first |
| 🥈 角色定义 | oh-my-claudecode | `agents/*.md` × 19 | 19 个角色 prompt 直接抄 |
| 🥈 SDK | claude-swarm | `07-agent-design/claude-swarm/` | 用 Claude Agent SDK 实现 |

---

### C4. Worktree / Parallel Execution

| | 仓库 | 文件 | 卖点 |
|---|---|---|---|
| 🥇 | **agent-orchestrator** | `07-agent-design/agent-orchestrator/` | 每 agent 独立 git worktree，并行修 CI/PR review |
| 🥈 | agent-farm | `07-agent-design/agent-farm/` | 多 cc 会话并行框架 |

---

### C5. Hand-off Protocol（agent 间协议）

| | 仓库 | 文件 | 卖点 |
|---|---|---|---|
| 🥇 | **hermes-agent** | `agent/acp_adapter/` + `acp_registry/` | **ACP 协议**（Agent Communication Protocol），用户自有，独家 |
| 🥈 | crewai | `crew.py` 内部 task delegation | 简单消息传递 |

---

## 🔬 D. 开发与运维（5 个模块）

### D1. Replay / 会话回放

| | 仓库 | 文件 | 卖点 |
|---|---|---|---|
| 🥇 | **agentmemory** | `src/replay/jsonl-parser.ts` | JSONL 会话回放标准实现 |

---

### D2. Eval / Self-Correct

| | 仓库 | 文件 | 卖点 |
|---|---|---|---|
| 🥇 | **agentmemory** | `src/eval/{metrics-store,validator,quality,self-correct}.ts` | 4 文件成体系 |
| 🥈 | aider | `aider/coders/base_coder.py` 内的 lint feedback | error-repair 反馈循环 |

---

### D3. Observability Dashboard

| | 仓库 | 文件 | 卖点 |
|---|---|---|---|
| 🥇 实时网页 | **agentmemory** | `src/viewer/server.ts` + `document.ts` (:3111) | 内置 viewer，0 外部依赖 |
| 🥇 多 agent | **claude-code-hooks-multi-agent-observability** | `08-infrastructure/hooks/claude-code-hooks-multi-agent-observability/` | 多 agent 实时事件流可视化 |

---

### D4. CLI / 入口

| | 仓库 | 文件 | 卖点 |
|---|---|---|---|
| 🥇 | **agentmemory** | `src/cli/connect/` | 安装/启动/connect 多 client 一条龙 |
| 🥈 | aider | `aider/main.py` | Python 单文件 CLI（但 CCN 161，别全抄） |

---

### D5. 设置 / 配置

| | 仓库 | 文件 | 卖点 |
|---|---|---|---|
| 🥇 | **oh-my-claudecode** | `commands/omc-setup.md` + `commands/omc-doctor.md` | 一键安装 + 健康检查 |

---

## 🎨 E. 前端 / UI / SDK（7 个模块，🆕 2026-05-25）

> 来源：`/home/l/projects/agent-infra-hub/10-frontend-stack/` 浅克隆 7 个明星仓库  
> 详细分析见 [2026-05-25-frontend-stack-analysis.md](2026-05-25-frontend-stack-analysis.md)

### E1. 构建工具 / Dev Server

| | 仓库 | 文件 | 卖点 |
|---|---|---|---|
| 🥇 | **vitejs/vite** | `packages/vite/src/node/server/` + `plugin.ts` | HMR + ESM dev server 标杆，插件协议被全行业采用 |
| 🥈 | turbopack / rspack | — | Rust 重写版，需更高性能再换 |

### E2. UI 组件库（拷贝式）

| | 仓库 | 文件 | 卖点 |
|---|---|---|---|
| 🥇 | **shadcn-ui/ui** | `apps/v4/registry/new-york-v4/ui/` | 拷贝粘贴范式，无 npm 依赖；**自带 [SKILL.md](../10-frontend-stack/shadcn-ui/skills/shadcn/SKILL.md) 含新字段 `user-invocable` / `allowed-tools`** |
| 🥈 | radix-ui / headlessui | — | 底层无样式原语，shadcn 就是基于 radix |

### E3. 异步状态管理

| | 仓库 | 文件 | 卖点 |
|---|---|---|---|
| 🥇 | **TanStack/query** | `packages/query-core/src/` | 框架无关核心 + staleTime/gcTime 双缓存 + 自动 dedup |
| 🥈 | swr | — | Vercel 出品，更轻但功能少 |

### E4. BFF / Edge web framework

| | 仓库 | 文件 | 卖点 |
|---|---|---|---|
| 🥇 | **honojs/hono** | `src/hono-base.ts` (545) + `src/context.ts` (780) | 极致优雅，5 router 可换，类型推导一流；适合 MCP server / RAG API |
| 🥈 | fastify | — | Node 老牌，性能也好但 API 较繁琐 |

### E5. LLM SDK / Provider 适配

| | 仓库 | 文件 | 卖点 |
|---|---|---|---|
| 🥇 | **vercel/ai** | `packages/ai/src/` + 58 个 provider 包 | 当前最完整的 provider 集合 + `LanguageModelV2` 契约 + v5 agent loop 原语 |
| 🥈 | hermes-agent provider 层 | — | 仅参考接口，实际抄 vercel-ai |

### E6. Chat UI 组件

| | 仓库 | 文件 | 卖点 |
|---|---|---|---|
| 🥇 | **assistant-ui** | `packages/core/` + `packages/react/` | Thread / Branching / 流式 + 工具调用 UI；附 6 个 Python 包（LangGraph 接入） |
| 🥈 | vercel/ai-chatbot | — | 模板项目，可参考结构 |

### E7. 工具链（fmt + lint）

| | 仓库 | 文件 | 卖点 |
|---|---|---|---|
| 🥇 | **biomejs/biome** | `crates/biome_*` (Rust) | 单 binary 解决 fmt+lint+import-sort+a11y，10-100x 快 |
| 🥈 | prettier + eslint | — | 老牌组合，若已重度配置不必换 |

**前端层的 3 种拼装姿势**：见 [2026-05-25-frontend-stack-analysis.md §三](2026-05-25-frontend-stack-analysis.md)。

---

## 🎯 推荐拼装：3 种姿势

### 姿势 A：极简单 agent（500 行）
```
loop      → cline ToolExecutor.ts          (削减到 200 行)
memory    → aider history.py 简版         (50 行 JSONL)
tools     → 自己 3-5 个 MCP tool            (200 行)
provider  → aider llm.py                   (50 行)
```
**目标场景**：本地脚本、个人助手

### 姿势 B：生产单 agent（5k 行）
```
loop      → cline ToolExecutor.ts 完整         (659)
memory    → cline ContextManager.ts 完整        (1295)
            + agentmemory hybrid-search.ts     (324)
tools     → MCP standard (claude-code-mcp-enhanced)
hooks     → agentmemory 12 hooks              (12×80=960)
provider  → hermes adapters × 3                (600)
streaming → cline parse-assistant-message.ts  (200)
sandbox   → cline CommandPermissionController.ts
skills    → 选 10 个 scientific-skills + symlink
viewer    → agentmemory viewer/server.ts      (200)
```
**目标场景**：Claude Code 风格的编码 agent

### 姿势 C：Multi-agent 系统（10k+ 行）
```
基础同 B + 
orchestrator   → OMC team-bridge.cjs / crewai crew.py
worktree       → agent-orchestrator
subagent role  → OMC agents/*.md × 19
hand-off       → hermes-agent ACP
observability  → claude-code-hooks-multi-agent-observability
```
**目标场景**：Team 协作、并行修 PR/CI、Devil's Advocate 评审

---

## ⛔ 反面教材（不要抄）

| 仓库 | 文件 | 问题 |
|---|---|---|
| hermes-agent | `agent/conversation_loop.py` | CCN 707 巨型函数 |
| aider | `aider/main.py` | CCN 161，多副作用入口 |
| langchain | LCEL 抽象层 | 学接口可以，**别抄实现** |
| cline | VSCode 紧耦合部分 | 抽 core/ 即可，UI 部分跳过 |
| agentmemory | `mcp/server.ts` 单文件 1730 行 | 工具注册逻辑要拆 |
| agentmemory | `DESIGN.md` | 是 Lamborghini 广告文案，疑似 LLM 投错文件 |

---

## 📌 与已有产出的关系

- **`/home/l/agent_research/04-synthesis/RECOMMENDATIONS.md`** — 5 champion × 10 primitive 的原始矩阵
- **`/home/l/projects/agent-infra-hub/09-agent-infra-catalog/2026-05-25-three-new-repos-analysis.md`** — 3 新仓库定位
- **`/home/l/projects/agent-infra-hub/06-catalogs/scientific-skills-INDEX.md`** — 138 skills 索引
- **本文件** — 把上面三个串成一张拼装表

---

## ⏭️ 下一步建议

1. **按姿势 B 跑 PoC**：抓 cline + agentmemory + 5 个 scientific-skills 拼一个最小 demo
2. **写 stack-loader**：一个脚本自动把上面所有"主选"文件 symlink/clone 到 `./vendor/`
3. **跨仓库去重**：agent-orchestrator 和 agent-farm 重叠度高，看哪个更新更勤
4. **统一 SKILL.md schema**：对齐 `~/.copilot/skills/*` 与 scientific-skills 的 frontmatter 字段
