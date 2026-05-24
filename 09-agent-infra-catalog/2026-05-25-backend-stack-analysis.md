# 2026-05-25 — Rust/Go 后端栈深度调研（12 个明星仓库）

> 目的：把 agent 系统的后端层补齐。Rust 提供性能 + 内存安全（向量/搜索 DB 首选），Go 提供高并发 + 简洁部署（LLM serving / MCP / agent 框架）。

## 一、阵容

### Rust 6 仓库（→ `11-rust-backend/`）

| 仓库 | Star | 规模 | 角色 |
|---|---|---|---|
| [tokio-rs/axum](../11-rust-backend/axum/) | 22k+ | 296 RS / 5.4M | Rust web framework |
| [qdrant/qdrant](../11-rust-backend/qdrant/) | 24k+ | 1332 RS / 24M | 向量 DB |
| [meilisearch/meilisearch](../11-rust-backend/meilisearch/) | 50k+ | 723 RS / 16M | 全文搜索引擎 |
| [quickwit-oss/tantivy](../11-rust-backend/tantivy/) | 12k+ | 430 RS / 14M | BM25 搜索库（Lucene 替代） |
| [0xPlaygrounds/rig](../11-rust-backend/rig/) | 3k+ | 656 RS / 17M / **19 个 crates** | Rust LLM/agent 框架 |
| [ratatui/ratatui](../11-rust-backend/ratatui/) | 10k+ | 236 RS / 5.3M | TUI 库（Claude Code CLI 类） |

### Go 6 仓库（→ `12-go-backend/`）

| 仓库 | Star | 规模 | 角色 |
|---|---|---|---|
| [ollama/ollama](../12-go-backend/ollama/) | 100k+ | 808 GO / 15M | 本地 LLM serving |
| [cloudwego/eino](../12-go-backend/eino/) | 3k+ | 338 GO / 14M | ByteDance LLM 框架（adk/flow/compose） |
| [tmc/langchaingo](../12-go-backend/langchaingo/) | 5k+ | 671 GO / 20M | LangChain Go 端口 |
| [weaviate/weaviate](../12-go-backend/weaviate/) | 12k+ | 4328 GO / 49M | 向量 DB（生产级） |
| [mark3labs/mcp-go](../12-go-backend/mcp-go/) | 4k+ | 180 GO / 3.6M | MCP server SDK |
| [gptscript-ai/gptscript](../12-go-backend/gptscript/) | 3k+ | 158 GO / 9.8M | 声明式 LLM 脚本 |

合计 ~192 MB。

## 二、每个仓库的"抄什么"

### Rust 侧

#### 1️⃣ tokio-rs/axum — Rust 版 Hono

**热点**：
- `axum/src/extract/` — Request 提取器（typed extractors，Rust 类型推导最高水准）
- `axum/src/routing/` — 路由 trie + 中间件层（Tower 集成）
- `axum/src/handler/` — handler trait 与变参类型

**抄走**：FromRequest 范式（任意类型只要实现 trait 就能当参数注入）；与 `tower` 中间件的桥接。

**适用**：rag-dashboard 想把 Go gateway 改成 Rust，或者新建 MCP server 高性能侧车。

---

#### 2️⃣ qdrant/qdrant — 向量 DB（24k★）

**热点**：
- `lib/collection/src/` — collection 管理 + 分片
- `lib/segment/src/` — 索引核心（HNSW + payload filter）
- `lib/storage/src/` — RocksDB / mmap 持久化
- `lib/api/src/grpc/` — gRPC 接口

**抄走**：
- HNSW 实现（业界除 FAISS 外最完整的开源）
- payload filtering 与向量索引的联合查询
- sharding + replication 协议

**对照**：rag-dashboard 用 chromadb？换 qdrant 性能 + 内存控制都好得多。`rig-qdrant` 已有直连 crate。

---

#### 3️⃣ meilisearch — 全文搜索引擎（50k★）

**结构**：`crates/` 下含 `meilisearch / index-scheduler / milli (核心索引) / dump / benchmarks`。  
**抄走**：
- typo-tolerance（自动纠错）算法
- 排序规则可配置（words → typo → proximity → attribute → sort → exactness）
- 增量索引

**适用**：RAG 的 lexical 召回层（替代 ES）；用户搜索框。

---

#### 4️⃣ tantivy — BM25 搜索库

**特点**：有 `ARCHITECTURE.md` 文档，是 Lucene 思想的 Rust 重写，**meilisearch 不基于它**（meilisearch 用自家 milli）。

**抄走**：
- 单文件嵌入式倒排索引（无服务器进程）
- segment merge 策略
- columnar storage (`columnar/`)

**适用**：本地 RAG 场景，不需要起独立服务；rag-dashboard 的混合检索若想从 Python rank-bm25 换成 Rust，可用 tantivy + PyO3 binding。

---

#### 5️⃣ rig — Rust LLM/agent 框架（**最被低估**）

**ECOSYSTEM.md 证据**：Coral Protocol、HelixDB、Neon、St Jude 在生产使用。

**19 个 crates**（覆盖度惊人）：

```
rig-core      ← 核心抽象
rig-derive    ← 宏

provider 集成:
  rig-bedrock, rig-gemini-grpc

vector DB 集成（9 个！）:
  rig-qdrant, rig-mongodb, rig-postgres, rig-sqlite,
  rig-lancedb, rig-milvus, rig-neo4j, rig-scylladb, rig-surrealdb,
  rig-helixdb, rig-s3vectors

其他:
  rig-memory       ← 记忆模块
  rig-vectorize    ← 向量化
  rig-fastembed    ← 嵌入模型集成
  rig-vertexai     ← Google Vertex
```

**抄走**：
- `rig-core` 的 `CompletionModel` / `EmbeddingModel` / `Agent` trait 设计 — 比 LangChain 优雅
- 9 个向量 DB adapter 的统一接口（可参考做 Python 版）
- `rig-memory` 短/长期记忆抽象

**对照 BEST-OF-STACK 已有的 vercel-ai**：vercel-ai 强 provider 集成（58 个），rig 强向量 DB 集成（9 个）。两者互补。

---

#### 6️⃣ ratatui — TUI 库

**特点**：有 `ARCHITECTURE.md` + `BREAKING-CHANGES.md`，Claude Code / gemini-cli 等 CLI agent 的 TUI 基础。

**抄走**：
- Widget 渲染模型（声明式）
- `Frame` + `Buffer` 双缓冲
- Layout 算法（constraint-based）

**适用**：自研 CLI agent；rag-dashboard 想加个本地终端界面。

---

### Go 侧

#### 7️⃣ ollama — 本地 LLM serving（100k★，必读）

**热点**：
- `server/` — HTTP API（兼容 OpenAI）
- `cmd/` — CLI（`ollama run/pull/list`）
- `convert/` — GGUF 模型转换
- `discover/` — 硬件探测（GPU/CPU）
- 🔥 **`anthropic/anthropic.go`** — Anthropic API 兼容层（让 Claude Code 能直连 ollama！）

**抄走**：
- OpenAI/Anthropic 兼容 API 双协议实现
- 模型仓库 + 增量下载（类 docker push/pull）
- GPU/Metal 自动调度

**适用**：所有需要本地推理的 agent；BeautyOS Hermes 本地化首选。

---

#### 8️⃣ eino — ByteDance LLM 框架

**热点**：
- `adk/` — **Agent Development Kit**，含 `react.go / deterministic_transfer.go / failover_chatmodel.go / turn_loop.go / interrupt.go / cancel.go` — agent 主循环全套
- `flow/agent/` `flow/indexer/` `flow/retriever/` — RAG 三件套
- `compose/` — 编排原语（类 LangChain LCEL）
- `components/` — model / embedding / retriever / tool 抽象
- `callbacks/` — 中间件
- `ext/` — 扩展实现

**抄走**：
- `turn_loop.go` agent 主循环（含 interrupt / cancel）
- `failover_chatmodel.go` 模型 failover
- `compose/` 图式编排

**对照**：比 langchaingo 设计更新更工程化（ByteDance 内部 spawned）。Go agent 框架首选。

---

#### 9️⃣ langchaingo — LangChain Go 端口

**结构**：`agents / chains / callbacks / documentloaders / embeddings / memory / outputparsers / prompts / textsplitter / tools / vectorstores`

**抄走**：
- 标准 LangChain 概念在 Go 中的映射
- `vectorstores/` 多向量 DB 适配
- `outputparsers/` 结构化输出解析

**避坑**：与 Python LangChain 一样的设计臃肿问题，**复杂 agent 优先选 eino**。langchaingo 更适合"我有现成 LangChain Python，想换 Go"的迁移场景。

---

#### 🔟 weaviate — 向量 DB（生产级）

**特点**：4328 个 Go 文件（最大的一个），**带 `CLAUDE.md`** 含强硬的 "No bug is ever out of scope" 工程文化文档。

**热点**：
- `adapters/` — 多种 vectorizer/generative module 接入（openai/cohere/huggingface/ollama/...）
- `cluster/` — Raft 复制
- `modules/` — 插件式模块（生成、向量化、reranker）

**抄走**：
- 模块化 vectorizer 协议（每个 embedding 模型一个 module）
- 内置 reranker
- BM25 + 向量混合搜索

**对照 qdrant**：qdrant 更轻快，weaviate 更"应用层完整"（自带 embedding/rerank）。RAG 想要 batteries-included → weaviate；想要纯向量引擎 → qdrant。

---

#### 1️⃣1️⃣ mcp-go — MCP Go SDK

**热点**：
- `server/hooks.go` — server 端 hooks
- `server/elicitation.go` — 🆕 MCP elicitation（让 server 反问 user）
- `server/client_info_store.go` — 多客户端会话
- `server/http_cors.go` — HTTP/SSE transport
- `mcptest/` — 测试工具
- `otel/` — OpenTelemetry 集成

**抄走**：
- MCP server 端完整生命周期（initialize / list_tools / call_tool）
- elicitation 模式（双向交互，比 stdio 强）
- otel 接入示范

**适用**：用 Go 写 MCP server（最快路径）。注意：rag-dashboard 已有 Go 后端，给某个内部功能加 MCP 出口非常合适。

---

#### 1️⃣2️⃣ gptscript — 声明式 LLM 脚本

**亮点**：用 markdown/YAML 写 agent 工作流，不用写代码。Acorn Labs（曾做 Rancher）出品。

**热点**：
- `pkg/runner/` — 执行引擎
- `pkg/tools/` — 内置工具集
- `pkg/openai/` — OpenAI 适配

**抄走**：
- "自然语言 + YAML 当代码"的脚本协议
- 工具/agent 嵌套调用模型

**适用场景**：给非开发用户写 agent 流程（业务侧）；rag-dashboard 想暴露"流程编辑器"给客户。

## 三、补到 BEST-OF-STACK 的新模块（Layer F + G）

### Layer F. Rust 后端（4 模块）

| 模块 | 🥇 主选 | 备选 |
|---|---|---|
| F1. Rust web framework | **axum** `axum/src/` | actix-web |
| F2. 向量 DB（Rust） | **qdrant** `lib/segment/src/` | — |
| F3. 搜索引擎/库 | **meilisearch**（完整 app）/ **tantivy**（lib） | — |
| F4. Rust LLM agent 框架 | **rig** `crates/rig-core/` | — |

### Layer G. Go 后端（5 模块）

| 模块 | 🥇 主选 | 备选 |
|---|---|---|
| G1. 本地 LLM serving | **ollama** `server/` + `anthropic/` | llama.cpp 本体 |
| G2. Go LLM 框架 | **eino** `adk/` + `flow/` | langchaingo（迁移友好） |
| G3. 向量 DB（Go） | **weaviate** `adapters/` + `modules/` | — |
| G4. MCP server (Go) | **mcp-go** `server/` | — |
| G5. 声明式 agent 脚本 | **gptscript** `pkg/runner/` | — |

并把 TUI（ratatui）补到 Layer C 编排层作 CLI 形态：

| 模块 | 🥇 主选 |
|---|---|
| C6. TUI / CLI 形态 | **ratatui** `src/` + `examples/` |

→ 详细更新见 [BEST-OF-STACK.md](BEST-OF-STACK.md)（4 层 22 模块 → 7 层 39 模块）。

## 四、推荐组合（按场景）

### 场景 D：Rust 性能侧车（RAG 召回延迟瓶颈）
```
qdrant + tantivy + axum (BFF) + rig-core (LLM 调度)
```
→ 嵌入式部署一个 Rust binary，吃延迟敏感的检索。

### 场景 E：完整 Go 后端 agent（BeautyOS / rag-dashboard 类）
```
ollama (本地推理) + eino (agent loop) + weaviate (RAG)
+ mcp-go (对外 MCP 出口) + gptscript (业务流程编辑)
```
→ 全 Go 部署，单一运行时；适合 Hermes/BeautyOS 这种已有 Go 基础设施的项目。

### 场景 F：纯 Rust agent（性能/嵌入式）
```
rig-core + rig-qdrant + ratatui (CLI) + axum (API)
```
→ 单 binary 几 MB 发布，无 GC，适合边缘部署。

## 五、文化收获：3 个仓库附带的 AI 协作文档

跨克隆 19 个仓库（含上一轮 7 前端 + 这轮 12）后，发现这些仓库**主动给 Claude Code/agent 写了协作指引**：

| 仓库 | 文档 | 看点 |
|---|---|---|
| **weaviate** | `CLAUDE.md` | "No bug is ever out of scope" — 给 agent 的强硬质量规范 |
| **rig** | `AGENTS.md` + `ECOSYSTEM.md` | agent 上下文 + 生态地图（哪些公司在用） |
| **meilisearch** | `AGENTS.md` | 给 agent 的导航 |
| **mcp-go** | `AGENTS.md` | 同上 |
| **ratatui** | `ARCHITECTURE.md` | 架构图给 agent 读 |
| **tantivy** | `ARCHITECTURE.md` | 同上 |

**结论**：成熟项目正在标配 `AGENTS.md` / `CLAUDE.md` / `ARCHITECTURE.md`。建议 rag-dashboard / hermes-agent 也加上，让接入它们的 agent 拿到稳定上下文。
