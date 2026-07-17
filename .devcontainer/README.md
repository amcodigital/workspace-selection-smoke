# Dev Container ownership and Envbuilder subset

Copier owns `.devcontainer/**`. Change repository dependencies, agent settings,
plugins, MCP configuration, and project skills in their native files instead.

The first AMCO Coder canary accepts only this closed subset:

- `.devcontainer/devcontainer.json`, which must build from a Dockerfile rather
  than a prebuilt `image`;
- exactly the keys `build.dockerfile`, `build.context`, `remoteUser`, and
  `postCreateCommand`; any other key is rejected;
- the repository-local Dockerfile, pinned byte-for-byte. `mise.toml` and
  `mise.lock` are pinned indirectly, through the fixed `postCreateCommand`; and
- no Compose, Features, privileges, capabilities, security options, mounts,
  forwarding, fallback image, credentials, or remote image cache.

The guard closes the keys inside `devcontainer.json`, not the files on disk.
Other files may sit under `.devcontainer/`, including this guide.

Before an operator creates a Coder workspace, the pinned `amco-infra`
`scripts/coder-envbuilder-compat --repo-root PATH --json` guard must accept the
exact repository commit and its Dev Container SHA-256.
