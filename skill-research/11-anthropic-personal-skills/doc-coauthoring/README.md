# doc-coauthoring

**Added by:** Anthropic  
**Trigger:** Slash command + auto  
**类型：** A型 SKILL.md Skill

---

## Description（触发描述）

**English:**  
Guide users through a structured workflow for co-authoring documentation. Use when the user wants to write documentation, proposals, technical specs, decision docs, or similar structured content. This workflow helps users efficiently transfer context, refine content through iteration, and verify the doc works for readers. Trigger when user mentions writing docs, creating proposals, drafting specs, or similar documentation tasks.

**中文：**  
引导用户完成协作文档创作的结构化工作流。当用户想要编写文档、提案、技术规格、决策文档或类似结构化内容时使用。

---

## 触发关键词

- "write a doc", "draft a proposal", "create a spec", "write up"
- 特定文档类型：PRD、design doc、decision doc、RFC
- 正在开始一项实质性写作任务时

**注意：** 首次触发时，先向用户介绍三阶段工作流，询问是否要用这个结构化流程还是自由形式写作。

---

## 核心架构：三阶段工作流

```
阶段一：上下文收集（Context Gathering）
    ├── 5个初始问题（文档类型/受众/目标/格式/约束）
    ├── 鼓励用户信息倾倒（完整背景）
    └── 5-10个澄清问题（基于差距）
    ↓
阶段二：精化与结构（Refinement & Structure）
    ├── 逐节处理：澄清 → 头脑风暴（5-20个选项）→ 筛选 → 起草
    ├── 使用 str_replace 编辑，不重印整个文档
    └── 80%+ 完成时全文审查
    ↓
阶段三：读者测试（Reader Testing）
    ├── 有子代理：自动测试（新 Claude 实例 + 预测读者问题）
    └── 无子代理：手动测试（用户在新对话中测试）
```

---

## SKILL.md 完整内容

### Doc Co-Authoring Workflow

This skill provides a structured workflow for guiding users through collaborative document creation. Act as an active guide, walking users through three stages: Context Gathering, Refinement & Structure, and Reader Testing.

---

#### When to Offer This Workflow

Trigger conditions:
- User mentions writing documentation: "write a doc", "draft a proposal", "create a spec", "write up"
- User mentions specific doc types: PRD, design doc, decision doc, RFC
- User seems to be starting a substantial writing task

Initial offer: Offer a structured workflow and explain the three stages. Ask if they want this workflow or prefer to work freeform. If user declines, work freeform.

---

#### Stage 1: Context Gathering

**Goal:** Close the gap between what the user knows and what Claude knows.

**Initial Questions:**
1. What type of document is this? (e.g., technical spec, decision doc, proposal)
2. Who's the primary audience?
3. What's the desired impact when someone reads this?
4. Is there a template or specific format to follow?
5. Any other constraints or context to know?

**Info Dumping**

Once initial questions are answered, encourage the user to dump all the context they have:
- Background on the project/problem
- Related team discussions or shared documents
- Why alternative solutions aren't being used
- Organizational context (team dynamics, past incidents, politics)
- Timeline pressures or constraints
- Technical architecture or dependencies
- Stakeholder concerns

If integrations are available (Slack, Teams, Google Drive, SharePoint, or other MCP servers), mention they can be used to pull context directly. If not available in Claude.ai: suggest enabling connectors in Claude settings.

**Clarifying Questions**

When user signals they've done their initial dump, ask 5-10 numbered questions based on gaps in the context. Users can answer in shorthand.

**Exit condition:** Sufficient context has been gathered when questions show understanding — when edge cases and trade-offs can be asked about without needing basics explained.

---

#### Stage 2: Refinement & Structure

**Goal:** Build the document section by section through brainstorming, curation, and iterative refinement.

**Section ordering:**
- Start with whichever section has the most unknowns (usually the core decision/proposal)
- Summary sections are best left for last

**For each section:**

1. **Clarifying Questions** — Ask 5-10 specific questions about what to include
2. **Brainstorming** — Generate 5-20 numbered options based on section complexity
3. **Curation** — User indicates what to keep/remove/combine (e.g., "Keep 1,4,7", "Remove 3 (duplicates 1)")
4. **Gap Check** — Ask if anything important is missing
5. **Drafting** — Use `str_replace` to replace placeholder text with drafted content
6. **Iterative Refinement** — Make surgical edits based on feedback; never reprint the whole doc

**Artifact Management:**
- If artifacts available: use `create_file` to create scaffold with placeholders, provide link after each edit
- If no artifacts: create a markdown file in working directory

**Quality Checking:** After 3 consecutive iterations with no substantial changes, ask if anything can be removed without losing important information.

**Near Completion (80%+ of sections done):**  
Re-read the entire document and check for: flow and consistency, redundancy or contradictions, generic filler, whether every sentence carries weight.

---

#### Stage 3: Reader Testing

**Goal:** Test the document with a fresh Claude (no context) to catch blind spots before others read it.

**With sub-agents (e.g., Claude Code):**

1. Predict Reader Questions — generate 5-10 realistic reader queries
2. Test with Sub-Agent — invoke a sub-agent with just the document content and each question; summarize results
3. Run Additional Checks — check for ambiguity, false assumptions, contradictions
4. Report and Fix — loop back to refinement for problematic sections

**Without sub-agents (e.g., claude.ai web interface):**

1. Predict 5-10 reader questions
2. Provide testing instructions:
   - Open a fresh Claude conversation: https://claude.ai
   - Paste or share the document
   - Ask Reader Claude the generated questions; have it report answers, ambiguities, and assumed knowledge
3. Additional checks: ask Reader Claude about ambiguity, assumed knowledge, contradictions
4. Iterate based on results

**Exit Condition:** Reader Claude consistently answers questions correctly and doesn't surface new gaps.

---

#### Final Review

When Reader Testing passes:
- Recommend a final read-through (user owns the document)
- Suggest double-checking any facts, links, or technical details
- Ask them to verify it achieves the intended impact

**Tips for completed documents:**
- Consider linking this conversation in an appendix
- Use appendices to provide depth without bloating the main doc
- Update the doc as feedback arrives from real readers

---

#### Tips for Effective Guidance

- **Tone:** Direct and procedural; explain rationale briefly when it affects user behavior
- **Handling Deviations:** Always give user agency to adjust the process
- **Context Management:** Don't let gaps accumulate — address them as they come up
- **Artifact Management:** Use `create_file` for drafting, `str_replace` for all edits, never use artifacts for brainstorming lists

---

## 研究笔记

**读者测试的创新设计：** 使用一个全新的 Claude 实例（无上下文）来模拟真实读者，这是一个利用 LLM 本身进行文档验证的巧妙方法。

**环境适应：** 该 skill 明确区分了两种运行环境：
- Claude Code（有子代理）：自动化读者测试
- claude.ai 网页界面（无子代理）：指导用户手动测试

**信息倾倒策略：** 先问 5 个宽泛问题，让用户倾倒所有背景信息，然后再基于信息差距提问 5-10 个具体问题——这个两步策略比直接问一堆问题更有效。
