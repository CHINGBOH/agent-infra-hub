# 08-infrastructure — Agent 基础设施四大支柱

LLM 只是 CPU，这里是围绕它的微型 OS 的四个核心子系统：
**Hooks（中断）/ Context Window（内存）/ Tool Use & MCP（系统调用）/ Subagent Isolation（进程隔离）**

---

## 子系统导航

```
08-infrastructure/
│
├── hooks/                     中断系统 — 拦截 Agent 生命周期每个节点
│   ├── claude-code-hooks-mastery/         13 个生命周期事件完整实现
│   ├── claude-code-hooks-multi-agent-observability/  多 Agent 实时监控
│   └── claude-code-hooks/                即用 hooks 集合
│
├── context-window/            内存管理 — Token 优化与 Compaction 策略
│   └── token-optimizer/                  Ghost token 检测 + 5层压缩策略
│
├── tool-use-mcp/              系统调用层 — Tool Use 模式与 MCP 服务器
│   ├── claude-code-mcp/                  Claude Code 作为 MCP Server（agent-in-agent）
│   ├── claude-code-mcp-enhanced/         增强版 MCP：Boomerang 模式 + 任务编排
│   └── claude-code-everything/           全栈指南：MCP + hooks + tool_use + BMAD
│
└── subagent-isolation/        进程隔离 — Subagent 上下文隔离与协调
    ├── ECC/                              82k★ Agent Harness 完整系统
    └── claude-code-sub-agent-collective/ Hub-and-Spoke 上下文工程研究
```

---

## 一、Hooks — 中断系统

> 对应计算机体系中的**中断处理器**。LLM 执行到某个节点，框架暂停，把控制权交给你的脚本，你决定是否放行、修改、阻断。

### 13 个生命周期事件（完整图谱）

```
Session 层
  session_start.py      ← 会话启动，注入项目上下文、环境变量
  session_end.py        ← 会话结束，清理、总结、写日志

User 层
  user_prompt_submit.py ← 用户提交 prompt，可增强/过滤/记录

SubAgent 层
  subagent_start.py     ← 子进程启动
  subagent_stop.py      ← 子进程结束

Tool 层（最常用）
  pre_tool_use.py       ← 工具调用前 ← 唯一可以【阻断】的 hook
  post_tool_use.py      ← 工具调用后（成功）
  post_tool_use_failure.py ← 工具调用失败

Permission 层
  permission_request.py ← 权限请求时（新增 HTTP hook 支持）

Context 层
  pre_compact.py        ← Compaction 触发前（可注入保留指令）

Notification 层
  notification.py       ← 系统通知事件
  stop.py               ← Agent 停止

Setup 层
  setup.py              ← 初始化配置
```

**关键规则：只有 `pre_tool_use` 可以返回非零退出码来阻断执行**，其余 hooks 是观察者。

---

### hooks/claude-code-hooks-mastery （disler）

```
路径：hooks/claude-code-hooks-mastery/
原仓：https://github.com/disler/claude-code-hooks-mastery
特点：13 个事件全覆盖 + TTS 音频反馈 + 安全过滤 + JSON 审计日志
```

**核心实现（`.claude/hooks/`）：**

| 文件 | 功能 | 典型用途 |
|------|------|---------|
| `pre_tool_use.py` | 工具调用前拦截 | 阻断危险命令（`rm -rf`/`git push --force`） |
| `post_tool_use.py` | 工具调用后处理 | 自动运行 lint/format，验证输出 |
| `session_start.py` | 会话启动 | 注入项目规范、环境检查 |
| `pre_compact.py` | Compaction 前 | 注入"压缩时保留关键变量列表"指令 |
| `notification.py` | 通知 | TTS 语音播报当前 Agent 状态 |
| `validators/` | 校验器库 | 可复用的校验逻辑 |
| `utils/` | 工具函数 | JSON 序列化、日志工具 |

**与 survey-platform 的用途：**
```
pre_tool_use   → 阻断 LLM 生成的危险 R 命令（drop table / rm data）
post_tool_use  → Rscript 执行后自动 lint 检查
pre_compact    → 确保分析状态（已完成模块列表）在 compaction 后保留
session_start  → 注入数据库 schema，让 LLM 不会幻觉变量名
```

---

### hooks/claude-code-hooks-multi-agent-observability （disler）

```
路径：hooks/claude-code-hooks-multi-agent-observability/
原仓：https://github.com/disler/claude-code-hooks-multi-agent-observability
特点：通过 hooks 实现多 Agent 实时追踪，零侵入
```

**设计思路：** 每个 subagent 的 `subagent_start/stop` hook 向中央日志服务推送事件 → 主进程通过监控面板看到所有子进程状态，无需修改 Agent 代码。

---

### hooks/claude-code-hooks （karanb192）

```
路径：hooks/claude-code-hooks/
原仓：https://github.com/karanb192/claude-code-hooks
特点：开箱即用的 hook 脚本集合，复制粘贴即可用
```

**hook-scripts 分类：**
```
pre-tool-use/   → 安全检查（危险命令过滤）
post-tool-use/  → 格式化（Prettier/Black 自动跑）
notification/   → 桌面通知、Slack 推送
utils/          → 共享工具函数
```

---

## 二、Context Window — 内存管理

> 对应计算机体系中的**内存管理单元（MMU）**。Context Window 是 LLM 的工作内存，满了会触发 Compaction（类似内存换页），管理不当会导致关键信息丢失或 token 爆炸。

### Claude Code 的 5 层 Compaction 流水线

```
每次 API 调用前，按序执行（最便宜优先）：

1. Budget Reduction   → 裁剪超预算内容
2. Snip              → 删除低价值片段
3. Microcompact      → 微压缩：压缩重复内容
4. Context Collapse  → 折叠：将多轮对话合并为摘要
5. Auto-Compact      → 兜底：LLM 生成全局摘要
```

**成本参考：** cache read=10%, cache write=125%，默认 TTL=5 分钟  
**缓冲区：** 约 33K-45K tokens 为安全工作区

---

### context-window/token-optimizer （alexgreensh）

```
路径：context-window/token-optimizer/
原仓：https://github.com/alexgreensh/token-optimizer
特点：7信号质量评分 + Ghost Token 检测 + Delta Mode（~97% 节省）
```

**Ghost Token 概念（核心）：**
```
Ghost Token = 占用 context 空间但对当前任务无价值的 token

两类来源：
  Runtime 浪费（15-25%）：冗长命令输出、verbose 日志
  Structural 浪费（75-85%）：臃肿的 CLAUDE.md、unused skills、
                             重复 system reminder、stale MEMORY.md、
                             死掉的 MCP server
```

**7 信号质量评分系统：**
```
评分维度：context 利用率 / ghost token 比例 / compaction 健康度
         / skill 加载效率 / tool 调用成功率 / 重复内容 / 结构浪费
→ 输出字母评级（A/B/C/D/F），诊断当前 session 健康状态
```

**关键文件：**
```
skills/token-dashboard/  ← 可视化 token 使用 skill
hooks/                   ← token 监控 hook
commands/                ← 诊断命令
docs/                    ← Ghost Token 原理文档
```

**与 survey-platform 用途：**  
`pre_compact` hook + token-optimizer → 确保分析状态在 compaction 时不丢失

---

## 三、Tool Use & MCP — 系统调用层

> 对应计算机体系中的**系统调用接口（syscall）**。LLM 无法直接触碰外部世界，tool_use 是它唯一的系统调用方式。MCP 是标准化的工具协议层。

### Tool Use 调用流程

```
LLM 生成 tool_use 块
  └→ 框架路由（匹配工具名）
       ├→ 内置工具（Bash/Read/Write/Edit）→ 直接执行
       └→ MCP 工具 → JSON-RPC → MCP Server → 外部服务

框架把执行结果作为 tool_result 注回 context
LLM 看到结果，继续生成
```

---

### tool-use-mcp/claude-code-mcp （steipete）

```
路径：tool-use-mcp/claude-code-mcp/
原仓：https://github.com/steipete/claude-code-mcp
模式：Claude Code as MCP Server（agent-in-agent）
```

**核心设计：把整个 Claude Code 包装成一个 MCP 工具**

```
外部 LLM（Cursor/其他 Claude）
  └→ 调用 MCP tool: claude_code(prompt="重构这个函数")
       └→ 启动 Claude Code CLI（--dangerously-skip-permissions）
            └→ Claude Code 在隔离环境跑完任务
                 └→ 返回结果给外部 LLM
```

**意义：** 任何支持 MCP 的 LLM 都能把 Claude Code 当一个强力工具调用，实现真正的"agent 套 agent"递归结构。

---

### tool-use-mcp/claude-code-mcp-enhanced （grahama1970）

```
路径：tool-use-mcp/claude-code-mcp-enhanced/
原仓：https://github.com/grahama1970/claude-code-mcp-enhanced
特点：Boomerang 模式 + 任务编排 + 可靠性增强
```

**Boomerang 模式（核心创新）：**
```
复杂任务 → 拆分为 Markdown 子任务列表
         → 每个子任务作为独立 MCP 调用执行
         → 结果收集回主流程（像回旋镖一样飞出去再飞回来）

对比直接调用：避免单次调用 token 爆炸，每个子任务独立 context
```

**关键文件：**
```
claude-code-orchestrator.md ← Boomerang 编排模式文档
ENHANCEMENTS.md             ← 相比原版的改进点
QUICKSTART.md               ← 快速集成指南
src/                        ← TypeScript 实现
```

---

### tool-use-mcp/claude-code-everything （wesammustafa）

```
路径：tool-use-mcp/claude-code-everything/
原仓：https://github.com/wesammustafa/Claude-Code-Everything-You-Need-to-Know
特点：最全的 Claude Code 实战手册，MCP + hooks + tool_use + BMAD 全覆盖
```

**`.claude/` 目录（直接可用）：**
```
.claude/
├── agents/    ← Agent 定义（带 tools 字段）
├── commands/  ← slash commands
├── hooks/     ← hook 脚本
└── settings.json ← 权限配置
```

**BMAD 方法**（Breakthrough Multi-Agent Development）：结构化 multi-agent 开发流程，贯穿整个文档。

---

## 四、Subagent Isolation — 进程隔离

> 对应计算机体系中的**进程隔离与 IPC**。每个 subagent 是独立进程，有自己的 context 空间，通过"摘要返回"与主进程通信（类似 IPC），防止上下文污染。

### Subagent 隔离原则

```
主 Claude                    Subagent Claude
─────────────────────────────────────────────
完整对话历史                  只有自己的 prompt
所有 skills 加载              只有被赋予的工具
看不到 subagent 内部          只返回最终摘要
多个 subagent 互不知晓        完全上下文隔离

→ "Summary-only return" 是防止 context blow-up 的关键设计
```

---

### subagent-isolation/ECC （affaan-m）⭐ 82k Stars

```
路径：subagent-isolation/ECC/
原仓：https://github.com/affaan-m/everything-claude-code
规模：82k★ 10k+ forks，10+ 个月生产验证，支持 Claude/Codex/Cursor/Gemini
定位：Agent Harness 性能优化系统
```

**NanoClaw v2（内置编排引擎）：**
```
model routing    → 按任务类型路由到最合适的模型
skill hot-loading → 按需加载 skill，不全量注入（最小上下文原则）
session mgmt     → branching / searching / exporting / compacting / metrics
```

**关键目录（survey-platform 最相关）：**

| 目录 | 内容 | 用途 |
|------|------|------|
| `skills/agentic-os/` | Agent OS 抽象层 skill | 围绕 LLM 的微型 OS 设计 |
| `skills/agentic-engineering/` | Agent 工程实践 | pipeline 设计规范 |
| `skills/agent-harness-construction/` | Harness 构建指南 | **直接指导 app/agent.py 设计** |
| `skills/agent-introspection-debugging/` | Agent 自省调试 | 排查 LLM 幻觉 |
| `skills/agent-eval/` | Agent 评估框架 | 量化分析质量 |
| `hooks/hooks.json` | hooks 配置 | 完整 hooks 配置示例 |
| `hooks/memory-persistence/` | 记忆持久化 hook | 跨 session 保存关键信息 |
| `mcp-configs/` | MCP 配置集合 | 各种 MCP server 配置模板 |
| `agents/` | Agent 定义集合 | 可直接引用的 agent 角色 |
| `docs/` | 完整文档 | 含中文版 README |
| `the-longform-guide.md` | 长文指南 | 深度原理解析 |
| `the-security-guide.md` | 安全指南 | Agent 安全设计 |
| `SOUL.md` | 设计哲学 | Agent Harness 核心理念 |

**安装：**
```bash
npx ecc install        # 标准安装
npx ecc consult        # 咨询模式
```

---

### subagent-isolation/claude-code-sub-agent-collective （vanzan01）

```
路径：subagent-isolation/claude-code-sub-agent-collective/
原仓：https://github.com/vanzan01/claude-code-sub-agent-collective
特点：Hub-and-Spoke 上下文工程研究，30+ agent，TDD 强制执行
```

**Hub-and-Spoke 架构：**
```
                  ┌─────────────────┐
  所有请求         │  Hub（中央路由）  │  统一入口，避免 agent 自选路由
  ───────────────→│  task-orchestrator│  集中质量控制
                  └────────┬────────┘
                           │ 按任务类型路由
         ┌─────────────────┼─────────────────┐
         ↓                 ↓                 ↓
    Spoke-A             Spoke-B           Spoke-C
  (测试专家)           (实现专家)         (文档专家)
```

**关键文件：**
```
USER-GUIDE.md      ← 使用指南
CLAUDE.md          ← Hub agent 的行为定义
templates/         ← Spoke agent 模板
lib/               ← 路由逻辑实现
docs/              ← 上下文工程研究文档
```

---

## 四大支柱与 survey-platform 的完整映射

```
基础设施组件              survey-platform 对应位置
──────────────────────────────────────────────────────────────────

Hooks（中断）
  pre_tool_use          → 阻断危险 Rscript 命令（drop/rm）
  post_tool_use         → 执行后自动 lint，写 log
  pre_compact           → 注入"保留已完成模块列表"指令
  session_start         → 注入 SQLite schema 防变量名幻觉
  subagent_stop         → 子 Agent 完成后触发下一步

Context Window（内存）
  5层 compaction        → agent.py 需要感知 token 用量
  Ghost Token 检测      → CLAUDE.md 精简，unused skills 清除
  pre_compact hook      → 关键分析状态在压缩后存活
  token-optimizer skill → 实时监控 session 健康度

Tool Use & MCP（系统调用）
  tool_use 主循环       → app/tools.py 的 10 个工具函数
  MCP boomerang 模式    → 复杂分析任务拆成子调用
  agent-in-agent        → R 分析作为 MCP server 被主 Agent 调用
  .claude/settings.json → 工具权限配置

Subagent Isolation（进程隔离）
  summary-only return   → 分析 Agent 只返回结果摘要给主 Agent
  hub-and-spoke         → 主 Agent 作为 hub，数据/分析/报告 Agent 作为 spoke
  ECC/agent-harness     → app/agent.py 的架构参考
  NanoClaw hot-loading  → 按需加载 skill，不全量注入
```

---

## 推荐阅读顺序

```
理解原理（1小时）：
  1. hooks/claude-code-hooks-mastery/.claude/hooks/ 的实现（直接读代码）
  2. context-window/token-optimizer/docs/（Ghost Token 原理）
  3. subagent-isolation/ECC/SOUL.md（设计哲学）
  4. subagent-isolation/ECC/the-longform-guide.md（深度原理）

动手实践：
  5. hooks/claude-code-hooks/hook-scripts/（即用脚本）
  6. tool-use-mcp/claude-code-mcp-enhanced/QUICKSTART.md（MCP 集成）
  7. subagent-isolation/ECC/skills/agent-harness-construction/（Harness 构建）
```

---

*最后更新：2026-05-22*
