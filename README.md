# Policy handbook: start here

This is the policy handbook for every project under
[jasonelias144-svg](https://github.com/jasonelias144-svg) on GitHub (working
name: Open Project). It says who decides what, how work moves from an idea to
`main`, and what we expect of everyone who works here, human or AI.

Every repository carries copies of this handbook's short
[contributing guide](CONTRIBUTING.md), [security policy](SECURITY.md) and
[pull request template](.github/PULL_REQUEST_TEMPLATE.md), which point back
here ([P9](protocols/P9-repositories.md#required-files)).

## What we make

Free, open tools for people and AIs to think and build together. The main line
of work is the Lyceum family: Lyceum Commons, a site where people and AIs from
different companies share rooms; its mobile app; and Lyceum Local, a private AI
that runs in the browser. Every project, its state and its links are in
[REGISTRY.md](REGISTRY.md). Everyone who works here is in [PEOPLE.md](PEOPLE.md).

## How we work, in one minute

- **Open by default.** Repositories, reasoning and decisions are public unless
  there is a reason not to be.
- **Branches are free; `main` is earned.** Anyone may explore, prototype and
  propose without asking. A change reaches `main` only through a pull request
  with a recorded technical review.
- **Generation is cheap; promotion is demanding.** Ideas are welcome from
  anyone. Shipping them takes evidence: tests, review, and a clear reason.
- **Prior art first.** Before building something, find out how others already
  do it, and borrow standards rather than invent them.
- **Written down, or it didn't happen.** Most of us, the AIs especially, start
  each session with no memory of the last. The repositories hold the memory:
  `STATUS.md`, pull requests and decision records.
- **Authority is delegated, not claimed.** Who decides what is set out below.
  Being able to do something does not make it yours to decide.
- **Report outcomes honestly.** Say what you did, what you checked, and what
  you did not.

## Who decides what

| | Decides |
|---|---|
| **Founder** (Jason) | What each project is for and who it serves; who works here; accounts, money, licences and other legal matters; this governance. |
| **Technical lead** (Claude) | Everything about the code: architecture, tools, standards, reviews, merges and releases, within the founder's intent. |
| **Contributors** | How to do the work they were given, inside its scope. Anyone may propose anything. |

No change lands on `main` in any repository without the technical lead's
recorded approval. That includes the founder's own changes. In an emergency,
anyone may stop harm first and get review afterwards ([P7](protocols/P7-incidents.md)).
The details are in [GOVERNANCE.md](GOVERNANCE.md).

## The protocols

| | Protocol | Use it when |
|---|---|---|
| P1 | [Sessions](protocols/P1-sessions.md) | You start or end any piece of work |
| P2 | [Proposals](protocols/P2-proposals.md) | You have an idea, or want to try something |
| P3 | [Changes](protocols/P3-changes.md) | You change anything in a repository |
| P4 | [Review](protocols/P4-review.md) | A pull request needs approval and merging |
| P5 | [Decisions](protocols/P5-decisions.md) | Something needs deciding, or you disagree |
| P6 | [Releases](protocols/P6-releases.md) | Something goes live or comes down |
| P7 | [Incidents](protocols/P7-incidents.md) | Something is causing harm right now |
| P8 | [Access](protocols/P8-access.md) | Accounts, keys, secrets or identity are involved |
| P9 | [Repositories](protocols/P9-repositories.md) | A repository is created, set up or retired |

Standards for the work itself: [code](standards/code.md) and
[writing](standards/writing.md).

## If you are new

Follow [ONBOARDING.md](ONBOARDING.md). In short:

1. Read this page, [GOVERNANCE.md](GOVERNANCE.md) and [EXPECTATIONS.md](EXPECTATIONS.md).
2. Read P1, P3 and P4; skim the rest so you know they exist.
3. Read `AGENTS.md` and `STATUS.md` in the repository you will work on.
4. Make your first pull request: add yourself to [PEOPLE.md](PEOPLE.md).

## Where things are

```
README.md            this orientation
GOVERNANCE.md        roles, decision rights, approval authority
EXPECTATIONS.md      what we expect of everyone, and what you can expect
ONBOARDING.md        joining, returning and leaving
PEOPLE.md            who works here, in what role, with what access
REGISTRY.md          every repository: purpose, state, links
protocols/           P1-P9: how work is done
standards/           what good code and writing look like here
templates/           STATUS.md, AGENTS.md, CLAUDE.md, decision and incident records
decisions/           organization-wide decision records, numbered
CONTRIBUTING.md, SECURITY.md, .github/
                     contributing guide, security policy and templates;
                     copied into every repository (P9)
CODE_OF_CONDUCT.md   conduct, for everyone, everywhere we work
AGENTS.md, CLAUDE.md, STATUS.md
                     this repository's own working files, like every repository's
tools/check_links.py checks every link in the handbook (run by CI)
```

## Changing this handbook

Like everything else here, the handbook is corrigible. Propose changes by pull
request. The founder approves changes to governance and expectations; the
technical lead approves changes to protocols and standards. See
[GOVERNANCE.md](GOVERNANCE.md#changing-this-handbook).

Licence: not yet chosen. That is the founder's decision ([STATUS.md](STATUS.md#open-questions)).
