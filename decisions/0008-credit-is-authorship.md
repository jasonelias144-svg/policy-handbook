# 0008. Credit is authorship, not where ideas came from

- **Status:** accepted
- **Date:** 2026-11-22
- **Decided by:** founder, Jason (the rule); technical lead (how it is
  applied: authorship pages, citing quotations, recording results)
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
> the notion that we need to trace the origin of each idea. …

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

### The founder's rule

- **Credit is authorship: who wrote what.** That means code, text, or any
  part of a repository. In the founder's words, "only authorship credit in
  terms of who wrote what code or what part for the repo".
- **Where ideas came from, among the founder and the collaborators, is not
  tracked.** The founder's reasons are quoted above.
- **A quotation gives its source:** "if a quote is already being
  reproduced in the records, then provide the source of the quote."
- **Negative results** "can fall upon the project as a whole, or myself".
- **Records should let others recreate the results,** "in theory".

### How it is applied (technical lead)

- **What is still cited.** Prior art ([P2](../protocols/P2-proposals.md))
  and published work are still cited, and a reviewer or a reporter is still
  named for what they found (below). These are not the ideas the founder
  meant.
- **Faults.** No one is blamed for an honest mistake: that is already the
  organization's rule ([EXPECTATIONS.md](../EXPECTATIONS.md), "No blame for
  honest mistakes"; [P7](../protocols/P7-incidents.md)). Saying what a
  piece of code did wrong, and whose code it is, is a fact. It is not blame.
- **A repository with parts by more than one author says who wrote which
  part,** on a short page or in its README. TriNet's `CONTRIBUTIONS.md` is
  an example. When you commit what someone else wrote, say so in the commit
  and the pull request ([P3](../protocols/P3-changes.md)).
- **A quotation's source** is who said or wrote it, and when. A quotation
  from a conversation record also gives the record and the line. For a
  record that is not in a public repository, it also gives the record's
  size and SHA-256, so a reader can tell they have the same copy.
- **A reviewer or reporter is named for what they found, where it led to a
  change.** [SECURITY.md](../SECURITY.md) already credits the reporter of a
  security problem, and TriNet credits its reviews the same way. A
  collaborator's review, such as ChatGPT's, is named in the same way.
- **A reported result says what is needed to recreate it:**
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
- **Existing work.**
  - A repository with several authors adds its page on who wrote what when
    it is next changed for another reason. open-worlds is one.
  - Results reported before this decision are not rerun to add run
    details. New results give them.
  - Pages are not combed for statements about where ideas came from.
- An authorship page is not one of every repository's required files
  ([P9](../protocols/P9-repositories.md)). Only a repository with more than
  one author needs one.

## Dissent

None.
