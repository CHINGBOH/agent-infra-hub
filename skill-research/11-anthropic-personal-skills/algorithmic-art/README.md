# algorithmic-art

**Added by:** Anthropic  
**Trigger:** Slash command + auto  
**类型：** A型 SKILL.md Skill

---

## Description（触发描述）

**English:**  
Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art, algorithmic art, flow fields, or particle systems. Create original algorithmic art rather than copying existing artists' work to avoid copyright violations.

**中文：**  
使用 p5.js 通过种子随机性和交互式参数探索创作生成艺术。当用户请求使用代码创作艺术、生成艺术、算法艺术、流场或粒子系统时使用。创作原创算法艺术，避免复制现有艺术家的作品。

---

## 核心架构：两阶段创作

```
用户请求
    ↓
阶段一：算法哲学创作（.md 文件）
    ├── 命名运动（1-2词）
    ├── 阐明哲学（4-6段）
    └── 捕捉细微概念线索
    ↓
阶段二：p5.js 实现（.html + .js 文件）
    ├── 步骤0：读取 templates/viewer.html（必须！）
    ├── 在模板基础上实现算法
    └── 保留所有固定部分，只替换可变部分
```

**关键原则：** 哲学文本是创作过程的中间产物，不是最终输出给用户的文档——它是第二阶段的创作指南。

---

## SKILL.md 完整内容

### ALGORITHMIC PHILOSOPHY CREATION

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

- *"Organic Turbulence"*: Chaos constrained by natural law, order emerging from disorder. Flow fields driven by layered Perlin noise. Thousands of particles following vector forces, their trails accumulating into organic density maps.
- *"Quantum Harmonics"*: Discrete entities exhibiting wave-like interference patterns. Particles initialized on a grid, each carrying a phase value that evolves through sine waves.
- *"Recursive Whispers"*: Self-similarity across scales, infinite depth in finite space. Branching structures that subdivide recursively, constrained by golden ratios.
- *"Field Dynamics"*: Invisible forces made visible through their effects on matter. Vector fields constructed from mathematical functions or noise.
- *"Stochastic Crystallization"*: Random processes crystallizing into ordered structures. Randomized circle packing or Voronoi tessellation.

**ESSENTIAL PRINCIPLES**
- ALGORITHMIC PHILOSOPHY: Creating a computational worldview to be expressed through code
- PROCESS OVER PRODUCT: Beauty emerges from the algorithm's execution — each run is unique
- PARAMETRIC EXPRESSION: Ideas communicate through mathematical relationships, forces, behaviors
- ARTISTIC FREEDOM: Provide creative implementation room
- PURE GENERATIVE ART: Making LIVING ALGORITHMS, not static images
- EXPERT CRAFTSMANSHIP: Final algorithm must feel meticulously crafted, refined through countless iterations

---

### DEDUCING THE CONCEPTUAL SEED

CRITICAL STEP: Before implementing, identify the subtle conceptual thread from the original request.

THE ESSENTIAL PRINCIPLE: The concept is a subtle, niche reference embedded within the algorithm — not always literal, always sophisticated. Someone familiar with the subject should feel it intuitively, while others simply experience a masterful generative composition.

---

### P5.JS IMPLEMENTATION

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

### INTERACTIVE ARTIFACT CREATION

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

---

## 关键资源文件

| 文件 | 作用 | 何时读取 |
|------|------|---------|
| `templates/viewer.html` | 所有 HTML Artifact 的必需起点 | P5.js 实现前必须读取 |
| `templates/generator_template.js` | p5.js 最佳实践参考 | 参考，非必须 |

---

## 研究笔记

**与 canvas-design 的对比：**  
两者都是两阶段创作模式（哲学 → 实现），但：
- algorithmic-art：动态交互式 HTML，使用 p5.js，输出 `.html` + `.js`
- canvas-design：静态艺术品，输出 `.pdf` 或 `.png`

**设计亮点：**  
"先读模板"的强制步骤（STEP 0）是一个有趣的约束模式——通过 SKILL.md 中的强制指令，确保输出风格一致性。
