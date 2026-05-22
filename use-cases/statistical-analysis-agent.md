# Statistical Analysis Agent Playbook

This playbook is the shortest path for an agent that needs to design or implement a statistical analysis agent using this repository.

## Goal

Build an agent workflow that can ingest tabular data, clean it, run R/statistical analysis, verify numeric claims, generate Quarto reports, and coordinate subagents with quality gates and context discipline.

## Read Order

1. Start with the root map: `README.md`
   - Use the quick index for R, Quarto, ClaudeR, subagents, metaswarm, context, and MCP.
   - Use the `survey-analysis-platform` mapping near the bottom as the first architecture sketch.

2. Read the R and reporting layer: `02-r-quarto/README.md`
   - R code generation: `02-r-quarto/agentic-skills/writing-r-code/SKILL.md`
   - Scientific Quarto authoring: `02-r-quarto/agentic-skills/writing-qmd-scientific/SKILL.md`
   - Quarto official skill entry: `02-r-quarto/posit-dev-skills/quarto/quarto-authoring/SKILL.md`
   - Statistical verification and R MCP: `02-r-quarto/ClaudeR/clauder-mcp/README.md`
   - Claim audit protocol: `02-r-quarto/ClaudeR/inst/prompts/reviewer_zero.md`

3. Read the subagent roles: `05-subagents/README.md`
   - Data cleaning: `05-subagents/awesome-claude-code-subagents/categories/05-data-ai/data-engineer.md`
   - Statistical analysis: `05-subagents/awesome-claude-code-subagents/categories/05-data-ai/data-analyst.md`
   - Advanced modeling: `05-subagents/awesome-claude-code-subagents/categories/05-data-ai/data-scientist.md`
   - Research/reporting: `05-subagents/awesome-claude-code-subagents/categories/10-research-analysis/data-researcher.md`
   - Context coordination: `05-subagents/awesome-claude-code-subagents/categories/09-meta-orchestration/context-manager.md`

4. Read orchestration and quality gates: `07-agent-design/README.md`
   - Full workflow: `07-agent-design/metaswarm/ORCHESTRATION.md`
   - Design gate: `07-agent-design/metaswarm/skills/design-review-gate/SKILL.md`
   - Execution loop: `07-agent-design/metaswarm/skills/orchestrated-execution/SKILL.md`
   - Agent architecture background: `07-agent-design/Dive-into-Claude-Code/docs/architecture_zh.md`

5. Read runtime infrastructure: `08-infrastructure/README.md`
   - Context control: `08-infrastructure/context-window/token-optimizer/skills/token-optimizer/SKILL.md`
   - Boomerang task split: `08-infrastructure/tool-use-mcp/claude-code-mcp-enhanced/README.md`
   - Subagent isolation: `08-infrastructure/subagent-isolation/claude-code-sub-agent-collective/README.md`
   - Harness construction: `08-infrastructure/subagent-isolation/ECC/README.zh-CN.md`

6. Read candidate infrastructure extensions: `09-agent-infra-catalog/catalog.yaml`
   - Deterministic routing: `09-agent-infra-catalog/orchestrators/agent-kit/README.md`
   - Governance: `09-agent-infra-catalog/governance-guardrails/agent-governance-toolkit/README.md`
   - MCP/A2A gateway: `09-agent-infra-catalog/routing-gateways/agentgateway/README.md`
   - Skill control plane: `09-agent-infra-catalog/skill-systems/agent-skills/README.md`

## Reference Architecture

```text
Statistical Analysis Orchestrator
  ├─ Intake and plan
  │    └─ metaswarm plan / plan-review-gate pattern
  ├─ Data cleaning
  │    └─ data-engineer subagent
  ├─ R statistical execution
  │    ├─ data-analyst subagent
  │    ├─ writing-r-code skill
  │    └─ ClaudeR MCP execute_r / execute_r_with_plot
  ├─ Advanced modeling
  │    └─ data-scientist subagent
  ├─ Reporting
  │    ├─ writing-qmd-scientific skill
  │    └─ Posit Quarto authoring skill
  ├─ Claim verification
  │    └─ ClaudeR reviewer_zero audit protocol
  ├─ Quality gates
  │    ├─ design-review-gate
  │    └─ orchestrated-execution adversarial review
  ├─ Context management
  │    └─ token-optimizer and pre_compact state preservation
  ├─ Tool runtime
  │    └─ ClaudeR MCP + claude-code-mcp-enhanced boomerang pattern
  └─ Governance and routing candidates
       ├─ agent-governance-toolkit
       ├─ agentgateway
       └─ agent-kit
```

## Query Hints

Use these keywords with `rg` when navigating the repository:

```bash
rg -n "writing-r-code|ClaudeR|reviewer_zero|data-analyst|data-engineer|design-review-gate|orchestrated-execution|token-optimizer|claude-code-mcp-enhanced|agentgateway|agent-governance" .
```

## Current Gaps

- This playbook is currently hand-maintained; the same mapping should eventually be generated from a unified repository catalog.
- `09-agent-infra-catalog/catalog.yaml` has machine-readable metadata, but `01-08` still need equivalent metadata.
- The repository needs an FTS/SQLite/MCP query layer so agents can ask for capabilities instead of manually scanning Markdown.
