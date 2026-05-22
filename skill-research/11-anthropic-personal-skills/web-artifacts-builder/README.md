# web-artifacts-builder

**Added by:** Anthropic  
**Trigger:** Slash command + auto  
**类型：** A型 SKILL.md Skill  
**文档状态：** ⚠️ 内容基于官方 Skill 模式推断重构（原始 SKILL.md 未被抓取到）

---

## Description（触发描述）

**English:**  
Build complex multi-component HTML artifacts. Use this when users need to create rich, interactive HTML applications with multiple distinct sections, components, or functional areas — dashboards, tools, multi-panel apps, etc.

**中文：**  
构建复杂多组件 HTML Artifact。当用户需要创建包含多个独立区域、组件或功能模块的富交互 HTML 应用时使用 —— 仪表盘、工具类应用、多面板 App 等。

---

## 与其他 HTML Skill 的区别

| Skill | 适用场景 |
|-------|---------|
| `web-artifacts-builder` | 多组件复杂 HTML App（仪表盘、工具、多面板） |
| `algorithmic-art` | 单一生成艺术展示（p5.js 全屏交互） |
| `frontend-design` | 生产级单页面组件（强设计感，视觉优先） |
| `playground` | 单一主题的参数探索交互器 |

---

## SKILL.md 内容（推断重构）

> **注：** 以下内容根据 Anthropic 官方 Skills 的共通模式（algorithmic-art、playground、frontend-design）推断重构，供参考。如需原文，在 claude.ai/customize/skills 中启用此 skill 后可直接查看。

---

### 核心工作方式

构建包含多个功能组件的复杂 HTML Artifact。所有输出为单一 `.html` 文件，内联所有 CSS 和 JS，无外部依赖。

**典型组件类型：**
- 导航栏 / 侧边栏
- 数据展示卡片 / 列表
- 图表区域（内联 SVG 或 Canvas）
- 模态框 / 对话框
- 表单 + 数据输入
- 状态管理区（通知、进度、筛选）

---

### 构建流程

#### Step 1：组件分解

收到需求后，首先完成组件规划：

```
1. 识别主要功能区域（每个区域 = 一个组件）
2. 确定组件间的数据流方向
3. 定义全局状态对象
4. 规划布局骨架（CSS Grid / Flexbox）
```

**关键问题：**
- 有多少个独立功能区？
- 哪些组件需要共享状态？
- 用户的主要操作路径是什么？

---

#### Step 2：架构设计

**状态管理模式（单一状态源）：**

```javascript
const state = {
  // 所有组件共享的数据
  data: [],
  filters: {},
  selectedItem: null,
  ui: { sidebarOpen: true, activeTab: 'overview' }
};

function setState(updates) {
  Object.assign(state, updates);
  renderAll(); // 全量重渲染，简单可靠
}

function renderAll() {
  renderHeader();
  renderSidebar();
  renderMainContent();
  renderStatusBar();
}
```

**组件函数模式：**

```javascript
function renderComponent(container, data) {
  container.innerHTML = `
    <div class="component-wrapper">
      ${buildComponentHTML(data)}
    </div>
  `;
  attachComponentListeners(container);
}
```

---

#### Step 3：实现要求

**布局：**
- 使用 CSS Grid 实现主布局骨架
- 使用 Flexbox 实现组件内部排列
- 必须响应式（最小支持 768px 宽度）
- 固定 viewport 高度，内容区滚动

**样式：**
- CSS 变量定义设计令牌（颜色、间距、字体）
- 组件样式命名空间隔离（BEM 或前缀）
- 动画使用 CSS transition（避免 JS 动画）

**交互：**
- 所有用户操作通过 `setState()` 更新状态
- 每次状态变更触发相关组件重渲染
- 操作反馈即时可见（加载、成功、错误状态）

---

#### Step 4：质量检查

完成后必须验证：

- [ ] 所有组件数据连通（修改一处影响相关组件）
- [ ] 空状态有占位展示（无数据时不破版）
- [ ] 错误状态有处理（输入验证、边界条件）
- [ ] 组件独立可复用（内部逻辑不泄漏）

---

### 常见组件模板

#### 仪表盘布局

```html
<div class="app" style="display:grid; grid-template-rows:60px 1fr; grid-template-columns:240px 1fr; height:100vh">
  <header class="header" style="grid-column:1/-1">...</header>
  <nav class="sidebar">...</nav>
  <main class="content" style="overflow-y:auto">...</main>
</div>
```

#### 数据表 + 筛选器

```javascript
function renderTable(data, filters) {
  const filtered = applyFilters(data, filters);
  return `
    <div class="table-toolbar">${renderFilters(filters)}</div>
    <table class="data-table">
      <thead>${renderTableHead()}</thead>
      <tbody>${filtered.map(renderRow).join('')}</tbody>
    </table>
    <div class="pagination">${renderPagination(filtered.length)}</div>
  `;
}
```

#### 模态框

```javascript
function openModal(content) {
  setState({ modal: { open: true, content } });
}

function renderModal() {
  if (!state.modal?.open) return '';
  return `
    <div class="modal-overlay" onclick="closeModal()">
      <div class="modal-box" onclick="event.stopPropagation()">
        ${state.modal.content}
        <button onclick="closeModal()">×</button>
      </div>
    </div>
  `;
}
```

---

### 与 algorithmic-art 的关键区别

| 维度 | web-artifacts-builder | algorithmic-art |
|------|----------------------|-----------------|
| 模板要求 | 无强制起始模板 | **必须**先读 `templates/viewer.html` |
| 核心挑战 | 多组件状态协调 | 生成算法设计 |
| 输出格式 | 单 HTML（含业务逻辑） | HTML + JS（生成艺术） |
| 设计风格 | 功能导向 | 艺术导向 |

---

## 典型触发场景

- "帮我做一个数据仪表盘，有图表、筛选和表格"
- "Create a project management tool with kanban board"
- "Build a multi-tab settings panel with form validation"
- "做一个有侧边导航和主内容区的后台界面"

## 不触发场景

- 简单单页面（无多组件）→ 用 `frontend-design`
- 生成艺术 → 用 `algorithmic-art`
- 参数探索工具 → 用 `playground`

---

## 数据来源说明

原始 SKILL.md 未在 2026-05-23 的 claude.ai/customize/skills 抓取中获取。本文档内容基于以下来源推断重构：

- Anthropic 官方 7 个已完整记录的 Personal Skills 的共通模式
- `playground` 插件 SKILL.md（状态管理模式）
- `frontend-design` 插件 SKILL.md（HTML 实现规范）
- `algorithmic-art` Skill 的模板约束模式

如需原文，建议在 claude.ai 中直接启用该 skill 查看。
