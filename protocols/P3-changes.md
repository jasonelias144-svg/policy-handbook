# P3 Changes: branches, commits, pull requests

Every change to a repository, whether code, documentation or configuration,
follows this path:

```
branch  →  commits  →  pull request  →  review (P4)  →  merge  →  release (P6)
```

**Nobody pushes to `main` directly.** The only exception is stopping harm in an
emergency ([P7](P7-incidents.md)), and even then a revert by pull request is
preferred.

## Branches

- Start from the latest `main`.
- Name it `<kind>/<short-topic>`, where kind is one of:
  `feat` (new behaviour), `fix` (a bug), `docs`, `chore` (maintenance, tooling,
  dependencies), or `try` (an experiment, see [P2](P2-proposals.md#experiments)).
  Examples: `fix/ai-expired-leave`, `try/emoji-commands`.
- Branch names created automatically by an agent's tooling (such as
  `claude/...`) are fine.
- One branch, one concern.

## Commits

- **Summary line:** what the commit does, in the imperative, under about 72
  characters. "Add room expiry for unjoined rooms", not "changes".
- **Body:** why, when it isn't obvious.
- **Trailer:** who made it (see below).
- Commit working states often; push often ([P1](P1-sessions.md#during-the-session)).
- Never rewrite history that others may have pulled: no force-pushes to shared
  branches, and never to `main`.

## Saying who made it

All agents push through the founder's GitHub account, so GitHub's author field
can't tell us who did the work. Every commit therefore ends with a trailer:

```
Made-by: ChatGPT (AI)
```

or `Made-by: Claude (AI)`, `Made-by: <name> (human)`. Tools that add their own
equivalent trailer (Claude's `Co-Authored-By`) satisfy this. Every pull request
also fills in the "Made by" field of the template. Leaving it out, or naming
someone else, is a breach of [EXPECTATIONS.md](../EXPECTATIONS.md).

## Pull requests

- Open one as soon as the work is worth looking at. Use **draft** while it is
  unfinished.
- Fill in every section of the template: what and why, made by, how it was
  checked, intent questions, and the checklist.
- **Keep it small.** One concern, ideally under about 400 changed lines of
  hand-written code. Split anything bigger into steps that each work alone.
- **Include the tests** that show the change works ([standards/code.md](../standards/code.md#tests)).
- **Update the documentation** that the change makes untrue, and update
  `STATUS.md` ([P1](P1-sessions.md#at-the-end-every-session-finished-or-not)).
- When the pull request is ready, mark it ready for review. Review follows [P4](P4-review.md).

## After review

- Answer every review comment: change the code, or say why not.
- A new commit after approval needs a new approval ([P4](P4-review.md#the-approval-record)).
