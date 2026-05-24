# 第 4 批分析 · RAG + Evaluation 栈（2026-05-25）

> 在前三批（基础设施→前端→后端→Python agent/异步/观测）之后，本批补齐**检索增强**与**评测**两个关键能力维度。

## 一、阵容（10 个仓库 / ~1.1 GB）

### 16-rag-stack（6 个，~916 MB）
| 仓库 | 星 | 体量 | AGENTS.md/CLAUDE.md |
|---|---|---|---|
| ragflow | 40k★ | 125M / 821 py | ✅ ✅ |
| llama_index | 35k★ | 570M / 3834 py | — |
| haystack | 17k★ | 77M / 560 py | ✅ ✅ |
| graphrag | 22k★ | 31M / 570 py | — |
| LightRAG | 15k★ | 20M / 284 py | ✅ ✅ |
| FlashRAG | 2k★ | 95M / 86 py | — |

### 17-evaluation（4 个，~195 MB）
| 仓库 | 星 | 体量 | 用途 |
|---|---|---|---|
| ragas | 9k★ | 38M / 387 py | RAG metric 事实标准 |
| lm-evaluation-harness | 9k★ | 97M / 786 py | HF Leaderboard 引擎 |
| gorilla | 12k★ | 34M / 213 py | BFCL function-calling 评测 |
| opencompass | 5k★ | 27M / 3015 py | 中文 LLM 评测 |

## 二、抄什么（按重要性）

### 🥇 ragflow/deepdoc — 当之无愧的工业级文档解析器
- `parser/` 覆盖 pdf / docx / excel / ppt / html / md / json / audio
- `vision/` OCR + 版面分析（表格 / 公式 / 图片）
- **国内开源最完整的文档管线**，比 unstructured 更细
- 任何 RAG 项目「文档入库」环节直接照抄

### 🥇 llama_index 29 类集成 = 适配器宝典
`llama-index-integrations/` 的 29 个子目录：
```
agent / callbacks / embeddings / evaluation / extractors / graph_rag /
graph_stores / indices / ingestion / llms / memory / node_parser /
observability / output_parsers / postprocessor / program / protocols /
question_gen / readers / retrievers / response_synthesizers / selectors /
storage / tools / vector_stores / workflow / cli / ... 
```
- 选 RAG 组件先翻这个目录的接口
- 每类都有 5-50+ 厂商实现，写适配器骨架最佳

### 🥇 ragas pattern — LLM-as-Judge 标准实现
- `src/ragas/metrics/` 每个 metric = 一个 prompt + 解析器
- faithfulness / answer_relevancy / context_precision / context_recall
- **任何自建评测系统的起点**

### 🥈 gorilla BFCL — function-calling 唯一标杆
`berkeley-function-call-leaderboard/`：
- simple / parallel / multi-turn / live / hallucination 五大类
- 自家 agent 上线前的必跑回归

### 🥈 ragflow agent canvas
`ragflow/agent/canvas.py` + `component/` + `sandbox/`：
- 可视化编排 + 沙箱执行
- 与 dify 互为参考

### 🥉 LightRAG vs graphrag 对照学习
- **LightRAG**（284 py）= 知识图谱 RAG 最简实现，看懂概念
- **graphrag**（570 py）= Microsoft 工业实现，看懂工程

## 三、BEST-OF-STACK 新增两层（K + L）

```
Layer K  RAG 检索        5 模块
Layer L  Evaluation      4 模块
```

合计：**12 层 × 59 模块**（上一批为 10 层 × 50）。

### K 层（RAG 检索）5 模块
| 模块 | 🥇 主选 | 🥈 备选 | 一句话理由 |
|------|--------|--------|------------|
| 文档解析 | ragflow/deepdoc | unstructured | 国内最完整工业级管线 |
| RAG 框架 | llama_index | haystack | 29 类集成 + 最大生态 |
| 知识图谱 RAG | graphrag (Microsoft) | LightRAG (HKUDS) | 工业 vs 极简对照 |
| RAG 算法基线 | FlashRAG | — | 16 种算法学术对照 |
| RAG Pipeline DAG | haystack | llama_index workflow | 强类型 component + 可视化 |

### L 层（Evaluation）4 模块
| 模块 | 🥇 主选 | 🥈 备选 | 一句话理由 |
|------|--------|--------|------------|
| RAG 评测 | ragas | TruLens | 事实标准 |
| Tool-use 评测 | gorilla BFCL | — | function-call 唯一标杆 |
| 通用 LLM 评测 | lm-evaluation-harness | — | HF Leaderboard 引擎 |
| 中文评测 | opencompass | — | 上海 AI Lab，国产首选 |

## 四、4 种 RAG 推荐组合

### 组合 K — RAG MVP（学习/原型）
```
LightRAG + FlashRAG + ragas
```
~120M，3 仓库读完即懂 RAG。

### 组合 L — 工业 RAG（中文）
```
ragflow（含 deepdoc）+ ragas + opencompass
```
完整文档管线 + 评测 + 中文场景。

### 组合 M — Agent + RAG 全栈
```
llama_index + langgraph + ragas + langfuse + qdrant
```
组件最齐全 + agent 编排 + 评测 + 可观测 + 向量库。

### 组合 N — 知识图谱 RAG
```
graphrag + ragflow/deepdoc + langfuse
```
图谱召回 + 多模态解析 + 全链路追踪。

## 五、AGENTS.md / CLAUDE.md 更新统计

41 个新仓库累计：
- **39%** ship AGENTS.md（+4）
- **34%** ship CLAUDE.md（+5）
- 4/10 本批仓库都带（ragflow / haystack / LightRAG / ragas）

→ RAG/eval 这两类高频被 agent 调用的领域，AGENTS.md 普及率反而更高。

## 六、累计统计

- **82 个仓库 · ~5.0 GB · 17 个分类**
- **BEST-OF-STACK：12 层 × 59 模块**
