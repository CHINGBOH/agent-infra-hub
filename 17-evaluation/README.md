# 17-evaluation — LLM / Agent 评测明星仓库

> 第 4 批克隆。覆盖：RAG 评测、通用 LLM 评测、Tool-use 评测、中文评测。

## 4 个仓库一览

| 仓库 | 星 | 体量 | 抄什么 |
|------|----|----|--------|
| 🥇 **[ragas](./ragas/)** | 9k★ | 38M / 387 py | RAG 评测事实标准：faithfulness / answer_relevancy / context_precision 等 |
| 🥈 **[lm-evaluation-harness](./lm-evaluation-harness/)** | 9k★ | 97M / 786 py | EleutherAI；HF leaderboard 用的就是它；60+ benchmark task |
| **[gorilla](./gorilla/)** | 12k★ | 34M / 213 py | **BFCL**（Berkeley Function-Calling Leaderboard）= tool-use 评测唯一公认标杆 |
| **[opencompass](./opencompass/)** | 5k★ | 27M / 3015 py | 上海 AI Lab；中文 LLM 评测主流，C-Eval / MMLU-CN 等 |

## 抄作业重点

### 1. ragas pattern — 用 LLM 当裁判
- `src/ragas/metrics/` 每个 metric 就是一个 prompt + 解析器
- 任何想自建评测的项目都可以照搬骨架

### 2. gorilla/BFCL — function-calling 评测
- `berkeley-function-call-leaderboard/`
- 测试 simple / parallel / multi-turn / live / hallucination 五类
- 自家 agent 上线前必跑

### 3. lm-evaluation-harness — task 注册模式
- 每个 benchmark 是一个 yaml + python 文件
- 极易扩展，适合内部 benchmark 套件骨架

### 4. opencompass — 中文场景
- 模型 ↔ 数据集 ↔ 评测器三层解耦
- 中文项目首选

## 在 BEST-OF-STACK 中的位置
→ **Layer L (Evaluation)** 新增 4 模块（RAG 评测 / 通用 LLM / Tool-use / 中文评测）
