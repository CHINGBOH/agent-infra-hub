# Anthropic 官方 Personal Skills 完整档案

**来源：** https://claude.ai/customize/skills（2026-05-23 爬取）  
**类别：** A型 SKILL.md Skill（Anthropic 官方发布）  
**触发方式：** Slash command + auto（用户输入斜杠命令或 Claude 自动识别上下文触发）

---

## 技能总览

| 技能名称 | 简介（中） | 核心机制 | 关键文件依赖 |
|----------|------------|----------|------------|
| [algorithmic-art](algorithmic-art/) | 用 p5.js 创作生成艺术 | 两阶段：算法哲学 → p5.js 实现 | `templates/viewer.html`（必读） |
| [canvas-design](canvas-design/) | 用设计哲学生成静态视觉艺术 | 两阶段：设计哲学 → 画布表达 | `./canvas-fonts` 字体目录 |
| [doc-coauthoring](doc-coauthoring/) | 结构化协作文档写作工作流 | 三阶段：收集上下文 → 精化结构 → 读者测试 | 无（使用子代理测试） |
| [internal-comms](internal-comms/) | 内部沟通文档写作 | 路由到 examples/ 模板 | `examples/` 目录（4个指南文件） |
| [mcp-builder](mcp-builder/) | 构建高质量 MCP 服务器 | 四阶段：研究 → 实现 → 测试 → 评估 | `references/` 目录（多个文档） |
| [skill-creator](skill-creator/) | 创建和评估技能 | 评估循环 + 描述优化 | `agents/`、`scripts/`、`references/` |
| [slack-gif-creator](slack-gif-creator/) | 制作适合 Slack 的动态 GIF | PIL + GIFBuilder 库 | `core/gif_builder.py` |
| [theme-factory](theme-factory/) | 为 Artifact 应用主题样式 | 分析现有 Artifact → 应用 CSS 设计令牌系统 | `themes/` 目录（推测） |
| [web-artifacts-builder](web-artifacts-builder/) | 构建复杂多组件 HTML Artifact | 组件分解 → 状态设计 → 单文件实现 | 无强制模板（推测） |

---

## 与其他 Skill 类型的区别

这 9 个技能均为 **Anthropic 官方发布的 Personal Skills**，与本研究目录中其他 skill 的区别：

| 维度 | 本目录（Personal Skills） | 08-personal-skills（个人 Skills） | 05-examples/superpowers | 09-skill-creator |
|------|--------------------------|----------------------------------|------------------------|-----------------|
| 来源 | Anthropic 官方，claude.ai | 用户个人（~/.claude/skills/） | superpowers 插件 | skill-creator 插件 |
| 安装方式 | claude.ai 界面启用 | 手动放置文件 | 插件安装 | 插件安装 |
| 技能数量 | 9个 | 4个 | 8个 | 1个（含子agent） |
| 特点 | 面向创意/内容生成 | 面向代码工作流 | 面向软件工程方法论 | 面向技能开发本身 |

---

## 技能哲学模式

Anthropic 这批 Personal Skills 共享几个设计哲学：

### 1. 二阶段创作模式（algorithmic-art、canvas-design）
```
第一阶段：生成"哲学"文本（.md）
    ↓ 哲学指导创作
第二阶段：技术实现（.html / .pdf / .png）
```
哲学文本是中间产物，不直接给用户，而是作为第二阶段的创作指南。

### 2. 结构化工作流模式（doc-coauthoring）
```
阶段一：上下文收集（提问 → 用户信息倾倒 → 澄清）
阶段二：精化结构（逐节头脑风暴 → 筛选 → 起草）
阶段三：读者测试（子代理测试 or 手动测试）
```

### 3. 路由分发模式（internal-comms）
```
识别沟通类型 → 从 examples/ 加载对应指南文件 → 按指南执行
```
SKILL.md 本身极简，真正的知识在 examples/ 的各个指南文件中。

### 4. 四阶段工程模式（mcp-builder）
```
研究阶段 → 实现阶段 → 审查测试 → 创建评估
```
每个阶段都有对应的 references/ 文档支持。

---

## 数据来源说明

- 中文版：用户通过 claude.ai 界面爬取，内容包含 skill 1-7（algorithmic-art 到 slack-gif-creator）
- 英文版：用户通过 claude.ai 界面爬取，内容包含 skill 1-6（algorithmic-art 到 skill-creator）
- theme-factory 和 web-artifacts-builder：仅有技能名称和一行描述，SKILL.md 内容未获取到
