# 11-rust-backend — Rust 后端"抄作业"参考

> 2026-05-25 浅克隆 6 个 Rust 后端明星仓库（合计 ~82 MB）。详细分析见 [../09-agent-infra-catalog/2026-05-25-backend-stack-analysis.md](../09-agent-infra-catalog/2026-05-25-backend-stack-analysis.md)。

## 仓库清单

| 仓库 | Star | 大小 | 模块 | 抄什么 |
|---|---|---|---|---|
| [axum/](axum/) | 22k+ | 5.4M | web 框架 | `axum/src/extract/` typed extractors |
| [qdrant/](qdrant/) | 24k+ | 24M | 向量 DB | `lib/segment/src/` HNSW + payload filter |
| [meilisearch/](meilisearch/) | 50k+ | 16M | 全文搜索引擎 | `crates/milli/` typo-tolerance 算法 |
| [tantivy/](tantivy/) | 12k+ | 14M | BM25 嵌入式库 | `src/` + `columnar/` Lucene Rust 版 |
| [rig/](rig/) | 3k+ | 17M | LLM agent 框架 | `crates/rig-core/` + 9 个向量 DB adapter |
| [ratatui/](ratatui/) | 10k+ | 5.3M | TUI 库 | `src/` Widget + Layout constraint |

## 三个推荐组合

**性能侧车（嵌入式 RAG）**：`qdrant + tantivy + axum + rig-core`  
**纯 Rust agent**：`rig + rig-qdrant + ratatui + axum`  
**RAG 召回延迟优化**：`qdrant`（替代 chromadb）+ `tantivy`（替代 rank-bm25）

## ⭐ 看点

- **rig 是被低估的明星** — 19 个 crates，覆盖 9 个向量 DB；Coral Protocol / Neon / 圣裘德医院在生产使用
- **qdrant vs weaviate**：qdrant 轻快（纯向量引擎）；weaviate 应用层完整（自带 embedding/rerank）
- **tantivy 不被 meilisearch 使用** — meilisearch 用自家 milli；两者并列两个独立 Rust 搜索方案
