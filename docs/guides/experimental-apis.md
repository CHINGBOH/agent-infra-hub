# Experimental APIs — 实验性 Claude Code 依赖处理

> 在 [MANIFEST §Experimental APIs](../../MANIFEST.md#experimental-apis) 之上的展开版。详述每一个实验性 flag 的引入风险、替代方案与回退策略。

---

## 实验性 API 清单

### `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`

| 项 | 内容 |
|----|------|
| 状态 | Research preview，无稳定文档 |
| 暴露的工具 | `TeamCreate`、`SendMessage` |
| 启用方式 | `.claude/settings.json` 的 `env` 字段，或 shell rc 导出 |
| 影响范围 | 见下表 |

**仓库内引用此 flag 的位置：**

| 文件 | 用途 |
|------|------|
| [07-agent-design/wshobson-agents/plugins/agent-teams/](../../07-agent-design/wshobson-agents/plugins/agent-teams/) | plugin 直接依赖 |
| [08-infrastructure/hooks/claude-code-hooks-multi-agent-observability/README.md](../../08-infrastructure/hooks/claude-code-hooks-multi-agent-observability/README.md) | 监控 hook 配 agent teams |
| [08-infrastructure/subagent-isolation/ECC/docs/token-optimization.md](../../08-infrastructure/subagent-isolation/ECC/docs/token-optimization.md) | token 优化与 agent teams 联动 |
| [04-research/academic-research-skills/docs/PERFORMANCE.md](../../04-research/academic-research-skills/docs/PERFORMANCE.md) | 性能调优文档（同时强调"内部并行不需要此 flag"） |
| [07-agent-design/ruflo/docs/USERGUIDE.md](../../07-agent-design/ruflo/docs/USERGUIDE.md) | 企业 swarm + agent teams |

**判断准则：**

| 你的需求 | 是否需要启用 |
|----------|--------------|
| 单 session 内并行 spawn subagent | ❌ 不需要——内置 `Agent` tool 已支持 |
| 跨 session 持久的 manual team coordination | ✅ 需要 |
| 学术研究的 ARS（academic-research-skills）流水线 | ❌ 不需要——其 README 明确说明 |
| wshobson `agent-teams` plugin | ✅ 需要 |

**回退策略：**

如果实验性 API 在未来版本被移除或改签名，受影响 plugin/文档需要：

1. `agent-teams` plugin：fall back 到 `agent-orchestration`（标准 API）
2. 监控 hook：移除 `TeamCreate` 触发器，改用 `Stop` hook
3. ECC token 优化：保留方法论部分，移除 flag 引用

---

## 引入新实验性依赖的流程

1. **评估替代方案** — 仓库已有的稳定方式能否实现？
2. **隔离影响面** — 把依赖关进一个独立目录/plugin，不要散落到核心导航。
3. **同步标注** — 在以下位置都加引用：
   - `MANIFEST.md` `## Experimental APIs` 表格加行
   - 使用该 flag 的每个文档顶部加 ⚠️ 提示并链回 `#experimental-apis`
   - [reference/manifest-structure.md](../reference/manifest-structure.md) 的「实验性 APIs」表
4. **写回退** — 在引入文档里明确：API 被废弃后怎么办。

---

## MCP `code-review-graph` server

| 项 | 内容 |
|----|------|
| 状态 | 🟡 本地工具，未发布 npm/PyPI 包 |
| 启用方式 | 用户需自行启动本地 MCP server |
| 影响范围 | [MANIFEST §Knowledge Graphs](../../MANIFEST.md#knowledge-graphs) 全部查询都依赖 |

**用法示例：**

```python
mcp__code-review-graph__semantic_search_nodes_tool(
    query="extractor plugin",
    repo_root="/home/l/projects/03_third-party-sources/yt-dlp",
)
```

**回退：** server 不可用时，agent 可直接读取 `repo_root` 下的源码——会更慢但仍能完成任务。

---

## 监控指标

`make docs-links` 会扫所有标注 ⚠️ 的文档；future 改进可：

- 自动扫 `CLAUDE_CODE_EXPERIMENTAL_*` 字符串出现位置，与本文清单对照，发现新增引用时报告。
- 在 `tools/docs_gen.py` 加 `experimental` task。
