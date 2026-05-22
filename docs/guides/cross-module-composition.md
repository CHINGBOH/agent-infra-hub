# 跨模块组合 — 07 × 08 × 09 实操指南

> [MANIFEST §跨模块组合速查](../../MANIFEST.md#cross-refs) 的展开版。给你一个具体场景，告诉你**怎么把仓库里的组件拼成完整 agent**。

---

## 选型流程

```
1. 选模式  (07-agent-design)        — 解决"多个 agent 怎么协作"
       │
       ▼
2. 加底座  (08-infrastructure)      — 解决"hooks/context/隔离怎么配"
       │
       ▼
3. 加治理  (09-agent-infra-catalog) — 解决"监控/路由/合规怎么搞"
       │
       ▼
4. 选 plugin  (07-agent-design/wshobson-agents-INDEX.md) — 具体落地任务能力
```

---

## 五个完整场景

### 场景 A — CI/CD 自动化代码评审

| 层 | 选择 | 路径 |
|----|------|------|
| 模式 | agent-orchestrator（PR 触发 + 修复循环） | [07-agent-design/agent-orchestrator/](../../07-agent-design/agent-orchestrator/) |
| Hooks | claude-code-hooks-mastery（Stop/Notification 注入审计） | [08-infrastructure/hooks/claude-code-hooks-mastery/](../../08-infrastructure/hooks/claude-code-hooks-mastery/) |
| 隔离 | ECC（每个 PR 独立 sandbox） | [08-infrastructure/subagent-isolation/ECC/](../../08-infrastructure/subagent-isolation/ECC/) |
| 治理 | wshobson `signed-audit-trails` + `comprehensive-review` | [07-agent-design/wshobson-agents/plugins/signed-audit-trails/](../../07-agent-design/wshobson-agents/plugins/signed-audit-trails/) |
| 观测 | claude-code-dashboard | [09-agent-infra-catalog/observability-hud/claude-code-dashboard/](../../09-agent-infra-catalog/observability-hud/claude-code-dashboard/) |

### 场景 B — 大规模并行内容生成（50+ agent）

| 层 | 选择 |
|----|------|
| 模式 | agent-farm（pool 调度）或 ccswarm（git worktree 隔离） |
| Hooks | claude-code-hooks-multi-agent-observability（事件溯源） |
| Context | token-optimizer（PreCompact 5 层压缩） |
| 隔离 | ccswarm 内置 worktree，或 sub-agent-collective Hub-and-Spoke |
| 观测 | dashboard + multi-agent-observability 联动 |

### 场景 C — 9 阶段质量门控（论文/报告生成）

| 层 | 选择 |
|----|------|
| 模式 | metaswarm（9 阶段：规划→研究→设计→实现→测试→审查→优化→文档→交付） |
| Hooks | hooks-mastery PostToolUse 注入阶段评估 |
| Context | token-optimizer（长流程必备） |
| 隔离 | sub-agent-collective（评估 agent 独立上下文） |
| 治理 | agent-governance-toolkit（policy + audit） |

参考实战：[../../use-cases/statistical-analysis-agent.md](../../use-cases/statistical-analysis-agent.md)

### 场景 D — Agent-in-Agent（嵌套调用）

| 层 | 选择 |
|----|------|
| 模式 | claude-code-mcp（把 Claude Code 暴露为 MCP server） |
| Hooks | PreToolUse 审计 + 限流 |
| 路由 | agentgateway（MCP/A2A proxy） |
| 治理 | wshobson `protect-mcp`（Cedar policy + Ed25519 receipts） |

### 场景 E — 企业 RAG + Swarm

| 层 | 选择 |
|----|------|
| 模式 | ruflo（Swarm + 向量检索 + 企业安全） |
| Context | token-optimizer + context-management plugin |
| 隔离 | sub-agent-collective |
| 治理 | agent-governance-toolkit（policy） + signed-audit-trails |
| 观测 | dashboard |

---

## 反模式（不要这么搭）

| 错误组合 | 为什么 |
|----------|--------|
| metaswarm + agent-farm | 阶段门控天然串行；并行 farm 会破坏阶段输入/输出契约 |
| ccswarm worktree + Hub-and-Spoke | worktree 已隔离，再上 Hub-and-Spoke 是双重隔离，吞吐损耗 |
| 启用 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` 但只为内部并行 | 内置 `Agent` tool 就够；实验性 flag 增加不必要风险，见 [experimental-apis.md](experimental-apis.md) |
| 跳过 hooks 直接上大规模 swarm | 没有 PostToolUse 审计 = 黑盒，事故无法溯源 |

---

## 落地 checklist

1. ☐ 在 `use-cases/<name>.md` 写出你的场景，引用本指南某个组合。
2. ☐ 把目标用到的 plugin 列出，从 [wshobson `_INDEX.md`](../../07-agent-design/wshobson-agents-INDEX.md) 挑。
3. ☐ 检查是否依赖实验性 flag，参考 [experimental-apis.md](experimental-apis.md)。
4. ☐ 在 `catalog.json` 加你 use-case 的 resource 条目。
5. ☐ 跑 `make docs-catalog` 确认引用路径存在。
6. ☐ 跑 `make docs-links` 确认你 use-case 文档里的链接都通。
