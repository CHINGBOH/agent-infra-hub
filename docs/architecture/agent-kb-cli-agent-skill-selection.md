# Agent KB CLI Agent And Skill Selection

This document selects the agent architectures and skills that are most useful for completing the `agent-infra-hub` knowledge-base Agent CLI.

## Target

The CLI should help humans and agents ask this repository questions, retrieve grounded context, inspect source chunks, and discover relevant skills/subagents/catalog entries. It should remain local-first and service-free by default, while leaving clean extension points for Milvus, knowledge graphs, DeepSeek synthesis, MCP, and governance.

## Core Execution Chain

```text
Human / Agent question
  -> CLI UX and command contract
  -> query routing and domain expansion
  -> SQLite metadata + FTS retrieval
  -> optional vector retrieval backend
  -> optional graph/entity traversal
  -> context pack assembly
  -> source-grounded answer discipline
  -> audit / quality gate
```

## Must-Use References

| Role | Path | Why it fits |
|------|------|-------------|
| CLI implementation | `05-subagents/awesome-claude-code-subagents/categories/06-developer-experience/cli-developer.md` | Best fit for command hierarchy, flags, error messages, JSON output, shell automation, and developer UX. |
| RAG/retrieval architecture | `06-catalogs/alirezarezvani-claude-skills/engineering/skills/rag-architect/SKILL.md` | Covers chunking, sparse/dense/hybrid retrieval, reranking, context assembly, evaluation, and vector database choices. |
| Database schema | `06-catalogs/alirezarezvani-claude-skills/engineering/skills/database-designer/SKILL.md` | Best fit for the SQLite/Postgres metadata schema, indexes, migrations, and future audit tables. |
| Knowledge synthesis | `05-subagents/awesome-claude-code-subagents/categories/09-meta-orchestration/knowledge-synthesizer.md` | Fits catalog synthesis, entity extraction, relationship mapping, insight extraction, and knowledge evolution. |
| Workflow orchestration | `05-subagents/awesome-claude-code-subagents/categories/09-meta-orchestration/workflow-orchestrator.md` | Fits build/search/ask/show/stats workflows, state transitions, retry/fallback behavior, and auditability. |
| Design gate | `07-agent-design/metaswarm/skills/design-review-gate/SKILL.md` | Fits review of the CLI design before deeper implementation: product, architecture, UX/API, security, and TDD readiness. |

## High-Value Supporting Skills

| Area | Path | Use in CLI |
|------|------|------------|
| Hybrid search | `07-agent-design/wshobson-agents/plugins/llm-application-dev/skills/hybrid-search-implementation/SKILL.md` | Use when adding BM25 + vector fusion and reranking. |
| Vector tuning | `07-agent-design/wshobson-agents/plugins/llm-application-dev/skills/vector-index-tuning/SKILL.md` | Use when introducing Milvus/Qdrant/pgvector backends. |
| Embeddings | `07-agent-design/wshobson-agents/plugins/llm-application-dev/skills/embedding-strategies/SKILL.md` | Use for model choice, chunk embedding, caching, and re-embedding policies. |
| RAG implementation | `07-agent-design/wshobson-agents/plugins/llm-application-dev/skills/rag-implementation/SKILL.md` | Use for productionizing retrieval/answer assembly beyond the current context-pack CLI. |
| MCP integration | `05-subagents/awesome-claude-code-subagents/categories/06-developer-experience/mcp-developer.md` | Use when exposing the CLI as an MCP tool for other agents. |
| Documentation | `05-subagents/awesome-claude-code-subagents/categories/06-developer-experience/documentation-engineer.md` | Use for command docs, examples, and agent-facing contracts. |
| Test automation | `05-subagents/awesome-claude-code-subagents/categories/04-quality-security/test-automator.md` | Use for CLI regression tests and fixture-based search tests. |
| Security review | `05-subagents/awesome-claude-code-subagents/categories/04-quality-security/security-auditor.md` | Use before adding shell execution, remote fetch, or MCP exposure. |
| Context control | `08-infrastructure/context-window/token-optimizer/skills/token-optimizer/SKILL.md` | Use when tuning context-pack size, chunk limits, and agent handoff payloads. |

## Recommended Agent Team

Use these as roles, not necessarily always-running agents:

| Agent | Source | Responsibility |
|-------|--------|----------------|
| `agent-kb-cli-lead` | adapted from `cli-developer` + `workflow-orchestrator` | Own command contract, release scope, and task sequencing. |
| `retrieval-architect` | adapted from `rag-architect` + hybrid search skills | Own chunking, FTS, vector, reranking, and context-pack quality. |
| `metadata-db-designer` | adapted from `database-designer` | Own SQLite/Postgres schema, migrations, indexes, and audit tables. |
| `knowledge-curator` | adapted from `knowledge-synthesizer` | Own taxonomy, tags, catalog enrichment, and entity relationships. |
| `mcp-interface-designer` | adapted from `mcp-developer` | Own future MCP tool surface for agents. |
| `qa-gate` | adapted from `design-review-gate`, `test-automator`, `security-auditor` | Own regression tests, source-grounding checks, and risky feature review. |

## What To Build Next

1. Stabilize the local CLI: `build`, `search`, `ask`, `show`, `docs`, `stats`. Done for the baseline implementation.
2. Add query expansion and bilingual routing for Chinese questions. Done for the construction-cost path.
3. Add a `recommend` command that maps user intent to skills, agents, and source paths. Done for the baseline implementation.
4. Add regression fixtures for expected top results.
5. Add richer metadata extraction from `SKILL.md` and subagent frontmatter.
6. Add optional vector backend interface, with Milvus as a production candidate.
7. Add optional graph export: entities and edges from skills, agents, repos, capabilities, and use cases.
8. Add an optional DeepSeek synthesis layer that consumes retrieved sources and emits a grounded final answer.
9. Expose the CLI as MCP only after local behavior and security boundaries are stable.

## Decision

For this repository, the best architecture is not a heavyweight autonomous agent first. The right base is a deterministic local CLI that returns grounded context packs. Agent behavior should sit on top of that CLI, using selected skills and subagent roles for design, retrieval, curation, QA, and future MCP exposure.
