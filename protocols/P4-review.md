# P4 Review: technical review, approval, merge

Every change reaches `main` through a technical review by the technical lead,
recorded on the pull request ([GOVERNANCE.md](../GOVERNANCE.md#approval-authority)).

## When reviews happen

The technical lead works in sessions, so a review happens when a session runs:
the founder starts one, or a scheduled review task does. A pull request marked
ready for review should get its review in the next session. If something has
waited too long, tell the founder.

## What the reviewer checks

1. **It does what the pull request says**, and nothing it doesn't say.
2. **It is within the founder's intent.** Purpose questions are flagged, not
   settled in review ([P5](P5-decisions.md)).
3. **The checks pass.** The reviewer runs the repository's tests and checks
   itself, or reads the CI results for the exact commit. "The author said so" is
   not enough.
4. **It meets the [code standards](../standards/code.md)**: tests, clarity,
   dependencies, security, privacy.
5. **No secrets or personal data** in the diff or the history it adds.
6. **The documentation and `STATUS.md` are updated.**
7. **It can be undone**, or the pull request says how to recover if it goes wrong.
8. **It says who made it** ([P3](P3-changes.md#saying-who-made-it)).

## The approval record

The review is recorded as a comment on the pull request, in this form:

```
Technical review: APPROVED at <commit SHA, first 7+ characters>
- Checked: <what was run, and the result>
- Standards: <met, or the exceptions and why they are accepted>
- Intent questions: none | <how they were resolved, with a link>
- Notes: <anything the author or the next session should know>
Reviewer: Claude (technical lead), session <link if available>
```

The verdict is one of:

- **APPROVED**: may be merged as is, at that commit.
- **CHANGES REQUESTED**: the comments say what must change.
- **DECLINED**: will not be merged, with the reason. The work can come back
  as a new proposal.

An approval covers **only the commit it names.** Any later commit needs a new
approval. For a small follow-up, the new review can be brief.

Line-by-line comments go on the diff as usual; the record above is the verdict.

## Merging

- After APPROVED at the current head commit, the technical lead merges, or the
  author may merge.
- Use the merge method the repository's `AGENTS.md` names (squash by default).
- Delete the branch after merging.
- If the change needs a release, follow [P6](P6-releases.md).

A merge without an approval record at the head commit is a breach. The change
is reverted until it has been reviewed, whoever made it.

## The technical lead's own changes

The reviewer can't independently review its own work, so:

- **Routine changes** (bug fixes, documentation, small features, dependency
  updates) merge after the checks pass and a written **self-review** is recorded
  in the same format, marked `Self-review`.
- **Significant changes** also need an **independent review**: a fresh session
  that had no part in writing the change reviews it from the pull request
  alone, before merging. A change is significant if it:
  - changes the architecture, or how or where data is stored, including migrations;
  - touches identity, authentication, permissions, secrets or other security;
  - changes a public API, or anything other software depends on;
  - changes how something is deployed or hosted; or
  - deletes data, or is larger than about 400 changed lines of hand-written code.

## The founder's own changes

The founder has committed to the same path: a pull request (often written for
them by an agent), reviewed and recorded like any other.
