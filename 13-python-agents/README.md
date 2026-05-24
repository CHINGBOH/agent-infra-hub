# 13-python-agents — Python Agent 框架"抄作业"参考

> 2026-05-25 浅克隆 6 个 Python agent 明星仓库（~393 MB）。详细分析见 [../09-agent-infra-catalog/2026-05-25-python-infra-obs-analysis.md](../09-agent-infra-catalog/2026-05-25-python-infra-obs-analysis.md)。

| 仓库 | Star | 大小 | 抄什么 |
|---|---|---|---|
| [dify/](dify/) | 90k+ | 144M | `api/core/{agent,mcp,memory}/` 一站式平台 |
| [autogen/](autogen/) | 40k+ | 62M | `autogen-core/src/autogen_core/_agent*.py` runtime + pub-sub |
| [crewai/](crewai/) | 28k+ | 149M | `lib/crewai-core/src/` role-based |
| [langgraph/](langgraph/) | 10k+ | 14M | `libs/langgraph/{pregel,channels,graph}/` + 检查点 |
| [openai-agents/](openai-agents/) | 8k+ | 21M | `src/agents/{guardrail,handoffs,computer}.py` |
| [smolagents/](smolagents/) | 15k+ | 4.1M | 仅 75 个 py 文件 — agent 最小可读实现 |

## 选型指南

| 想做什么 | 选 |
|---|---|
| 给业务用户做 agent SaaS | **dify**（直接部署 / 抄业务架构） |
| 多 agent 消息协作 | **autogen** |
| Role/Task 显式建模 | **crewai** |
| 长跑 / 中断恢复 / Py+JS 双端 | **langgraph** |
| OpenAI 生态 + computer use | **openai-agents** |
| 教学 / 原型 / CodeAgent | **smolagents** |

⭐ **6/6 都自带 AGENTS.md 或 CLAUDE.md**，是当前 Python agent 圈的事实标准。
