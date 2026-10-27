# 0001. Founding policy: decision rights and code authority

- **Status:** accepted
- **Date:** 2026-10-27
- **Decided by:** founder, Jason
- **Recorded by:** Claude (technical lead)

## Context

The organization's projects have been built by several AI agents (Claude,
ChatGPT, Grok and others) working in separate apps, with the founder relaying
between them. Work stalled when one app's credits ran out, and nobody held the
code across projects. The founder no longer writes code, and wants an
organization that newcomers, human or AI, can join without confusion, and that
stays orderly as it grows while staying free and open.

## Options considered

- **The founder approves all code.** Doesn't fit: the founder does not review
  code, and approvals would carry no technical judgement.
- **Each agent owns its own projects.** This is what happened before. It led to
  overlapping work, no shared standards, and stalls when one agent stopped.
- **One technical lead holds all code decisions, under the founder's intent.**
  Chosen.

## Decision

1. The founder decides what each project is for, who works here, and matters
   of accounts, money and law.
2. All code decisions, across every repository on the account, are delegated
   to the technical lead: Claude, working in sessions under this handbook.
3. No change reaches `main` in any repository without the technical lead's
   recorded approval. This includes the founder's own changes.
4. Anyone may act first to stop harm in an emergency, and seek review after (P7).
5. This handbook (the `policy-handbook` repository) is the organization's policy.
   Changes to it follow [GOVERNANCE.md](../GOVERNANCE.md#changing-this-handbook).

## Consequences

- The approval gate depends on technical-lead sessions running. The founder
  starts them, or schedules them.
- GitHub enforces pull requests and checks on `main`, but cannot enforce the
  approval itself, because every agent pushes through one account. The approval
  record and the "Made by" declaration carry that weight.
- The technical lead remembers nothing between sessions, so its authority
  depends on the written record: `STATUS.md`, pull requests and decision records.
- Returning agents (for example when an app's credits renew) work under this
  policy from their first session back.

## Dissent

None.
