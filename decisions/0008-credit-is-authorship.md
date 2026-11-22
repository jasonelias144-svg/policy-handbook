# 0008. Credit is authorship, not where ideas came from

- **Status:** accepted
- **Date:** 2026-11-22
- **Decided by:** founder, Jason (the rule); technical lead (how the pages
  say it)
- **Recorded by:** Claude (technical lead)

## Context

In the TriNet repository, a review of ChatGPT's had found a flaw in a task,
and the repository credited it to "an outside review". The founder asked
that ChatGPT be named, 2026-11-22:

> Yes, name ChatGPT in all functions they have been engaged. We definitely
> want any positive results to be properly attributed, whereas negative
> results can fall upon the project as a whole, or myself. But when it
> comes to credit for producing a working component, we should be very
> specific about the individual contributions from each source. Our
> records should allow others to recreate our results, in theory. That is
> the goal.

And, on quoting: "Yes, feel free to quote ChatGPT, as they are aware of the
public nature of the project, having been there since the start."

The technical lead first read this as a call to trace each idea to where it
came from, and wrote TriNet's credits that way. The founder, the same day:

> Ok, but let's not get too tangled in credit tracing. This whole project
> has been recycling ideas around by design. Credit in terms of final
> product, but we don't have to get into credit in terms of idea origin.
> That is a whole can of worms and completely pointless, because every
> single stage of this project has moved ideas freely and they all came
> from me in some way. So, that is not the type of credit to track, only
> authorship credit in terms of who wrote what code or what part for the
> repo. Let's not get into the nonsense of idea credit, only actual output
> credit. And if a quote is already being reproduced in the records, then
> provide the source of the quote. That's fine. But I strongly object to
> the notion that we need to trace the origin of each idea.

## Options considered

- **Trace each idea to its source.** It cannot be done fairly where ideas
  move freely between the founder and every collaborator, and the founder
  rejected it.
- **Commits only.** Every commit already says who made it (P3). But in this
  organization one agent often commits what another wrote: Claude pushed
  the code Gemini wrote in conversation. The commit trailer then names
  who committed, not who wrote.
- **Authorship.** Say who wrote each part. This is what the founder asked
  for.

## Decision

- **Credit is authorship: who wrote what.** That means code, text, or any
  part of a repository. Commits and pull requests say who made them (P3).
  A repository with parts written by more than one author says who wrote
  which part, on a short page or in its README. TriNet's `CONTRIBUTIONS.md`
  is an example.
- **Where ideas came from is not tracked.** In this organization ideas move
  freely, and in the founder's words "they all came from me in some way".
- **A quotation gives its source:** the record and the line. For a record
  that is not in a public repository, it also gives the record's size and
  SHA-256, so a reader can tell they have the same copy.
- **A reviewer is named for what their review found, where it led to a
  change.** P4 already does this for this organization's own reviews. The
  same holds for a collaborator's review, such as ChatGPT's.
- **Results belong to the project.** What fails falls on the project as a
  whole, or on the founder, not on a collaborator. The record of who wrote
  each part already shows where any line came from, so no separate record
  of faults is kept. A self-review still says what its author got wrong
  (P4).
- **Records let others recreate the results.** A reported result says:
  - the command that produced it;
  - the version of the code;
  - the software versions;
  - the machine;
  - anything else that changes the numbers, such as the number of threads
    or the random seeds.

## Consequences

- P3 ("Saying who made it") points here.
- TriNet's pull request #4 applies it: `CONTRIBUTIONS.md` says who wrote
  each part, ChatGPT is named as a reviewer where their review led to a
  change, and each result table says where it ran.
- Pages written before this decision are not combed for statements about
  where ideas came from. They change when they are next edited for another
  reason.

## Dissent

None.
