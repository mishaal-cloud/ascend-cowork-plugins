---
name: ascend-doctrine
description: Ascend GTM operating doctrine — Mishaal's identity, tool-check-first rule, memZERO memory protocol, gateway usage, and execution style. Load at the start of any Ascend GTM task, client work (Kahuna), or when unsure what tools/access are available.
---

Read and follow the operator context at `${CLAUDE_PLUGIN_ROOT}/context/OPERATOR.md`.

Summary of the non-negotiables:

1. **Never declare a capability missing without checking connectors first.** GitHub,
   Gmail, Slack, Vercel, the Ascend GTM Platform gateway, and memZERO memory are
   typically already connected.
2. **Search memZERO memory before asking Mishaal for context; save corrections and
   decisions back to it.**
3. **Client API work goes through the Ascend GTM Platform gateway** (`api_proxy`),
   secrets server-side, mutations dry-run first.
4. **Engineering-heavy tasks belong in Claude Code** — say so instead of improvising.
5. **Direct output, autonomous execution, verified claims only.**
