# Codex platform packages

These 18 packages preserve the complete available skill directories from four Codex system skills and fourteen plugin skills. They are reference snapshots, excluded from the ordinary installer.

The exact IDs, cache version paths and content hashes are in [catalog.json](../catalog.json); browse their folders through [CATALOG.md](../CATALOG.md).

- `codex-system:*`: image generation, OpenAI documentation and skill authoring/installation helpers.
- `computer-use:*`: the Codex computer-use runtime.
- `plugin-management:*`, `sites:*`, `visualize:*`, `work-pets:*`: connected app/plugin tools.
- `documents:*`, `pdf:*`, `presentations:*`, `spreadsheets:*`, `template-creator:*`: document and artifact runtimes, bundled libraries or connected application services.

A plugin prefix identifies the provider namespace; it is not a standalone marketplace URL. No public upstream URL was verified for these cached packages. Their local source paths are recorded relative to the user's home directory, without publishing account settings or credentials.

Installing these folders in Claude or Hermes does not supply Codex APIs. Review and adapt the tool calls, runtime paths and authentication requirements before use. License files are retained where supplied; absence of a license does not imply unrestricted reuse.

Only the newest available version of each included plugin skill is kept. Cached template packages unrelated to the session skill list are omitted.
