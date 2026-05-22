# agent-infra-hub — Make targets
#
# Living-documentation pipeline. Run `make docs` after changing CLI signatures,
# catalog entries, or moving files. CI should run `make docs-check`.

.PHONY: help docs docs-cli docs-links docs-catalog docs-check kb-build kb-stats clean-pyc

help: ## Show this help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-18s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

docs: ## Regenerate all derived documentation (CLI ref, link report, catalog audit).
	python3 tools/docs_gen.py all

docs-cli: ## Regenerate only CLI reference from argparse introspection.
	python3 tools/docs_gen.py cli

docs-links: ## Audit every markdown link in the repo.
	python3 tools/docs_gen.py links

docs-catalog: ## Audit catalog.json + 09-agent-infra-catalog/catalog.yaml against the filesystem.
	python3 tools/docs_gen.py catalog

docs-check: ## CI gate — fail if any committed generated doc is stale.
	python3 tools/docs_gen.py check

kb-build: ## Build the local SQLite/FTS knowledge index.
	python3 tools/agent_kb.py build

kb-stats: ## Show knowledge base statistics.
	python3 tools/agent_kb.py stats

clean-pyc: ## Remove Python bytecode caches.
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
