# workspace-selection-smoke

## AMCO coding brain

This repo is the `workspace-selection-smoke` source in AMCO's coding brain. Every AMCO repo is a
source in the same brain, and cross-source search is federated — so what one
repo learned is available here.

**Check the brain before grepping the tree or searching the web.** Upstream's
brain-first-lookup recipe is blunt about why: an agent that searches externally
before checking the brain is spending money for a worse answer. The brain holds
AMCO's *decisions and history*; the tree holds *current code*. Both matter, and
the brain is far faster for "why is it like this."

The brain is available over MCP (see `.mcp.json`) as `amco-brain`:

1. `search "<topic>"` — keyword; cheap, exact, no embeddings needed
2. `query "what do we know about <topic>"` — hybrid/semantic; catches paraphrase
3. only then grep, read source, or search the web

**Writing back.** Durable findings — a decision, a trap, a corrected assumption,
a runbook step — go into markdown **in this repo**. CI syncs on push. Do not
write straight to the brain's database: GitHub is the system of record and the
database is a derived cache, so a direct write has no repo behind it and is lost
on any rebuild.

Full recipe: `amcodigital/amco-brain` → `docs/recipes/brain-agent-loop.md`.
