# slack-gif-creator

**Added by:** Anthropic  
**Trigger:** Slash command + auto  
**类型：** A型 SKILL.md Skill（工具包模式）

---

## Description（触发描述）

**English:**  
Knowledge and toolkit for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request creating an animated GIF for Slack.

**中文：**  
用于创建针对 Slack 优化的动态 GIF 的知识和工具包。提供约束条件、验证工具和动画概念。当用户请求为 Slack 制作动态 GIF 时使用。

---

## Slack GIF 技术规格

| 参数 | Emoji GIF | 消息 GIF |
|------|-----------|---------|
| 尺寸 | 128×128 px | 480×480 px |
| 推荐 FPS | 10-30（越低文件越小） | 10-30 |
| 颜色数 | 48-128 | 48-128 |
| 时长限制 | ≤3 秒 | 无严格限制 |

---

## SKILL.md 完整内容

### Slack Requirements

**Dimensions:**
- Emoji GIF: 128×128 (recommended)
- Message GIF: 480×480

**Parameters:**
- FPS: 10-30 (lower = smaller file size)
- Colors: 48-128 (fewer = smaller)
- Duration: Keep Emoji GIFs under 3 seconds

---

### Core Workflow

```python
from core.gif_builder import GIFBuilder
from PIL import Image, ImageDraw

# 1. Create builder
builder = GIFBuilder(width=128, height=128, fps=10)

# 2. Generate frames
for i in range(12):
    frame = Image.new('RGB', (128, 128), (240, 248, 255))
    draw = ImageDraw.Draw(frame)
    # Draw animation using PIL primitives
    builder.add_frame(frame)

# 3. Save and optimize
builder.save('output.gif', num_colors=48, optimize_for_emoji=True)
```

---

### Drawing Graphics

**Using uploaded images:**
```python
from PIL import Image
uploaded = Image.open('file.png')
# Use directly, or reference only for color/style
```

**Drawing from scratch:**
```python
from PIL import ImageDraw
draw = ImageDraw.Draw(frame)

# Circle/ellipse
draw.ellipse([x1, y1, x2, y2], fill=(r,g,b), outline=(r,g,b), width=3)
# Polygon (stars, triangles, etc.)
draw.polygon(points, fill=(r,g,b), outline=(r,g,b), width=3)
# Lines
draw.line([(x1,y1),(x2,y2)], fill=(r,g,b), width=5)
# Rectangles
draw.rectangle([x1,y1,x2,y2], fill=(r,g,b), outline=(r,g,b), width=3)
```

**Tips for making graphics look good:**
- Use thicker lines (width=2 or higher)
- Add visual depth (gradient backgrounds, layered shapes)
- Make shapes interesting (highlights, halos, patterns)

---

## 依赖库

| 库 | 用途 |
|----|------|
| `PIL` (Pillow) | 图像绘制、帧合成 |
| `core.gif_builder` | GIF 构建和优化工具（skill 内置） |

---

## 关键资源文件

| 文件/目录 | 作用 |
|-----------|------|
| `core/gif_builder.py` | GIFBuilder 类实现 |
| `requirements.txt` | Python 依赖（PIL 等） |

---

## 研究笔记

**工具包型 skill 的特点：** slack-gif-creator 包含了 `core/` 目录（实际的 Python 库），这使它介于 A型（SKILL.md）和 C型（Plugin 包）之间。它的 SKILL.md 提供工作流指导，而 `core/` 提供实际的代码工具。

**文件结构推断：**
```
slack-gif-creator/
├── SKILL.md
├── core/
│   └── gif_builder.py      ← GIFBuilder 类
└── requirements.txt         ← PIL 等依赖
```

**注意：** 爬取的内容仅包含中文版（英文版的爬取数据在 skill-creator 之后中断），但核心工作流和代码示例已完整。
