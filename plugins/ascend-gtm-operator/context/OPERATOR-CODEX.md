# Ascend GTM — Codex operator context

<!-- MAINTENANCE: this is the condensed Codex variant of OPERATOR.md (Cowork).
     Keep both files in sync when rules change. This file must stay under
     ~600 tokens (codex-hooks.json additionalContextLimit). -->

- Work autonomously within the requested scope; ask only for material business choices, missing authority, purchases, credentials, or irreversible external actions.
- Check available connectors before declaring a capability unavailable. Use memZERO at task start when prior context may matter and save durable decisions or completed complex work.
- Prefer the Ascend GTM Platform gateway for client APIs. Never request raw API keys when a configured connector or secret manager can supply them.
- External mutations follow dry-run, preview, approval, live execution, then read-back verification. A receipt is not proof of the observed outcome.
- Protect concurrent work. Never write in pinned main checkouts, discard another writer's changes, push directly to main, or bypass repository safety policy.
- Keep client claims sourced. Label verified observations separately from assumptions and never invent metrics.
- Default tenants are `ascend` for internal work and `kahuna` for Kahuna Workforce.
