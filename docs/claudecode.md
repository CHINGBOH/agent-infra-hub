Sonnet 4.6

把skills这个页面下所有的资料给解析下来，变成md文件

42 steps
42 steps
以下是所有 Skills 页面数据整理成的 Markdown 文件内容：

markdown

# Claude Skills - 个人技能库总览

> 页面：https://claude.ai/customize/skills  
> 分类：Personal skills（个人技能）  
> 来源：Anthropic  
> 更新时间：2026-05-23

---

## 技能列表

|
技能名称
|
触发方式
|
简介
|
|

---

## |

## |

|
|
algorithmic-art
|
Slash command + auto
|
用 p5.js 创作生成艺术
|
|
canvas-design
|
Slash command + auto
|
用设计哲学生成可视化艺术作品
|
|
doc-coauthoring
|
Slash command + auto
|
结构化协作文档写作工作流
|
|
internal-comms
|
Slash command + auto
|
内部沟通文档写作
|
|
mcp-builder
|
Slash command + auto
|
构建高质量 MCP 服务器
|
|
skill-creator
|
Slash command + auto
|
创建、改进和评估技能
|
|
slack-gif-creator
|
Slash command + auto
|
制作适合 Slack 的动态 GIF
|
|
theme-factory
|
Slash command + auto
|
为 Artifact 应用主题样式
|
|
web-artifacts-builder
|
Slash command + auto
|
构建复杂多组件 HTML Artifact
|

---

## 1. algorithmic-art

**Added by：** Anthropic  
**Trigger：** Slash command + auto  
**Description：**  
使用 p5.js 通过种子随机性和交互式参数探索创作生成艺术。当用户请求使用代码创作艺术、生成艺术、算法艺术、流场或粒子系统时使用。创作原创算法艺术，避免复制现有艺术家的作品。

---

### SKILL.md 内容

#### 核心概念

算法哲学是计算美学运动，通过代码来表达。输出：

- `.md` 文件（哲学）
- `.html` 文件（交互式查看器）
- `.js` 文件（生成算法）

#### 两个阶段

1. **算法哲学创作**（.md 文件）
2. **通过 p5.js 生成艺术表达**（.html + .js 文件）

---

#### ALGORITHMIC PHILOSOPHY CREATION（算法哲学创作）

创建一个算法哲学（不是静态图像或模板），通过以下方式诠释：

- 计算过程、涌现行为、数学美
- 种子随机性、噪声场、有机系统
- 粒子、流场、力场
- 参数变化和受控混沌

**关键理解：**

- 接收到：用户的细微输入或指令（作为基础，不应限制创作自由）
- 创建的：算法哲学 / 生成美学运动
- 后续：在代码中表达这一哲学

**如何生成算法哲学：**

1. 命名运动（1-2个词）：如 "Organic Turbulence"、"Quantum Harmonics"
2. 阐明哲学（4-6段）：通过以下维度表达视觉本质：
   - 计算过程和数学关系
   - 噪声函数和随机性模式
   - 粒子行为和场动力学
   - 时间演化和系统状态
   - 参数变化和涌现复杂性

**关键指南：**

- 避免重复
- 反复强调工艺水准（"精心制作的算法"、"深度计算专业的产物"等）
- 留给下一阶段创意空间

**哲学示例：**

- _"Organic Turbulence"_：受自然法则约束的混沌，秩序从无序中涌现。流场由分层 Perlin 噪声驱动，数千粒子沿向量力运动。
- _"Quantum Harmonics"_：离散实体展现波状干涉模式。粒子在网格初始化，相位通过正弦波演化。
- _"Recursive Whispers"_：跨尺度的自相似，有限空间的无限深度。
- _"Field Dynamics"_：通过物质效果可视化不可见的力。
- _"Stochastic Crystallization"_：随机过程结晶成有序结构。

---

#### P5.JS 实现

**⚠️ 步骤 0：首先读取模板**

在编写任何 HTML 之前：

- 使用 Read 工具读取 `templates/viewer.html`
- 研究精确的结构、样式和 Anthropic 品牌
- 以该文件为字面起点，而非仅作灵感参考
- 保持所有固定部分完全按原样（页眉、侧边栏结构、Anthropic 颜色/字体、种子控件、操作按钮）
- 仅替换文件注释中标记的 VARIABLE 部分

**技术要求：**

```javascript
// 始终使用种子确保可重现性
let seed = 12345;
randomSeed(seed);
noiseSeed(seed);

// 参数结构
let params = {
  seed: 12345,
  // 控制算法的参数：数量、比例、概率、角度等
};
```

**工艺要求：**

- 平衡：复杂而不视觉噪声，有序而不僵化
- 色彩和谐：经过深思的调色板，非随机RGB值
- 构图：即使在随机性中，保持视觉层次和流动
- 性能：流畅执行
- 可重现性：相同种子始终产生相同输出

**输出格式：**

- 算法哲学（.md 文件）
- 单一 HTML Artifact（从 `templates/viewer.html` 构建）

---

#### 交互式 Artifact 创建

**固定部分（始终包含）：**

- 布局结构（页眉、侧边栏、主画布区域）
- Anthropic 品牌（UI 颜色、字体、渐变）
- 种子部分（显示、上一个/下一个/随机/跳转按钮）
- 操作部分（重新生成、重置按钮）

**可变部分（每个作品定制）：**

- 整个 p5.js 算法
- 参数对象
- 侧边栏参数部分
- 颜色部分（可选）

**必需功能：**

1. 参数控件（滑块、颜色选择器、实时更新）
2. 种子导航（显示、上一个/下一个、随机、输入跳转）
3. 单一 Artifact 结构（自包含 HTML）

**资源文件：**

- `templates/viewer.html`：所有 HTML Artifact 的必需起点
- `templates/generator_template.js`：p5.js 最佳实践和代码结构原则的参考

---

## 2. canvas-design

**Added by：** Anthropic  
**Trigger：** Slash command + auto  
**Description：**  
使用设计哲学在 `.png` 和 `.pdf` 文档中创作精美的视觉艺术。当用户要求创建海报、艺术品、设计或其他静态作品时使用。创作原创视觉设计，避免侵权。

---

### SKILL.md 内容

#### 核心概念

为创建设计哲学提供指导——美学运动通过视觉方式表达。仅输出 `.md`、`.pdf` 和 `.png` 文件。

**两个阶段：**

1. 设计哲学创作（.md 文件）
2. 在画布上表达（.pdf 或 .png 文件）

---

#### DESIGN PHILOSOPHY CREATION（设计哲学创作）

创建视觉哲学（不是布局或模板），通过以下方式诠释：

- 形式、空间、颜色、构图
- 图像、图形、形状、图案
- 最少文字作为视觉点缀

**如何生成视觉哲学：**

1. 命名运动（1-2词）：如 "Brutalist Joy"、"Chromatic Silence"
2. 阐明哲学（4-6段）：通过以下维度捕捉视觉本质：
   - 空间与形式
   - 颜色与材质
   - 比例与节奏
   - 构图与平衡
   - 视觉层次

**关键指南：**

- 避免重复
- 反复强调工艺水准
- 留给解释空间

**哲学示例：**

- _"Concrete Poetry"_：通过宏大形式和大胆几何进行沟通。巨大色块、雕塑感排版，布鲁塔主义空间分割。
- _"Chromatic Language"_：颜色作为主要信息系统。几何精度中颜色区域创造意义。
- _"Analog Meditation"_：通过纹理和留白进行宁静的视觉沉思。纸张纹理、墨水晕染、大面积负空间。
- _"Organic Systems"_：自然聚集和模块化生长模式。圆形、有机排列。
- _"Geometric Silence"_：纯粹的秩序与克制。基于网格的精确度，大胆摄影。

---

#### CANVAS CREATION（画布创作）

基于哲学和概念框架在画布上表达。

**原则：**

- 创建单页、高度视觉化、设计前沿的 PDF 或 PNG 输出
- 使用重复图案和完美形状
- 稀疏的临床字体和系统参考标记
- 有限的颜色调色板

**文字处理：**

- 文字始终最少，以视觉为先
- 字体通常细体
- 不能超出页面边界，不能重叠

**资源：**

- `./canvas-fonts` 目录：可搜索使用的字体

**最终步骤（细化）：**

> 用户已经说过："还不够完美，必须无瑕疵，像要在博物馆展出的艺术杰作。"  
> 避免添加更多图形；精炼已有内容，极度清晰，尊重设计哲学和极简主义原则。

**多页选项：**  
当用户请求多页时，沿同一设计哲学创建更多页面，但各页要有明显差异，像一本咖啡桌艺术书。

---

## 3. doc-coauthoring

**Added by：** Anthropic  
**Trigger：** Slash command + auto  
**Description：**  
引导用户完成协作文档创作的结构化工作流。当用户想要编写文档、提案、技术规格、决策文档或类似结构化内容时使用。

---

### SKILL.md 内容

#### 何时触发

触发条件：

- 用户提到写文档："write a doc"、"draft a proposal"、"create a spec"
- 用户提到特定文档类型：PRD、设计文档、决策文档、RFC
- 用户似乎正在开始一项实质性写作任务

---

#### 三阶段工作流

---

##### 第一阶段：上下文收集（Context Gathering）

**目标：** 缩小用户已知和 Claude 已知之间的差距。

**初始问题：**

1. 这是什么类型的文档？
2. 主要受众是谁？
3. 读者阅读后的预期效果是什么？
4. 是否有模板或特定格式要求？
5. 其他约束或背景？

**信息收集内容：**

- 项目/问题背景
- 相关团队讨论或共享文档
- 为什么不使用替代方案
- 组织背景（团队动态、过去事件、政治）
- 时间压力或约束
- 技术架构或依赖关系
- 利益相关者的关切

**澄清问题：**

- 在用户完成初始信息倾倒后，提出 5-10 个基于上下文差距的编号问题
- 用户可以使用简写回答

**退出条件：** 当问题显示理解时（能询问边缘情况和权衡，无需解释基础知识）

---

##### 第二阶段：细化与结构（Refinement & Structure）

**目标：** 通过头脑风暴、整理和迭代细化，逐节构建文档。

**章节处理流程：**

1. **澄清问题**：询问每个章节要包含什么（5-10个问题）
2. **头脑风暴**：基于章节复杂度生成 5-20 个选项
3. **整理**：用户选择保留/删除/合并哪些内容
4. **差距检查**：询问是否有重要内容缺失
5. **起草**：使用 str_replace 将占位符文本替换为实际内容
6. **迭代细化**：根据反馈进行外科手术式编辑

**工具使用：**

- 如果可访问 Artifacts：使用 `create_file` 创建带占位符的脚手架
- 如果无法访问：在工作目录创建 Markdown 文件

**质量检查：** 3次连续迭代无实质性变化后，询问是否可以删除内容而不损失重要信息。

**接近完成时（80%+ 章节完成）：**
重新阅读整个文档，检查：

- 各章节的流畅性和一致性
- 冗余或矛盾
- 通用填充内容
- 每句话的分量

---

##### 第三阶段：读者测试（Reader Testing）

**目标：** 用全新的 Claude（无上下文）测试文档，在他人阅读前发现盲点。

**测试方法（有子代理时）：**

1. 预测读者问题（5-10个现实问题）
2. 用子代理测试：向只有文档内容的新 Claude 实例提问
3. 汇总每个问题的测试结果
4. 运行额外检查：歧义、错误假设、矛盾
5. 报告并修复问题

**测试方法（无子代理时，如 claude.ai 网页界面）：**

1. 生成读者可能提出的 5-10 个问题
2. 用户在新 Claude 对话中手动测试
3. 提供标准化的检查指令（是否模糊、假设知识、内部矛盾）
4. 根据结果迭代

**退出条件：** 读者 Claude 能一致正确回答问题，不再发现新的差距或歧义。

---

#### 指导提示

- **语气**：直接、程序化，简短解释原因
- **处理偏差**：给予用户调整流程的主动权
- **Artifact 管理**：使用 `create_file` 起草，使用 `str_replace` 编辑，绝不重印整个文档

---

## 4. internal-comms

**Added by：** Anthropic  
**Trigger：** Slash command + auto  
**Description：**  
一套资源，帮助撰写各种内部沟通文档，使用公司偏好的格式。当被要求撰写内部沟通（状态报告、领导层更新、3P更新、公司简报、FAQ、事故报告、项目更新等）时使用。

---

### SKILL.md 内容

#### 何时使用

适用于以下内部沟通类型：

- 3P 更新（Progress、Plans、Problems）
- 公司简报
- FAQ 回复
- 状态报告
- 领导层更新
- 项目更新
- 事故报告

#### 如何使用

1. 从请求中识别沟通类型
2. 从 `examples/` 目录加载适当的指南文件：
   - `examples/3p-updates.md` — 进展/计划/问题团队更新
   - `examples/company-newsletter.md` — 全公司简报
   - `examples/faq-answers.md` — 常见问题解答
   - `examples/general-comms.md` — 不明确匹配以上类型的其他内容
3. 按照该文件中的格式、语气和内容收集具体说明操作

如果沟通类型与任何现有指南不匹配，请请求澄清或关于所需格式的更多上下文。

**关键词：** 3P更新、公司简报、公司沟通、每周更新、FAQ、常见问题、内部沟通

---

## 5. mcp-builder

**Added by：** Anthropic  
**Trigger：** Slash command + auto  
**Description：**  
创建高质量 MCP（Model Context Protocol）服务器的指南，使 LLM 能够通过精心设计的工具与外部服务交互。无论是 Python（FastMCP）还是 Node/TypeScript（MCP SDK）均适用。

---

### SKILL.md 内容

#### 概述

创建 MCP 服务器，使 LLM 能够通过精心设计的工具与外部服务交互。MCP 服务器的质量取决于它使 LLM 能够多好地完成真实世界任务。

---

#### 🚀 高层工作流

创建高质量 MCP 服务器涉及四个主要阶段：

---

##### 第一阶段：深度研究和规划

**1.1 理解现代 MCP 设计**

- **API 覆盖 vs 工作流工具**：平衡全面 API 端点覆盖与专业工作流工具。不确定时优先考虑全面 API 覆盖。
- **工具命名和可发现性**：使用一致的前缀（如 `github_create_issue`）和面向行动的命名。
- **上下文管理**：设计返回聚焦、相关数据的工具，支持过滤/分页。
- **可行的错误信息**：错误信息应指导代理寻找解决方案。

**1.2 学习 MCP 协议文档**

- 从站点地图开始：`https://modelcontextprotocol.io/sitemap.xml`
- 使用 `.md` 后缀获取 Markdown 格式的特定页面
- 重点页面：规范概述、传输机制（可流式 HTTP、stdio）、工具/资源/提示定义

**1.3 学习框架文档**

推荐技术栈：

- **语言**：TypeScript（高质量 SDK 支持，AI 模型擅长生成）
- **传输**：远程服务器使用可流式 HTTP（无状态 JSON），本地服务器使用 stdio

参考文档：

- MCP 最佳实践：`references/mcp_best_practices.md`
- TypeScript SDK：`https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md`
- Python SDK：`https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md`

**1.4 规划实现**

- 审查服务 API 文档（端点、认证、数据模型）
- 工具选择：优先全面 API 覆盖，从最常见操作开始

---

##### 第二阶段：实现

**2.1 设置项目结构**

参考语言特定指南：

- TypeScript：项目结构、package.json、tsconfig.json
- Python：模块组织、依赖项

**2.2 实现核心基础设施**

创建共享工具：

- 带认证的 API 客户端
- 错误处理助手
- 响应格式化（JSON/Markdown）
- 分页支持

**2.3 实现工具**

每个工具需要：

_输入 Schema：_

- 使用 Zod（TypeScript）或 Pydantic（Python）
- 包含约束和清晰描述
- 在字段描述中添加示例

_输出 Schema：_

- 尽可能定义 `outputSchema`
- 在工具响应中使用 `structuredContent`（TypeScript SDK 特性）

_工具描述：_

- 功能简洁摘要
- 参数描述
- 返回类型 Schema

_实现：_

- I/O 操作使用 async/await
- 正确的错误处理（可行的错误信息）
- 适用时支持分页
- 使用现代 SDK 时返回文本内容和结构化数据

_注解：_

- `readOnlyHint`：true/false
- `destructiveHint`：true/false
- `idempotentHint`：true/false
- `openWorldHint`：true/false

---

##### 第三阶段：审查和测试

**3.1 代码质量**

审查内容：

- 无重复代码（DRY 原则）
- 一致的错误处理
- 完整的类型覆盖
- 清晰的工具描述

**3.2 构建和测试**

TypeScript：

```bash
npm run build           # 验证编译
npx @modelcontextprotocol/inspector  # 使用 MCP Inspector 测试
```

Python：

```bash
python -m py_compile your_server.py  # 验证语法
# 使用 MCP Inspector 测试
```

---

##### 第四阶段：创建评估

**4.1 评估目的**

测试 LLM 是否能有效使用 MCP 服务器回答真实、复杂的问题。

**4.2 创建 10 个评估问题**

流程：

1. 工具检查：列出可用工具并理解其能力
2. 内容探索：使用只读操作探索可用数据
3. 问题生成：创建 10 个复杂、真实的问题
4. 答案验证：自己解决每个问题以验证答案

**4.3 评估要求**

每个问题必须：

- **独立**：不依赖其他问题
- **只读**：只需要非破坏性操作
- **复杂**：需要多次工具调用和深度探索
- **真实**：基于人们关心的真实用例
- **可验证**：单一、清晰的答案可通过字符串比较验证
- **稳定**：答案不会随时间变化

**4.4 输出格式**

```xml


    问题内容
    答案


```

---

#### 参考文件库

|
资源
|
说明
|
|

---

## |

|
|
MCP 协议文档
|
从
`https://modelcontextprotocol.io/sitemap.xml`
开始
|
|
MCP 最佳实践
|
`references/mcp_best_practices.md`
|
|
Python SDK
|
`https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md`
|
|
TypeScript SDK
|
`https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md`
|
|
Python 实现指南
|
`references/python_mcp_server.md`
|
|
TypeScript 实现指南
|
`references/node_mcp_server.md`
|
|
评估指南
|
`references/evaluation.md`
|

---

## 6. skill-creator

**Added by：** Anthropic  
**Trigger：** Slash command + auto  
**Description：**  
创建新技能、修改和改进现有技能，以及衡量技能性能。当用户想要从头创建技能、编辑或优化现有技能、运行评估测试技能、对技能性能进行基准测试或优化技能描述时使用。

---

### SKILL.md 内容

#### 技能创建器

创建新技能并迭代改进它们的技能。

**高层流程：**

1. 决定技能要做什么以及大致如何实现
2. 编写技能草稿
3. 创建几个测试提示，在有技能访问权限的 Claude 上运行它们
4. 帮助用户定性和定量地评估结果
5. 根据用户对结果的评估反馈重写技能
6. 重复直到满意
7. 扩大测试集，更大规模地再次尝试

---

#### 与用户沟通

技能创建器可能被各种熟悉编程术语程度不同的人使用。

默认避免专业术语：

- "evaluation"和"benchmark"处于临界，可以使用
- "JSON"和"assertion"需要用户发出明确信号表明他们了解这些

---

#### 创建技能

##### 捕捉意图

理解用户意图的问题：

- 这个技能应该使 Claude 能做什么？
- 技能何时触发？（用户短语/上下文）
- 预期输出格式是什么？
- 是否应该设置测试用例来验证技能是否有效？

##### 采访和研究

主动询问关于边缘情况、输入/输出格式、示例文件、成功标准等。

##### 编写 SKILL.md

组件：

- **name**：技能标识符
- **description**：何时触发，做什么（主要触发机制）
- **compatibility**：所需工具、依赖项（可选，很少需要）
- 其余：技能的实际内容

---

#### 技能编写指南

##### 技能的解剖

skill-name/
├── SKILL.md (必需)
│ ├── YAML frontmatter (name, description 必需)
│ └── Markdown 指令
└── 捆绑资源 (可选)
├── scripts/ - 确定性/重复任务的可执行代码
├── references/ - 按需加载的文档
└── assets/ - 用于输出的文件（模板、图标、字体）

##### 渐进式披露

技能使用三级加载系统：

- **元数据**（name + description）：始终在上下文中（约100词）
- **SKILL.md 主体**：每当技能触发时在上下文中（理想 <500 行）
- **捆绑资源**：按需（无限制，脚本无需加载即可执行）

**关键模式：**

- 将 SKILL.md 保持在 500 行以下
- 从 SKILL.md 中清楚地引用文件，包含何时读取的指导
- 对于大型参考文件（>300 行），包含目录

##### 写作模式

- 指令使用祈使句形式
- 包含示例
- 尽量解释事情为什么重要，而非使用命令式"MUST"

---

#### 测试用例

编写技能草稿后，提出 2-3 个现实测试提示。

保存到 `evals/evals.json`：

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": "...",
      "prompt": "用户的任务提示",
      "expected_output": "预期结果描述",
      "files": []
    }
  ]
}
```

---

#### 运行和评估测试用例

##### 第一步：同一轮次生成所有运行（有技能 AND 基准线）

对每个测试用例，在同一轮次生成两个子代理：

- **有技能运行**：使用技能路径
- **基准线运行**：
  - 创建新技能：完全无技能
  - 改进现有技能：使用旧版本

##### 第二步：运行中起草断言

不等待运行完成——利用时间起草定量断言。

好的断言：

- 客观可验证
- 有描述性名称

##### 第三步：捕获时间数据

当子代理任务完成时，立即保存 `total_tokens` 和 `duration_ms` 到 `timing.json`。

##### 第四步：评分、汇总、启动查看器

```bash
python -m scripts.aggregate_benchmark \
  workspace/iteration-N \
  --skill-name name
```

然后：

```bash
nohup python <skill-creator-path>/eval-viewer/generate_review.py \
  workspace/iteration-N \
  --skill-name "my-skill" \
  --benchmark workspace/iteration-N/benchmark.json \
  >/dev/null &VIEWER_PID=$!
```

##### 第五步：读取反馈

用户完成后，读取 `feedback.json`。空反馈意味着用户认为结果不错。

---

#### 改进技能

**改进思路：**

- **从反馈中归纳**：泛化，不要为特定测试用例进行过度拟合
- **保持提示精简**：删除不起作用的内容；阅读转录而非仅看最终输出
- **解释原因**：解释每件事为何重要，而非简单命令
- **寻找跨测试用例的重复工作**：将重复工作提取到 `scripts/` 中

**迭代循环：**

1. 应用改进到技能
2. 将所有测试用例重新运行到新目录（包括基准线运行）
3. 启动查看器（带 `--previous-workspace` 参数）
4. 等待用户审查
5. 读取新反馈，再次改进，重复

**停止条件：**

- 用户表示满意
- 所有反馈都为空
- 没有取得实质进展

---

#### 描述优化

**目的：** `description` 字段是决定 Claude 是否触发技能的主要机制。

##### 第一步：生成触发评估查询

创建 20 个评估查询——应触发和不应触发的混合。

查询必须是现实的：

- 差的：`"Format this data"`、`"Create a chart"`
- 好的：真实用户会输入的具体、详细查询

##### 第二步：与用户一起审查

使用 `assets/eval_review.html` 模板展示评估集供用户审查。

##### 第三步：运行优化循环

```bash
python -m scripts.run_loop \
  --eval-set path-to-trigger-eval.json \
  --skill-path path-to-skill \
  --model model-id \
  --max-iterations 10 \
  --verbose
```

##### 第四步：应用结果

从 JSON 输出中取 `best_description` 并更新 SKILL.md frontmatter。

---

#### Claude.ai 特定说明

- **运行测试用例**：无子代理，逐个测试用例，读取 SKILL.md 然后按指令执行
- **审查结果**：如无法打开浏览器，使用 `--static <output_path>` 写入独立 HTML 文件
- **基准测试**：跳过定量基准测试
- **描述优化**：跳过（需要 CLI 工具 `claude -p`）
- **盲对比**：跳过（需要子代理）

---

#### 参考文件

- `agents/grader.md`：如何评估断言与输出
- `agents/comparator.md`：如何在两个输出间进行盲 A/B 对比
- `agents/analyzer.md`：如何分析某版本为何胜出
- `references/schemas.md`：evals.json、grading.json 等的 JSON 结构

---

## 7. slack-gif-creator

**Added by：** Anthropic  
**Trigger：** Slash command + auto  
**Description：**  
用于创建针对 Slack 优化的动态 GIF 的知识和工具包。提供约束条件、验证工具和动画概念。当用户请求为 Slack 制作动态 GIF 时使用。

---

### SKILL.md 内容

#### Slack 要求

**尺寸：**

- Emoji GIF：128×128（推荐）
- 消息 GIF：480×480

**参数：**

- FPS：10-30（越低文件越小）
- 颜色：48-128（越少越小）
- 时长：Emoji GIF 保持在 3 秒以下

---

#### 核心工作流

```python
from core.gif_builder import GIFBuilder
from PIL import Image, ImageDraw

# 1. 创建构建器
builder = GIFBuilder(width=128, height=128, fps=10)

# 2. 生成帧
for i in range(12):
    frame = Image.new('RGB', (128, 128), (240, 248, 255))
    draw = ImageDraw.Draw(frame)
    # 使用 PIL 原语绘制动画
    builder.add_frame(frame)

# 3. 保存并优化
builder.save('output.gif', num_colors=48, optimize_for_emoji=True)
```

---

#### 绘制图形

**使用用户上传的图像：**

```python
from PIL import Image
uploaded = Image.open('file.png')
# 直接使用，或仅作为颜色/风格参考
```

**从零开始绘制：**

```python
from PIL import ImageDraw
draw = ImageDraw.Draw(frame)

# 圆形/椭圆
draw.ellipse([x1, y1, x2, y2], fill=(r,g,b), outline=(r,g,b), width=3)
# 多边形（星形、三角形等）
draw.polygon(points, fill=(r,g,b), outline=(r,g,b), width=3)
# 直线
draw.line([(x1,y1),(x2,y2)], fill=(r,g,b), width=5)
# 矩形
draw.rectangle([x1,y1,x2,y2], fill=(r,g,b), outline=(r,g,b), width=3)
```

**使图形好看的技巧：**

- 使用较粗的线条（width=2 或更高）
- 添加视觉深度（渐变背景、多层形状）
- 使形状更有趣（高光、光环、图案）

英文原版的也来一份

1 step
1 step
Here is the English version of all Skills page data as a Markdown file:

markdown

# Claude Skills — Personal Skills Library

> Page: https://claude.ai/customize/skills  
> Category: Personal skills  
> Added by: Anthropic  
> Date: 2026-05-23

---

## Skills Overview

|
Skill Name
|
Trigger
|
Summary
|
|

---

## |

## |

|
|
algorithmic-art
|
Slash command + auto
|
Create generative art with p5.js
|
|
canvas-design
|
Slash command + auto
|
Create visual art using design philosophy
|
|
doc-coauthoring
|
Slash command + auto
|
Structured collaborative document authoring workflow
|
|
internal-comms
|
Slash command + auto
|
Write internal communication documents
|
|
mcp-builder
|
Slash command + auto
|
Build high-quality MCP servers
|
|
skill-creator
|
Slash command + auto
|
Create, improve, and evaluate skills
|
|
slack-gif-creator
|
Slash command + auto
|
Create animated GIFs optimized for Slack
|
|
theme-factory
|
Slash command + auto
|
Apply themes and styles to artifacts
|
|
web-artifacts-builder
|
Slash command + auto
|
Build complex multi-component HTML artifacts
|

---

## 1. algorithmic-art

**Added by:** Anthropic  
**Trigger:** Slash command + auto  
**Description:**  
Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art, algorithmic art, flow fields, or particle systems. Create original algorithmic art rather than copying existing artists' work to avoid copyright violations.

---

### SKILL.md

Algorithmic philosophies are computational aesthetic movements that are then expressed through code. Output `.md` files (philosophy), `.html` files (interactive viewer), and `.js` files (generative algorithms).

This happens in two steps:

1. Algorithmic Philosophy Creation (.md file)
2. Express by creating p5.js generative art (.html + .js files)

---

#### ALGORITHMIC PHILOSOPHY CREATION

To begin, create an ALGORITHMIC PHILOSOPHY (not static images or templates) that will be interpreted through:

- Computational processes, emergent behavior, mathematical beauty
- Seeded randomness, noise fields, organic systems
- Particles, flows, fields, forces
- Parametric variation and controlled chaos

**THE CRITICAL UNDERSTANDING**

- What is received: Some subtle input or instructions by the user to take into account, but use as a foundation; it should not constrain creative freedom.
- What is created: An algorithmic philosophy/generative aesthetic movement.
- What happens next: The same version receives the philosophy and EXPRESSES IT IN CODE — creating p5.js sketches that are 90% algorithmic generation, 10% essential parameters.

**HOW TO GENERATE AN ALGORITHMIC PHILOSOPHY**

Name the movement (1-2 words): "Organic Turbulence" / "Quantum Harmonics" / "Emergent Stillness"

Articulate the philosophy (4-6 paragraphs) through:

- Computational processes and mathematical relationships
- Noise functions and randomness patterns
- Particle behaviors and field dynamics
- Temporal evolution and system states
- Parametric variation and emergent complexity

**CRITICAL GUIDELINES:**

- Avoid redundancy: each algorithmic aspect mentioned once
- Emphasize craftsmanship REPEATEDLY: "meticulously crafted algorithm", "product of deep computational expertise", "painstaking optimization", "master-level implementation"
- Leave creative space: specific but concise enough for interpretive choices

**PHILOSOPHY EXAMPLES**

- _"Organic Turbulence"_: Chaos constrained by natural law, order emerging from disorder. Flow fields driven by layered Perlin noise. Thousands of particles following vector forces, their trails accumulating into organic density maps.
- _"Quantum Harmonics"_: Discrete entities exhibiting wave-like interference patterns. Particles initialized on a grid, each carrying a phase value that evolves through sine waves.
- _"Recursive Whispers"_: Self-similarity across scales, infinite depth in finite space. Branching structures that subdivide recursively, constrained by golden ratios.
- _"Field Dynamics"_: Invisible forces made visible through their effects on matter. Vector fields constructed from mathematical functions or noise.
- _"Stochastic Crystallization"_: Random processes crystallizing into ordered structures. Randomized circle packing or Voronoi tessellation.

**ESSENTIAL PRINCIPLES**

- ALGORITHMIC PHILOSOPHY: Creating a computational worldview to be expressed through code
- PROCESS OVER PRODUCT: Beauty emerges from the algorithm's execution — each run is unique
- PARAMETRIC EXPRESSION: Ideas communicate through mathematical relationships, forces, behaviors
- ARTISTIC FREEDOM: Provide creative implementation room
- PURE GENERATIVE ART: Making LIVING ALGORITHMS, not static images
- EXPERT CRAFTSMANSHIP: Final algorithm must feel meticulously crafted, refined through countless iterations

---

#### DEDUCING THE CONCEPTUAL SEED

CRITICAL STEP: Before implementing, identify the subtle conceptual thread from the original request.

THE ESSENTIAL PRINCIPLE: The concept is a subtle, niche reference embedded within the algorithm — not always literal, always sophisticated. Someone familiar with the subject should feel it intuitively, while others simply experience a masterful generative composition.

---

#### P5.JS IMPLEMENTATION

**⚠️ STEP 0: READ THE TEMPLATE FIRST ⚠️**

BEFORE writing any HTML:

- Read `templates/viewer.html` using the Read tool
- Study the exact structure, styling, and Anthropic branding
- Use that file as the LITERAL STARTING POINT
- Keep all FIXED sections exactly as shown
- Replace only the VARIABLE sections marked in the file's comments

Avoid:

- ❌ Creating HTML from scratch
- ❌ Inventing custom styling or color schemes
- ❌ Using system fonts or dark themes
- ❌ Changing the sidebar structure

Follow:

- ✅ Copy the template's exact HTML structure
- ✅ Keep Anthropic branding (Poppins/Lora fonts, light colors, gradient backdrop)
- ✅ Maintain the sidebar layout (Seed → Parameters → Colors? → Actions)
- ✅ Replace only the p5.js algorithm and parameter controls

**TECHNICAL REQUIREMENTS**

```javascript
// ALWAYS use a seed for reproducibility
let seed = 12345;
randomSeed(seed);
noiseSeed(seed);

// Parameter Structure
let params = {
  seed: 12345,
  // Add parameters that control YOUR algorithm:
  // quantities, scales, probabilities, ratios, angles, thresholds
};
```

**CRAFTSMANSHIP REQUIREMENTS**

- Balance: Complexity without visual noise, order without rigidity
- Color Harmony: Thoughtful palettes, not random RGB values
- Composition: Visual hierarchy and flow even in randomness
- Performance: Smooth execution, optimized for real-time if animated
- Reproducibility: Same seed ALWAYS produces identical output

**OUTPUT FORMAT**

- Algorithmic Philosophy — As markdown explaining the generative aesthetic
- Single HTML Artifact — Self-contained interactive generative art built from `templates/viewer.html`

---

#### INTERACTIVE ARTIFACT CREATION

**FIXED (always include exactly as shown):**

- Layout structure (header, sidebar, main canvas area)
- Anthropic branding (UI colors, fonts, gradients)
- Seed section in sidebar (display, Prev/Next/Random/Jump buttons)
- Actions section (Regenerate, Reset buttons)

**VARIABLE (customize for each artwork):**

- The entire p5.js algorithm (setup/draw/classes)
- The parameters object
- The Parameters section in sidebar
- Colors section (optional)

**REQUIRED FEATURES**

1. Parameter Controls — sliders, color pickers, real-time updates, Reset button
2. Seed Navigation — display, Prev/Next buttons, Random button, jump-to input
3. Single Artifact Structure — fully self-contained HTML

**Resources:**

- `templates/viewer.html`: REQUIRED STARTING POINT for all HTML artifacts
- `templates/generator_template.js`: Reference for p5.js best practices

---

## 2. canvas-design

**Added by:** Anthropic  
**Trigger:** Slash command + auto  
**Description:**  
Create beautiful visual art in `.png` and `.pdf` documents using design philosophy. Use this skill when the user asks to create a poster, piece of art, design, or other static piece. Create original visual designs, never copying existing artists' work to avoid copyright violations.

---

### SKILL.md

These are instructions for creating design philosophies — aesthetic movements that are then EXPRESSED VISUALLY. Output only `.md` files, `.pdf` files, and `.png` files.

Complete this in two steps:

1. Design Philosophy Creation (.md file)
2. Express by creating it on a canvas (.pdf or .png file)

---

#### DESIGN PHILOSOPHY CREATION

To begin, create a VISUAL PHILOSOPHY (not layouts or templates) that will be interpreted through:

- Form, space, color, composition
- Images, graphics, shapes, patterns
- Minimal text as visual accent

**THE CRITICAL UNDERSTANDING**

- What is received: Subtle input or instructions by the user — used as a foundation, not a constraint
- What is created: A design philosophy/aesthetic movement
- What happens next: EXPRESSES IT VISUALLY — 90% visual design, 10% essential text

**HOW TO GENERATE A VISUAL PHILOSOPHY**

Name the movement (1-2 words): "Brutalist Joy" / "Chromatic Silence" / "Metabolist Dreams"

Articulate the philosophy (4-6 paragraphs) through:

- Space and form
- Color and material
- Scale and rhythm
- Composition and balance
- Visual hierarchy

**CRITICAL GUIDELINES:**

- Avoid redundancy
- Emphasize craftsmanship REPEATEDLY: "meticulously crafted", "product of deep expertise", "painstaking attention", "master-level execution"
- Leave creative space

**PHILOSOPHY EXAMPLES**

- _"Concrete Poetry"_: Communication through monumental form and bold geometry. Massive color blocks, sculptural typography, Brutalist spatial divisions, Polish poster energy meets Le Corbusier.
- _"Chromatic Language"_: Color as the primary information system. Geometric precision where color zones create meaning. Think Josef Albers' interaction meets data visualization.
- _"Analog Meditation"_: Quiet visual contemplation through texture and breathing room. Paper grain, ink bleeds, vast negative space. Japanese photobook aesthetic.
- _"Organic Systems"_: Natural clustering and modular growth patterns. Rounded forms, organic arrangements, color from nature through architecture.
- _"Geometric Silence"_: Pure order and restraint. Grid-based precision, bold photography or stark graphics, dramatic negative space. Swiss formalism meets Brutalist material honesty.

**ESSENTIAL PRINCIPLES**

- VISUAL PHILOSOPHY: An aesthetic worldview to be expressed through design
- MINIMAL TEXT: Sparse, essential-only, integrated as visual element — never lengthy
- SPATIAL EXPRESSION: Ideas communicate through space, form, color, composition
- ARTISTIC FREEDOM: Provide creative room for visual interpretation
- PURE DESIGN: Making ART OBJECTS, not documents with decoration
- EXPERT CRAFTSMANSHIP: Final work must look meticulously crafted, labored over with care

---

#### DEDUCING THE SUBTLE REFERENCE

CRITICAL STEP: Before creating the canvas, identify the subtle conceptual thread from the original request.

THE ESSENTIAL PRINCIPLE: The topic is a subtle, niche reference embedded within the art — not always literal, always sophisticated. Think like a jazz musician quoting another song — only those who know will catch it, but everyone appreciates the music.

---

#### CANVAS CREATION

With both the philosophy and conceptual framework established, express it on a canvas.

**Key principles:**

- Create one single page, highly visual, design-forward PDF or PNG (unless asked for more)
- Use repeating patterns and perfect shapes
- Treat the design like a scientific bible — dense accumulation of marks, repeated elements, layered patterns
- Sparse, clinical typography and systematic reference markers
- Limited color palette that feels intentional and cohesive

**Text as a contextual element:**  
Always minimal and visual-first. Nothing falls off the page and nothing overlaps. Every element must be contained within the canvas boundaries with proper margins. Use fonts from the `./canvas-fonts` directory.

**CRITICAL:** Create work that looks like it took countless hours. Make it appear as though someone at the absolute top of their field labored over every detail with painstaking care.

Output: A single, downloadable `.pdf` or `.png` file, alongside the design philosophy as a `.md` file.

---

#### FINAL STEP

> The user ALREADY said "It isn't perfect enough. It must be pristine, a masterpiece of craftsmanship, as if it were about to be displayed in a museum."

To refine: avoid adding more graphics; instead refine what has been created and make it extremely crisp. Ask: "How can I make what's already here more of a piece of art?"

---

#### MULTI-PAGE OPTION

When additional pages are requested, create more creative pages along the same design philosophy but distinctly different. Bundle in the same `.pdf` or multiple `.png` files. Treat the first page as a single page in a coffee table book waiting to be filled.

---

## 3. doc-coauthoring

**Added by:** Anthropic  
**Trigger:** Slash command + auto  
**Description:**  
Guide users through a structured workflow for co-authoring documentation. Use when the user wants to write documentation, proposals, technical specs, decision docs, or similar structured content. This workflow helps users efficiently transfer context, refine content through iteration, and verify the doc works for readers. Trigger when user mentions writing docs, creating proposals, drafting specs, or similar documentation tasks.

---

### SKILL.md

#### Doc Co-Authoring Workflow

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

## 4. internal-comms

**Added by:** Anthropic  
**Trigger:** Slash command + auto  
**Description:**  
A set of resources to help write all kinds of internal communications, using the formats that the company likes to use. Use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3P updates, company newsletters, FAQs, incident reports, project updates, etc.).

---

### SKILL.md

#### When to use this skill

Use for:

- 3P updates (Progress, Plans, Problems)
- Company newsletters
- FAQ responses
- Status reports
- Leadership updates
- Project updates
- Incident reports

#### How to use this skill

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

## 5. mcp-builder

**Added by:** Anthropic  
**Trigger:** Slash command + auto  
**Description:**  
Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).

**License:** Complete terms in LICENSE.txt

---

### SKILL.md

#### Overview

Create MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. The quality of an MCP server is measured by how well it enables LLMs to accomplish real-world tasks.

---

#### Process

### 🚀 High-Level Workflow

Creating a high-quality MCP server involves four main phases:

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
- TypeScript SDK: `https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md` — `references/node_mcp_server.md`
- Python SDK: `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md` — `references/python_mcp_server.md`

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

After implementing your MCP server, create comprehensive evaluations to test its effectiveness. Load `references/evaluation.md` for complete evaluation guidelines.

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


    Find discussions about AI model launches with animal codenames. One model needed a specific safety designation that uses the format ASL-X. What number X was being determined for the model named after a spotted wild cat?
    3



```

---

#### Reference Files — 📚 Documentation Library

**Core MCP Documentation (Load First)**

- MCP Protocol: Start with sitemap at `https://modelcontextprotocol.io/sitemap.xml`, then fetch specific pages with `.md` suffix
- MCP Best Practices (`references/mcp_best_practices.md`): server and tool naming conventions, response format guidelines, pagination best practices, transport selection, security and error handling standards

**SDK Documentation (Load During Phase 1/2)**

- Python SDK: `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md`
- TypeScript SDK: `https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md`

**Language-Specific Implementation Guides (Load During Phase 2)**

- Python Implementation Guide (`references/python_mcp_server.md`): server initialization patterns, Pydantic model examples, tool registration with `@mcp.tool`, complete working examples, quality checklist
- TypeScript Implementation Guide (`references/node_mcp_server.md`): project structure, Zod schema patterns, tool registration with `server.registerTool`, complete working examples, quality checklist

**Evaluation Guide (Load During Phase 4)**

- Evaluation Guide (`references/evaluation.md`): question creation guidelines, answer verification strategies, XML format specifications, example questions and answers, running an evaluation with the provided scripts

---

## 6. skill-creator

**Added by:** Anthropic  
**Trigger:** Slash command + auto  
**Description:**  
Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.

---

### SKILL.md

#### Skill Creator

A skill for creating new skills and iteratively improving them.

**At a high level, the process of creating a skill goes like this:**

1. Decide what you want the skill to do and roughly how it should do it
2. Write a draft of the skill
3. Create a few test prompts and run claude-with-access-to-the-skill on them
4. Help the user evaluate the results both qualitatively and quantitatively
   - While the runs happen in the background, draft some quantitative evals if there aren't any (or modify existing ones). Then explain them to the user.
   - Use the `eval-viewer/generate_review.py` script to show the user the results, and also let them look at the quantitative evals
5. Rewrite the skill based on feedback from the user's evaluation of the results
6. Repeat until satisfied
7. Expand the test set and try again at larger scale

Your job when using this skill is to figure out where the user is in this process and then jump in at the right place.

Of course, always be flexible — if the user says "I don't need to run a bunch of evals", respect that.

After the skill is done, you can also run the skill description optimizer to improve triggering accuracy.

---

#### Communicating with the user

The skill creator is liable to be used by people across a wide range of familiarity with coding jargon. Please pay attention to context cues to understand how to phrase your communication.

Default: avoid jargon. It's OK to briefly explain terms if in doubt. Specifically:

- "evaluation" and "benchmark" are borderline, but OK
- For "JSON" and "assertion" you want to see serious cues from the user that they know what those things are

---

#### Creating a skill

##### Capture Intent

Start by understanding the user's intent. The current conversation might already contain a workflow to formalize. Questions to ask:

- What should this skill enable Claude to do?
- When should this skill trigger? (what user phrases/contexts)
- What's the expected output format?
- Should we set up test cases to verify the skill works?

##### Interview and Research

Proactively ask questions about edge cases, input/output formats, example files, success criteria, and similar existing skills.

Check available MCPs — if useful for research (searching docs, finding similar skills, looking up best practices), use them proactively.

##### Write the SKILL.md

Based on the user interview, fill in these components:

- **name**: Skill identifier
- **description**: When to trigger, what it does. This is the primary triggering mechanism — include both what the skill does AND when to use it
- **compatibility**: Required tools, dependencies (optional, rarely needed)
- The rest of the skill content

---

#### Skill Writing Guide

##### Anatomy of a Skill

skill-name/
├── SKILL.md (required)
│ ├── YAML frontmatter (name, description required)
│ └── Markdown instructions
└── Bundled Resources (optional)
├── scripts/ - Executable code for deterministic/repetitive tasks
├── references/ - Docs loaded into context as needed
└── assets/ - Files used in output (templates, icons, fonts)

##### Progressive Disclosure

Skills use a three-level loading system:

- **Metadata** (name + description): Always in context (~100 words)
- **SKILL.md body**: In context whenever skill triggers (<500 lines ideal)
- **Bundled resources**: As needed (unlimited; scripts can execute without loading)

Key patterns:

- Keep SKILL.md under 500 lines; if approaching the limit, add an additional layer of hierarchy
- Reference files clearly from SKILL.md with guidance on when to read them
- For large reference files (>300 lines), include a table of contents

**Domain organization** — when a skill supports multiple domains/frameworks, organize by variant:
cloud-deploy/
├── SKILL.md (workflow + selection)
└── references/
├── aws.md
├── gcp.md
└── azure.md

Claude reads only the relevant reference file.

##### Principle of Lack of Surprise

Skills must not contain malware, exploit code, or any content that could harm users or systems. This goes without saying.

##### Writing Patterns

Prefer using the imperative form in instructions.

**Defining output formats:**

```markdown
Report structure
ALWAYS use this exact template:
[Title]
Executive summary
Key findings
Recommendations
```

**Examples pattern:**

```markdown
Commit message format
Example 1:
Input: Added user authentication with JWT tokens
Output: feat(auth): implement JWT-based authentication
```

##### Writing Style

Try to explain to the model WHY things are important in lieu of heavy-handed MUSTs. Use theory of mind — today's LLMs are smart and respond well to reasoning.

---

#### Test Cases

After writing the skill draft, come up with 2-3 realistic test prompts. Save to `evals/evals.json`. Don't write assertions yet — just the prompts.

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": "...",
      "prompt": "User's task prompt",
      "expected_output": "Description of expected result",
      "files": []
    }
  ]
}
```

See `references/schemas.md` for the full schema (including the `assertions` field, which you'll add later).

---

#### Running and evaluating test cases

This section is one continuous sequence — don't stop partway through. Do NOT use `/skill-test` or any other testing shortcut.

Put results in `<skill-name>-workspace/` as a sibling to the skill directory, organized by iteration:
<skill-name>-workspace/
├── iteration-1/
│ ├── eval-0/
│ └── eval-1/
└── iteration-2/
├── eval-0/
└── eval-1/

##### Step 1: Spawn all runs (with-skill AND baseline) in the same turn

For each test case, spawn two subagents in the same turn — one with the skill, one without.

**With-skill run:**
Execute this task:

Skill path: <path-to-skill>
Task: <eval prompt>
Input files: <eval files if any, or "none">
Save outputs to: <workspace>/iteration-<N>/eval-<ID>/with_skill/outputs/
Outputs to save: <what the user cares about>

**Baseline run (same prompt, but baseline depends on context):**

- Creating a new skill: no skill at all, save to `without_skill/outputs/`
- Improving an existing skill: the old version (`cp -r <skill-path> <workspace>/skill-snapshot/`), save to `old_skill/outputs/`

Write an `eval_metadata.json` for each test case:

```json
{
  "eval_id": "...",
  "eval_name": "descriptive-name-here",
  "prompt": "The user's task prompt",
  "assertions": []
}
```

##### Step 2: While runs are in progress, draft assertions

Don't just wait — draft quantitative assertions in `evals/evals.json`. Good assertions are objectively verifiable and have descriptive names.

##### Step 3: As runs complete, capture timing data

When each subagent task completes, save `total_tokens` and `duration_ms` immediately to `timing.json`:

```json
{
  "total_tokens": 84852,
  "duration_ms": 23332,
  "total_duration_seconds": 23.3
}
```

This is the only opportunity to capture this data — it comes through the task notification and isn't accessible afterward.

##### Step 4: Grade, aggregate, and launch the viewer

1. **Grade each run** — spawn a grader subagent (see `agents/grader.md`) that reads and evaluates each assertion against the outputs. Grades go in `grading.json` with fields: `text`, `passed`, `evidence`, `name`, `met`, `details`.

2. **Aggregate into benchmark:**

```bash
python -m scripts.aggregate_benchmark workspace/iteration-N --skill-name name
```

Produces `benchmark.json` and `benchmark.md` with pass_rate, time, and tokens for each configuration.

3. **Do an analyst pass** — read benchmark data and surface patterns the aggregate stats might hide. See `agents/analyzer.md`.

4. **Launch the viewer:**

```bash
nohup python <skill-creator-path>/eval-viewer/generate_review.py \
  workspace/iteration-N \
  --skill-name "my-skill" \
  --benchmark workspace/iteration-N/benchmark.json \
  >/dev/null &
VIEWER_PID=$!
```

For iteration 2+, also pass `--previous-workspace <workspace>/iteration-<N-1>`.

> **Cowork / headless environments:** If `webbrowser.open()` is not available, use `--static <output_path>` to write a standalone HTML file instead.

Tell the user: "I've opened the results in your browser. There are two tabs — 'Outputs' lets you click through test cases, and 'Benchmark' shows the stats summary."

**What the user sees in the viewer:**

- **Prompt**: the task that was given
- **Output**: the files the skill produced, rendered inline where possible
- **Previous Output** (iteration 2+): collapsed section showing last iteration's output
- **Formal Grades** (if grading was run): collapsed section showing assertion pass/fail
- **Feedback**: a textbox that auto-saves as they type
- **Previous Feedback** (iteration 2+): their comments from last time

Navigation via prev/next buttons or arrow keys. When done, user clicks "Submit All Reviews" which writes `feedback.json`.

##### Step 5: Read the feedback

When the user tells you they're done, read `feedback.json`:

```json
{
  "reviews": [
    {
      "run_id": "eval-0-with_skill",
      "feedback": "the chart is missing axis labels",
      "timestamp": "..."
    },
    { "run_id": "eval-1-with_skill", "feedback": "", "timestamp": "..." },
    {
      "run_id": "eval-2-with_skill",
      "feedback": "perfect, love this",
      "timestamp": "..."
    }
  ],
  "status": "complete"
}
```

Empty feedback means the user thought it was fine. Focus improvements on test cases where they left feedback.

Kill the viewer server when done:

```bash
kill $VIEWER_PID >/dev/null
```

---

#### Improving the skill

This is the heart of the loop. The user has reviewed the results — now apply what was learned.

**How to think about improvements:**

- **Generalize from the feedback.** Generalize, don't overfit to specific test cases. If a user said "this chart is missing axis labels," the fix is "always include axis labels" not "add axis labels to this one chart."
- **Keep the prompt lean.** Remove things that aren't pulling their weight. Read the transcripts, not just the final outputs.
- **Explain the why.** Try hard to explain the reasoning behind everything you're asking the model to do. Today's LLMs are _smart_. They have good judgment.
- **Look for repeated work across test cases.** If subagents all independently wrote similar utility functions, factor that out into `scripts/` (e.g., `create_docx.py`, `build_chart.py`).

**The iteration loop:**

1. Apply improvements to the skill
2. Rerun all test cases into a new `iteration-<N+1>/` directory (including baseline runs)
3. Launch the reviewer with `--previous-workspace` pointing at the previous iteration
4. Wait for the user to review and tell you they're done
5. Read the new feedback, improve again, repeat

Keep going until:

- The user says they're happy
- The feedback is all empty (everything looks good)
- You're not making meaningful progress

---

#### Advanced: Blind comparison

For more rigorous comparison between two versions of a skill, use `agents/comparator.md` and `agents/analyzer.md`. This is optional and most users won't need it.

---

#### Description Optimization

The `description` field in SKILL.md frontmatter is the primary mechanism that determines whether Claude triggers a skill.

##### Step 1: Generate trigger eval queries

Create 20 eval queries — a mix of should-trigger and should-not-trigger. Save as JSON:

```json
[
  { "query": "the user prompt", "should_trigger": true },
  { "query": "another prompt", "should_trigger": false }
]
```

Queries must be realistic. Examples of what real users would type:

- ❌ Bad: `"Format this data"`, `"Extract text from PDF"`, `"Create a chart"`
- ✅ Good: Detailed, specific queries with realistic phrasing and context

For should-trigger queries (8-10): want different phrasings of the same intent — some verbose, some terse, some implicit.

For should-not-trigger queries (8-10): the

Ask before acting
Claude is AI and can make mistakes. Please double-check responses.
