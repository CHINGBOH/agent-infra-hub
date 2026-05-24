# 2026-05-25 — Python Agent + 异步基础设施 + 可观测性（12 仓库）

> 第三批"抄作业"调研。Python agent 是当前生态主力；异步基础设施给 agent 提供并发/持久化；可观测性是上生产前的必备。

## 一、阵容

### Python Agent（→ `13-python-agents/`）

| 仓库 | Star | 规模 | 角色 |
|---|---|---|---|
| [langgenius/dify](../13-python-agents/dify/) | 90k+ | 3014 py + 1732 ts | 一站式 agent 平台（含 RAG + Workflow + MCP） |
| [microsoft/autogen](../13-python-agents/autogen/) | 40k+ | 546 py / 10 包 | 多 agent 对话（含 Magentic-One/Studio） |
| [crewAIInc/crewAI](../13-python-agents/crewai/) | 28k+ | 1188 py / 6 子包 | Role-based agent crew |
| [langchain-ai/langgraph](../13-python-agents/langgraph/) | 10k+ | 357 py | 有状态 agent 图（Pregel 模型 + 多语言 SDK） |
| [openai/openai-agents-python](../13-python-agents/openai-agents/) | 8k+ | 775 py | OpenAI 官方 agent SDK |
| [huggingface/smolagents](../13-python-agents/smolagents/) | 15k+ | **75 py** | 极简代码 agent（"the bare minimum"） |

### 异步基础设施（→ `14-async-infra/`）

| 仓库 | Star | 规模 | 角色 |
|---|---|---|---|
| [temporalio/temporal](../14-async-infra/temporal/) | 12k+ | 2681 go | Workflow 引擎（持久化任意逻辑） |
| [nats-io/nats-server](../14-async-infra/nats-server/) | 16k+ | 256 go | 消息队列（agent 间通信） |
| [trycua/cua](../14-async-infra/cua/) | 8k+ | 662 py / 11 libs | Computer-use sidecar（含 QEMU/Lume/Xfce 完整桌面栈） |

### 可观测性（→ `15-observability/`）

| 仓库 | Star | 规模 | 角色 |
|---|---|---|---|
| [langfuse/langfuse](../15-observability/langfuse/) | 10k+ | 1578 ts | LLM 全栈可观测（trace + eval + prompt） |
| [Arize-ai/phoenix](../15-observability/phoenix/) | 5k+ | 1158 py + 1423 ts | LLM eval + tracing |
| [traceloop/openllmetry](../15-observability/openllmetry/) | 6k+ | 678 py / **31 instrumentations** | LLM 的 OpenTelemetry |

合计 ~932 MB。

## 二、每个仓库的"抄什么"

### Python Agent 侧

#### 1️⃣ dify — 90k★ 一站式平台

**结构亮点**：`api/core/` 下完整模块覆盖
```
agent/        memory/         extension/      indexing_runner.py
app/          mcp/            external_data_tool/  llm_generator/
callback_handler/  moderation/  datasource/     model_manager.py
```

**抄走**：
- `api/core/mcp/` — Python 端 MCP client 集成范式
- `api/core/agent/` — agent loop（含 tool calling、CoT、function calling 三套实现）
- Workflow DSL → YAML 持久化
- 多租户 + RBAC（生产 SaaS 级）

**避坑**：dify 是 monolith，不要整包依赖；按模块拆抄。

---

#### 2️⃣ autogen — 40k★ Microsoft 多 agent

**10 个子包**：`autogen-core / autogen-agentchat / autogen-ext / autogen-magentic-one / autogen-studio / agbench / magentic-one-cli / pyautogen`

**热点**：`autogen-core/src/autogen_core/` 暴露完整 agent 原语
```
_agent.py / _agent_id.py / _agent_metadata.py
_agent_proxy.py / _agent_runtime.py / _agent_type.py
_closure_agent.py / _cancellation_token.py
_component_config.py / _default_subscription.py
```

**抄走**：
- Agent runtime + subscription / pub-sub 模型（区别于其他框架的直接调用）
- `Magentic-One` 任务规划器（GAIA benchmark 实现）
- `autogen-studio` 可视化 agent 编辑器

**对照 crewai**：autogen 是 "agent 之间发消息"，crewai 是 "role + task + crew"。autogen 更底层、crewai 更应用层。

---

#### 3️⃣ crewai — 28k★ Role-based

**结构**：`lib/{crewai-core, crewai, crewai-tools, cli, devtools}` —— 多包 monorepo

**抄走**：
- Agent / Task / Crew / Process 四层抽象（业务可读性最高）
- `crewai-tools/` 工具集（搜索、文件、代码执行）
- CLI 脚手架（`crewai create crew xxx`）

**适用**：业务流程显式可读的场景；非开发用户可参与设计。

---

#### 4️⃣ langgraph — 10k★ 有状态 agent 图

**亮点**：基于 **Google Pregel** 模型（图节点 + 消息传递 + 检查点）

**热点**：`libs/langgraph/langgraph/`
```
pregel/    ← 图执行引擎（核心创新）
channels/  ← 状态通道
graph/     ← DSL（StateGraph / MessageGraph）
managed/   ← 受管状态
```

**多语言 SDK**：`libs/sdk-py` + `libs/sdk-js` —— 唯一同时提供 Py + JS SDK 的 agent 框架

**抄走**：
- 检查点机制（`checkpoint-postgres` / `checkpoint-sqlite` 单独包）—— 这是 langgraph 在生产部署中最强的卖点
- 中断 + 人在环（human-in-the-loop）
- 状态图 DSL

**适用**：需要复杂多步工作流 + 中途中断恢复的场景；rag-dashboard 想要可恢复的长任务。

---

#### 5️⃣ openai-agents — 8k★ 官方 SDK

**热点**：`src/agents/`
```
agent.py / agent_output.py / agent_tool_input.py / agent_tool_state.py
handoffs/        ← agent 之间交接（autogen 风格）
mcp/             ← MCP client
guardrail.py     ← 守卫栏（输入/输出过滤）
computer.py      ← Computer Use Tool
lifecycle.py
```

**抄走**：
- `guardrail.py` —— OpenAI 官方推荐的 agent 守卫范式
- `handoffs/` 多 agent 转交
- `lifecycle.py` 生命周期 hook

**地位**：当前 GPT 系列原生 agent 的事实标准 SDK。

---

#### 6️⃣ smolagents — 15k★ 极简（**75 个 .py 文件**）

**全部源文件**：
```
agents.py / agent_types.py / cli.py / default_tools.py
gradio_ui.py / local_python_executor.py / mcp_client.py / memory.py
```

**核心理念**：用 Python 代码而非 JSON 描述 agent 行为（**CodeAgent**）。LLM 直接生成 Python 调用工具。

**抄走**：
- `local_python_executor.py` 沙箱 Python 执行（限制 import、限制资源）
- "用代码当 tool call" 的协议（比 JSON tool call 表达力强）
- 想了解 "agent 至少需要什么" → 读这 75 个文件

**适用**：教学/原型 + 代码生成场景（CodeAgent 比 JSON ReAct 更强）。

---

### 异步基础设施侧

#### 7️⃣ temporal — Workflow 引擎

**结构**：`service/{frontend, history, matching, worker}` —— 4 个微服务

**核心价值**：**任何 Python/Go/TS/Java 代码加 `@workflow` 装饰器就持久化**，进程崩溃后从断点继续。

**抄走**：
- Workflow + Activity 抽象（worker pool）
- Event sourcing 持久化模型
- Determinism replay

**适用 agent 场景**：长跑 agent（小时/天级）、需要崩溃恢复、多 agent 协调。

---

#### 8️⃣ nats-server — 消息队列

**特点**：单 binary, 12MB，集群模式 + JetStream 持久化。

**抄走**：
- Subject 命名空间（比 Kafka topic 灵活）
- Request-Reply pattern（适合 agent 间 RPC）
- JetStream（持久化 + 重放）

**适用**：多 agent 系统的消息总线；BeautyOS Hermes 想做事件驱动。

---

#### 9️⃣ cua — Computer-use sidecar（**117MB**）

**11 个子包**：
```
libs/{cua-bench, cuabot, cua-driver, kasm, lume, lumier, qemu-docker, xfce, python, typescript}
```

包含 **完整桌面虚拟化栈**（Xfce / QEMU / Lume macOS VM）。

**抄走**：
- 给 agent 一个完整 Linux 桌面（点击/截图/键盘）
- macOS 上跑 macOS VM 的 lume

**对照**：openai-agents 的 `computer.py` 只是接口；cua 是完整后端。两者搭配用。

---

### 可观测性侧

#### 🔟 langfuse — LLM 全栈可观测（10k★）

**结构**：`packages/{app, components, ee, features, ...}` Next.js + TRPC monorepo

**抄走**：
- Trace / Generation / Span 数据模型（LLM 特化的 OTel）
- Prompt management（版本 / A/B）
- Eval（LLM-as-judge + 人工标注）
- Self-hostable 完整方案

**适用**：所有 LLM 生产部署的标配可观测后台。**rag-dashboard 应该接入 langfuse**。

---

#### 1️⃣1️⃣ phoenix — Arize 出品 eval + tracing（5k★）

**双语言**：`src/phoenix/`（Python 后端）+ `app/`（React 前端）

**抄走**：
- LLM eval 框架（语义评估 / hallucination 检测）
- Vector store visualizer（embedding 降维可视化）
- 与 LlamaIndex / LangChain 深度集成

**对照 langfuse**：langfuse 更通用 + Self-host 友好；phoenix 更偏 eval 工作流 + 已有 ML 团队。

---

#### 1️⃣2️⃣ openllmetry — LLM 的 OTel（**31 个 instrumentation**）

**31 个 instrumentation 包**覆盖：
```
LLM 厂商：anthropic / bedrock / cohere / google-genai / groq / openai / together / mistral
RAG/向量：chromadb / lancedb / marqo / milvus / pinecone / qdrant / weaviate
框架：crewai / haystack / langchain / llamaindex / mcp / vertexai / agno
其他：alephalpha / replicate / sagemaker / transformers / watsonx / ollama
```

**抄走**：
- 直接拿来插桩自己的项目（**比手写 OTel 快 10x**）
- 各 LLM 调用如何映射 OTel attributes / spans 的最佳实践参考

**适用**：任何 Python LLM 项目想加 tracing — 这是 30 行代码搞定的方案。

## 三、补到 BEST-OF-STACK 的新层（H / I / J）

### Layer H. Python Agent 框架（5 模块）

| 模块 | 🥇 主选 | 备选 |
|---|---|---|
| H1. 一站式 agent 平台 | **dify** `api/core/` | — |
| H2. 多 agent 框架（消息） | **autogen** `autogen-core/` | crewai（role 风格） |
| H3. 有状态 agent graph | **langgraph** `libs/langgraph/{pregel,channels,graph}/` | — |
| H4. 官方 SDK | **openai-agents** `src/agents/{guardrail,handoffs,mcp}/` | — |
| H5. 极简代码 agent | **smolagents** `src/smolagents/` (75 文件读完) | — |

### Layer I. 异步基础设施（3 模块）

| 模块 | 🥇 主选 |
|---|---|
| I1. Workflow 引擎 | **temporalio/temporal** `service/{frontend,history,matching,worker}/` |
| I2. 消息总线 | **nats-server** `server/` |
| I3. Computer-use sidecar | **trycua/cua** `libs/{cua-driver,lume,qemu-docker}/` |

### Layer J. 可观测性（3 模块）

| 模块 | 🥇 主选 | 备选 |
|---|---|---|
| J1. LLM 全栈可观测 | **langfuse** `web/src/`（self-hosted） | phoenix |
| J2. LLM eval 工作流 | **phoenix** `src/phoenix/` | langfuse evals 部分 |
| J3. LLM OTel 插桩 | **openllmetry** 31 个 instrumentation 包 | 无 |

→ BEST-OF-STACK 升级到 **10 层 × 50 模块**。

## 四、新增推荐组合

### 场景 G：Python 全栈 agent
```
dify (UI/平台) + langgraph (workflow) + openai-agents (SDK) + langfuse (obs)
```

### 场景 H：教学/原型快速验证
```
smolagents + openllmetry + sqlite-based langfuse
```

### 场景 I：长跑 agent（数小时/天）
```
langgraph (检查点) + temporal (workflow 持久化) + nats (消息) + langfuse
```

### 场景 J：桌面自动化 agent
```
openai-agents (SDK + computer.py) + cua (桌面后端) + langfuse
```

## 五、AGENTS.md/CLAUDE.md 已成上游标配

跨过去 3 批 31 个仓库的统计：

| 文档类型 | 数量 | 覆盖率 |
|---|---|---|
| 含 `AGENTS.md` | 11/31 | 35% |
| 含 `CLAUDE.md` | 9/31 | 29% |
| 含 `ARCHITECTURE.md` | 4/31 | 13% |

最新 12 个仓库中 **9/12** 含 `AGENTS.md` 或 `CLAUDE.md`——这是当前明星项目的事实标准。建议 rag-dashboard / hermes-agent / BeautyOS 也加上以方便 Claude Code/Codex 接入。
