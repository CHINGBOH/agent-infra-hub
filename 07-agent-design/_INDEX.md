# 07-agent-design — Agent 架构模式索引

> 多 Agent 协作设计模式全集。从这里选择适合你场景的架构模板。

---

## 模式选型速查

| 我需要… | 选这个 | 关键特性 |
|---------|--------|---------|
| 有依赖关系的多步骤任务 | **claude-swarm** | DAG 任务调度 |
| 20-50 个 agent 大规模并行 | **agent-farm** | 锁协调，分布式 |
| 高质量输出，需要评审门控 | **metaswarm** | 9阶段工作流 |
| 代码团队模拟（lead/实现/review） | **wshobson-agents** | 三角色分工 |
| 并行改代码但不冲突 | **ccswarm** | git worktree 隔离 |
| CI/PR 自动化流水线 | **agent-orchestrator** | PR审查+修复循环 |
| 企业级安全+知识检索 | **ruflo** | Swarm+RAG+安全 |
| 子任务需要严格隔离 | **ECC / sub-agent-collective** | Hub-and-Spoke |
| 了解所有模式后再选 | **ultimate-guide** | 20+ 模式参考 |
| 深入理解 Claude Code 内部 | **Dive-into-Claude-Code** | 学术级逆向分析 |

---

## 一、DAG 任务依赖模式

### claude-swarm

```
路径: claude-swarm/
来源: affaan-m
核心: 有向无环图（DAG）任务调度
```

**适用场景：** 任务之间有明确依赖关系，需要按依赖顺序并发执行。

**关键机制：**
- 将任务定义为 DAG 节点
- 自动解析依赖，并发执行无依赖任务
- 依赖满足后触发下游任务

---

## 二、大规模并行 Swarm

### agent-farm

```
路径: agent-farm/
来源: Dicklesworthstone
核心: 20-50 并行 agent + 分布式锁协调
```

**适用场景：** 大量独立子任务需要同时处理，如批量文件处理、大规模代码生成。

**关键机制：**
- Agent Pool 动态调度
- 分布式锁防止资源竞争
- 任务队列 + 结果聚合

---

## 三、分阶段质量门控

### metaswarm

```
路径: metaswarm/
来源: dsifry
核心: 9阶段工作流 + 质量评估门控
```

**适用场景：** 对输出质量要求高，需要多轮评审和迭代改进。

**9个阶段：** 规划 → 研究 → 设计 → 实现 → 测试 → 审查 → 优化 → 文档 → 交付

**关键机制：**
- 每个阶段有明确的输入/输出定义
- 评估 Agent 在关键节点进行质量门控
- 未通过则反馈给上一阶段重做

---

## 四、团队角色分工

### wshobson-agents

```
路径: wshobson-agents/
来源: wshobson
核心: Lead / Implementation / Review 三角色
```

**适用场景：** 模拟真实开发团队，有明确职责分工。

**角色定义：**
- **Lead Agent** — 任务分解，工作分配，结果整合
- **Implementation Agent** — 执行具体编码任务
- **Review Agent** — 代码审查，质量保证

**规模：** 81 个插件，适合复杂项目

---

## 五、Git Worktree 隔离

### ccswarm

```
路径: ccswarm/
来源: nwiizo (Go 实现)
核心: 每个 Agent 独立 git worktree
```

**适用场景：** 多个 Agent 需要同时修改不同代码文件，避免冲突。

**关键机制：**
- 为每个 Agent 创建独立的 git worktree
- Agent 在自己的 worktree 中工作，互不干扰
- 完成后通过 merge 整合

---

## 六、CI/PR 自动化

### agent-orchestrator

```
路径: agent-orchestrator/
来源: ComposioHQ
核心: PR评审 + 自动修复循环
```

**适用场景：** DevOps 自动化，代码提交后自动审查和修复。

**关键机制：**
- 监听 PR 事件
- 自动运行审查 Agent
- 发现问题 → 触发修复 Agent → 验证 → 重新审查

---

## 七、企业级 RAG + Swarm

### ruflo

```
路径: ruflo/
来源: ruvnet
核心: Swarm + 向量检索 + 企业安全
```

**适用场景：** 知识密集型企业任务，需要检索内部知识库并协作处理。

**关键机制：**
- Swarm 协调多 Agent 协作
- RAG 提供背景知识
- 企业级权限和安全控制

---

## 八、Hub-and-Spoke 进程隔离

### ECC (Engineering Command Center)

```
路径: ../08-infrastructure/subagent-isolation/ECC/
来源: affaan-m
规模: 82k GitHub Stars
核心: 完整 Agent Harness 系统
```

**适用场景：** 需要强隔离的子任务，安全敏感场景。

### claude-code-sub-agent-collective

```
路径: ../08-infrastructure/subagent-isolation/claude-code-sub-agent-collective/
来源: vanzan01
核心: Hub-and-Spoke 上下文隔离
```

**关键机制：**
- 中心 Hub Agent 负责协调和状态管理
- 每个子 Agent 只接收必要的上下文
- 结果汇总到 Hub

---

## 九、参考资料

### Dive-into-Claude-Code（学术级分析）

```
路径: Dive-into-Claude-Code/
来源: VILA-Lab
```

学术论文级别的 Claude Code 内部架构逆向分析。包含：
- Agent 执行模型
- Tool use 机制
- 上下文管理策略
- 性能特性

适合深入理解平台能力后做架构设计决策。

---

### ultimate-guide（20+ 模式速查）

```
路径: ultimate-guide/
来源: FlorianBruniaux
```

所有已知的 Claude Code workflow 模式分类索引。包括：
- Sequential 顺序模式
- Parallel 并行模式
- Conditional 条件分支
- Loop 循环迭代
- Hierarchical 层级委派
- ...共 20+ 种模式

**使用方式：** 模式选型时先读此文档，然后找对应的实现仓库。

---

## 模式组合示例

```
数据工程 Pipeline:
  dag (claude-swarm) + worktree_isolation (ccswarm)

代码开发团队:
  team_roles (wshobson-agents) + quality_gate (metaswarm)

知识库问答系统:
  hub_spoke (sub-agent-collective) + rag (ruflo)

大规模文件处理:
  parallel_swarm (agent-farm) + isolation (ECC)
```
