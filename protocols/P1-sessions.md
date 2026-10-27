# P1 Sessions: start, work, hand off

A session is one sitting of work: one conversation with an AI agent, or one
stretch of work by a person. Most of our contributors remember nothing between
sessions, so every session starts from what is written down and ends by writing
down what the next one needs.

## At the start

1. **Orient.** If you are new, or back after a break, follow
   [ONBOARDING.md](../ONBOARDING.md) first.
2. **Read the repository's `AGENTS.md` and `STATUS.md`.** `STATUS.md` says what
   is in progress, what is next, and what is waiting on whom.
3. **Check open pull requests and branches.** Someone may have left work half
   done; the handoff is in their pull request or on their branch's `STATUS.md`.
4. **Know your task.** It comes from the founder, from the top of "Next" in
   `STATUS.md`, or from an accepted proposal. If you have none, ask; don't
   invent one.
5. **Start from the latest `main`** on a new branch ([P3](P3-changes.md#branches)).

## During the session

- **Push early and often.** Sessions and the machines they run on end without
  warning. Work that is only on a disposable machine is lost.
- **Keep to the task.** If you notice another problem, write it under "Noticed"
  in `STATUS.md`, or open an issue. Fix it in the same pull request only if it
  is tiny and directly in your way.
- **Stop at intent questions.** If the right behaviour depends on what the
  founder wants, ask ([P5](P5-decisions.md)), and carry on with whatever doesn't
  depend on the answer.
- **Check before you claim.** Run the tests and checks the repository's
  `AGENTS.md` names, and note the results.

## At the end (every session, finished or not)

1. **Push everything** to your branch.
2. **Update `STATUS.md` on your branch:** what you changed, the state now, the
   next step, open questions, and a line in the log. Use the
   [template](../templates/STATUS.md).
3. **Open or update the pull request** using the template. If the work is
   unfinished, open it as a draft so the handoff is visible.
4. **Report to whoever started the session:** what was done, what was checked
   and how, what was not checked, and what comes next. Plainly; no padding.

## The handoff test

Could a capable stranger, with no memory of this session, pick the work up
from `STATUS.md` and the pull request alone? If not, the session isn't finished.
