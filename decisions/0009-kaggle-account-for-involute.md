# 0009. The technical lead manages Involute's Kaggle account

- **Status:** accepted
- **Date:** 2026-11-23
- **Decided by:** founder, Jason (the delegation); technical lead (the
  safeguards)
- **Recorded by:** Claude (technical lead)

## Context

Involute, a private repository until 2027-01-20, is our entry in Google
Quantum AI's Verifiable Quantum Circuit Compilation competition on Kaggle.
The competition allows one Kaggle account per person, and the founder's is
the only one we use. Under [GOVERNANCE.md](../GOVERNANCE.md), accounts are
the director's to decide, and the technical lead advises and implements.
The technical lead had asked for a standing go-ahead to submit. The
founder answered, 2026-11-23:

> You may submit from my Kaggle account and to my Kaggle account. You can
> add it to your list of official activities, and place managing the
> project Kaggle account alongside managing GitHub repos for the project.

## Options considered

- **A go-ahead for each submission.** Safe, but it makes the founder a
  step in every cycle, five times a day at most.
- **A standing go-ahead, with no conditions.** Fast, but a broken or
  unverified entry could reach the leaderboard under the founder's name.
- **A standing go-ahead behind a gate,** each submission reported. This is
  what the technical lead recommended, with one more condition: that
  each submission beat our own previous best.

The founder granted a standing go-ahead without conditions. The gate and
the other safeguards below are the technical lead's own ("Decided by"),
and they drop the "previous best" condition: a test, such as the first
submission of the competition's own sample, or a probe of the
leaderboard need not beat it, and the two final submissions, not the
best score, are what is judged.

## Decision

### The founder's delegation

- The technical lead manages the founder's Kaggle account **for the
  Involute project**, as they manage the project's GitHub repositories:
  its notebooks, datasets and submissions.
- The technical lead may submit to the competition from that account.

### Safeguards (technical lead)

These are in Involute's `docs/RULES.md` ("Our submissions") and
`AGENTS.md`:

- **A gate before every submission:** the file checks the competition's
  scoring makes, then all three official verifiers under two salts, every
  result kept.
- **Our own code.** Every circuit submitted is built by code in the
  repository, or is the competition's own sample, said so.
- **Reported the same day** to the founder, and recorded in the project's
  ledger with the archive's SHA-256 and its scores.
- **Private by default.** Notebooks and datasets on the account stay
  private unless the founder decides otherwise. Nothing is posted on the
  forums without the founder.
- **The account's token** lives only in the session environment's network
  secrets: never printed, written, or asked for in a conversation
  ([P8](../protocols/P8-access.md)). Every session in that environment
  can use it, not only Involute's; the limit to this one project is kept
  by practice, not enforced. [PEOPLE.md](../PEOPLE.md) lists the access.
- **What stays the founder's:** the account itself, accepting rules and
  terms, people (team invitations and mergers on the account), the
  choice of the two final submissions (unless the founder says
  otherwise), prize documents, and anything that costs money.

## Consequences

- [GOVERNANCE.md](../GOVERNANCE.md)'s row on accounts points here.
- The delegation covers this one project and this one account. Another
  project or account needs the founder's word again.
- The founder may withdraw it at any time; the technical lead then stops
  submitting at once.

## Dissent

None.
