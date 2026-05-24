# MCP Server 开发技能集（mcp-server-dev 插件）

来源：`~/.claude/plugins/marketplaces/claude-plugins-official/plugins/mcp-server-dev/`

该插件包含三个相互关联的 skill，覆盖 MCP server 开发的完整路径。

---

## 三个 Skill 的关系

```
用户说"build an MCP server"
          ↓
    build-mcp-server      ← 入口 skill（决策引导）
    ├── 询问用例、受众、规模
    ├── 确定部署模型
    │   ├── ✅ Remote HTTP  → 在 build-mcp-server 内直接完成
    │   ├── UI 交互需求    → 移交 build-mcp-app
    │   └── 本地运行需求   → 移交 build-mcpb
    └── 确定工具设计模式
```

---

## Skill 1：build-mcp-server（入口决策层）

**文件**：`build-mcp-server/SKILL.md`

### 5个决策阶段

| 阶段 | 内容 |
|------|------|
| Phase 1 | 询问用例（连接什么？用户是谁？有多少操作？需要交互UI吗？什么认证？） |
| Phase 2 | 推荐部署模型（Remote HTTP / Elicitation / MCP App / MCPB / Local stdio） |
| Phase 3 | 工具设计模式（一操作一工具 vs Search+Execute） |
| Phase 4 | 框架选择（TypeScript SDK vs FastMCP） |
| Phase 5 | 脚手架或移交其他 skill |

### 部署模型决策矩阵

| 场景 | 推荐部署 | 工具模式 |
|------|----------|---------|
| 包装小型 SaaS API | Remote HTTP | 一操作一工具 |
| 包装大型 SaaS API（50+端点） | Remote HTTP | Search+Execute |
| SaaS API + 富交互表单/选择器 | MCP App（远程） | 一操作一工具 |
| 驱动本地桌面应用 | MCPB | 一操作一工具 |
| 本地应用 + 会话内 UI | MCP App（MCPB） | 一操作一工具 |
| 读写本地文件系统 | MCPB | 视规模而定 |
| 个人原型 | Local stdio | 最快即可 |

### 核心原则：先 load Claude 特定文档

```
在回答任何问题或脚手架之前，先抓取：
https://claude.com/docs/llms-full.txt
（Claude 连接器文档的完整导出）
```

### 工具设计规范（references/tool-design.md）

**描述即契约**：
```
# 好的工具描述
search_issues — 在标题和内容中搜索 issue。返回最多 `limit` 条，按最新排序。
               不搜索评论或 PR——用 search_comments/search_prs。

# 差的工具描述  
search_issues — 搜索 issue。
```

**参数 schema 要紧**：
```typescript
{
  query: z.string().describe("关键词，支持引号短语"),
  status: z.enum(["open", "closed", "all"]).default("open").describe("..."),
  limit: z.number().int().min(1).max(50).default(10).describe("上限50"),
}
```

**工具注解（Anthropic 目录必须有）**：

| 注解 | 含义 | 主机行为 |
|------|------|---------|
| `readOnlyHint: true` | 无副作用 | 可自动批准 |
| `destructiveHint: true` | 删除/覆盖 | 弹出确认框 |
| `idempotentHint: true` | 可安全重试 | 可重试 |
| `openWorldHint: true` | 调用外部网络 | 可显示网络指示器 |

**Anthropic 目录硬性要求**：
- 每个工具必须有 `readOnlyHint`、`destructiveHint`、`title` 注解
- 工具名 ≤64 字符
- 读写操作必须分开为独立工具
- 工具描述不得指令 Claude 行为（视为 prompt injection）

---

## Skill 2：build-mcpb（本地捆绑包）

**文件**：`build-mcpb/SKILL.md`

### MCPB 是什么

MCPB（Model Context Protocol Bundle）= 将 MCP server 与运行时打包在一起的 `.mcpb` 文件。用户无需安装 Node/Python，一个文件搞定。

**使用前提**：server **必须**在用户本地机器运行。否则用 Remote HTTP。

### .mcpb 包结构

```
my-server.mcpb          (zip 压缩包)
├── manifest.json       ← 身份、入口、配置 schema、兼容性
├── server/             ← MCP server 代码
│   ├── index.js
│   └── node_modules/   ← 捆绑的依赖
└── icon.png
```

### manifest.json 格式

```json
{
  "$schema": "https://raw.githubusercontent.com/anthropics/mcpb/main/schemas/mcpb-manifest-v0.4.schema.json",
  "manifest_version": "0.4",
  "name": "my-server",
  "version": "0.1.0",
  "server": {
    "type": "node",
    "entry_point": "server/index.js",
    "mcp_config": {
      "command": "node",
      "args": ["${__dirname}/server/index.js"],
      "env": {
        "ROOT_DIR": "${user_config.rootDir}"
      }
    }
  },
  "user_config": {
    "rootDir": {
      "type": "directory",
      "title": "根目录",
      "required": true
    }
  },
  "compatibility": {
    "claude_desktop": ">=1.0.0",
    "platforms": ["darwin", "win32", "linux"]
  }
}
```

**关键**：`${__dirname}` 用于 bundle 内相对路径，`${user_config.key}` 引用安装时配置。

### 构建流程

```bash
# Node
npm install
npx esbuild src/index.ts --bundle --platform=node --outfile=server/index.js
npx @anthropic-ai/mcpb pack

# Python  
pip install -t server/vendor -r requirements.txt
npx @anthropic-ai/mcpb pack
```

### 安全警告

**MCPB 没有沙箱**。进程以完整用户权限运行，没有 manifest 级别的权限控制。路径校验、spawn 白名单全靠开发者自己写。

---

## Skill 3：build-mcp-app（交互 UI 组件）

**文件**：`build-mcp-app/SKILL.md`

### MCP App 是什么

在 MCP server 基础上增加 **UI resources**——嵌入聊天界面的交互式组件（picker、表单、图表、进度条等）。一次构建，可在 Claude 和 ChatGPT 等支持 apps surface 的主机中运行。

### 何时用 Widget vs Elicitation

| 需求 | Elicitation | Widget |
|------|-------------|--------|
| 确认是/否 | ✅ 够用 | 过度设计 |
| 从短 enum 选择 | ✅ 够用 | 过度设计 |
| 填写简单表单 | ✅ 够用 | 过度设计 |
| 从大型可搜索列表选择 | ❌ 不支持 | ✅ |
| 选择前视觉预览 | ❌ | ✅ |
| 图表/地图/diff 展示 | ❌ | ✅ |
| 实时进度 | ❌ | ✅ |

### 架构：工具 + 资源双注册

```typescript
// 1. 工具：返回数据，声明用哪个 UI
registerAppTool(server, "pick_contact", {
  description: "打开联系人选择器",
  inputSchema: { filter: z.string().optional() },
  _meta: { ui: { resourceUri: "ui://widgets/picker.html" } },
}, async ({ filter }) => {
  const contacts = await db.search(filter);
  return { content: [{ type: "text", text: JSON.stringify(contacts) }] };
});

// 2. 资源：提供 HTML
registerAppResource(server, "Contact Picker", "ui://widgets/picker.html", {},
  async () => ({
    contents: [{
      uri: "ui://widgets/picker.html",
      mimeType: RESOURCE_MIME_TYPE,  // "text/html;profile=mcp-app"
      text: pickerHtml,
    }],
  }),
);
```

### Widget 运行时 API（App 类）

| 方法 | 方向 | 用途 |
|------|------|------|
| `app.ontoolresult = fn` | 主机→Widget | 接收工具返回值 |
| `app.sendMessage({...})` | Widget→主机 | 向对话注入消息 |
| `app.updateModelContext({...})` | Widget→主机 | 静默更新上下文 |
| `app.callServerTool({name, arguments})` | Widget→Server | 调用 server 上其他工具 |
| `app.openLink({url})` | Widget→主机 | 打开链接（沙箱禁止 window.open） |
| `app.getHostContext()` | 主机→Widget | 主题、尺寸、displayMode |

### 关键注意事项

- `/*__EXT_APPS_BUNDLE__*/` 占位符必须被 server 替换为 ext-apps 的 bundle 内容——不能从 CDN 加载（CSP 会拦截）
- Widget 不能访问主机页面 DOM、cookie、storage
- 对外网络请求必须通过 `callServerTool` 路由（CSP 限制）
- Widget 要小而专一：picker 只管选，chart 只管展示

---

## 参考文件索引

### build-mcp-server/references/
- `remote-http-scaffold.md` — TS SDK 和 FastMCP 的最小远程 server
- `deploy-cloudflare-workers.md` — Cloudflare Workers 最快部署路径
- `tool-design.md` — 工具描述和 schema 设计规范
- `auth.md` — OAuth、CIMD、DCR、token 存储模式
- `resources-and-prompts.md` — Resources 和 Prompts 原语
- `elicitation.md` — 工具调用中途请求用户输入（能力检测+降级）
- `server-capabilities.md` — instructions/sampling/roots/logging/progress/取消
- `versions.md` — 版本敏感声明记录表

### build-mcpb/references/
- `manifest-schema.md` — manifest.json 字段完整参考
- `local-security.md` — 路径穿越、沙箱、最小权限

### build-mcp-app/references/
- `iframe-sandbox.md` — CSP/沙箱约束、bundle 内联模式、图片处理、主机主题
- `widget-templates.md` — picker/confirm/progress/display 可复用 HTML 模板
- `apps-sdk-messages.md` — App 类完整 API：widget↔主机↔server 消息、生命周期
- `payload-budgeting.md` — 主机工具结果大小限制、裁剪策略
- `abuse-protection.md` — Anthropic 出口 CIDR、限流、响应缓存
- `directory-checklist.md` — 提交 Anthropic 连接器目录的预检清单
