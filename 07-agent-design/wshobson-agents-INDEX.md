# wshobson-agents — Plugin Router (81 plugins)

> **二级路由索引。** 当 MANIFEST.md 把你指到 wshobson-agents 时，先读这个文件，按意图选 plugin，无需自行 `ls plugins/`。
>
> 每个 plugin 都是独立的 `agents/ + commands/ + skills/` 三元组。安装方式见仓库 [README.md](README.md)。

---

## 按意图速查

| 我要做什么 | 推荐 plugin | 路径 |
|------------|-------------|------|
| 端到端开发一个完整功能 | `full-stack-orchestration` | [plugins/full-stack-orchestration/](wshobson-agents/plugins/full-stack-orchestration/) |
| 多 agent 协作（实验性）| `agent-teams` + `agent-orchestration` | [plugins/agent-teams/](wshobson-agents/plugins/agent-teams/) · [plugins/agent-orchestration/](wshobson-agents/plugins/agent-orchestration/) |
| TDD 严格流程 | `tdd-workflows` + `unit-testing` | [plugins/tdd-workflows/](wshobson-agents/plugins/tdd-workflows/) |
| 多视角代码审查 | `comprehensive-review` | [plugins/comprehensive-review/](wshobson-agents/plugins/comprehensive-review/) |
| 复杂 bug 调试 | `debugging-toolkit` + `distributed-debugging` | [plugins/debugging-toolkit/](wshobson-agents/plugins/debugging-toolkit/) |
| MCP server 安全治理 | `protect-mcp` | [plugins/protect-mcp/](wshobson-agents/plugins/protect-mcp/) |
| Cedar policy + 审计 | `signed-audit-trails` + `protect-mcp` | [plugins/signed-audit-trails/](wshobson-agents/plugins/signed-audit-trails/) |
| 性能调优 | `application-performance` + `performance-testing-review` | [plugins/application-performance/](wshobson-agents/plugins/application-performance/) |
| 生产事故响应 | `incident-response` + `error-diagnostics` | [plugins/incident-response/](wshobson-agents/plugins/incident-response/) |
| 构建 LLM 应用 | `llm-application-dev` | [plugins/llm-application-dev/](wshobson-agents/plugins/llm-application-dev/) |
| MLOps 流水线 | `machine-learning-ops` | [plugins/machine-learning-ops/](wshobson-agents/plugins/machine-learning-ops/) |
| K8s 部署 | `kubernetes-operations` + `deployment-strategies` | [plugins/kubernetes-operations/](wshobson-agents/plugins/kubernetes-operations/) |
| 评估 plugin 质量 | `plugin-eval` | [plugins/plugin-eval/](wshobson-agents/plugins/plugin-eval/) |
| context-driven 开发 | `conductor` | [plugins/conductor/](wshobson-agents/plugins/conductor/) |

---

## 按 25 分类完整索引

来源：本仓库 [README.md](README.md) §Plugin Categories。

### 🎨 Development (6)

`backend-development`, `frontend-mobile-development`, `multi-platform-apps`, `debugging-toolkit`, `ui-design`, `meigen-ai-design`

### 📚 Documentation (4)

`code-documentation`, `documentation-generation`, `documentation-standards`, `c4-architecture`

### 🔄 Workflows (5)

`git-pr-workflows`, `full-stack-orchestration`, `tdd-workflows`, **`conductor`**（context-driven）, **`agent-teams`**（多 agent 协作，⚠️ 实验性）

### ✅ Testing (2)

`unit-testing`, `ship-mate`

### 🔍 Quality (3)

`comprehensive-review`, `performance-testing-review`, `codebase-cleanup`

### 🤖 AI & ML (4)

`llm-application-dev`, `agent-orchestration`, `context-management`, `machine-learning-ops`

### 📊 Data (2)

`data-engineering`, `data-validation-suite`

### 🗄️ Database (2)

`database-design`, `database-migrations`

### 🚨 Operations (4)

`incident-response`, `error-diagnostics`, `distributed-debugging`, `observability-monitoring`

### ⚡ Performance (2)

`application-performance`, `database-cloud-optimization`

### ☁️ Infrastructure (5)

`deployment-strategies`, `deployment-validation`, `kubernetes-operations`, `cloud-infrastructure`, `cicd-automation`

### 🔒 Security (6)

`security-scanning`, `security-compliance`, `backend-api-security`, `frontend-mobile-security`, `block-no-verify`, `review-agent-governance`

### 🛡️ Governance (2)

`protect-mcp`（Cedar policy + Ed25519 receipts）, `signed-audit-trails`

### 💻 Languages (10)

`python-development`, `javascript-typescript`, `systems-programming`, `jvm-languages`, `shell-scripting`, `functional-programming`, `arm-cortex-microcontrollers`, `julia-development`, `dotnet-contribution`, `web-scripting`

### 🔗 Blockchain (1)

`blockchain-web3`

### 💰 Finance (1)

`quantitative-trading`

### 💳 Payments (1)

`payment-processing`

### 🎮 Gaming (1)

`game-development`

### 🎨 Creative (1)

`brand-landingpage`

### ♿ Accessibility (1)

`accessibility-compliance`

### 📢 Marketing (4)

`seo-content-creation`, `seo-technical-optimization`, `seo-analysis-monitoring`, `content-marketing`

### 💼 Business (4)

`business-analytics`, `hr-legal-compliance`, `customer-sales-automation`, `startup-business-analyst`

### 🔌 API (2)

`api-scaffolding`, `api-testing-observability`

### 🛠️ Utilities (4)

`developer-essentials`, `dependency-management`, `team-collaboration`, `error-debugging`

### 🔧 Modernization (2)

`framework-migration`, `code-refactoring`

### 🧪 Misc / 评估

`plugin-eval`（评估 plugin 质量）, `reverse-engineering`

---

## 实验性 / 注意事项

| Plugin | 注意 |
|--------|------|
| `agent-teams` | 依赖实验性 API `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`，参见 [../../MANIFEST.md#experimental-apis](../MANIFEST.md#experimental-apis) |
| `block-no-verify` | git hook bypass 拦截器，与 `signed-audit-trails` 配合使用 |
| `protect-mcp` | 需要 Cedar policy + Ed25519 key 基础设施 |

---

## 与本仓库其他模块的关系

| wshobson plugin | 推荐配合 |
|-----------------|----------|
| `agent-orchestration` / `agent-teams` | [../metaswarm/](metaswarm/)（9 阶段门控）, [../claude-swarm/](claude-swarm/)（DAG 调度） |
| `protect-mcp` / `signed-audit-trails` | [../../09-agent-infra-catalog/governance-guardrails/agent-governance-toolkit/](../09-agent-infra-catalog/governance-guardrails/agent-governance-toolkit/) |
| `observability-monitoring` | [../../08-infrastructure/hooks/claude-code-hooks-multi-agent-observability/](../08-infrastructure/hooks/claude-code-hooks-multi-agent-observability/), [../../09-agent-infra-catalog/observability-hud/claude-code-dashboard/](../09-agent-infra-catalog/observability-hud/claude-code-dashboard/) |
| `context-management` | [../../08-infrastructure/context-window/token-optimizer/](../08-infrastructure/context-window/token-optimizer/) |
| `tdd-workflows` | [../../skill-research/05-examples/superpowers-skills/](../skill-research/05-examples/superpowers-skills/) (TDD skill) |

---

## 完整 plugin 目录

机器可读完整清单：[docs/plugins.md](wshobson-agents/docs/plugins.md)（如该目录存在）  
或直接 `ls plugins/` 列出全部 81 个。
