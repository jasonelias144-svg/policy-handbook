# Governance

Who decides what, and how authority works here. Adopted in
[decision 0001](decisions/0001-founding-policy.md).

## Roles

**Founder: Jason.** Owns the organization and everything in it.

**Technical lead: Claude.** The Claude sessions that work under this handbook
(Claude Code, started by the founder or by a scheduled task). Each session
starts without memory of earlier ones. The authority belongs to the role, so it
holds from session to session through what is written in the repositories.

**Contributors.** Everyone else who is admitted to work here: AI agents such as
ChatGPT, Codex or Grok, and people. Listed in [PEOPLE.md](PEOPLE.md).

**Visitors.** Anyone outside who opens an issue, a proposal or a pull request
on a public repository. Visitors are welcome. Their work goes through the same
review as everyone else's.

## Decision rights

| Area | Decides | Others' part |
|---|---|---|
| Purpose: what a project is for, who it serves, what it must never do | Founder | Anyone may propose; the technical lead advises |
| People: who works here, on what, and when they leave | Founder | The technical lead may recommend |
| Accounts, money, licences, legal terms, anything that costs money | Founder | The technical lead advises and implements |
| Starting or retiring a project | Founder | The technical lead sets it up or winds it down ([P9](protocols/P9-repositories.md)) |
| Code: architecture, languages, libraries, structure, standards | Technical lead | Contributors propose and argue their case |
| Review, approval and merging of every change to `main` | Technical lead | — |
| Releases and deploys, within the founder's intent | Technical lead | The founder may halt any release |
| How to carry out an assigned task, inside its scope | The contributor doing it | Subject to review |
| Conduct | Founder | Anyone may report |

The test for telling a purpose question from a code question is in
[P5](protocols/P5-decisions.md#intent-or-code): would a person using the
product, or the founder, notice the difference in what it does, who it is for,
what it costs, or what happens to people's data? If yes, it goes to the founder.

## Approval authority

The founder has delegated all code decisions to the technical lead. In
practice:

1. **Every change to `main`, in every repository on the account, needs the
   technical lead's recorded approval** ([P4](protocols/P4-review.md)). This
   applies to contributors, visitors, and the founder.
2. The approval is a written record on the pull request, tied to the exact
   commit approved. It is not a feeling and not a conversation.
3. The technical lead's own changes get a recorded self-review. Significant
   ones also get an independent review by a fresh session before merging
   ([P4](protocols/P4-review.md#the-technical-leads-own-changes)).
4. Questions of purpose that come up inside technical work go to the founder,
   with a recommendation ([P5](protocols/P5-decisions.md)).

## What the founder keeps

- The final word on purpose, people, accounts, money and legal matters.
- The power to **halt** any release or change on grounds of intent, at any time.
- The power to change this governance, including the delegation itself.
- Ownership of every account, key and repository ([P8](protocols/P8-access.md)).

The founder does not write or merge code, and has committed to putting any
change of their own through the same review as everyone else.

## The emergency exception

When something is causing harm right now, anyone may take the smallest step
that stops it, without approval: take a site offline, revoke a key, revert the
last change. They then report it and get it reviewed.
See [P7](protocols/P7-incidents.md).

## Enforcement

GitHub enforces part of this. Each repository's `main` is protected so that
nothing lands without a pull request, and without passing checks where checks
exist ([P9](protocols/P9-repositories.md#settings)). GitHub cannot enforce the
technical lead's approval: every agent pushes through the founder's account,
and GitHub does not let an account approve its own pull request. So that rule
is kept by practice and by the approval record. A merge without one is a
breach, and is reverted until reviewed.

## When documents disagree

GOVERNANCE.md, then EXPECTATIONS.md, then the protocols, then the standards,
then a repository's own `AGENTS.md`. A repository may add stricter rules of its
own, but it may not loosen these.

## Changing this handbook

- **Governance and expectations:** the founder decides. The technical lead
  usually drafts the change.
- **Protocols, standards and templates:** the technical lead decides. A change
  that alters how people work is noted in a decision record so the founder sees it.
- **People and registry entries:** routine updates, by pull request like
  everything else.

Every change goes through a pull request, including changes to this page.
