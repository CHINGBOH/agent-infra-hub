# Construction Cost Knowledge Base Agent Playbook

This playbook is the shortest path for an agent that needs to design or implement a construction cost knowledge base agent using this repository.

## Goal

Build an agent workflow that can manage construction cost standards, bill of quantities, quota items, material prices, regional rules, and project case documents. The agent should support source-grounded retrieval QA, structured classification, citation provenance, table analysis, reports, quality gates, multi-agent division of labor, MCP/tool integration, and governance.

This repository provides the agent infrastructure and implementation guidance. It does not currently provide construction cost domain source content such as local pricing rules, official quota databases, or material price bulletins.

## Read Order

1. Start with the root map: `README.md`
   - Use it to locate data analysis, document processing, subagents, RAG, MCP, quality gates, governance, and context management.

2. Read the RAG and knowledge-base design layer:
   - RAG architecture: `06-catalogs/alirezarezvani-claude-skills/engineering/skills/rag-architect/SKILL.md`
   - Database schema design: `06-catalogs/alirezarezvani-claude-skills/engineering/skills/database-designer/SKILL.md`

3. Read document and table processing skills:
   - PDF: `06-catalogs/composio-awesome-claude-skills/document-skills/pdf/SKILL.md`
   - DOCX: `06-catalogs/composio-awesome-claude-skills/document-skills/docx/SKILL.md`
   - XLSX: `06-catalogs/composio-awesome-claude-skills/document-skills/xlsx/SKILL.md`
   - Excel automation candidate: `06-catalogs/composio-awesome-claude-skills/composio-skills/excel-automation/SKILL.md`
   - Mistral OCR/RAG library candidate: `06-catalogs/composio-awesome-claude-skills/composio-skills/mistral-ai-automation/SKILL.md`

4. Read data quality and tabular analysis guidance:
   - Data quality audit: `06-catalogs/alirezarezvani-claude-skills/engineering/data-quality-auditor/skills/data-quality-auditor/SKILL.md`
   - Data analysis pipeline: `01-data-analysis/claude-data-analysis-ultra/README.md`
   - Skill usage guide: `01-data-analysis/claude-data-analysis-ultra/SKILLS_USAGE.md`

5. Read citation, provenance, and claim-audit patterns:
   - Academic research architecture: `04-research/academic-research-skills/docs/ARCHITECTURE.md`
   - Setup and corpus adapters: `04-research/academic-research-skills/docs/SETUP.md`
   - Adapter contract: `04-research/academic-research-skills/academic-pipeline/references/adapters/overview.md`
   - Claim verification: `04-research/academic-research-skills/academic-pipeline/references/claim_verification_protocol.md`
   - Claim audit calibration: `04-research/academic-research-skills/academic-pipeline/references/claim_audit_calibration_protocol.md`

6. Read subagent role definitions:
   - Subagent index: `05-subagents/README.md`
   - Requirements and workflow: `05-subagents/awesome-claude-code-subagents/categories/08-business-product/business-analyst.md`
   - Data pipelines: `05-subagents/awesome-claude-code-subagents/categories/05-data-ai/data-engineer.md`
   - Data analysis: `05-subagents/awesome-claude-code-subagents/categories/05-data-ai/data-analyst.md`
   - SQL/schema work: `05-subagents/awesome-claude-code-subagents/categories/02-language-specialists/sql-pro.md`
   - Research synthesis: `05-subagents/awesome-claude-code-subagents/categories/10-research-analysis/research-analyst.md`
   - Knowledge synthesis: `05-subagents/awesome-claude-code-subagents/categories/09-meta-orchestration/knowledge-synthesizer.md`
   - Workflow orchestration: `05-subagents/awesome-claude-code-subagents/categories/09-meta-orchestration/workflow-orchestrator.md`
   - MCP integration: `05-subagents/awesome-claude-code-subagents/categories/06-developer-experience/mcp-developer.md`
   - Documentation: `05-subagents/awesome-claude-code-subagents/categories/06-developer-experience/documentation-engineer.md`

7. Read quality gate and execution loop patterns:
   - Orchestration overview: `07-agent-design/metaswarm/ORCHESTRATION.md`
   - Design gate: `07-agent-design/metaswarm/skills/design-review-gate/SKILL.md`
   - Execution loop: `07-agent-design/metaswarm/skills/orchestrated-execution/SKILL.md`

8. Read runtime infrastructure:
   - Context optimization: `08-infrastructure/context-window/token-optimizer/skills/token-optimizer/SKILL.md`
   - MCP boomerang pattern: `08-infrastructure/tool-use-mcp/claude-code-mcp-enhanced/README.md`
   - Agent gateway: `09-agent-infra-catalog/routing-gateways/agentgateway/README.md`
   - Governance toolkit: `09-agent-infra-catalog/governance-guardrails/agent-governance-toolkit/README.md`
   - Deterministic routing candidate: `09-agent-infra-catalog/orchestrators/agent-kit/README.md`

## Reference Architecture

```text
Construction Cost Knowledge Base Agent
  ├─ Intake and requirements
  │    └─ business-analyst + workflow-orchestrator
  ├─ Document ingestion
  │    ├─ PDF standards and quota documents
  │    ├─ DOCX tender/spec documents
  │    ├─ XLSX bills of quantities and material price sheets
  │    └─ OCR / remote document library adapters where needed
  ├─ Structured extraction
  │    ├─ standard clauses
  │    ├─ bill items
  │    ├─ quota items
  │    ├─ material prices
  │    ├─ regional rules
  │    └─ project cases
  ├─ Storage
  │    ├─ relational schema for canonical entities
  │    ├─ FTS index for exact legal/standard wording
  │    ├─ vector index for semantic retrieval
  │    └─ graph index for cost-code, quota, material, region, and project relationships
  ├─ Retrieval
  │    ├─ hybrid retrieval
  │    ├─ metadata filtering by region, date, standard version, discipline
  │    ├─ reranking
  │    └─ context assembly with source anchors
  ├─ Answering
  │    ├─ source-grounded responses
  │    ├─ page / clause / table-row citation
  │    ├─ refusal when source is missing or version does not apply
  │    └─ uncertainty and assumption disclosure
  ├─ Cost analysis
  │    ├─ material price trend analysis
  │    ├─ bill-of-quantities comparison
  │    ├─ abnormal quantity / unit-price detection
  │    └─ project case benchmarking
  ├─ Reporting
  │    ├─ DOCX/PDF narrative reports
  │    ├─ XLSX cost matrices
  │    └─ audit trail exports
  ├─ Quality gates
  │    ├─ claim-source alignment
  │    ├─ numerical recalculation
  │    ├─ region/date/version applicability check
  │    ├─ quota-code validation
  │    └─ no-source refusal gate
  ├─ Tool/MCP layer
  │    ├─ document store tools
  │    ├─ database query tools
  │    ├─ search/retrieval tools
  │    └─ report generation tools
  └─ Governance
       ├─ RBAC
       ├─ audit log
       ├─ rate/cost limits
       └─ dangerous tool blocking
```

## Storage Choice

Use three storage layers instead of forcing all data into one database.

```text
Relational database
  Best for canonical records, tables, prices, versions, audit logs, joins, and exact filters.
  Good candidates: PostgreSQL first; SQLite is enough for a small local prototype.

Vector database
  Best for semantic retrieval over document chunks, clauses, table captions, and case descriptions.
  Milvus is a good simulation/production candidate for this layer.
  Treat it as a vector database, not as the source of truth for all structured cost data.

Knowledge graph
  Best for explainable relationships:
    quota item -> cost code -> material -> region -> standard version -> project case.
  Use it when questions require traversal, dependency reasoning, conflict detection, or ontology maintenance.
```

Recommended prototype order:

1. Start with relational tables + local vector index to validate ingestion and retrieval.
2. Add Milvus when the document/chunk volume grows or when multiple agents need shared vector retrieval.
3. Add a graph layer after the cost-code taxonomy, quota relationships, material mapping, and regional rules are stable enough to model.

For construction cost, Milvus and a knowledge graph solve different problems. Milvus finds semantically similar evidence, while the graph explains how entities are connected. The best architecture is usually hybrid retrieval: exact SQL/FTS filters first, vector recall second, graph expansion third, then rerank and cite.

## Suggested Database Model

```text
documents
  id, title, source_type, file_path, jurisdiction, discipline,
  standard_version, effective_date, publisher, checksum, ingested_at

document_chunks
  id, document_id, chunk_text, page_start, page_end, clause_id,
  table_id, row_ref, embedding_id, token_count

cost_codes
  id, code, name, parent_code, discipline, jurisdiction, standard_version

quota_items
  id, code, title, unit, description, work_scope, calculation_rule,
  jurisdiction, standard_version, source_chunk_id

bill_items
  id, project_id, item_code, description, quantity, unit, unit_price,
  total_price, source_file, source_row_ref

material_prices
  id, material_code, material_name, spec, unit, price, currency,
  region, effective_date, source_document_id, source_row_ref

project_cases
  id, project_name, location, building_type, gross_floor_area,
  structure_type, start_date, finish_date, total_cost, source_document_id

answer_claims
  id, answer_id, claim_text, claim_type, cited_chunk_id,
  verification_status, verification_notes

audit_logs
  id, actor, action, target_type, target_id, decision,
  reason, created_at, trace_id
```

## Recommended Agent Roles

```text
construction-kb-orchestrator
  Owns workflow, task routing, state, and quality gates.

document-ingestion-agent
  Extracts text/tables from PDFs, DOCX, XLSX, OCR outputs, and attaches source anchors.

cost-taxonomy-agent
  Maintains cost-code hierarchy, quota item taxonomy, and domain glossary.

retrieval-agent
  Designs and tunes hybrid retrieval, metadata filters, reranking, and context assembly.

pricing-analysis-agent
  Handles material price trends, outlier detection, project comparisons, and table QA.

citation-auditor-agent
  Checks every answer claim against source chunks, page numbers, clauses, rows, and versions.

report-writer-agent
  Generates narrative reports, cost matrices, and executive summaries.

governance-agent
  Enforces RBAC, audit logs, sensitive data policy, and dangerous-tool blocking.
```

## Quality Gates

- Region applicability: answer must match the user's jurisdiction/region.
- Version applicability: answer must use the correct standard/quota version for the target date.
- Clause grounding: legal or standard claims require page/clause/table-row citations.
- Numeric recalculation: totals, unit prices, and percentage changes must be recomputed.
- Source availability: no source means refuse or mark as unsupported.
- Conflict handling: when two sources disagree, return both and explain version/date precedence.
- Table integrity: extracted table rows must preserve row labels, units, and formulas where possible.
- Auditability: every final answer should be traceable to document chunks and tool calls.

## Query Hints

Use these searches when navigating the repository:

```bash
rg -n "rag-architect|database-designer|data-quality-auditor|document-skills|pdf|docx|xlsx|Material Passport|claim verification|design-review-gate|agentgateway|agent-governance" . -g '*.md' -g '!**/.harness/**'
```

## Current Gaps

- No construction-cost domain corpus is present in this repository.
- No construction-cost ontology, cost-code taxonomy, quota schema, or material price schema is currently first-class metadata.
- `09-agent-infra-catalog/catalog.yaml` has machine-readable metadata, but most useful artifacts in `01-08` still need equivalent catalog entries.
- Full-repository search should exclude generated artifacts, `.harness`, vendor data, dependency lockfiles, and test fixtures by default.
