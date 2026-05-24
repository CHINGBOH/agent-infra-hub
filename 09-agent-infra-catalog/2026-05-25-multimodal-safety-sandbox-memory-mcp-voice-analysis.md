# 第 5 批分析 · 多模态 + 安全 + 沙箱 + 记忆 + MCP + 语音（2026-05-25）

> 一口气补齐 agent 工程的 6 个关键能力维度，**24 个仓库 / ~1.1 GB**。

## 一、阵容总览

| 分类 | 仓库 | 主要收获 |
|---|---|---|
| **18-multimodal** | Qwen-Agent, vision-agent, InternVL, LLaVA | 多模态 agent loop / VLM 参考 |
| **19-safety** | garak, NeMo-Guardrails, presidio, promptbench, llm-attacks | 红队 + 防护轨 + PII + 攻击 |
| **20-sandbox** | e2b, daytona, open-interpreter, pyodide | 代码沙箱 SaaS + WASM + 本地 |
| **21-memory** | mem0, letta, zep, cognee | 自动事实 / 分层 / 图谱式记忆 |
| **22-mcp-ecosystem** | mcp-servers, mcp-python-sdk, mcp-agent, awesome-mcp | 官方 SDK + 7 个参考 server |
| **23-voice** | livekit-agents, pipecat, vocode-core | 71 个 plugin / 实时管线 |

## 二、本批 6 个「金牌发现」

### 🥇 garak/probes/ — 红队 44 类 probe
事实上的 LLM 红队标准。每个 probe 是一个 attack pattern：
`dan / jailbreak / promptinject / atkgen / leak / encoding / continuation / xss ...`
**自家 agent 上线前必跑**。NVIDIA 出品。

### 🥇 livekit-agents/livekit-plugins/ — 71 个 plugin
TTS/STT/LLM/Avatar/Browser 厂商适配的最完整集合：
anthropic / openai / google / aws / azure / elevenlabs / deepgram / cartesia / assemblyai / ...
**写语音 agent 选这个零门槛**。

### 🥇 mem0/openmemory/ + skills/ — 记忆产品的 agent-friendly 范本
ships 完整的 **`skills/`**（5 个子 skill：mem0 / mem0-cli / mem0-integrate / mem0-test-integration / mem0-vercel-ai-sdk）+ **AGENTS.md + CLAUDE.md** + **openmemory/** MCP 服务。
**记忆产品 + 自家 MCP 服务的最佳实践范本**。

### 🥇 mcp-servers/src/{filesystem,git,memory,fetch,time,sequentialthinking,everything}
**写 MCP server 的 7 个官方范本**。要做 hermes-agent 的本地 MCP 直接抄这套。

### 🥇 e2b/packages/python-sdk + pyodide
- e2b = 后端 LLM 代码沙箱事实接口
- pyodide = 浏览器侧 Python WASM
- 二者组合 = **任何场景都有 sandbox 方案**

### 🥇 cognee + letta + mem0 三选一
- **mem0**: 30k★ 用户最多，自动事实抽取，cluster 模式
- **letta** (15k★): 前 MemGPT，core/recall/archival 分层
- **cognee** (5k★): 知识图谱 ECL 管线，1524 py，最重也最完整

## 三、BEST-OF-STACK 新增 6 层（M-R）

```
Layer M  Multimodal       3 模块
Layer N  Safety           4 模块
Layer O  Sandbox          4 模块
Layer P  Memory           4 模块
Layer Q  MCP Ecosystem    3 模块
Layer R  Voice / 实时     3 模块
```

合计：**18 层 × 80 模块**（上一批 12 层 × 59）。

## 四、AGENTS.md / CLAUDE.md 文化爆发（截至本批）

| 批次 | 仓库 | AGENTS.md | CLAUDE.md |
|---|---|---|---|
| 0 (基线) | 31 | 35% | 29% |
| 1-4 (41 个新) | 41 | 39% | 34% |
| **5 (本批 24 个)** | 24 | **46%** | **38%** |

→ 本批是 AGENTS.md 普及率最高的一批。**记忆 / MCP / 语音 / 沙箱** 是 agent 调用最密集的领域，因此上游率先标准化 agent 文档。

## 五、6 种新组合（合计已达 14 种姿势）

### 组合 O — 红队 + 防护 + 评测
```
garak + NeMo-Guardrails + presidio + promptbench
```
完整上线前安全栈。

### 组合 P — Memory-first agent
```
mem0 + openmemory(MCP) + langgraph + langfuse
```
长跑 agent 的记忆 + 编排 + 观测。

### 组合 Q — 浏览器侧 agent（无后端）
```
pyodide + Vercel AI SDK + mcp-python-sdk
```
完全前端方案。

### 组合 R — 语音实时 agent
```
livekit-agents + pipecat + e2b + langfuse
```
实时对话 + 工具执行 + 观测。

### 组合 S — MCP-native agent
```
mcp-servers + mcp-python-sdk + mcp-agent + Claude Code
```
全用 MCP 协议拼装。

### 组合 T — 多模态 agent
```
Qwen-Agent + vision-agent + InternVL + livekit
```
视觉 + 语音多模态。

## 六、累计统计

- **106 个仓库 · ~6.1 GB · 23 个分类目录**
- **BEST-OF-STACK：18 层 × 80 模块**
- 累计「金牌发现」≥ 30 个
