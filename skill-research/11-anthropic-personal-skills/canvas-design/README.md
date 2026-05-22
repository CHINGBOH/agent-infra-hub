# canvas-design

**Added by:** Anthropic  
**Trigger:** Slash command + auto  
**类型：** A型 SKILL.md Skill

---

## Description（触发描述）

**English:**  
Create beautiful visual art in `.png` and `.pdf` documents using design philosophy. Use this skill when the user asks to create a poster, piece of art, design, or other static piece. Create original visual designs, never copying existing artists' work to avoid copyright violations.

**中文：**  
使用设计哲学在 `.png` 和 `.pdf` 文档中创作精美的视觉艺术。当用户要求创建海报、艺术品、设计或其他静态作品时使用。创作原创视觉设计，避免侵权。

---

## 核心架构：两阶段创作

```
用户请求
    ↓
阶段一：设计哲学创作（.md 文件）
    ├── 命名运动（1-2词）："Brutalist Joy"、"Chromatic Silence"
    ├── 阐明哲学（4-6段）：空间/颜色/比例/构图/层次
    └── 识别用户请求中的细微概念线索
    ↓
阶段二：画布创作（.pdf 或 .png 文件）
    ├── 基于哲学在画布上表达
    ├── 使用 ./canvas-fonts 目录的字体
    └── 精炼到博物馆级别
```

**与 algorithmic-art 的平行结构：** 两个 skill 都使用相同的两阶段模式，但载体不同：
- algorithmic-art → 动态 HTML（p5.js）
- canvas-design → 静态 PDF/PNG（画布）

---

## SKILL.md 完整内容

These are instructions for creating design philosophies — aesthetic movements that are then EXPRESSED VISUALLY. Output only `.md` files, `.pdf` files, and `.png` files.

Complete this in two steps:
1. Design Philosophy Creation (.md file)
2. Express by creating it on a canvas (.pdf or .png file)

---

### DESIGN PHILOSOPHY CREATION

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

- *"Concrete Poetry"*: Communication through monumental form and bold geometry. Massive color blocks, sculptural typography, Brutalist spatial divisions, Polish poster energy meets Le Corbusier.
- *"Chromatic Language"*: Color as the primary information system. Geometric precision where color zones create meaning. Think Josef Albers' interaction meets data visualization.
- *"Analog Meditation"*: Quiet visual contemplation through texture and breathing room. Paper grain, ink bleeds, vast negative space. Japanese photobook aesthetic.
- *"Organic Systems"*: Natural clustering and modular growth patterns. Rounded forms, organic arrangements, color from nature through architecture.
- *"Geometric Silence"*: Pure order and restraint. Grid-based precision, bold photography or stark graphics, dramatic negative space. Swiss formalism meets Brutalist material honesty.

**ESSENTIAL PRINCIPLES**
- VISUAL PHILOSOPHY: An aesthetic worldview to be expressed through design
- MINIMAL TEXT: Sparse, essential-only, integrated as visual element — never lengthy
- SPATIAL EXPRESSION: Ideas communicate through space, form, color, composition
- ARTISTIC FREEDOM: Provide creative room for visual interpretation
- PURE DESIGN: Making ART OBJECTS, not documents with decoration
- EXPERT CRAFTSMANSHIP: Final work must look meticulously crafted, labored over with care

---

### DEDUCING THE SUBTLE REFERENCE

CRITICAL STEP: Before creating the canvas, identify the subtle conceptual thread from the original request.

THE ESSENTIAL PRINCIPLE: The topic is a subtle, niche reference embedded within the art — not always literal, always sophisticated. Think like a jazz musician quoting another song — only those who know will catch it, but everyone appreciates the music.

---

### CANVAS CREATION

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

### FINAL STEP

> The user ALREADY said "It isn't perfect enough. It must be pristine, a masterpiece of craftsmanship, as if it were about to be displayed in a museum."

To refine: avoid adding more graphics; instead refine what has been created and make it extremely crisp. Ask: "How can I make what's already here more of a piece of art?"

---

### MULTI-PAGE OPTION

When additional pages are requested, create more creative pages along the same design philosophy but distinctly different. Bundle in the same `.pdf` or multiple `.png` files. Treat the first page as a single page in a coffee table book waiting to be filled.

---

## 关键资源文件

| 文件/目录 | 作用 | 何时使用 |
|-----------|------|---------|
| `./canvas-fonts` | 可用字体目录 | 画布创作时搜索使用 |

---

## 研究笔记

**"博物馆级别"的预设反馈：** SKILL.md 中内置了用户的否定反馈——"还不够完美，必须无瑕疵，像要在博物馆展出的艺术杰作"——并预先给出了如何应对这个反馈的指导（精炼而非增加）。这是一个有趣的防御性设计。

**哲学命名的美学：** Anthropic 在 skill 中给出的哲学示例名称（"Concrete Poetry"、"Chromatic Silence"等）体现了对艺术史的深度理解，这些不是随机命名。
