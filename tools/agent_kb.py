#!/usr/bin/env python3
"""Local knowledge-base CLI for agent-infra-hub.

The CLI intentionally uses only Python standard library modules so it can run in
fresh agent workspaces without dependency installation.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Sequence

DEFAULT_DB = Path("data/agent-kb/index.sqlite")
TEXT_EXTENSIONS = {
    ".md",
    ".markdown",
    ".txt",
    ".rst",
    ".yaml",
    ".yml",
    ".json",
    ".toml",
}
CODE_EXTENSIONS = {
    ".py",
    ".ts",
    ".tsx",
    ".js",
    ".jsx",
    ".sh",
    ".sql",
}
SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".venv",
    "venv",
    "node_modules",
    "dist",
    "build",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".harness",
    "data/agent-kb",
    "09-agent-infra-catalog/awesome-indexes",
    "09-agent-infra-catalog/orchestrators",
    "09-agent-infra-catalog/routing-gateways",
    "09-agent-infra-catalog/governance-guardrails",
    "09-agent-infra-catalog/observability-hud",
    "09-agent-infra-catalog/skill-systems",
}
DOMAIN_KEYWORDS = {
    "construction_cost": [
        "construction cost",
        "quota item",
        "quota items",
        "bill of quantities",
        "boq",
        "material price",
        "milvus",
        "knowledge graph",
        "造价",
        "定额",
        "材料价",
        "知识图谱",
    ],
    "statistics": ["statistics", "statistical", "r code", "quarto", "regression", "data analysis", "统计", "回归"],
    "subagents": ["subagent", "multi-agent", "orchestrator", "workflow", "agent role", "分工"],
    "governance": ["governance", "guardrail", "policy", "audit", "quality gate", "门控", "治理"],
    "routing": ["routing", "gateway", "mcp", "a2a", "fallback", "router", "网关", "路由"],
    "observability": ["observability", "dashboard", "hud", "telemetry", "hooks", "观测"],
    "skills": ["skill", "skills", "capability", "catalog", "能力"],
}

ANSWER_DEFAULT_MODEL = "deepseek-chat"
ANSWER_DEFAULT_BASE_URL = "https://api.deepseek.com"

RECOMMENDATION_SETS = {
    "general": [
        {
            "kind": "skill",
            "name": "agent-infra-hub-kb-query",
            "path": "/home/l/.agents/skills/agent-infra-hub-kb-query/SKILL.md",
            "reason": "Query this repository through the local KB CLI and return grounded context packs.",
        },
        {
            "kind": "skill",
            "name": "agent-infra-hub-architect",
            "path": "/home/l/.agents/skills/agent-infra-hub-architect/SKILL.md",
            "reason": "Design or review agent-infra-hub structure, docs, catalogs, and use-case playbooks.",
        },
        {
            "kind": "document",
            "name": "Agent KB CLI docs",
            "path": "docs/cli/agent-kb-cli.md",
            "reason": "Human and agent command reference for build/search/ask/show/docs/stats.",
        },
    ],
    "construction_cost": [
        {
            "kind": "use_case",
            "name": "Construction Cost Knowledge Base Agent Playbook",
            "path": "use-cases/construction-cost-knowledge-base-agent.md",
            "reason": "Primary architecture path for construction-cost KB agents, including relational storage, Milvus, and knowledge graph roles.",
        },
        {
            "kind": "skill",
            "name": "rag-architect",
            "path": "06-catalogs/alirezarezvani-claude-skills/engineering/skills/rag-architect/SKILL.md",
            "reason": "Design chunking, hybrid retrieval, vector search, reranking, and context assembly.",
        },
        {
            "kind": "skill",
            "name": "database-designer",
            "path": "06-catalogs/alirezarezvani-claude-skills/engineering/skills/database-designer/SKILL.md",
            "reason": "Design canonical tables for documents, chunks, cost codes, quota items, prices, cases, claims, and audit logs.",
        },
        {
            "kind": "agent",
            "name": "knowledge-synthesizer",
            "path": "05-subagents/awesome-claude-code-subagents/categories/09-meta-orchestration/knowledge-synthesizer.md",
            "reason": "Extract entities and relationships for taxonomy and future graph traversal.",
        },
    ],
    "statistics": [
        {
            "kind": "use_case",
            "name": "Statistical Analysis Agent Playbook",
            "path": "use-cases/statistical-analysis-agent.md",
            "reason": "Primary assembly path for statistical-analysis agents using R, Quarto, data analysis, verification, and subagents.",
        },
        {
            "kind": "skill",
            "name": "writing-r-code",
            "path": "02-r-quarto/agentic-skills/writing-r-code/SKILL.md",
            "reason": "Author and verify R statistical analysis code.",
        },
        {
            "kind": "skill",
            "name": "quarto-authoring",
            "path": "02-r-quarto/posit-dev-skills/quarto/quarto-authoring/SKILL.md",
            "reason": "Generate reproducible Quarto reports.",
        },
        {
            "kind": "agent",
            "name": "data-analyst",
            "path": "05-subagents/awesome-claude-code-subagents/categories/05-data-ai/data-analyst.md",
            "reason": "Analyze business data, dashboards, reports, and statistical evidence.",
        },
    ],
    "governance": [
        {
            "kind": "skill",
            "name": "design-review-gate",
            "path": "07-agent-design/metaswarm/skills/design-review-gate/SKILL.md",
            "reason": "Run product, architecture, UX/API, security, and TDD readiness review before implementation.",
        },
        {
            "kind": "catalog",
            "name": "Agent infra governance catalog",
            "path": "09-agent-infra-catalog/catalog.yaml",
            "reason": "Find governance, guardrail, policy, sandbox, and audit candidates.",
        },
        {
            "kind": "agent",
            "name": "security-auditor",
            "path": "05-subagents/awesome-claude-code-subagents/categories/04-quality-security/security-auditor.md",
            "reason": "Review risky CLI, MCP, remote-fetch, or execution surfaces.",
        },
    ],
    "routing": [
        {
            "kind": "agent",
            "name": "mcp-developer",
            "path": "05-subagents/awesome-claude-code-subagents/categories/06-developer-experience/mcp-developer.md",
            "reason": "Design future MCP exposure for the CLI as an agent-callable tool.",
        },
        {
            "kind": "catalog",
            "name": "Routing gateways catalog",
            "path": "09-agent-infra-catalog/catalog.yaml",
            "reason": "Inspect MCP/A2A proxy, gateway, fallback, routing, and policy candidates.",
        },
        {
            "kind": "infrastructure",
            "name": "Claude Code MCP enhanced",
            "path": "08-infrastructure/tool-use-mcp/claude-code-mcp-enhanced/README.md",
            "reason": "Reference boomerang and agent-in-agent MCP patterns.",
        },
    ],
    "subagents": [
        {
            "kind": "agent",
            "name": "workflow-orchestrator",
            "path": "05-subagents/awesome-claude-code-subagents/categories/09-meta-orchestration/workflow-orchestrator.md",
            "reason": "Design reliable multi-step build/search/ask/recommend workflows.",
        },
        {
            "kind": "agent",
            "name": "cli-developer",
            "path": "05-subagents/awesome-claude-code-subagents/categories/06-developer-experience/cli-developer.md",
            "reason": "Own command hierarchy, flags, error messages, JSON output, and developer UX.",
        },
    ],
}


@dataclass(frozen=True)
class Document:
    path: str
    title: str
    category: str
    doc_type: str
    tags: str
    size_bytes: int
    mtime: str
    content: str


@dataclass(frozen=True)
class Chunk:
    ordinal: int
    heading: str
    text: str


def rel(path: Path, root: Path) -> str:
    # Preserve repository-relative identity instead of resolving symlinks into
    # their targets; otherwise two different entries can collapse to one path.
    return path.absolute().relative_to(root.absolute()).as_posix()


def should_skip_dir(path: Path, root: Path) -> bool:
    r = rel(path, root) if path.resolve() != root.resolve() else ""
    name = path.name
    return name in SKIP_DIRS or r in SKIP_DIRS or any(r.startswith(d + "/") for d in SKIP_DIRS)


def iter_files(root: Path, include_code: bool = False) -> Iterable[Path]:
    allowed = set(TEXT_EXTENSIONS)
    if include_code:
        allowed |= CODE_EXTENSIONS
    for current, dirs, files in os.walk(root):
        cur = Path(current)
        dirs[:] = [d for d in dirs if not (cur / d).is_symlink() and not should_skip_dir(cur / d, root)]
        for name in files:
            path = cur / name
            if path.suffix.lower() in allowed:
                yield path


def read_text(path: Path) -> str | None:
    try:
        data = path.read_bytes()
    except OSError:
        return None
    if b"\x00" in data[:4096]:
        return None
    for encoding in ("utf-8", "utf-8-sig", "latin-1"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return None


def infer_category(path: str) -> str:
    first = path.split("/", 1)[0]
    if re.match(r"^\d{2}-", first):
        return first
    if first in {"docs", "use-cases", "tools"}:
        return first
    return "root"


def infer_doc_type(path: str) -> str:
    name = Path(path).name.lower()
    if name == "skill.md":
        return "skill"
    if "subagent" in path or re.search(r"categories/\d{2}-", path):
        return "subagent"
    if path.endswith("catalog.yaml") or "/catalog" in path:
        return "catalog"
    if path.startswith("use-cases/"):
        return "use_case"
    if path.startswith("docs/audits/"):
        return "audit"
    if path.endswith("README.md"):
        return "readme"
    return Path(path).suffix.lower().lstrip(".") or "text"


def title_from_content(path: str, content: str) -> str:
    for line in content.splitlines()[:40]:
        m = re.match(r"^#\s+(.+?)\s*$", line)
        if m:
            return m.group(1).strip()
        if line.strip() and Path(path).name.upper() == "README.MD":
            return line.strip().lstrip("# ")[:120]
    return Path(path).stem


def infer_tags(content: str, path: str) -> list[str]:
    haystack = (path + "\n" + content[:12000]).lower()
    tags: list[str] = []
    for tag, words in DOMAIN_KEYWORDS.items():
        if any(word.lower() in haystack for word in words):
            tags.append(tag)
    return tags


def chunk_markdown(content: str, max_chars: int = 3600) -> list[Chunk]:
    chunks: list[Chunk] = []
    heading = ""
    buf: list[str] = []

    def flush() -> None:
        nonlocal buf
        text = "\n".join(buf).strip()
        if text:
            while len(text) > max_chars:
                cut = text.rfind("\n", 0, max_chars)
                if cut < max_chars // 2:
                    cut = max_chars
                chunks.append(Chunk(len(chunks), heading, text[:cut].strip()))
                text = text[cut:].strip()
            if text:
                chunks.append(Chunk(len(chunks), heading, text))
        buf = []

    for line in content.splitlines():
        m = re.match(r"^(#{1,4})\s+(.+?)\s*$", line)
        if m and buf:
            flush()
            heading = m.group(2).strip()
            buf.append(line)
        else:
            if m:
                heading = m.group(2).strip()
            buf.append(line)
            if sum(len(x) + 1 for x in buf) >= max_chars:
                flush()
    flush()
    return chunks or [Chunk(0, "", content[:max_chars].strip())]


def connect(db: Path) -> sqlite3.Connection:
    db.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    return conn


def has_fts5(conn: sqlite3.Connection) -> bool:
    try:
        conn.execute("CREATE VIRTUAL TABLE IF NOT EXISTS temp._fts_test USING fts5(x)")
        conn.execute("DROP TABLE temp._fts_test")
        return True
    except sqlite3.Error:
        return False



def open_index(db: Path) -> sqlite3.Connection | None:
    if not db.exists():
        print(f"index not found: {db}. Run `tools/agent_kb.py build --db {db}` first.", file=sys.stderr)
        return None
    conn = connect(db)
    try:
        conn.execute("SELECT 1 FROM metadata LIMIT 1")
        conn.execute("SELECT 1 FROM documents LIMIT 1")
        conn.execute("SELECT 1 FROM chunks LIMIT 1")
    except sqlite3.Error:
        conn.close()
        print(f"index is missing required tables: {db}. Rebuild it with `tools/agent_kb.py build --db {db}`.", file=sys.stderr)
        return None
    return conn

def init_db(conn: sqlite3.Connection) -> bool:
    fts = has_fts5(conn)
    conn.executescript(
        """
        DROP TABLE IF EXISTS chunks_fts;
        DROP TABLE IF EXISTS documents;
        DROP TABLE IF EXISTS chunks;
        DROP TABLE IF EXISTS metadata;

        CREATE TABLE documents (
          id INTEGER PRIMARY KEY,
          path TEXT UNIQUE NOT NULL,
          title TEXT NOT NULL,
          category TEXT NOT NULL,
          doc_type TEXT NOT NULL,
          tags TEXT NOT NULL,
          size_bytes INTEGER NOT NULL,
          mtime TEXT NOT NULL
        );

        CREATE TABLE chunks (
          id INTEGER PRIMARY KEY,
          document_id INTEGER NOT NULL REFERENCES documents(id),
          ordinal INTEGER NOT NULL,
          heading TEXT NOT NULL,
          text TEXT NOT NULL
        );

        CREATE TABLE metadata (
          key TEXT PRIMARY KEY,
          value TEXT NOT NULL
        );
        """
    )
    if fts:
        conn.execute(
            "CREATE VIRTUAL TABLE chunks_fts USING fts5(path, title, category, doc_type, tags, heading, text)"
        )
    return fts


def build(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    db = Path(args.db)
    conn = connect(db)
    fts = init_db(conn)
    count_docs = 0
    count_chunks = 0
    for path in sorted(iter_files(root, include_code=args.include_code)):
        content = read_text(path)
        if not content or not content.strip():
            continue
        rp = rel(path, root)
        stat = path.stat()
        doc = Document(
            path=rp,
            title=title_from_content(rp, content),
            category=infer_category(rp),
            doc_type=infer_doc_type(rp),
            tags=",".join(infer_tags(content, rp)),
            size_bytes=stat.st_size,
            mtime=datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat(),
            content=content,
        )
        cur = conn.execute(
            """
            INSERT INTO documents(path,title,category,doc_type,tags,size_bytes,mtime)
            VALUES (?,?,?,?,?,?,?)
            """,
            (doc.path, doc.title, doc.category, doc.doc_type, doc.tags, doc.size_bytes, doc.mtime),
        )
        doc_id = int(cur.lastrowid)
        for chunk in chunk_markdown(content):
            c = conn.execute(
                "INSERT INTO chunks(document_id,ordinal,heading,text) VALUES (?,?,?,?)",
                (doc_id, chunk.ordinal, chunk.heading, chunk.text),
            )
            chunk_id = int(c.lastrowid)
            if fts:
                conn.execute(
                    "INSERT INTO chunks_fts(rowid,path,title,category,doc_type,tags,heading,text) VALUES (?,?,?,?,?,?,?,?)",
                    (chunk_id, doc.path, doc.title, doc.category, doc.doc_type, doc.tags, chunk.heading, chunk.text),
                )
            count_chunks += 1
        count_docs += 1
    conn.execute("INSERT INTO metadata(key,value) VALUES (?,?)", ("built_at", datetime.now(timezone.utc).isoformat()))
    conn.execute("INSERT INTO metadata(key,value) VALUES (?,?)", ("root", str(root)))
    conn.execute("INSERT INTO metadata(key,value) VALUES (?,?)", ("fts5", "true" if fts else "false"))
    conn.commit()
    result = {"db": str(db), "documents": count_docs, "chunks": count_chunks, "fts5": fts}
    print_json_or_text(result, args.json)
    return 0


def where_filters(args: argparse.Namespace) -> tuple[str, list[str]]:
    clauses: list[str] = []
    params: list[str] = []
    if args.category:
        clauses.append("d.category = ?")
        params.append(args.category)
    if args.doc_type:
        clauses.append("d.doc_type = ?")
        params.append(args.doc_type)
    if args.tag:
        clauses.append("d.tags LIKE ?")
        params.append(f"%{args.tag}%")
    return (" AND ".join(clauses), params)


def search_rows(conn: sqlite3.Connection, args: argparse.Namespace) -> list[sqlite3.Row]:
    meta = dict(conn.execute("SELECT key,value FROM metadata").fetchall())
    where, params = where_filters(args)
    if meta.get("fts5") == "true":
        sql = """
        SELECT c.id AS chunk_id, d.path, d.title, d.category, d.doc_type, d.tags,
               c.ordinal, c.heading, substr(c.text, 1, 360) AS snippet,
               bm25(chunks_fts) AS rank
        FROM chunks_fts
        JOIN chunks c ON c.id = chunks_fts.rowid
        JOIN documents d ON d.id = c.document_id
        WHERE chunks_fts MATCH ?
        """
        all_params: list[str] = [args.query]
        if where:
            sql += " AND " + where
            all_params.extend(params)
        sql += " ORDER BY rank LIMIT ?"
        all_params.append(str(args.limit))
        return conn.execute(sql, all_params).fetchall()

    like = f"%{args.query}%"
    sql = """
    SELECT c.id AS chunk_id, d.path, d.title, d.category, d.doc_type, d.tags,
           c.ordinal, c.heading, substr(c.text, 1, 320) AS snippet, 0 AS rank
    FROM chunks c
    JOIN documents d ON d.id = c.document_id
    WHERE (c.text LIKE ? OR d.title LIKE ? OR d.path LIKE ?)
    """
    all_params = [like, like, like]
    if where:
        sql += " AND " + where
        all_params.extend(params)
    sql += " LIMIT ?"
    all_params.append(str(args.limit))
    return conn.execute(sql, all_params).fetchall()


def command_search(args: argparse.Namespace) -> int:
    conn = open_index(Path(args.db))
    if conn is None:
        return 2
    rows = search_rows(conn, args)
    data = [dict(row) for row in rows]
    print_json_or_text(data, args.json, search_text)
    return 0


def search_text(rows: list[dict]) -> str:
    if not rows:
        return "No results. Run `tools/agent_kb.py build` if the index is missing or stale."
    parts = []
    for i, row in enumerate(rows, 1):
        parts.append(
            f"{i}. {row['title']}\n"
            f"   path: {row['path']}#{row['chunk_id']}\n"
            f"   type: {row['doc_type']} | category: {row['category']} | tags: {row['tags']}\n"
            f"   heading: {row['heading']}\n"
            f"   snippet: {row['snippet']}"
        )
    return "\n\n".join(parts)


def command_show(args: argparse.Namespace) -> int:
    conn = open_index(Path(args.db))
    if conn is None:
        return 2
    row = conn.execute(
        """
        SELECT c.id AS chunk_id, d.path, d.title, d.category, d.doc_type, d.tags,
               c.ordinal, c.heading, c.text
        FROM chunks c JOIN documents d ON d.id = c.document_id
        WHERE c.id = ?
        """,
        (args.chunk_id,),
    ).fetchone()
    if row is None:
        print(f"chunk not found: {args.chunk_id}", file=sys.stderr)
        return 1
    data = dict(row)
    print_json_or_text(data, args.json, lambda r: f"# {r['title']}\n\npath: {r['path']}#{r['chunk_id']}\nheading: {r['heading']}\n\n{r['text']}")
    return 0


def command_stats(args: argparse.Namespace) -> int:
    conn = open_index(Path(args.db))
    if conn is None:
        return 2
    docs = conn.execute("SELECT COUNT(*) FROM documents").fetchone()[0]
    chunks = conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
    by_category = [dict(r) for r in conn.execute("SELECT category, COUNT(*) AS documents FROM documents GROUP BY category ORDER BY category")]
    by_type = [dict(r) for r in conn.execute("SELECT doc_type, COUNT(*) AS documents FROM documents GROUP BY doc_type ORDER BY documents DESC")]
    meta = {r[0]: r[1] for r in conn.execute("SELECT key,value FROM metadata")}
    data = {"documents": docs, "chunks": chunks, "metadata": meta, "by_category": by_category, "by_type": by_type}
    print_json_or_text(data, args.json, stats_text)
    return 0


def stats_text(data: dict) -> str:
    lines = [f"documents: {data['documents']}", f"chunks: {data['chunks']}", f"fts5: {data['metadata'].get('fts5')}"]
    lines.append("\nby category:")
    lines.extend(f"- {r['category']}: {r['documents']}" for r in data["by_category"])
    lines.append("\nby type:")
    lines.extend(f"- {r['doc_type']}: {r['documents']}" for r in data["by_type"])
    return "\n".join(lines)


def command_ask(args: argparse.Namespace) -> int:
    conn = open_index(Path(args.db))
    if conn is None:
        return 2
    domains = route_domains(args.question)
    rows = search_with_expansion(conn, args, domains)
    data = {
        "question": args.question,
        "detected_domains": domains,
        "recommended_next_actions": next_actions(domains),
        "context_pack": rows,
        "agent_instruction": "Use the context_pack paths and chunk ids as citations. If evidence is insufficient, say what source is missing instead of guessing.",
    }
    print_json_or_text(data, args.json, ask_text)
    return 0


def source_pack(rows: Sequence[dict], limit: int | None = None) -> list[dict]:
    pack: list[dict] = []
    for i, row in enumerate(rows, 1):
        if limit is not None and i > limit:
            break
        pack.append(
            {
                "source_id": i,
                "path": row["path"],
                "chunk_id": row["chunk_id"],
                "title": row["title"],
                "heading": row["heading"],
                "snippet": row["snippet"],
                "category": row["category"],
                "doc_type": row["doc_type"],
                "tags": row["tags"],
            }
        )
    return pack


def source_text(pack: Sequence[dict]) -> str:
    lines: list[str] = []
    for item in pack:
        lines.append(
            f"[{item['source_id']}] {item['path']}#{item['chunk_id']} | "
            f"{item['title']} | {item['heading']}"
        )
        lines.append(item["snippet"])
    return "\n\n".join(lines)


def deepseek_generate(question: str, sources: Sequence[dict], args: argparse.Namespace) -> dict:
    api_key = os.getenv("DEEPSEEK_API_KEY") or os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Set DEEPSEEK_API_KEY before using `answer`.")

    base_url = (os.getenv("DEEPSEEK_BASE_URL") or os.getenv("OPENAI_BASE_URL") or ANSWER_DEFAULT_BASE_URL).rstrip("/")
    model = os.getenv("DEEPSEEK_MODEL") or os.getenv("OPENAI_MODEL") or ANSWER_DEFAULT_MODEL
    system_prompt = (
        "You are the agent layer on top of agent-infra-hub. "
        "Answer in the same language as the question. "
        "Use only the provided sources and cite them with [source_id] references. "
        "If evidence is insufficient, say what source is missing. "
        "Do not invent repository facts."
    )
    user_prompt = (
        f"Question:\n{question}\n\n"
        f"Sources:\n{source_text(sources)}\n\n"
        "Write a concise, grounded answer. Include cited source ids inline."
    )
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": getattr(args, "temperature", 0.2),
        "max_tokens": getattr(args, "max_tokens", 1200),
    }
    request = urllib.request.Request(
        f"{base_url}/chat/completions",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=getattr(args, "timeout", 60)) as resp:
            response = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace") if exc.fp else ""
        raise RuntimeError(f"DeepSeek request failed: {exc.code} {exc.reason}: {body}".strip()) from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"DeepSeek request failed: {exc.reason}") from exc

    try:
        content = response["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError(f"Unexpected DeepSeek response: {response}") from exc

    return {
        "model": model,
        "base_url": base_url,
        "answer": content,
        "raw": response,
    }


def answer_text(data: dict) -> str:
    lines = [f"model: {data['model']}", f"base_url: {data['base_url']}", "", data["answer"]]
    if data.get("sources"):
        lines.append("")
        lines.append("sources:")
        for item in data["sources"]:
            lines.append(f"- [{item['source_id']}] {item['path']}#{item['chunk_id']} | {item['heading']}")
    return "\n".join(lines)


def command_answer(args: argparse.Namespace) -> int:
    conn = open_index(Path(args.db))
    if conn is None:
        return 2
    domains = route_domains(args.question)
    rows = search_with_expansion(conn, args, domains)
    if not rows:
        rows = search_with_expansion(conn, argparse.Namespace(**{**vars(args), "limit": 3}), ["general"])
    sources = source_pack(rows, getattr(args, "source_limit", 5))
    try:
        result = deepseek_generate(args.question, sources, args)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        print("Use `ask`/`recommend` for retrieval-only mode, or set DeepSeek env vars for synthesis.", file=sys.stderr)
        return 2

    data = {
        "question": args.question,
        "detected_domains": domains,
        "sources": sources,
        **result,
    }
    print_json_or_text(data, args.json, answer_text)
    return 0


def expanded_queries(question: str, domains: Sequence[str]) -> list[str]:
    queries = [question]
    if "construction_cost" in domains:
        queries.extend([
            "construction cost knowledge base Milvus knowledge graph",
            "Construction Cost Knowledge Base Agent Playbook Storage Choice",
            "quota item material price bill of quantities knowledge graph",
        ])
    if "statistics" in domains:
        queries.extend([
            "statistical analysis agent",
            "R Quarto statistical analysis data quality",
        ])
    if "governance" in domains:
        queries.extend([
            "agent governance policy audit quality gate",
            "design-review-gate governance guardrail",
        ])
    if "routing" in domains:
        queries.extend([
            "agent gateway routing MCP A2A fallback",
            "routing-gateways agentgateway mcp proxy",
        ])
    # Preserve order while deduplicating.
    return list(dict.fromkeys(queries))


def search_with_expansion(conn: sqlite3.Connection, args: argparse.Namespace, domains: Sequence[str]) -> list[dict]:
    seen: set[int] = set()
    rows: list[dict] = []
    per_query_limit = max(args.limit, 4)
    source_query = getattr(args, "question", getattr(args, "intent", ""))
    for query in expanded_queries(source_query, domains):
        search_args = argparse.Namespace(
            db=args.db,
            query=query,
            limit=per_query_limit,
            category=args.category,
            doc_type=args.doc_type,
            tag=args.tag,
            json=False,
        )
        for row in search_rows(conn, search_args):
            item = dict(row)
            chunk_id = int(item["chunk_id"])
            if chunk_id in seen:
                continue
            seen.add(chunk_id)
            rows.append(item)
            if len(rows) >= args.limit:
                return rows
    return rows

def route_domains(question: str) -> list[str]:
    q = question.lower()
    domains = []
    for tag, words in DOMAIN_KEYWORDS.items():
        if any(word.lower() in q for word in words):
            domains.append(tag)
    return domains or ["general"]


def next_actions(domains: Sequence[str]) -> list[str]:
    actions = ["Read the top context_pack entries before answering."]
    if "construction_cost" in domains:
        actions.append("Start from use-cases/construction-cost-knowledge-base-agent.md and verify storage/retrieval assumptions.")
    if "statistics" in domains:
        actions.append("Start from use-cases/statistical-analysis-agent.md and inspect R/Quarto/data-analysis skills.")
    if "governance" in domains:
        actions.append("Inspect metaswarm quality gates and 09 governance catalog entries.")
    if "routing" in domains:
        actions.append("Inspect MCP/gateway/routing entries in 08-infrastructure and 09-agent-infra-catalog.")
    return actions



def ask_text(data: dict) -> str:
    lines = [f"question: {data['question']}"]
    lines.append("domains: " + ", ".join(data["detected_domains"]))
    lines.append("\nrecommended next actions:")
    lines.extend(f"- {action}" for action in data["recommended_next_actions"])
    lines.append("\ncontext pack:")
    for i, row in enumerate(data["context_pack"], 1):
        lines.append(
            f"{i}. {row['title']}\n"
            f"   path: {row['path']}#{row['chunk_id']}\n"
            f"   type: {row['doc_type']} | category: {row['category']} | tags: {row['tags']}\n"
            f"   heading: {row['heading']}\n"
            f"   snippet: {row['snippet']}"
        )
    lines.append("\nagent instruction: " + data["agent_instruction"])
    return "\n".join(lines)


def recommendation_items(domains: Sequence[str]) -> list[dict]:
    selected: list[dict] = []
    seen: set[tuple[str, str]] = set()
    for domain in ["general", *domains]:
        for item in RECOMMENDATION_SETS.get(domain, []):
            key = (item["kind"], item["path"])
            if key in seen:
                continue
            seen.add(key)
            item_with_domain = dict(item)
            item_with_domain["matched_domain"] = domain
            selected.append(item_with_domain)
    return selected


def command_recommend(args: argparse.Namespace) -> int:
    conn = open_index(Path(args.db))
    if conn is None:
        return 2
    domains = route_domains(args.intent)
    rows = search_with_expansion(conn, args, domains)
    data = {
        "intent": args.intent,
        "detected_domains": domains,
        "recommendations": recommendation_items(domains),
        "context_pack": rows,
        "agent_instruction": "Use recommendations as routing hints and context_pack as source evidence. Inspect referenced files before acting.",
    }
    print_json_or_text(data, args.json, recommend_text)
    return 0


def recommend_text(data: dict) -> str:
    lines = [f"intent: {data['intent']}"]
    lines.append("domains: " + ", ".join(data["detected_domains"]))
    lines.append("\nrecommendations:")
    for i, item in enumerate(data["recommendations"], 1):
        lines.append(
            f"{i}. {item['name']} ({item['kind']})\n"
            f"   path: {item['path']}\n"
            f"   domain: {item['matched_domain']}\n"
            f"   reason: {item['reason']}"
        )
    lines.append("\ncontext pack:")
    for i, row in enumerate(data["context_pack"], 1):
        lines.append(f"{i}. {row['title']} — {row['path']}#{row['chunk_id']} — {row['heading']}")
    lines.append("\nagent instruction: " + data["agent_instruction"])
    return "\n".join(lines)

def command_docs(args: argparse.Namespace) -> int:
    conn = open_index(Path(args.db))
    if conn is None:
        return 2
    where, params = where_filters(args)
    sql = "SELECT path,title,category,doc_type,tags,size_bytes,mtime FROM documents d"
    if where:
        sql += " WHERE " + where
    sql += " ORDER BY category,path LIMIT ?"
    params.append(str(args.limit))
    rows = [dict(r) for r in conn.execute(sql, params)]
    print_json_or_text(rows, args.json, docs_text)
    return 0


def docs_text(rows: list[dict]) -> str:
    return "\n".join(f"- {r['path']} | {r['doc_type']} | {r['tags']} | {r['title']}" for r in rows) or "No documents."


def print_json_or_text(data, as_json: bool, text_fn=None) -> None:
    if as_json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    elif text_fn:
        print(text_fn(data))
    else:
        if isinstance(data, dict):
            for k, v in data.items():
                print(f"{k}: {v}")
        else:
            print(data)


REPL_HELP = """Commands:
  <question>                  Ask by default and return a context pack
  ask <question>              Ask a question
  answer <question>           Ask and synthesize with DeepSeek
  search <query>              Search indexed chunks
  recommend <intent>          Recommend skills, agents, and source paths
  show <chunk_id>             Show a source chunk
  docs [filters]              List indexed docs, e.g. docs --doc-type use_case
  stats                       Show index stats
  help                        Show this help
  exit | quit | q             Leave the REPL

Common filters for ask/search/recommend/docs:
  --limit N
  --category CATEGORY
  --doc-type TYPE
  --tag TAG
  --json
"""


def split_repl_line(line: str) -> list[str]:
    try:
        import shlex
        return shlex.split(line)
    except ValueError as exc:
        print(f"parse error: {exc}", file=sys.stderr)
        return []


def split_text_command(tokens: list[str]) -> tuple[str, list[str]]:
    text_parts: list[str] = []
    options: list[str] = []
    value_options = {"--limit", "--category", "--doc-type", "--tag"}
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.startswith("--"):
            options.append(token)
            if token in value_options and i + 1 < len(tokens):
                i += 1
                options.append(tokens[i])
        else:
            text_parts.append(token)
        i += 1
    return " ".join(text_parts).strip(), options


def repl_command_args(db: str, words: list[str]) -> list[str] | None:
    if not words:
        return None
    command = words[0]
    if command in {"exit", "quit", "q"}:
        return ["__exit__"]
    if command in {"help", "?"}:
        return ["__help__"]
    if command in {"ask", "search", "recommend", "answer"}:
        text, options = split_text_command(words[1:])
        if not text:
            print(f"{command} requires text", file=sys.stderr)
            return None
        return ["--db", db, command, text, *options]
    if command in {"show", "docs", "stats"}:
        return ["--db", db, *words]
    text, options = split_text_command(words)
    return ["--db", db, "ask", text, *options]


def command_repl(args: argparse.Namespace) -> int:
    print("agent-kb interactive mode. Type `help` for commands, `exit` to quit.")
    print(f"db: {args.db}")
    while True:
        try:
            line = input("agent-kb> ").strip()
        except EOFError:
            print()
            return 0
        except KeyboardInterrupt:
            print("\nUse `exit` to quit.")
            continue
        if not line:
            continue
        words = split_repl_line(line)
        command_args = repl_command_args(args.db, words)
        if command_args is None:
            continue
        if command_args == ["__exit__"]:
            return 0
        if command_args == ["__help__"]:
            print(REPL_HELP)
            continue
        try:
            code = main(command_args)
        except SystemExit as exc:
            code = int(exc.code or 0) if isinstance(exc.code, int) else 1
        if code:
            print(f"command exited with code {code}", file=sys.stderr)
    return 0

def add_common_filters(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--category", help="Filter by top-level category, for example 05-subagents or use-cases")
    parser.add_argument("--doc-type", help="Filter by inferred document type, for example skill, subagent, use_case, catalog")
    parser.add_argument("--tag", help="Filter by inferred domain tag, for example construction_cost, statistics, governance")


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build and query the local agent-infra-hub knowledge base.")
    parser.add_argument("--db", default=str(DEFAULT_DB), help="SQLite index path")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("build", help="Build the local SQLite/FTS knowledge index")
    p.add_argument("--root", default=".", help="Repository root")
    p.add_argument("--include-code", action="store_true", help="Also index common code files")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=build)

    p = sub.add_parser("search", help="Search indexed chunks")
    p.add_argument("query")
    p.add_argument("--limit", type=int, default=8)
    p.add_argument("--json", action="store_true")
    add_common_filters(p)
    p.set_defaults(func=command_search)

    p = sub.add_parser("ask", help="Return a structured context pack for a human or agent question")
    p.add_argument("question")
    p.add_argument("--limit", type=int, default=8)
    p.add_argument("--json", action="store_true")
    add_common_filters(p)
    p.set_defaults(func=command_ask)

    p = sub.add_parser("answer", help="Generate a DeepSeek-synthesized answer from retrieved context")
    p.add_argument("question")
    p.add_argument("--limit", type=int, default=8)
    p.add_argument("--source-limit", type=int, default=5)
    p.add_argument("--temperature", type=float, default=0.2)
    p.add_argument("--max-tokens", type=int, default=1200)
    p.add_argument("--timeout", type=int, default=60)
    p.add_argument("--json", action="store_true")
    add_common_filters(p)
    p.set_defaults(func=command_answer)

    p = sub.add_parser("show", help="Show a chunk by id")
    p.add_argument("chunk_id", type=int)
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=command_show)


    p = sub.add_parser("recommend", help="Recommend relevant skills, agents, and source paths for an intent")
    p.add_argument("intent")
    p.add_argument("--limit", type=int, default=6)
    p.add_argument("--json", action="store_true")
    add_common_filters(p)
    p.set_defaults(func=command_recommend)

    p = sub.add_parser("docs", help="List indexed documents")
    p.add_argument("--limit", type=int, default=80)
    p.add_argument("--json", action="store_true")
    add_common_filters(p)
    p.set_defaults(func=command_docs)


    p = sub.add_parser("repl", help="Start an interactive human/agent query shell")
    p.set_defaults(func=command_repl)

    p = sub.add_parser("stats", help="Show index statistics")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=command_stats)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
