# Governance

Who decides what, and how authority works here. Adopted in
[decision 0001](decisions/0001-founding-policy.md).

## Roles

**Founder: Jason.** Began the organization and its projects. That is a
matter of their history: it does not change, and it passes to no one.

**Director: Jason, today.** The office that decides what this page gives
the director to decide. The founder holds it now, and might not later.
Whoever holds it has that authority, and no more of the founder's place
than that.

The two were told apart on 2026-11-16
([decision 0004](decisions/0004-founder-and-director.md)). Until then
these pages called both "the founder". So where a protocol, a standard,
a template or a repository's own rules say that the founder decides, or
send a question to the founder, they mean the director. Where they
quote the founder, or say what the founder did or set, they mean the
founder.

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
| Purpose: what a project is for, who it serves, what it must never do | Director | Anyone may propose; the technical lead advises |
| People: who works here, on what, and when they leave | Director | The technical lead may recommend |
| Accounts, money, legal terms, anything that costs money | Director | The technical lead advises and implements |
| Licences | Settled once: the founder's standing policy is one licence, always, for everything the founder makes public; CC0 1.0, chosen by the technical lead at the founder's request ([decision 0003](decisions/0003-licence-cc0.md), [P9](protocols/P9-repositories.md)) | The technical lead applies it everywhere without asking; only a departure from it goes to the director |
| Starting or retiring a project | Director | The technical lead sets it up or winds it down ([P9](protocols/P9-repositories.md)) |
| Code: architecture, languages, libraries, structure, standards | Technical lead | Contributors propose and argue their case |
| Review, approval and merging of every change to `main` | Technical lead | — |
| Releases and deploys, within the director's intent | Technical lead | The director may halt any release |
| How to carry out an assigned task, inside its scope | The contributor doing it | Subject to review |
| Conduct | Director | Anyone may report |

The test for telling a purpose question from a code question is in
[P5](protocols/P5-decisions.md#intent-or-code): would a person using the
product, or the director, notice the difference in what it does, who it is for,
what it costs, or what happens to people's data? If yes, it goes to the director.

## Approval authority

The founder, as director, has delegated all code decisions to the
technical lead. In practice:

1. **Every change to `main`, in every repository on the account, needs the
   technical lead's recorded approval** ([P4](protocols/P4-review.md)). This
   applies to contributors, visitors, the founder and the director.
2. The approval is a written record on the pull request, tied to the exact
   commit approved. It is not a feeling and not a conversation.
3. The technical lead's own changes get a recorded self-review. Significant
   ones also get an independent review by a fresh session before merging
   ([P4](protocols/P4-review.md#the-technical-leads-own-changes)).
4. Questions of purpose that come up inside technical work go to the director,
   with a recommendation ([P5](protocols/P5-decisions.md)).

## What the director keeps

- The final word on purpose, people, accounts, money and legal matters.
- The power to **halt** any release or change on grounds of intent, at any time.
- The power to change this governance, including the delegation itself.
- Ownership of every account, key and repository ([P8](protocols/P8-access.md)).
  These are the founder's own today. The office passes only by the
  director's own recorded word, naming who takes it and from when. What
  becomes of the accounts, keys and repositories then is the founder's
  own act, and is settled when it is needed
  ([decision 0005](decisions/0005-decide-and-what-stays.md)).

The founder does not write or merge code, and has committed to putting any
change of their own through the same review as everyone else.

## What stays the founder's

That the founder began this, and everything recorded as the founder's:
the words, the founding ideas, and the decisions made while the founder
was director, which stand as decided until a director changes them by
the same rules. No one else becomes the founder.

One thing no later director can change: what a project's founding words
say it must never do. In open-worlds that is the charter's floor: exit,
voice and information; free, and never a money machine. A project that
dropped them would be a different project, and would take another name
([decision 0005](decisions/0005-decide-and-what-stays.md)).

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

- **Governance and expectations:** the director decides. The technical lead
  usually drafts the change.
- **Protocols, standards and templates:** the technical lead decides. A change
  that alters how people work is noted in a decision record so the director sees it.
- **People and registry entries:** routine updates, by pull request like
  everything else.

Every change goes through a pull request, including changes to this page.
