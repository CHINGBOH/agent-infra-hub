# 14-async-infra — 异步基础设施"抄作业"参考

> 2026-05-25 浅克隆 3 个异步/基础设施仓库（~350 MB）。详细分析见 [../09-agent-infra-catalog/2026-05-25-python-infra-obs-analysis.md](../09-agent-infra-catalog/2026-05-25-python-infra-obs-analysis.md)。

| 仓库 | Star | 大小 | 抄什么 |
|---|---|---|---|
| [temporal/](temporal/) | 12k+ | 37M | `service/{frontend,history,matching,worker}/` Workflow 引擎 |
| [nats-server/](nats-server/) | 16k+ | 12M | `server/` 单 binary 消息总线（Subject + JetStream） |
| [cua/](cua/) | 8k+ | 301M | `libs/{cua-driver,lume,lumier,qemu-docker,xfce}/` 完整桌面虚拟化栈 |

## 何时用

- **Agent 跑超过 30 秒**：上 temporal 拿持久化 / 崩溃恢复
- **多 agent 协同**：上 nats（比 Kafka 轻 10x）
- **桌面自动化 agent**：用 cua 给 agent 完整桌面环境（Linux/macOS VM）
