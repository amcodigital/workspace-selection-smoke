# workspace-selection-smoke

Disposable **public** test rig for the AMCO Coder/Envbuilder **workspace-selection
canary** (`amcoinfra-lsev`). This is not a product repository and nothing here is
used in production.

It exists only so the canary has a public subject to seed with the Copier project
template and rebuild as a Coder workspace. It is public because workspace
repository access (the repo-scoped GitHub App broker, `amcoinfra-t2xk`) is not
built yet, so a private subject could not be cloned unattended.

Deliberately kept separate from `gascity-smoke`, which is Gas City's own
smoke-test rig, so that the two tracks do not entangle.

The canary permanently tags this repository and enables immutable releases on it.
