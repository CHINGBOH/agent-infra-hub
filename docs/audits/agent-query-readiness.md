# Agent Query Readiness Audit

Date: 2026-05-22

## Question

Can this repository act as an intelligent agent architecture infrastructure and code guidance repository for agents that query it directly?

Short answer: yes, but it is currently semi-intelligent. It is strong as a curated human-readable repository and usable by agents that can search with `rg`, read Markdown, and synthesize across directories. It is not yet a fully agent-native knowledge base because metadata, relationships, query APIs, and evals are incomplete.

## Test Scenario

A subagent simulated this task:

> Design a statistical analysis agent that can handle data cleaning, R statistical analysis, claim verification, Quarto reports, multi-agent division of labor, quality gates, context management, and tool/MCP integration.

The subagent used only repository-local materials.

## Result

The subagent could assemble a complete architecture from the repository:

```text
Main orchestrator
  ├─ Data cleaning: data-engineer subagent
  ├─ R statistics: data-analyst + writing-r-code + ClaudeR MCP
  ├─ Advanced modeling: data-scientist
  ├─ Reporting: writing-qmd-scientific + Quarto skill
  ├─ Claim verification: ClaudeR reviewer_zero protocol
  ├─ Quality gates: metaswarm design-review-gate + orchestrated-execution
  ├─ Context management: token-optimizer
  ├─ Tool/MCP runtime: ClaudeR MCP + claude-code-mcp-enhanced
  └─ Governance/routing candidates: agent-governance-toolkit, agentgateway, agent-kit
```

## What Works

- Root `README.md` routes by use case rather than listing files only.
- `02-r-quarto/README.md`, `05-subagents/README.md`, `07-agent-design/README.md`, and `08-infrastructure/README.md` provide useful second-level navigation.
- `09-agent-infra-catalog/catalog.yaml` is machine-readable and already has `category`, `artifact_types`, `agent_layers`, `capabilities`, `priority`, `import_mode`, and `local_path`.
- Core statistical-analysis materials are present and high quality.
- Local Markdown link checks on primary README files found no broken local Markdown links.

## Friction Found

- Agents still need to infer many next-hop paths. Example: a README may say `quarto/README.md`, but the full path is under `02-r-quarto/posit-dev-skills/`.
- The old sections `01-08` do not have unified metadata equivalent to `09-agent-infra-catalog/catalog.yaml`.
- Cross-directory relationships are implicit. The repository knows about R, Quarto, ClaudeR, metaswarm, token-optimizer, and MCP, but the graph connecting them is still prose.
- Search results can be noisy because the repository contains many large nested sources.
- Nested git repositories are useful for source reference but complicate root-level git status, indexing, and vendoring policy.
- Some README text still contains stale names or counts such as `skills-hub` paths and old repository totals.

## Intelligence Level

Current level: semi-intelligent.

Intelligent today:

- Human-readable routing by use case.
- Strong directory taxonomy.
- Some machine-readable catalog metadata in `09-agent-infra-catalog`.
- Skill files often use progressive disclosure, which helps agents read only the relevant entry point.

Not yet intelligent enough:

- No repository-wide artifact catalog for `01-08`.
- No FTS or vector index.
- No MCP server exposing repository queries.
- No relationship graph or capability resolver.
- No eval suite that measures whether agents can find the right materials within a bounded number of steps.

## Recommended Next Steps

1. Keep `use-cases/statistical-analysis-agent.md` as the canonical playbook for this tested scenario.
2. Create a root-level machine-readable catalog for `01-08`, then merge or link it with `09-agent-infra-catalog/catalog.yaml`.
3. Add a lightweight SQLite + FTS index with tables for artifacts, capabilities, paths, relationships, and use cases.
4. Add an MCP server exposing:
   - `search_artifacts(query)`
   - `resolve_capability(capability)`
   - `get_use_case_plan(name)`
   - `get_artifact_context(path)`
5. Add query evals. Example tasks:
   - Build a statistical analysis agent.
   - Build a Claude Code hook safety layer.
   - Choose a routing gateway for MCP/A2A.
   - Find governance controls for dangerous tool calls.
   - Choose a context optimization strategy.

## Verdict

This is already a credible agent architecture infrastructure guidance repository. Its next upgrade is not more raw content; it is making the existing content queryable, scored, and relational so agents can retrieve architecture components instead of rediscovering paths by reading prose.
