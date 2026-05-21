# 05-subagents — 专项 Subagent 分工

## 与 survey-analysis-platform 对应

| 平台模块 | Subagent 文件 |
|---------|--------------|
| 需求采集 agent | `categories/08-business-product/business-analyst.md` |
| 数据清洗 agent | `categories/05-data-ai/data-engineer.md` |
| 统计分析 agent | `categories/05-data-ai/data-analyst.md` |
| 高级建模 agent | `categories/05-data-ai/data-scientist.md` |
| 报告撰写 agent | `categories/10-research-analysis/data-researcher.md` |
| 管道编排 agent | `categories/09-meta-orchestration/` |

## 使用方式

```bash
# 查看 data-analyst subagent 定义
cat awesome-claude-code-subagents/categories/05-data-ai/data-analyst.md

# 批量安装到 Claude Code
cd awesome-claude-code-subagents && bash install-agents.sh

# 手动复制单个到项目
cp awesome-claude-code-subagents/categories/05-data-ai/data-analyst.md \
   ~/.claude/agents/data-analyst.md
```
