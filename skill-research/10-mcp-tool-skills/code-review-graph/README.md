# code-review-graph

**分类：MCP Tool 型 Skill（Category B）**  
**子类：知识图谱 / 代码结构分析**  
**版本：2.3.3（本机已安装）**  
**来源：https://github.com/tirth8205/code-review-graph**

---

## 核心思想

传统做法：AI 每次任务都重新读整个代码库。  
code-review-graph：用 Tree-sitter 预先解析所有代码，建立结构图，只把**必要的上下文**通过 MCP 传给 AI。

实测 token 减少 **4.9× ～ 27.3×**，同时提升代码审查质量。

---

## 本机安装状态

```
版本：2.3.3
安装路径：/home/l/miniconda3/bin/code-review-graph
MCP 配置：~/.mcp.json（cwd=/home/l，覆盖所有子项目）
agent-infra-hub 图状态：
  Nodes: 53 | Edges: 495 | Files: 1
  Languages: python
  Built: 2026-05-23T01:36:08
  Branch: master @ 9db9d94
```

---

## MCP 注册配置（~/.mcp.json）

```json
{
  "mcpServers": {
    "code-review-graph": {
      "command": "uvx",
      "args": ["code-review-graph", "serve"],
      "cwd": "/home/l",
      "type": "stdio"
    }
  }
}
```

`cwd=/home/l` 意味着该 MCP server 覆盖 home 下所有 git 仓库。

---

## 安装方法（复现）

```bash
# 基础安装
pip install code-review-graph

# 可选扩展
pip install code-review-graph[embeddings]    # 本地向量嵌入
pip install code-review-graph[communities]   # 社区检测
pip install code-review-graph[all]           # 全部

# 自动检测并配置所有 AI 工具（Claude Code、Cursor、Codex 等）
code-review-graph install

# 或手动注册到 Claude Code
code-review-graph install --platform claude-code

# 构建当前仓库的图
code-review-graph build

# 增量更新（仅解析变更文件，<2秒）
code-review-graph update
```

---

## 28 个 MCP 工具完整列表

Claude Code 中工具名前缀：`mcp__code-review-graph__`

### 核心查询工具

| 工具 | 作用 |
|------|------|
| `get_minimal_context_tool` | 极简上下文（~100 tokens），任务开始的第一个调用 |
| `get_impact_radius_tool` | 某次变更影响哪些文件/函数 |
| `get_review_context_tool` | Token 优化的代码审查上下文 |
| `query_graph_tool` | 查询调用者/被调用者/测试/导入/继承关系 |
| `traverse_graph_tool` | BFS/DFS 图遍历（带 token 预算控制） |
| `get_flow_tool` | 获取完整执行流程 |
| `list_flows_tool` | 列出所有已识别的执行流 |

### 分析工具

| 工具 | 作用 |
|------|------|
| `list_communities_tool` | 检测到的代码社区（功能模块划分） |
| `get_community_tool` | 获取特定社区详情 |
| `get_hub_nodes_tool` | 最高连接度的架构热点节点 |
| `get_bridge_nodes_tool` | 架构瓶颈（跨社区的桥接节点） |
| `get_knowledge_gaps_tool` | 结构弱点和未测试热点 |
| `get_surprising_connections_tool` | 意外的跨社区耦合 |
| `get_suggested_questions_tool` | 自动生成代码审查问题 |
| `get_architecture_overview_tool` | 基于社区的架构概览图 |

### 搜索与嵌入

| 工具 | 作用 |
|------|------|
| `semantic_search_nodes_tool` | 按名称或语义搜索实体 |
| `embed_graph_tool` | 为语义搜索生成向量嵌入 |
| `cross_repo_search_tool` | 跨仓库搜索 |

### 变更分析

| 工具 | 作用 |
|------|------|
| `detect_changes_tool` | 风险评分的变更影响分析 |
| `get_affected_flows_tool` | 哪些执行路径受到影响 |
| `get_review_context_tool` | 获取代码审查所需源码片段 |

### 重构工具

| 工具 | 作用 |
|------|------|
| `refactor_tool` | 重命名预览、死代码检测 |
| `apply_refactor_tool` | 应用重构操作 |
| `find_large_functions_tool` | 找出过大的函数 |

### 文档生成

| 工具 | 作用 |
|------|------|
| `generate_wiki_tool` | 从社区结构生成 Markdown wiki |
| `get_wiki_page_tool` | 获取 wiki 特定页面 |
| `get_docs_section_tool` | 获取文档特定章节 |

### 图管理

| 工具 | 作用 |
|------|------|
| `build_or_update_graph_tool` | 构建或增量更新图 |
| `list_graph_stats_tool` | 图统计信息 |
| `list_repos_tool` | 列出所有已索引的仓库 |
| `run_postprocess_tool` | 运行后处理（流分析、社区检测） |

---

## 5 个内置工作流（MCP Prompts）

| 工作流 | 用途 |
|--------|------|
| `review_changes` | 针对性代码审查 |
| `architecture_map` | 系统架构分析 |
| `debug_issue` | 根因调查 |
| `onboard_developer` | 开发者入职指南 |
| `pre_merge_check` | 合并前就绪验证 |

---

## CLI 命令速查

| 命令 | 用途 |
|------|------|
| `code-review-graph build` | 全量解析当前代码库 |
| `code-review-graph update` | 增量更新（仅变更文件） |
| `code-review-graph watch` | 监听文件变化自动更新 |
| `code-review-graph visualize` | 生成交互式 HTML 图 |
| `code-review-graph detect-changes` | 风险评分变更分析 |
| `code-review-graph wiki` | 从社区生成 Markdown wiki |
| `code-review-graph status` | 查看图状态 |
| `code-review-graph serve` | 启动 MCP server（由 Claude Code 自动调用） |

---

## 排除规则（.code-review-graphignore）

在仓库根目录创建此文件排除不需要索引的路径：

```
generated/**
*.generated.ts
vendor/**
node_modules/**
```

Git 仓库会自动跳过 `.gitignore` 中的文件。

---

## 与 SKILL.md 型 Skill 的关键区别

| 维度 | SKILL.md 型 | code-review-graph（MCP Tool 型） |
|------|-------------|----------------------------------|
| 存储形式 | Markdown 文本 | SQLite 图数据库（持久） |
| 激活方式 | Claude 读 description 判断 | 工具始终可用，Claude 按需调用 |
| Context 消耗 | 加载时消耗 Context | 工具调用结果按需返回，不预占 |
| 跨会话保留 | 否（每次重新加载） | 是（图数据库持久化） |
| 语言感知 | 否（纯文本指导） | 是（Tree-sitter 语法解析） |
| 支持语言 | 不限 | 23种语言 + Jupyter notebook |
| 安装成本 | 零（放 SKILL.md 即可） | pip install + 首次 build（~分钟级） |
| 更新方式 | 修改文件 | code-review-graph update（<2秒） |

---

## 在 CLAUDE.md 中的配置（已生效）

当前项目的 CLAUDE.md 已包含以下指令：

```markdown
## MCP Tools: code-review-graph

**IMPORTANT: This project has a knowledge graph. ALWAYS use the
code-review-graph MCP tools BEFORE using Grep/Glob/Read to explore
the codebase.**

### When to use graph tools FIRST
- Exploring code: semantic_search_nodes or query_graph instead of Grep
- Understanding impact: get_impact_radius instead of manually tracing imports
- Code review: detect_changes + get_review_context instead of reading entire files
- Finding relationships: query_graph with callers_of/callees_of/imports_of/tests_for
- Architecture questions: get_architecture_overview + list_communities
```

---

## 最佳实践（CLAUDE.md 规定的工作流）

```
任何代码探索任务：
1. 先 get_minimal_context(task="<你的任务>") — 定向获取上下文
2. 使用 detail_level="minimal" — 只在 minimal 不足时升级到 standard
3. 目标：任何 review/debug/refactor 任务 ≤5次工具调用，≤800 token 输出
```

---

## 支持的 23 种语言

Python, TypeScript, JavaScript, Go, Rust, Java, C, C++, C#, Ruby, PHP,
Swift, Kotlin, Scala, R, Bash, PowerShell, Nix, SQL, Perl, Objective-C,
TSX, + Jupyter/Databricks notebooks (.ipynb)
