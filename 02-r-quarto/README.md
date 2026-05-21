# 02-r-quarto — R + Quarto 工具链

## 快速选择

| 需求 | 用哪个 |
|------|--------|
| Quarto 报告语法、R Markdown 迁移 | `posit-dev-skills/quarto/` |
| tidyverse 代码风格 | `posit-dev-skills/tidyverse/` |
| 写 R 统计分析代码 | `agentic-skills/writing-r-code/` |
| 写科学 QMD 文档 | `agentic-skills/writing-qmd-scientific/` |
| R 代码 + Claude Code MCP 集成 | `ClaudeR/` |
| 统计结果核验（反幻觉） | `ClaudeR/clauder-mcp/` |

## posit-dev-skills — Posit 官方

```
posit-dev-skills/
├── quarto/          ← Quarto 文档：语法/cross-refs/callouts/迁移
├── tidyverse/       ← dplyr/ggplot2/purrr 最佳实践
├── r-lib/           ← R 包：usethis/devtools/pkgdown
├── shiny/           ← bslib 现代 Shiny Dashboard
├── brand-yml/       ← Quarto 统一品牌样式
├── ggsql/           ← ggplot2 + SQL
└── alt-text/        ← 图表无障碍描述
```

安装：`npx skills add posit-dev/skills/quarto`

## agentic-skills — 科学分析

```
agentic-skills/
├── writing-r-code/              ← R 代码生成规范
├── writing-qmd-scientific/      ← 科学 QMD 写作
├── creating-analysis-projects/  ← 项目脚手架
├── developing-r-packages/       ← 包开发
└── git-hygiene/                 ← Git 规范
```

## ClaudeR — MCP + 审计

- `clauder-mcp/` — MCP Server 配置（RStudio ↔ Claude Code）
- `inst/` — 手稿统计核验协议实现
- 安装指南：`llms-install.md`
