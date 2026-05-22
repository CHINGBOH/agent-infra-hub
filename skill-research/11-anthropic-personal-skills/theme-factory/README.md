# theme-factory

**Added by:** Anthropic  
**Trigger:** Slash command + auto  
**类型：** A型 SKILL.md Skill  
**文档状态：** ⚠️ 内容基于官方 Skill 模式推断重构（原始 SKILL.md 未被抓取到）

---

## Description（触发描述）

**English:**  
Apply themes and styles to artifacts. Use this when users want to restyle, re-theme, or apply a visual design system to an existing HTML artifact or component — without changing its functionality.

**中文：**  
为 Artifact 应用主题样式。当用户想对已有 HTML Artifact 或组件重新配色、调整风格、应用设计系统时使用 —— 功能不变，只改视觉。

---

## 与其他样式 Skill 的区别

| Skill | 适用场景 |
|-------|---------|
| `theme-factory` | **对已有 Artifact** 应用/更换主题（不改功能） |
| `frontend-design` | **从零创建**视觉鲜明的新界面 |
| `canvas-design` | 设计海报/静态视觉作品（PDF/PNG） |
| `web-artifacts-builder` | 构建新的多组件 HTML App |

---

## SKILL.md 内容（推断重构）

> **注：** 以下内容根据 Anthropic 官方 Skills 的共通模式推断重构，供参考。如需原文，在 claude.ai/customize/skills 中启用此 skill 后可直接查看。

---

### 核心工作方式

theme-factory 是一个**主题应用器**，而非从零创建界面。工作流程：

```
读取现有 Artifact → 分析 CSS 结构 → 选择/设计主题 → 应用 → 输出新版本
```

关键原则：**只改样式，不改结构和逻辑**。

---

### 触发流程

#### Step 1：分析现有 Artifact

读取用户的 HTML Artifact，提取：

- 当前颜色方案（背景、前景、强调色）
- 字体家族和大小层级
- 间距系统（margin/padding 规律）
- 组件类型（卡片、按钮、表格、表单等）
- 现有 CSS 变量（如有）

**诊断问题：**
- 视觉层级是否清晰？
- 色彩对比度是否达标？
- 整体风格一致性？

---

#### Step 2：主题方向选择

根据用户需求或 Artifact 用途确定主题方向：

**预设主题系列（推测）：**

| 主题 | 特征 | 适用场景 |
|------|------|---------|
| **Minimal Light** | 纯白背景、细灰边框、无衬线字体 | 工具类、数据展示 |
| **Dark Pro** | 深灰背景、高对比文字、等宽代码字体 | 开发工具、终端风格 |
| **Brand Warm** | 暖色调、Serif 标题、柔和阴影 | 内容展示、营销 |
| **Corporate Clean** | 蓝色调、严谨布局、系统字体 | 企业应用、报告 |
| **Playful** | 高饱和色、圆角、活泼字体 | 教育、娱乐 |
| **High Contrast** | 黑白 + 单一强调色，无障碍优先 | 可访问性要求高的场景 |

---

#### Step 3：CSS 设计令牌系统

**核心：将所有视觉属性转化为 CSS 变量**

```css
:root {
  /* Color Tokens */
  --color-bg-primary:    #ffffff;
  --color-bg-secondary:  #f8f9fa;
  --color-bg-tertiary:   #f0f2f5;
  --color-surface:       #ffffff;
  --color-border:        #e5e7eb;

  --color-text-primary:   #111827;
  --color-text-secondary: #6b7280;
  --color-text-tertiary:  #9ca3af;

  --color-accent:         #2563eb;
  --color-accent-hover:   #1d4ed8;
  --color-accent-light:   #dbeafe;

  --color-success:  #059669;
  --color-warning:  #d97706;
  --color-error:    #dc2626;

  /* Typography Tokens */
  --font-display: 'Font Name', sans-serif;
  --font-body:    'Font Name', sans-serif;
  --font-mono:    'Font Name', monospace;

  --text-xs:   0.75rem;
  --text-sm:   0.875rem;
  --text-base: 1rem;
  --text-lg:   1.125rem;
  --text-xl:   1.25rem;
  --text-2xl:  1.5rem;

  /* Spacing Tokens */
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;

  /* Shape Tokens */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-full: 9999px;

  /* Shadow Tokens */
  --shadow-sm:  0 1px 2px rgba(0,0,0,0.05);
  --shadow-md:  0 4px 6px rgba(0,0,0,0.07);
  --shadow-lg:  0 10px 15px rgba(0,0,0,0.10);
}
```

**Dark Theme 覆盖：**

```css
[data-theme="dark"] {
  --color-bg-primary:   #0f172a;
  --color-bg-secondary: #1e293b;
  --color-surface:      #1e293b;
  --color-border:       #334155;
  --color-text-primary: #f1f5f9;
  --color-text-secondary: #94a3b8;
}
```

---

#### Step 4：组件样式适配

对 Artifact 中每类组件使用令牌系统重写样式：

```css
/* Button — 使用令牌 */
.btn-primary {
  background: var(--color-accent);
  color: white;
  padding: var(--space-2) var(--space-4);
  border-radius: var(--radius-md);
  font-family: var(--font-body);
  font-size: var(--text-sm);
  transition: background 0.15s ease;
}
.btn-primary:hover {
  background: var(--color-accent-hover);
}

/* Card — 使用令牌 */
.card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  box-shadow: var(--shadow-sm);
}
```

---

#### Step 5：主题切换器（可选）

如 Artifact 支持，添加主题切换按钮：

```javascript
function applyTheme(themeName) {
  document.documentElement.setAttribute('data-theme', themeName);
  localStorage.setItem('preferred-theme', themeName);
}

// 持久化用户偏好
const savedTheme = localStorage.getItem('preferred-theme');
if (savedTheme) applyTheme(savedTheme);
```

---

### 质量检查清单

- [ ] 色彩对比度 ≥ 4.5:1（WCAG AA 标准）
- [ ] 所有颜色通过变量引用，无硬编码色值
- [ ] 功能性代码（JS 逻辑）未被修改
- [ ] 组件视觉一致（按钮、表单、卡片同一设计语言）
- [ ] 响应式样式未被破坏
- [ ] 字体回退链有效（`font-family: 'Font', fallback, sans-serif`）

---

## 典型触发场景

- "这个 HTML 看起来太默认了，帮我做一个深色专业主题"
- "Apply a warm, editorial theme to this dashboard"
- "把这个工具改成 Anthropic 风格（白底、圆角、蓝色强调色）"
- "这个界面颜色太乱，帮我统一一下设计语言"

## 不触发场景

- 从零创建新界面 → 用 `frontend-design`
- 改变组件功能或布局 → 直接编辑 HTML
- 创建静态设计图 → 用 `canvas-design`

---

## 设计哲学（推测）

theme-factory 的核心价值主张：**视觉风格和功能逻辑分离**。

一个良好应用了 theme-factory 的 Artifact：
- 可以通过切换 CSS 变量实现完全不同的视觉风格
- 功能代码不含任何颜色、字体的硬编码
- 设计令牌使后续主题调整成本极低

---

## 数据来源说明

原始 SKILL.md 未在 2026-05-23 的 claude.ai/customize/skills 抓取中获取。本文档内容基于以下来源推断重构：

- Anthropic 官方 7 个已完整记录的 Personal Skills 的共通模式
- `frontend-design` 插件 SKILL.md（CSS 设计美学规范）
- CSS 设计令牌系统最佳实践（Design Tokens W3C）
- 与 `canvas-design` 两阶段模式的对比分析

如需原文，建议在 claude.ai 中直接启用该 skill 查看。
