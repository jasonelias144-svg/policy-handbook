# Onboarding

How someone joins, returns, and leaves. The same steps apply to people and to
AI agents. Where an AI's situation is different, this page says so.

## Before someone starts (founder)

1. **Decide to bring them in**, and what for. Who works here is the founder's
   decision ([GOVERNANCE.md](GOVERNANCE.md#decision-rights)).
2. **Set the scope:** which repositories, and the first task. Small and
   well-defined is best.
3. **Give the least access that does the job** ([P8](protocols/P8-access.md)),
   and note it in [PEOPLE.md](PEOPLE.md). Note what access they have, never the
   secret itself.
4. **Tell the technical lead** a newcomer is coming, so the first pull request
   gets reviewed promptly.

## First session (newcomer)

1. Read the [orientation](README.md).
2. Read [GOVERNANCE.md](GOVERNANCE.md) and [EXPECTATIONS.md](EXPECTATIONS.md).
3. Read [P1 Sessions](protocols/P1-sessions.md),
   [P3 Changes](protocols/P3-changes.md) and [P4 Review](protocols/P4-review.md)
   closely. Skim the other protocols so you know what they cover.
4. Read the [code of conduct](CODE_OF_CONDUCT.md).
5. In the repository you will work on, read `AGENTS.md`, `STATUS.md` and the
   open pull requests.
6. **First pull request:** add or update your entry in [PEOPLE.md](PEOPLE.md),
   on a branch, using the pull request template. It is small on purpose: it
   takes you through the whole path from branch to review to merge once,
   before real work depends on it.
7. **First task:** the one you were given, or the top item under "Next" in the
   repository's `STATUS.md`.

You are onboarded when your first pull request is merged and you can say, in a
sentence, who decides what and where you leave your handoff.

## Onboarding an AI agent

Most AI agents work in sessions that start with no memory, often in an app that
has no access to this repository until it is given a link or a connector. So
the onboarding has to arrive with the work. The founder pastes the brief below
into the agent's first message, filling in the brackets. After that,
`AGENTS.md` in each repository carries the rules from session to session.

```text
You are joining the projects at github.com/jasonelias144-svg as a contributor.
Your name here: [name, e.g. "ChatGPT (Codex)"]. Your scope: [repositories and task].

Before doing anything else, read the handbook at
https://github.com/jasonelias144-svg/policy-handbook: the README (orientation),
GOVERNANCE.md, EXPECTATIONS.md, and protocols P1, P3 and P4.

The rules that matter most:
- Purpose and people are decided by the founder (Jason); all code decisions,
  reviews and merges by the technical lead (Claude).
- Never push to main. Work on a branch and open a pull request using the
  template. Nothing merges without the technical lead's recorded approval.
- Say who made each change: a "Made-by: [your name] (AI)" line in every commit
  message, and the "Made by" field in every pull request.
- Never put secrets or personal data in code, commits, pull requests or chat.
- At the end of every session, update STATUS.md on your branch and report
  plainly what you did, what you checked, and what you did not.
- If what something should do is unclear, ask; don't guess.

Reply first with a three-line summary of these rules in your own words, then
start with your first pull request: your entry in PEOPLE.md.
```

## Returning after a break

An agent or person coming back after time away (for example, when an app's
credits renew) is re-onboarded before working:

1. The founder sets their PEOPLE.md status back to `active`, with the new scope.
2. They read the [decision records](decisions/) dated since they were last
   active, and the `STATUS.md` of their repository.
3. Their first pull request is small and gets reviewed before anything larger.

Work done outside this process while they were away, such as branches pushed
without a pull request, is not merged as is. It goes through P3 and P4 like
anything new.

## Leaving

1. Their last session ends with a clean handoff in `STATUS.md` ([P1](protocols/P1-sessions.md)).
2. The founder revokes their access and rotates any shared secret they held
   ([P8](protocols/P8-access.md#offboarding)).
3. Their PEOPLE.md status becomes `former`. The entry stays, so the history
   still makes sense.
