# 第三方仓库知识索引

本目录记录已安装到本机并建立知识图谱索引的第三方仓库。  
所有仓库位于：`/home/l/projects/03_third-party-sources/`  
知识图谱工具：`code-review-graph`（通过 `--repo_root` 参数切换仓库）

---

## 索引总览

| 仓库 | 类型 | 图谱节点 | 图谱边 | 文件数 | 语言 | 安装时间 |
|------|------|---------|-------|-------|------|---------|
| [yt-dlp](#1-yt-dlp) | 视频下载工具 | 10,887 | 88,663 | 1,213 | Python | 2026-05-23 |
| [FinceptTerminal](#2-finceptterminal) | 金融终端 | 32,659 | 316,551 | 3,092 | Python/C++/TS | 2026-05-23 |
| [the-book-of-secret-knowledge](#3-the-book-of-secret-knowledge) | 知识资源集合 | 0 (仅文档) | — | 35 | Markdown | 2026-05-23 |
| [odoo](#4-odoo) | ERP 业务平台 | 91,330 | 885,531 | 10,465 | Python/JS/SQL | 2026-05-23 |
| [chrome-devtools-mcp](#5-chrome-devtools-mcp) | 浏览器调试 MCP | 4,202 | 33,155 | 174 | TypeScript/JS | 2026-05-23 |
| [codegraph](#6-codegraph) | 代码语义图谱 MCP | 2,114 | 21,676 | 150 | TypeScript | 2026-05-23 |
| [ai-engineering-from-scratch](#7-ai-engineering-from-scratch) | AI 工程课程 | 6,219 | 49,387 | 456 | Python/多语言 | 2026-05-23 |

---

## 1. yt-dlp

**仓库：** `/home/l/projects/03_third-party-sources/yt-dlp`  
**GitHub：** https://github.com/yt-dlp/yt-dlp  
**License：** Unlicense

### 功能

youtube-dl 的功能增强分支，支持数千个视频/音频网站的内容下载。

**核心能力：**
- 从 YouTube、Bilibili、Twitter、TikTok 等数千个网站下载视频/音频
- 格式选择（bestvideo+bestaudio、特定分辨率、codec）
- 字幕下载（自动翻译字幕、多语言）
- 播放列表和频道批量下载
- 速率限制、代理、Cookie 支持
- 元数据写入（标题/描述/缩略图嵌入）
- 后处理插件（FFmpeg 转码、SponsorBlock、章节分割）
- 浏览器 Cookie 提取（绕过登录限制）

**架构关键点（来自知识图谱）：**
- `yt_dlp/extractor/` — 每个网站一个 Extractor 类（1000+ 个）
- `yt_dlp/downloader/` — 协议实现（HTTP/HLS/DASH/RTMPe 等）
- `yt_dlp/postprocessor/` — FFmpeg/音频/元数据后处理
- `yt_dlp/YoutubeDL.py` — 核心协调器

**典型用法：**
```bash
yt-dlp -f "bestvideo+bestaudio" URL          # 最佳质量
yt-dlp --write-subs --sub-lang zh-Hans URL   # 下载中文字幕
yt-dlp -x --audio-format mp3 URL            # 提取音频
yt-dlp --cookies-from-browser chrome URL    # 使用浏览器 Cookie
```

**代码查询示例：**
```
repo_root=/home/l/projects/03_third-party-sources/yt-dlp
semantic_search_nodes("BilibiliExtractor")     # 找 B 站提取器
query_graph("YoutubeDL", "callees_of")         # 核心下载流程
```

---

## 2. FinceptTerminal

**仓库：** `/home/l/projects/03_third-party-sources/FinceptTerminal`  
**GitHub：** https://github.com/Fincept-Corporation/FinceptTerminal  
**License：** AGPL-3.0 / Commercial

### 功能

Bloomberg Terminal 的开源替代品。C++20 原生桌面应用（Qt6 UI）+ 嵌入 Python 做分析。

**核心能力：**
- 股票行情、期权链、期货数据实时展示
- 投资组合管理和风险分析
- 基本面分析（财务报表、估值模型）
- 技术指标和图表（K线、MACD、RSI）
- AI 驱动的股票研究和新闻摘要
- 节点编辑器（可视化金融策略构建）
- 加密货币市场数据
- 宏观经济数据（GDP/CPI/利率）
- 期权定价模型（Black-Scholes）
- 多数据源连接（Yahoo Finance/Alpha Vantage/Polygon）

**架构关键点：**
- `fincept_terminal/` — Python 分析层（数据获取/处理/模型）
- C++ Qt6 层 — UI 渲染和交互
- `agents/` — AI 分析代理
- 混合架构：C++ 负责性能，Python 负责分析逻辑

**代码查询示例：**
```
repo_root=/home/l/projects/03_third-party-sources/FinceptTerminal
semantic_search_nodes("portfolio")              # 找投资组合相关
semantic_search_nodes("options pricing")        # 期权定价
query_graph("PortfolioManager", "callees_of")
```

---

## 3. the-book-of-secret-knowledge

**仓库：** `/home/l/projects/03_third-party-sources/the-book-of-secret-knowledge`  
**GitHub：** https://github.com/trimstray/the-book-of-secret-knowledge  
**License：** MIT  
**注：** 纯文档仓库，无代码索引（code-review-graph 返回 0 节点）

### 内容

精心整理的技术资源汇编（命令行工具、安全工具、教程、备忘单、one-liner 集合）。

**章节结构（10大类）：**

| 章节 | 内容 |
|------|------|
| CLI Tools | Shell、文本编辑器、网络、安全、日志分析、数据库工具 |
| GUI Tools | 终端模拟器、浏览器、密码管理器、加密通讯 |
| Web Tools | SSL、DNS、隐私、性能分析、漏洞数据库 |
| Systems/Services | 操作系统、HTTP/DNS 服务、安全加固 |
| Networks | 网络工具、实验室环境 |
| Containers/Orchestration | Docker/K8s 工具、安全最佳实践 |
| Manuals/Tutorials | Shell、Python、系统加固、Web 安全教程 |
| Inspiring Lists | SysOps/DevOps、开发者、安全/渗透测试资源列表 |
| Hacking/Pentesting | 渗透工具库、靶场、CTF、漏洞赏金平台 |
| Daily Knowledge | RSS、IRC、安全资讯来源 |

**Shell One-liners 精选（书中收录）：**
- `lsof` 查看端口占用和网络连接
- `openssl` 生成证书、测试 TLS 连接
- `tcpdump` 流量捕获和协议分析
- `nmap` 端口扫描和服务识别
- `netcat` 文件传输、端口转发、简单 HTTP 服务
- `awk/sed/grep/perl` 文本处理 one-liners

**阅读方式：**
```bash
# 直接阅读（4442行）
cat /home/l/projects/03_third-party-sources/the-book-of-secret-knowledge/README.md
```

---

## 4. odoo

**仓库：** `/home/l/projects/03_third-party-sources/odoo`（branch: 17.0）  
**GitHub：** https://github.com/odoo/odoo  
**License：** LGPL-3.0  
**规模：** 10,465 文件 | 91,330 节点 | 885,531 边（最大的已索引仓库）

### 功能

全球最大开源 ERP 系统，模块化商业软件套件。

**核心模块（addons/）：**

| 模块类别 | 主要功能 |
|----------|---------|
| **会计** | 会计分录、发票、税务、多货币、财务报告 |
| **销售** | CRM、报价单、订单管理、价格表 |
| **采购** | 供应商管理、采购订单、询价 |
| **库存** | 多仓库、批次追踪、移库规则、条码 |
| **制造** | BOM、MO、工作中心、质检 |
| **项目** | 任务、甘特图、工时表、里程碑 |
| **人力资源** | 员工档案、考勤、工资单、假期 |
| **电商** | 商品页面、购物车、支付集成 |
| **网站** | 建站器、博客、论坛、在线活动 |
| **营销** | 邮件营销、社交媒体、活动管理 |

**技术架构：**
- ORM 层：`odoo/models.py`（Record、BaseModel）
- Web 框架：`odoo/http.py`（路由、RPC、Session）
- 视图引擎：`odoo/addons/web/`（XML 视图 + JS 前端）
- 工作流：`odoo/addons/base_automation/`
- 报表：QWeb 模板引擎

**代码查询示例（索引完成后）：**
```
repo_root=/home/l/projects/03_third-party-sources/odoo
semantic_search_nodes("account.move")          # 会计分录模型
query_graph("BaseModel", "callees_of")         # ORM 核心
get_architecture_overview()                    # 模块依赖全图
```

---

## 5. chrome-devtools-mcp

**仓库：** `/home/l/projects/03_third-party-sources/chrome-devtools-mcp`  
**GitHub：** https://github.com/ChromeDevTools/chrome-devtools-mcp  
**License：** Apache-2.0  
**发布：** npm `chrome-devtools-mcp`

### 功能

让 AI 编程助手（Claude、Cursor、Copilot）控制和检查 Chrome 浏览器的 MCP 服务器。

**核心工具（MCP Tools）：**

| 工具 | 功能 |
|------|------|
| `navigate_page` | 页面导航 |
| `take_screenshot` | 截图 |
| `click` / `fill` / `hover` | DOM 交互 |
| `evaluate_script` | 执行 JavaScript |
| `get_console_message` | 获取控制台输出 |
| `list_network_requests` | 网络请求列表 |
| `performance_start_trace` / `stop_trace` | 性能追踪 |
| `performance_analyze_insight` | 性能分析洞察 |
| `lighthouse_audit` | Lighthouse 审计 |
| `take_memory_snapshot` | 内存快照 |
| `fill_form` | 表单批量填写 |
| `wait_for` | 等待元素/条件 |

**与本机已安装版本的关系：**  
本机 `~/.mcp.json` 中已注册 `chrome-devtools-mcp` 插件（来自 plugin 系统），与本仓库是同一工具的源码版本。

**安装为 MCP：**
```json
{
  "mcpServers": {
    "chrome-devtools-mcp": {
      "command": "npx",
      "args": ["chrome-devtools-mcp"]
    }
  }
}
```

**代码查询示例：**
```
repo_root=/home/l/projects/03_third-party-sources/chrome-devtools-mcp
semantic_search_nodes("performance")           # 性能工具实现
query_graph("lighthouse_audit", "callees_of")  # Lighthouse 调用链
```

---

## 6. codegraph

**仓库：** `/home/l/projects/03_third-party-sources/codegraph`  
**GitHub：** https://github.com/colbymchenry/codegraph  
**License：** MIT  
**发布：** npm `@colbymchenry/codegraph`

### 功能

与 code-review-graph 同类的代码语义图谱工具，专为 AI 编程助手（Claude Code、Cursor、Codex 等）设计的 MCP 服务器。

**核心特性：**
- ~35% Token 减少
- ~70% 工具调用减少
- 100% 本地运行（无云端依赖）
- 支持 Claude Code / Cursor / Codex / opencode / Hermes Agent
- 零 Node.js 依赖（独立二进制）

**与 code-review-graph 的对比：**

| 维度 | codegraph | code-review-graph |
|------|-----------|-------------------|
| 语言 | TypeScript（Node.js） | Python |
| 依赖 | 零依赖二进制 | pip install |
| 后端 | SQLite | SQLite |
| 解析 | Tree-sitter | Tree-sitter |
| MCP 协议 | ✅ | ✅ |
| 社区检测 | 未知 | ✅（igraph） |
| 流分析 | 未知 | ✅ (1049 flows) |

**安装：**
```bash
# macOS/Linux
curl -fsSL https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.sh | sh
# 或
npx @colbymchenry/codegraph
```

**代码查询示例：**
```
repo_root=/home/l/projects/03_third-party-sources/codegraph
semantic_search_nodes("index")                 # 索引核心实现
query_graph("McpServer", "callees_of")         # MCP 工具注册
```

---

## 7. ai-engineering-from-scratch

**仓库：** `/home/l/projects/03_third-party-sources/ai-engineering-from-scratch`  
**GitHub：** https://github.com/rohitg00/ai-engineering-from-scratch  
**License：** MIT

### 功能

完整 AI 工程学习课程（435 课 / 20 阶段 / ~320 小时）。

**阶段结构：**

| 阶段 | 主题 | 节点数 |
|------|------|-------|
| Phase 00 | Setup & Tooling | 56 |
| Phase 01 | Math Foundations | 618 |
| Phase 02 | ML Fundamentals | 495 |
| Phase 03 | Deep Learning Core | 281 |
| Phase 04 | Computer Vision | 310 |
| Phase 05 | NLP Foundations | 208 |
| Phase 06 | Speech & Audio | 145 |
| Phase 07 | Transformers Deep Dive | 176 |
| Phase 08 | Generative AI | 197 |
| Phase 09 | Reinforcement Learning | 140 |
| Phase 10 | LLMs from Scratch | 389 |
| Phase 11 | LLM Engineering | 319 |
| Phase 12 | Multimodal AI | 269 |
| Phase 13 | Tools & Protocols | 245 |
| Phase 14 | Agent Engineering | 605 |
| Phase 15 | Autonomous Systems | 182 |
| Phase 16 | Multi-Agent & Swarms | 336 |
| Phase 17 | Infrastructure & Production | 160 |
| Phase 18 | Ethics, Safety & Alignment | 211 |
| Phase 19 | Capstone Projects | 230 |

---

## 如何使用知识图谱查询这些仓库

### 基础查询模式

```python
# 1. 语义搜索（找函数/类/概念）
mcp__code-review-graph__semantic_search_nodes(
    query="portfolio manager",
    repo_root="/home/l/projects/03_third-party-sources/FinceptTerminal"
)

# 2. 查调用关系
mcp__code-review-graph__query_graph(
    node_name="YoutubeDL",
    pattern="callees_of",
    repo_root="/home/l/projects/03_third-party-sources/yt-dlp"
)

# 3. 架构概览
mcp__code-review-graph__get_architecture_overview_tool(
    repo_root="/home/l/projects/03_third-party-sources/odoo"
)

# 4. 影响分析
mcp__code-review-graph__get_impact_radius_tool(
    node_name="account.move",
    repo_root="/home/l/projects/03_third-party-sources/odoo"
)
```

### 仓库路径速查

```
/home/l/projects/03_third-party-sources/yt-dlp
/home/l/projects/03_third-party-sources/FinceptTerminal
/home/l/projects/03_third-party-sources/the-book-of-secret-knowledge  (仅文档，无图谱)
/home/l/projects/03_third-party-sources/odoo
/home/l/projects/03_third-party-sources/chrome-devtools-mcp
/home/l/projects/03_third-party-sources/codegraph
/home/l/projects/03_third-party-sources/ai-engineering-from-scratch
```
