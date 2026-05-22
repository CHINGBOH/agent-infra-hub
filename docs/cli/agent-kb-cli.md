# Agent KB CLI

`tools/agent_kb.py` builds and queries a local knowledge base for this repository. It is designed for both humans and agents: human commands print concise text, while `--json` returns structured context packs.

## Build

```bash
./tools/agent_kb.py build
```

Default output database:

```text
data/agent-kb/index.sqlite
```

This database is a generated runtime artifact and is ignored by git. Rebuild it after cloning or after major documentation changes.

The index stores:

- documents: path, title, category, document type, tags, size, mtime
- chunks: heading-aware text chunks
- FTS index: SQLite FTS5 when available

The builder skips `.git`, dependency folders, generated caches, and locally cloned third-party repos under `09-agent-infra-catalog`.

## Search

```bash
./tools/agent_kb.py search "Milvus knowledge graph construction cost"
./tools/agent_kb.py search "data analysis agent" --tag statistics
./tools/agent_kb.py search "policy audit gateway" --tag governance --json
```

## Ask

`ask` is the agent-facing command. It does not pretend to be an LLM answer. It returns a context pack with paths, chunk ids, inferred domains, and recommended next actions.

```bash
./tools/agent_kb.py ask "我要做建筑造价知识库 agent，需要哪些资料？" --json
```

Agents should cite `path#chunk_id` entries from `context_pack` and refuse unsupported claims when the context pack is insufficient.

## Recommend

`recommend` maps an intent to relevant skills, agent roles, source paths, and supporting context. This is the best command when another agent needs routing hints before inspecting source files.

```bash
./tools/agent_kb.py recommend "build a construction cost knowledge base agent"
./tools/agent_kb.py recommend "design the Agent KB CLI MCP interface" --json
```

The command returns deterministic recommendations first, then a retrieval-backed context pack.

## Show A Chunk

```bash
./tools/agent_kb.py show 42
./tools/agent_kb.py show 42 --json
```

## List Documents

```bash
./tools/agent_kb.py docs --tag construction_cost
./tools/agent_kb.py docs --doc-type subagent --limit 20
```

## Stats

```bash
./tools/agent_kb.py stats
```

## Storage Roadmap

This CLI is the local control plane. It can later be backed by stronger storage layers:

- relational database for canonical metadata and audit logs
- Milvus for shared vector retrieval
- knowledge graph for entity relationship traversal

The current SQLite/FTS index is intentionally simple so the repository is immediately queryable without services.
