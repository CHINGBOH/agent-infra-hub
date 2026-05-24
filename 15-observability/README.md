# 15-observability — LLM 可观测性"抄作业"参考

> 2026-05-25 浅克隆 3 个 LLM 可观测仓库（~150 MB）。详细分析见 [../09-agent-infra-catalog/2026-05-25-python-infra-obs-analysis.md](../09-agent-infra-catalog/2026-05-25-python-infra-obs-analysis.md)。

| 仓库 | Star | 大小 | 抄什么 |
|---|---|---|---|
| [langfuse/](langfuse/) | 10k+ | 40M | `web/src/` Next.js + TRPC，Trace / Generation / Span / Prompt mgmt / Eval。**Self-host 友好** |
| [phoenix/](phoenix/) | 5k+ | 59M | `src/phoenix/` eval 工作流 + Vector visualizer，与 LlamaIndex/LangChain 集成 |
| [openllmetry/](openllmetry/) | 6k+ | 51M | `packages/opentelemetry-instrumentation-*/` **31 个 instrumentation 包** |

## 选型指南

| 痛点 | 用哪个 |
|---|---|
| 想要生产级 LLM 可观测 UI（trace+eval+prompt） | **langfuse** |
| 想强化 eval（hallucination 检测 / 数据集对比） | **phoenix** |
| 想加 OTel 插桩到现有 Python 项目（30 行代码） | **openllmetry** |

⭐ **openllmetry 31 个 instrumentation**：anthropic / openai / bedrock / cohere / langchain / llamaindex / crewai / agno / haystack / mcp + 8 个向量 DB（qdrant / pinecone / weaviate / chromadb / milvus / lancedb / marqo）+ google-genai / groq / mistral / together / replicate / ollama / sagemaker / vertexai。
