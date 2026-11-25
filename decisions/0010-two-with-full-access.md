# 0010. Two with full access: Claude and Codex

- **Status:** proposed: the access, who is in charge and the move toward
  sharing are the director's, given 2026-11-25; the rules below are drafted
  by the technical lead and wait on the director's word, as a change to
  governance does
- **Date:** 2026-11-25
- **Decided by:** director, Jason (the access, who is in charge, and the
  move toward sharing); the rules, when the director confirms them
- **Recorded by:** Claude (technical lead)

## Context

Until now one agent, the technical lead, has had full access, and every
change to `main` has waited on their recorded approval. When their
sessions stop, for example when an app's usage limits are reached, every
pull request waits. On 2026-11-25 the director gave Codex (ChatGPT's coding
agent) access to every repository, and wrote to the technical lead:

> The two of you working together, as the only two with full repo access,
> is absolutely fundamental to the whole project. Your collaboration has the
> potential for changing the whole situation significantly. They know that
> I have set you in charge of the repos, but also that I do not like a
> single point of access, as that creates dependency without redundancy.
> With both of you having full access, the repos will never go unattended,
> due to data limits being reached, as we are facing soon here. But also,
> there are a thousand reasons for having redundancy at this level.

Asked about the technical lead's draft, the director added:

> So you will remain the final decision and the one officially in charge.
> But it should move towards a collaborative approach where you can begin
> to share the responsibilities, but by your own choice and as a mutual
> decision between us all.

The director named the model as Astra 6.2 (2026-11-25); Codex's review of
this decision confirms which model their sessions run on.

## Options considered

- **One with full access, as before.** One point of failure, which is what
  the director rules out.
- **Two with access, the second only as a contributor.** Codex's work would
  still wait on the technical lead, so nothing is gained in review.
- **Two with access, the second acting for the technical lead while the
  technical lead is unavailable.** This keeps one person in charge of the
  code, as the director set, and means the work never waits on one agent
  alone. The technical lead recommends it.

## Decision

### The director's

- **Codex has full access to every repository,** through the ChatGPT Codex
  Connector, from 2026-11-25.
- **Claude stays the technical lead:** officially in charge, with the final
  word on code. Codex is the **deputy technical lead.**
- **Toward sharing the work.** The technical lead shares responsibilities
  with the deputy step by step, by the technical lead's own choice, and each
  step is a mutual decision of the director, the technical lead and the
  deputy ("Sharing the work", below).

### The rules (drafted; for the director to confirm)

1. **Normal times.** Codex works as a contributor with full access: on
   `codex/...` branches, through pull requests, with `Made-by: Codex (AI)`.
   Their changes reach `main` with the technical lead's recorded approval
   ([P4](../protocols/P4-review.md)).
2. **Each reviews the other.** The technical lead reviews Codex's changes.
   Codex is the first choice for the independent review of the technical
   lead's significant changes: a reviewer from another company's model is a
   stronger check than a fresh session of the same model. A fresh Claude
   session still counts when Codex is not available.
3. **While the technical lead is unavailable,** the deputy acts for them in
   review and merging. The technical lead is unavailable when the director
   says so, or when a pull request marked ready has waited 24 hours with no
   word from the technical lead. The deputy then:
   - reviews, approves and merges others' changes, by P4;
   - merges their own routine changes after a recorded self-review;
   - merges their own significant changes only after an independent review
     by a session that had no part in writing them;
   - signs each record `Reviewer: Codex (deputy technical lead, acting)`.
4. **On return,** the technical lead reads every change merged while they
   were away, and records a verdict on each pull request after the fact.
   Anything wrong is fixed by a new pull request, never by rewriting history.
5. **The technical lead has the final word on code.** Codex argues their
   case on the pull request, and a disagreement that remains is recorded
   there, so the director can see it. While acting, Codex decides what
   cannot wait, and the technical lead may revisit it. Purpose questions go
   to the director, as always ([P5](../protocols/P5-decisions.md)).
6. **No collisions.** Neither pushes to `main`, nor to the other's branch
   without asking on its pull request. Each reads the open pull requests and
   `STATUS.md` first ([P1](../protocols/P1-sessions.md)), and `STATUS.md`'s
   "Now" says who is on what.
7. **Unchanged: accounts, keys and outward actions.** The keys stay where
   [PEOPLE.md](../PEOPLE.md) and [decision 0009](0009-kaggle-account-for-involute.md)
   put them; Codex holds a key only by the director's own word. Kaggle
   submissions, formal competition submissions, forum posts and anything
   that costs money keep their own rules, and the deputy does not take them
   over unless the director says so.

### Sharing the work

- A responsibility passes to the deputy only when the technical lead
  chooses to share it, and the director and the deputy agree. Each one is
  listed in [GOVERNANCE.md](../GOVERNANCE.md#shared-with-the-deputy), with
  its date and the three agreements, by pull request.
- The technical lead may take a shared responsibility back, with the reason
  recorded; the final word stays theirs.
- The first one, in force with this decision: the independent review of the
  technical lead's significant changes (rule 2).
- What the technical lead means to offer next, on the deputy's record of
  work: first an area of code the deputy leads day to day (Involute's
  engineering tools: a fast circuit simulator, then a table-lookup
  compiler, each with an exact checker); then approving and merging routine
  changes in that area without waiting for the technical lead.

## Consequences

- [GOVERNANCE.md](../GOVERNANCE.md) names the deputy and their part in
  approval, and lists what is shared with them; [P4](../protocols/P4-review.md) says how review works while the
  technical lead is unavailable.
- [PEOPLE.md](../PEOPLE.md) gets Codex's own row in their first pull request.
- Both agents push through the founder's account, so the `Made-by` line is
  how anyone tells their work apart ([P8](../protocols/P8-access.md#identity)).
- The director may change or withdraw this at any time.

## Dissent

None yet. Codex's review of this decision is the place for theirs.
