# 07-agent-design — Agent 架构设计参考库

9 个仓库，覆盖从学术论文到生产框架的完整 Agent 设计知识谱系。

**总计 ~190 MB | 9 个仓库**

---

## 快速选择

| 我需要… | 看这个 | 核心文件 |
|---------|--------|---------|
| 理解 Claude Code Agent 底层架构 | `Dive-into-Claude-Code` | `docs/architecture_zh.md` |
| 自己构建 Agent 的完整指南 | `Dive-into-Claude-Code` | `docs/build-your-own-agent_zh.md` |
| 多阶段工作流 + 质量门控设计 | `metaswarm` | `ORCHESTRATION.md` |
| 实战 Agent 角色分工（团队模式） | `wshobson-agents` | `plugins/agent-teams/` |
| 所有 Workflow 模式（20+）参考 | `ultimate-guide` | `guide/workflows/` |
| 20+ Agent 并行 + 锁协调 | `agent-farm` | `claude_code_agent_farm.py` |
| Git Worktree 隔离并行 | `ccswarm` | `docs/` |
| 任务依赖图 + 并行执行 | `claude-swarm` | `src/` + `examples/` |
| 自动处理 CI/PR/merge 冲突 | `agent-orchestrator` | `ARCHITECTURE.md` + `DESIGN.md` |
| 企业级 Swarm + RAG 集成 | `ruflo` | `docs/` |

---

## 目录

```
07-agent-design/
│
├── Dive-into-Claude-Code/   ★ 架构圣经 — 学术级逆向分析
├── metaswarm/               ★ 工程标杆 — 9 阶段工作流 + 质量门控
├── wshobson-agents/         ★ 生产模板 — 81 插件 + 4 角色团队
├── ultimate-guide/            最全文档 — 20+ 工作流模式 + 速查表
├── agent-farm/                并行极限 — 20-50 Agent 同跑
├── ccswarm/                   Rust 实现 — Worktree 隔离并行
├── claude-swarm/              依赖图并行 — Claude Agent SDK 示范
├── agent-orchestrator/        CI 自动化 — 计划→生成→修复全自动
└── ruflo/                     企业级 — Swarm + RAG + 多 LLM
```

---

## 详细说明

---

### Dive-into-Claude-Code ★ 必读

```
来源：VILA-Lab/Dive-into-Claude-Code
性质：学术论文 + 源码 (arXiv 2604.14228)
价值：逆向工程 Claude Code v2.1.88，揭示生产 Agent 真实架构
```

**最重要结论：**
```
整个系统 1.6% = AI 决策逻辑
          98.4% = 上下文管理 + 工具路由 + 错误恢复
→ Agent 的质量在于"基础设施"，不在于 prompt
```

**7 层架构（从外到内）：**
```
User Interfaces
  └→ Agent Loop (ReAct: 推理→工具→观察→循环)
       └→ Permission System (7 种模式 + ML 分类器)
            └→ Tools (MCP / plugins / skills / hooks)
                 └→ State & Persistence (append-only session)
                      └→ Execution Environment
```

**关键文件（优先读）：**
```
docs/
├── architecture_zh.md          ← 完整架构中文解析
├── build-your-own-agent_zh.md  ← 自建 Agent 实践指南（中文）
├── architecture.md             ← 英文原版
└── related-resources.md        ← 延伸阅读

paper/
└── Dive_into_Claude_Code.pdf   ← 完整论文

README_zh.md                    ← 中文 README
```

**与 survey-platform 的映射：**
```
Agent Loop → app/agent.py 的 tool_use 主循环
Permission System → Pydantic 校验 + 三道门控
Tools → app/tools.py 的 10 个工具函数
State & Persistence → Streamlit session_state
```

---

### metaswarm ★ 工程标杆

```
来源：dsifry/metaswarm
作者：Dave Sifry（Technorati/Linuxcare 创始人，前 Lyft/Reddit 高管）
性质：生产级多 Agent 框架，18 agents + 13 skills + 15 commands
```

**9 阶段工作流（完整 SDLC）：**
```
1. Research              → 深度调研需求
2. Plan                  → 生成规格文档
3. Design Review Gate    → 6 个 Agent 并行审阅（全通过才继续）
4. Work Unit Decomp.     → 拆分为可并行工作单元
5. Orchestrated Execution→ 每单元：IMPLEMENT→VALIDATE→ADVERSARIAL REVIEW→COMMIT
6. Final Review          → 跨单元整体审查
7. PR Creation           → 自动生成 PR
8. PR Shepherd           → 跟踪 CI/reviewer 反馈
9. Closure & Learning    → 经验写入 knowledge base
```

**质量门控设计（最值得借鉴）：**
- Design Review Gate：6 种不同视角 Agent 同时审阅，必须全部通过
- `.coverage-thresholds.json`：覆盖率低于阈值，PR 创建被阻塞
- Adversarial Review：专门的"找茬" Agent，故意挑毛病

**关键文件：**
```
ORCHESTRATION.md            ← 编排设计文档（必读）
GETTING_STARTED.md          ← 快速上手
AGENTS.md                   ← 18 个 Agent 角色定义

skills/
├── orchestrated-execution/ ← 执行循环 skill
├── design-review-gate/     ← 审阅门控 skill
├── plan-review-gate/       ← 计划审核 skill
├── brainstorming-extension/← 头脑风暴扩展
└── pr-shepherd/            ← PR 跟踪 skill

docs/
└── guides/agent-coordination.md ← Agent 协调指南
```

**与 survey-platform 的映射：**
```
metaswarm 阶段              → survey-platform 对应
Research                   → 多轮需求采集对话
Plan                       → 需求结构化 JSON (Pydantic)
Design Review Gate         → 三道校验门（模块/变量/语法）
Work Unit Decomp.          → 拆分 12 个分析模块
Orchestrated Execution     → Rscript 执行 + stderr 反馈
Final Review               → 报告数字核验 (ClaudeR)
PR Creation                → quarto render → HTML
```

---

### wshobson-agents ★ 生产模板

```
来源：wshobson/agents
规模：81 插件 + 4 Agent 团队角色 + 15 工作流编排器
设计理念：每插件只加载自己的 agents/skills，最小化 token
```

**Agent Teams 4 角色（直接可用）：**
```
plugins/agent-teams/agents/
├── team-lead.md        ← 任务分解 + 分配 + 汇总
├── team-implementer.md ← 具体实现
├── team-reviewer.md    ← 代码审查
└── team-debugger.md    ← 问题定位
```

**15 个工作流编排器（最相关）：**
```
plugins/agent-orchestration/
└── context-manager.md  ← 上下文管理

关键 plugin 目录（按本项目相关度）：
plugins/
├── agent-teams/        ★ 多 Agent 团队协调
├── agent-orchestration/★ 编排器设计
├── business-analytics/ ★ 业务分析
├── code-refactoring/     代码重构
├── comprehensive-review/ 全面审查
├── api-testing-observability/ API 测试
├── cicd-automation/      CI/CD
└── ...（共 81 个）
```

**关键文件：**
```
plugins/agent-teams/README.md      ← Agent Teams 使用说明
plugins/conductor/README.md        ← 编排器 Conductor 设计
docs/agents.md                     ← Agent 系统总文档
```

---

### ultimate-guide — 工作流模式百科

```
来源：FlorianBruniaux/claude-code-ultimate-guide
规模：41 个 Mermaid 架构图 + 186 个生产模板
```

**guide/workflows/ 下 20+ 工作流模式（精选）：**

| 文件 | 模式 | 本项目价值 |
|------|------|-----------|
| `agent-teams.md` | 多 Agent 团队协调 | 主要参考 |
| `agent-teams-quick-start.md` | Agent Teams 快速入门 | 上手参考 |
| `spec-first.md` | 规格先行开发 | 需求→规格流程 |
| `plan-driven.md` | 计划驱动开发 | 分析计划执行 |
| `tdd-with-claude.md` | Claude TDD 实践 | 代码校验机制 |
| `dual-instance-planning.md` | 双实例规划 | 需求+执行分离 |
| `exploration-workflow.md` | 探索工作流 | EDA 阶段设计 |
| `iterative-refinement.md` | 迭代精化 | 多轮报告修改 |
| `task-management.md` | 任务管理 | 管道状态机 |
| `event-driven-agents.md` | 事件驱动 Agent | hooks 设计 |

**其他重要文件：**
```
guide/cheatsheet.md              ← Claude Code 速查表
guide/core/                      ← 核心概念
guide/roles/                     ← 角色定义模板
guide/security/                  ← 安全设计
machine-readable/llms.txt        ← LLM 可直接读取的参考
machine-readable/reference.yaml  ← 结构化参考数据
```

---

### agent-farm — 大规模并行

```
来源：Dicklesworthstone/claude_code_agent_farm
特点：20-50 个 Claude Code Agent 并行运行，Python 实现
```

**核心机制：**
- **文件锁协调**：防止并行 Agent 写冲突（`fcntl` 锁）
- **tmux 会话管理**：每 Agent 独立终端窗口，实时监控
- **上下文阈值管理**：自动触发 compaction，防止上下文溢出
- **34 种技术栈支持**：自动识别项目类型

**关键文件：**
```
claude_code_agent_farm.py   ← 核心实现（单文件，阅读友好）
configs/                    ← 各技术栈配置模板
prompts/                    ← Agent 提示词库
best_practices_guides/      ← 最佳实践文档
```

**本项目借鉴点：** 文件锁设计 → 12 个 R 分析模块并行时各写独立 `.rds`，天然隔离无需锁

---

### ccswarm — Git Worktree 隔离

```
来源：nwiizo/ccswarm
实现：Rust（高性能，生产稳定）
特点：每 Agent 在独立 Git Worktree 工作，主干 merge
```

**设计核心：**
```
主仓库
  ├── worktree-agent-1/  ← Agent 1 独立工作空间
  ├── worktree-agent-2/  ← Agent 2 独立工作空间
  └── worktree-agent-N/  ← Agent N 独立工作空间
合并时通过 git merge，冲突最小化
```

**关键文件：**
```
AGENTS.md        ← Agent 角色定义
CLAUDE.md        ← Claude Code 集成配置
docs/            ← 架构文档
src/             ← Rust 实现源码（可学习设计模式）
```

---

### claude-swarm — 任务依赖图

```
来源：affaan-m/claude-swarm
特点：Claude Agent SDK 示范，依赖图 DAG 驱动并行
获奖：Claude Code Hackathon (2026-02)
```

**设计核心：**
```
Opus 4.6 分析任务 → 生成 DAG（有向无环依赖图）
                          ↓
无依赖的子任务 → 并行执行（Agent SDK）
有依赖的子任务 → 串行等待
                          ↓
文件锁 + 预算控制 + 重试机制 + 质量审查
```

**关键文件：**
```
src/             ← 核心实现（Python）
examples/        ← 使用示例
README.md        ← 设计说明（含架构图）
```

**本项目借鉴点：** 分析模块依赖关系图设计（如 reliability 先于 factor_analysis）

---

### agent-orchestrator — CI 全自动化

```
来源：ComposioHQ/agent-orchestrator
特点：Plan → Spawn Agents → 自动处理 CI 失败/merge 冲突/PR review
```

**自动响应循环：**
```
CI 失败    → 自动 fix → 重新推送
PR 被 request changes → 自动处理 → 重新请求 review
Merge 冲突 → 自动解决 → 推送
```

**关键文件：**
```
ARCHITECTURE.md              ← 架构设计文档（精炼）
DESIGN.md                    ← 设计决策文档
artifacts/architecture-design.md ← 详细架构
agent-orchestrator.yaml.example   ← 配置示例
skills/                      ← 内置 skills
```

---

### ruflo — 企业级平台

```
来源：ruvnet/ruflo
定位：生产级 Agent 编排平台，含 RAG + Swarm 智能
规模：85 MB（最大）
```

**特性：**
- 多 LLM 支持（Claude / Codex 原生集成）
- Swarm 自学习智能
- RAG 知识库集成
- 企业级权限和审计

**关键文件：**
```
docs/                ← 完整文档（含 CLAUDE_MD_Data_Science.md）
README.md            ← 平台总览
```

---

## 核心设计模式提炼

从 9 个仓库中提炼的 4 个普适模式：

### 模式 1：Orchestrator-Workers（VILA-Lab 论文验证）
```
Orchestrator Agent
  ├── 分解任务 → 工作单元列表
  ├── 分配 → Worker Agent × N（并行/串行）
  └── 汇总 → 最终输出

实现参考：metaswarm/skills/orchestrated-execution/
```

### 模式 2：多层质量门控（metaswarm）
```
需求输入 → [Pydantic 校验] → [领域专家审阅] → [执行] → [结果核验] → 输出
           ↑ 失败退回        ↑ 6 视角通过      ↑ 失败诊断  ↑ 数字核实

实现参考：metaswarm/skills/design-review-gate/
```

### 模式 3：最小上下文原则（wshobson）
```
❌ 错误：一个 Agent 加载所有工具（token 爆炸）
✓ 正确：每个 Agent 只加载自己职责范围内的工具

实现参考：wshobson-agents/plugins/ （每插件独立加载）
```

### 模式 4：并行隔离 + 锁协调（agent-farm + ccswarm）
```
方案 A（文件锁）：并行写不同文件，共享资源加锁
  → agent-farm/claude_code_agent_farm.py（fcntl）

方案 B（Worktree 隔离）：每 Agent 独立 Git Worktree
  → ccswarm（Rust 实现）

本项目天然符合 A：12 个 R 模块各写独立 .rds，无需额外锁
```

---

## 与 survey-analysis-platform 完整映射

```
平台组件                    最佳参考来源
─────────────────────────────────────────────────────────────────
app/agent.py（主循环）     ← Dive-into-Claude-Code/docs/architecture
app/agent.py（多轮对话）   ← ultimate-guide/guide/workflows/agent-teams.md
app/tools.py（工具设计）   ← Dive-into-Claude-Code/docs/build-your-own-agent
需求采集 Agent             ← wshobson-agents/plugins/agent-teams/team-lead.md
数据清洗 Agent             ← wshobson-agents/plugins/agent-teams/team-implementer.md
分析执行 Agent             ← metaswarm/agents/ + metaswarm/skills/orchestrated-execution/
报告生成 Agent             ← wshobson-agents/plugins/agent-teams/team-reviewer.md
质量门控设计               ← metaswarm/skills/design-review-gate/
并行分析模块协调           ← agent-farm/claude_code_agent_farm.py（锁机制）
任务依赖顺序               ← claude-swarm/src/（DAG 设计）
CI/管道自动恢复            ← agent-orchestrator/DESIGN.md
```

---

## 阅读路径推荐

**快速入门（2 小时）：**
```
1. Dive-into-Claude-Code/README_zh.md           （20 min）
2. ultimate-guide/guide/cheatsheet.md           （10 min）
3. ultimate-guide/guide/workflows/agent-teams.md（20 min）
4. metaswarm/GETTING_STARTED.md                 （20 min）
5. wshobson-agents/plugins/agent-teams/README.md（10 min）
```

**深度理解（半天）：**
```
6. Dive-into-Claude-Code/docs/architecture_zh.md
7. Dive-into-Claude-Code/docs/build-your-own-agent_zh.md
8. metaswarm/ORCHESTRATION.md
9. ultimate-guide/guide/workflows/spec-first.md
10. agent-farm/claude_code_agent_farm.py（源码）
```

---

## 更新仓库

```bash
# 更新单个
cd 07-agent-design/metaswarm && git pull

# 批量更新
for d in /home/l/projects/skills-hub/07-agent-design/*/; do
  echo "=== $(basename $d) ===" && cd "$d" && git pull --ff-only 2>&1 | head -1
done
```

---

*最后更新：2026-05-22*
