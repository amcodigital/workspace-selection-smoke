---
name: workspace-selection-canary
description: Run the public workspace-selection smoke checks.
---

# Workspace selection canary

From the repository root, run `uv run python hello.py` and require
`hello from workspace-selection-smoke`. Then run
`uv run python hello_alias.py --version` and require `alias-0.1`. Do not create
`.beads/**`, create credentials, or contact production services.
