# internal-comms

**Added by:** Anthropic  
**Trigger:** Slash command + auto  
**类型：** A型 SKILL.md Skill（路由分发模式）

---

## Description（触发描述）

**English:**  
A set of resources to help write all kinds of internal communications, using the formats that the company likes to use. Use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3P updates, company newsletters, FAQs, incident reports, project updates, etc.).

**中文：**  
一套资源，帮助撰写各种内部沟通文档，使用公司偏好的格式。当被要求撰写内部沟通（状态报告、领导层更新、3P更新、公司简报、FAQ、事故报告、项目更新等）时使用。

---

## 触发关键词

3P updates、company newsletter、company comms、weekly update、faqs、common questions、updates、internal comms

---

## 核心架构：路由分发模式

```
识别沟通类型
    ↓
路由到对应指南文件（examples/ 目录）
    ├── 3P 更新 → examples/3p-updates.md
    ├── 公司简报 → examples/company-newsletter.md
    ├── FAQ 回复 → examples/faq-answers.md
    └── 其他内容 → examples/general-comms.md
    ↓
按照指南文件中的格式、语气、内容收集要求执行
```

**设计哲学：** SKILL.md 本身极简（约 200 字），真正的格式规范、写作指南在 examples/ 目录中。这是一个典型的"路由型 skill"——SKILL.md 只做决策，不做内容。

---

## SKILL.md 完整内容

### When to use this skill

Use for:
- 3P updates (Progress, Plans, Problems)
- Company newsletters
- FAQ responses
- Status reports
- Leadership updates
- Project updates
- Incident reports

### How to use this skill

1. Identify the communication type from the request
2. Load the appropriate guideline file from the `examples/` directory:
   - `examples/3p-updates.md` — For Progress/Plans/Problems team updates
   - `examples/company-newsletter.md` — For company-wide newsletters
   - `examples/faq-answers.md` — For answering frequently asked questions
   - `examples/general-comms.md` — For anything else that doesn't explicitly match one of the above
3. Follow the specific instructions in that file for formatting, tone, and content gathering

If the communication type doesn't match any existing guideline, ask for clarification or more context about the desired format.

**Keywords:** 3P updates, company newsletter, company comms, weekly update, faqs, common questions, updates, internal comms

---

## 支持文件（examples/ 目录）

| 文件 | 用途 |
|------|------|
| `examples/3p-updates.md` | Progress/Plans/Problems 团队更新模板和写法规范 |
| `examples/company-newsletter.md` | 公司全员简报格式和语气指南 |
| `examples/faq-answers.md` | 常见问题解答写法规范 |
| `examples/general-comms.md` | 通用内部沟通，不匹配上述三类时使用 |

（注：examples/ 文件内容未获取到，上表为从 SKILL.md 中推断的功能描述）

---

## 研究笔记

**路由模式的优势：**  
- SKILL.md 极短（<500 行限制不是问题）
- 各类沟通文档的具体格式规范存放在 examples/ 中，按需加载
- 易于扩展——新增沟通类型只需新增一个 examples/ 文件
- 符合 Progressive Disclosure 设计原则

**与 build-mcp-server 的相似性：**  
build-mcp-server 技能也使用路由模式——主 SKILL.md 决策，然后加载 references/ 中的具体文档。这是一个通用的 skill 设计模式。
