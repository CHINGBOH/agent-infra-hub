# mcp-builder

**Added by:** Anthropic  
**Trigger:** Slash command + auto  
**类型：** A型 SKILL.md Skill（四阶段工程模式）  
**License:** Complete terms in LICENSE.txt

---

## Description（触发描述）

**English:**  
Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).

**中文：**  
创建高质量 MCP（Model Context Protocol）服务器的指南，使 LLM 能够通过精心设计的工具与外部服务交互。无论是 Python（FastMCP）还是 Node/TypeScript（MCP SDK）均适用。

---

## 与 build-mcp-server 的对比

| 维度 | mcp-builder（本 skill） | build-mcp-server（插件内 skill） |
|------|------------------------|--------------------------------|
| 来源 | Anthropic Personal Skills | mcp-server-dev 插件 |
| 侧重 | 实现 + 评估（10道评估题） | 部署决策 + 框架选择 |
| 决策层 | 无（假设已确定要构建） | 有（Remote HTTP / MCPB / MCP App） |
| 评估阶段 | Phase 4（必须） | 不包含 |
| 推荐语言 | TypeScript（首选）+ Python | 两者均支持 |

---

## 核心架构：四阶段工程流程

```
Phase 1：深度研究和规划
    ├── 理解现代 MCP 设计原则
    ├── 学习 MCP 协议文档（从 sitemap.xml 开始）
    ├── 加载框架文档（TypeScript SDK / Python SDK）
    └── 规划实现（端点、认证、工具选择）

Phase 2：实现
    ├── 设置项目结构
    ├── 实现核心基础设施（API client、错误处理、分页）
    └── 实现工具（Input Schema + Output Schema + 注解）

Phase 3：审查和测试
    ├── 代码质量（DRY、类型覆盖、工具描述）
    └── 构建和测试（MCP Inspector）

Phase 4：创建评估（必须）
    ├── 工具检查
    ├── 内容探索（只读操作）
    ├── 创建 10 个评估问题
    └── 验证答案（自己解决）
```

---

## SKILL.md 完整内容

### Overview

Create MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. The quality of an MCP server is measured by how well it enables LLMs to accomplish real-world tasks.

---

### Phase 1: Deep Research and Planning

#### 1.1 Understand Modern MCP Design

- **API Coverage vs. Workflow Tools:** Balance comprehensive API endpoint coverage with specialized workflow tools. When uncertain, prioritize comprehensive API coverage.
- **Tool Naming and Discoverability:** Use consistent prefixes (e.g., `github_create_issue`, `github_list_repos`) and action-oriented naming.
- **Context Management:** Design tools that return focused, relevant data. Support filtering/pagination.
- **Actionable Error Messages:** Error messages should guide agents toward solutions with specific suggestions and next steps.

#### 1.2 Study MCP Protocol Documentation

Navigate the MCP specification:
- Start with the sitemap: `https://modelcontextprotocol.io/sitemap.xml`
- Fetch specific pages with `.md` suffix (e.g., `https://modelcontextprotocol.io/specification/draft.md`)

Key pages to review:
- Specification overview and architecture
- Transport mechanisms (streamable HTTP, stdio)
- Tool, resource, and prompt definitions

#### 1.3 Study Framework Documentation

**Recommended stack:**
- **Language:** TypeScript (high-quality SDK support, good compatibility, AI models excel at generating TypeScript)
- **Transport:** Streamable HTTP for remote servers (stateless JSON); stdio for local servers

**Load framework documentation:**
- MCP Best Practices: `references/mcp_best_practices.md`
- TypeScript SDK: `https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md` → `references/node_mcp_server.md`
- Python SDK: `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md` → `references/python_mcp_server.md`

#### 1.4 Plan Your Implementation

- **Understand the API:** Review the service's API documentation for key endpoints, authentication requirements, and data models.
- **Tool Selection:** Prioritize comprehensive API coverage. List endpoints to implement, starting with the most common operations.

---

### Phase 2: Implementation

#### 2.1 Set Up Project Structure

See language-specific guides for project setup:
- TypeScript: project structure, package.json, tsconfig.json
- Python: module organization, dependencies

#### 2.2 Implement Core Infrastructure

Create shared utilities:
- API client with authentication
- Error handling helpers
- Response formatting (JSON/Markdown)
- Pagination support

#### 2.3 Implement Tools

For each tool:

**Input Schema:**
- Use Zod (TypeScript) or Pydantic (Python)
- Include constraints and clear descriptions
- Add examples in field descriptions

**Output Schema:**
- Define `outputSchema` where possible for structured data
- Use `structuredContent` in tool responses (TypeScript SDK feature)
- Helps clients understand and process tool outputs

**Tool Description:**
- Concise summary of functionality
- Parameter descriptions
- Return type schema

**Implementation:**
- Async/await for I/O operations
- Proper error handling with actionable messages
- Support pagination where applicable
- Return both text content and structured data when using modern SDKs

**Annotations:**
- `readOnlyHint`: true/false
- `destructiveHint`: true/false
- `idempotentHint`: true/false
- `openWorldHint`: true/false

---

### Phase 3: Review and Test

#### 3.1 Code Quality

Review for:
- No duplicated code (DRY principle)
- Consistent error handling
- Full type coverage
- Clear tool descriptions

#### 3.2 Build and Test

**TypeScript:**
```bash
npm run build                           # Verify compilation
npx @modelcontextprotocol/inspector     # Test with MCP Inspector
```

**Python:**
```bash
python -m py_compile your_server.py    # Verify syntax
# Test with MCP Inspector
```

---

### Phase 4: Create Evaluations

#### 4.1 Understand Evaluation Purpose

Use evaluations to test whether LLMs can effectively use your MCP server to answer realistic, complex questions.

#### 4.2 Create 10 Evaluation Questions

Process:
1. **Tool Inspection:** List available tools and understand their capabilities
2. **Content Exploration:** Use READ-ONLY operations to explore available data
3. **Question Generation:** Create 10 complex, realistic questions
4. **Answer Verification:** Solve each question yourself to verify answers

#### 4.3 Evaluation Requirements

Ensure each question is:
- **Independent:** Not dependent on other questions
- **Read-only:** Only non-destructive operations required
- **Complex:** Requiring multiple tool calls and deep exploration
- **Realistic:** Based on real use cases humans would care about
- **Verifiable:** Single, clear answer that can be verified by string comparison
- **Stable:** Answer won't change over time

#### 4.4 Output Format

```xml
<evals>
  <eval>
    <question>Find discussions about AI model launches with animal codenames. One model needed a specific safety designation that uses the format ASL-X. What number X was being determined for the model named after a spotted wild cat?</question>
    <answer>3</answer>
  </eval>
</evals>
```

---

## 参考文件库

| 文件 | 加载时机 |
|------|---------|
| `references/mcp_best_practices.md` | Phase 1 首先加载 |
| `references/node_mcp_server.md` | Phase 1/2（TypeScript 实现指南） |
| `references/python_mcp_server.md` | Phase 1/2（Python 实现指南） |
| `references/evaluation.md` | Phase 4（评估指南） |

---

## 研究笔记

**评估阶段的必要性：** Phase 4 要求创建 10 道评估题并亲自验证答案，这是确保 MCP server 真正可用的质量保证机制。这个要求与 skill-creator 的评估理念一脉相承。

**outputSchema 的新特性：** 该 skill 提到了 `outputSchema` 和 `structuredContent`——这是 TypeScript SDK 的相对新功能，表示 Anthropic 在持续关注 MCP 协议的演进。

**与 build-mcp-server 插件的关系：** 两者互补，build-mcp-server 更侧重于"何时用什么架构"的战略决策，mcp-builder 更侧重于"如何高质量实现"的战术执行。
