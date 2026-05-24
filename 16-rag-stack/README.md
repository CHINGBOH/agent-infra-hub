# 16-rag-stack — RAG / 检索增强明星仓库

> 第 4 批克隆。专注于「检索 → 切分 → 索引 → 召回 → 重排 → 生成」全链路最强实现。

## 6 个仓库一览

| 仓库 | 星 | 体量 | 抄什么 |
|------|----|----|--------|
| 🥇 **[ragflow](./ragflow/)** | 40k★ | 125M / 821 py | 一站式 RAG：deepdoc 文档解析器（vision+parser）+ agent canvas + 沙箱 + AGENTS.md+CLAUDE.md |
| 🥈 **[llama_index](./llama_index/)** | 35k★ | 570M / 3834 py | **29 类集成**（agent/embeddings/llms/graph_rag/memory/observability/readers/postprocessor 等）= 终极适配器目录 |
| 🥉 **[haystack](./haystack/)** | 17k★ | 77M / 560 py | Pipeline DAG + 强类型 component；deepset 出品；AGENTS.md + CLAUDE.md |
| **[graphrag](./graphrag/)** | 22k★ | 31M / 570 py | Microsoft 图谱式 RAG（实体提取 → community → 多跳问答）|
| **[LightRAG](./LightRAG/)** | 15k★ | 20M / 284 py | 极简知识图谱 RAG（HKUDS 港大），AGENTS.md+CLAUDE.md |
| **[FlashRAG](./FlashRAG/)** | 2k★ | 95M / 86 py | 研究向 RAG 基线集合（人大），含 16 种算法对照 |

## 抄作业重点

### 1. ragflow/deepdoc — 文档解析金标
- `parser/` 处理 pdf/docx/excel/ppt/html/markdown/json/audio
- `vision/` OCR + 版面分析（表格/公式/图片）
- 这是国内最完整的工业级文档解析开源实现

### 2. llama_index 29 类集成 = 模块拼装清单
直接对照 `llama-index-integrations/` 的 29 个子目录决定要哪些组件，每类都有 5-50+ 实现。

### 3. ragflow agent canvas
`ragflow/agent/canvas.py` + `component/` — 可视化 agent 编排，对比 dify 的实现各有侧重。

### 4. LightRAG / graphrag — 知识图谱 RAG 对照
- LightRAG: 极简实现（284 py），适合学习
- graphrag: 工业实现（570 py），适合借鉴架构

## 在 BEST-OF-STACK 中的位置
→ **Layer K (RAG 检索)** 新增 5 模块（文档解析 / 切分 / 向量索引 / 图谱 RAG / 重排）
