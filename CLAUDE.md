# Claude Code Instructions — workspace-selection-smoke

Public workspace selection canary

- Read `mise.toml` before changing runtimes or tools; use `mise install --locked`.

- Use native uv commands such as `uv add`, `uv sync`, and `uv run`; commit `pyproject.toml` and `uv.lock`.


- Keep project-specific reusable skills under `.agents/skills/`, one directory per skill.
- Never commit credentials, tokens, webhooks, `.env` files, or machine-specific paths.
- Treat `.devcontainer/**` as Copier-owned; treat dependency files, Claude settings, plugins, MCP configuration, and repository skills as repository-owned.
