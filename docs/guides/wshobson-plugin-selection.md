# wshobson-agents — Plugin 选型决策树

> [二级路由 `_INDEX.md`](../../07-agent-design/wshobson-agents-INDEX.md) 的"为什么这么选"补充。81 个 plugin 不要硬记，按决策树走。

---

## 顶层决策

```
任务是 …？
├── 写新功能 / 重构        → §A 开发任务
├── 找 bug / 救火          → §B 调试与事故
├── 评审 / 守门             → §C 质量与治理
├── 跨多 agent 协作         → §D 编排
├── 部署 / 运维             → §E 基础设施
├── 数据 / ML / AI          → §F 数据与 AI
├── 业务 / 营销 / SEO       → §G 业务侧
└── 工具增强                 → §H 通用工具
```

---

## §A — 开发任务

| 子场景 | 首选 plugin | 配合 |
|--------|-------------|------|
| 端到端新功能 | `full-stack-orchestration` | `conductor`（context-driven） |
| 写 backend API | `backend-development` | `api-scaffolding`, `database-design` |
| 前端 / 移动 | `frontend-mobile-development` | `multi-platform-apps`, `ui-design` |
| TDD 严格流程 | `tdd-workflows` | `unit-testing`, `comprehensive-review` |
| 旧代码重构 | `code-refactoring` | `framework-migration`, `codebase-cleanup` |
| 特定语言 | `python-development` / `javascript-typescript` / `jvm-languages` / `systems-programming` / `functional-programming` / `julia-development` / `dotnet-contribution` / `shell-scripting` / `arm-cortex-microcontrollers` / `web-scripting` | — |

## §B — 调试与事故

| 子场景 | 首选 plugin |
|--------|-------------|
| 复杂本地 bug | `debugging-toolkit` |
| 分布式系统问题 | `distributed-debugging` |
| 错误类型分类 | `error-diagnostics`, `error-debugging` |
| 生产事故响应 | `incident-response` |
| 性能瓶颈 | `application-performance` + `performance-testing-review` |
| 数据库 / 云成本 | `database-cloud-optimization` |

## §C — 质量与治理

| 子场景 | 首选 plugin | 备注 |
|--------|-------------|------|
| 多视角代码评审 | `comprehensive-review` | 推荐默认入口 |
| 代码扫描 SAST | `security-scanning` | 配 `security-compliance` |
| Backend API 安全 | `backend-api-security` | |
| 前端/移动安全 | `frontend-mobile-security` | |
| MCP server 安全 | `protect-mcp` | Cedar policy + Ed25519 |
| 审计 trail | `signed-audit-trails` | 配 `block-no-verify` 防绕过 |
| Plugin 质量评估 | `plugin-eval` | |
| Agent governance review | `review-agent-governance` | 参考 [agent-governance-toolkit](../../09-agent-infra-catalog/governance-guardrails/agent-governance-toolkit/) |

## §D — 编排（⚠️ 注意实验性依赖）

| 子场景 | 首选 plugin | 注意 |
|--------|-------------|------|
| 多 agent 协作（单 session） | `agent-teams` | ⚠️ 需启用 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`，见 [experimental-apis.md](experimental-apis.md) |
| Agent 间编排 | `agent-orchestration` | — |
| Context 管理 | `context-management` | 配 [token-optimizer](../../08-infrastructure/context-window/token-optimizer/) |
| 团队协同 | `team-collaboration` | |

更复杂的拓扑（DAG、9 阶段、Hub-and-Spoke）→ 用 07 顶层的 agent pattern，不在 wshobson 范围。

## §E — 基础设施

| 子场景 | 首选 plugin |
|--------|-------------|
| K8s | `kubernetes-operations` |
| 部署策略 | `deployment-strategies` |
| 部署校验 | `deployment-validation` |
| 多云 | `cloud-infrastructure` |
| CI/CD | `cicd-automation` |
| 可观测 | `observability-monitoring` |
| 数据库设计 | `database-design`, `database-migrations` |
| 依赖管理 | `dependency-management` |

## §F — 数据与 AI

| 子场景 | 首选 plugin |
|--------|-------------|
| ETL / pipeline | `data-engineering` |
| 数据质量 | `data-validation-suite` |
| MLOps | `machine-learning-ops` |
| LLM 应用 | `llm-application-dev` |
| 量化交易 | `quantitative-trading` |
| 区块链 | `blockchain-web3` |

## §G — 业务侧

| 子场景 | 首选 plugin |
|--------|-------------|
| SEO 内容 | `seo-content-creation` |
| SEO 技术 | `seo-technical-optimization` |
| SEO 分析 | `seo-analysis-monitoring` |
| 内容营销 | `content-marketing` |
| 业务分析 | `business-analytics` |
| HR/法务 | `hr-legal-compliance` |
| 客户/销售 | `customer-sales-automation` |
| 初创业务 | `startup-business-analyst` |
| 品牌落地页 | `brand-landingpage` |
| 支付集成 | `payment-processing` |
| 游戏开发 | `game-development` |
| 可访问性 | `accessibility-compliance` |

## §H — 通用工具

| 子场景 | 首选 plugin |
|--------|-------------|
| 文档生成 | `documentation-generation`, `documentation-standards` |
| 代码文档 | `code-documentation` |
| C4 架构图 | `c4-architecture` |
| API 文档/测试 | `api-testing-observability` |
| Git/PR | `git-pr-workflows` |
| 通用助手 | `developer-essentials` |
| 逆向工程 | `reverse-engineering` |
| AI 视觉设计 | `meigen-ai-design` |

---

## 安装建议

不要 `/plugin install` 全部 81 个——按当前任务挑 3-5 个。每个 plugin 是独立 token 预算。

```bash
# 例：做一个 K8s 微服务，用 TDD
/plugin install backend-development
/plugin install tdd-workflows
/plugin install kubernetes-operations
/plugin install comprehensive-review
```

完整 plugin 索引：[../../07-agent-design/wshobson-agents-INDEX.md](../../07-agent-design/wshobson-agents-INDEX.md)。
