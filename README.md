# Ascend Plugins

Plugin marketplace for Ascend GTM — shared context and skills across Claude Cowork and Claude Code.

## Plugins

- **ascend-gtm-operator** — operator doctrine injected at session start (hook) + `/ascend-doctrine` skill. Covers: identity, tool-check-first rule, memZERO memory protocol, Ascend GTM Platform gateway usage, surface split (Cowork vs Claude Code), execution style.

## Install

**Cowork / Claude Desktop:** Customize → Plugins → + → Add marketplace → `mishaal-cloud/ascend-cowork-plugins` (or upload the plugin folder if private-repo sync is unavailable). Then install `ascend-gtm-operator`.

**Claude Code CLI:** `/plugin marketplace add mishaal-cloud/ascend-cowork-plugins` then `/plugin install ascend-gtm-operator@ascend-plugins`. Note: Claude Code already loads `~/.claude/CLAUDE.md` — installing there duplicates context; intended surface is Cowork.

## Related infrastructure

- memZERO memory connector for claude.ai/Cowork: `https://memory-auth.ascendgtm.net/mcp` (OAuth proxy → `memory-mcp.ascendgtm.net`, repo: `mishaal-cloud/memory-oauth-proxy`)
