# PoC 矩阵

把 `09-agent-infra-catalog/BEST-OF-STACK.md` 里的 18 层 × 80 模块
落成可跑的最小组合 demo。每个目录一个组合（命名取自 14 种 agent 组合姿势的字母 A-T）。

| ID | 名称 | 状态 | 一句话 |
| --- | --- | --- | --- |
| **S** | [MCP-native](./S-mcp-native/) | ✅ done | rag-dashboard 包成 MCP server，8 个 tool 接 Claude Code |
| P | 记忆持久化 | 🚧 待开 | mem0 + rag-dashboard，跨会话记得用户偏好 |
| O | 沙箱执行 | 🚧 待开 | e2b/daytona 跑 agent 生成的 python |
| R | 实时语音 | 🚧 待开 | livekit-agents 复用同一份 rag tool |
| Q | MCP 网关 | 🚧 待开 | 多 server 聚合到一个 endpoint |
| ... | ... | ... | 见 BEST-OF-STACK.md |

## 通用约定

- 每个 PoC 必须有：`README.md` / `requirements.txt` / `smoke.py`（或 `smoke.sh`）/ `client_demo.*`
- 后端依赖（rag-dashboard / qdrant / pg）默认假设跑在本机标准端口
- 不内嵌大模型 key，所有 secrets 走环境变量

## 起步顺序建议

1. 先跑 **S**（MCP-native）—— 验证 rag-dashboard API 在 MCP 协议上完整可用
2. 再上 **P**（记忆）—— mem0 + rag-dashboard 双向同步
3. 然后 **O**（沙箱）—— 让 agent 真能跑 python
4. 之后按需求挑 R / Q / 多模态 / 安全
