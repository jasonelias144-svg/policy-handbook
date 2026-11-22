# Troubleshooting

Problems we have met, what we tried, what failed and why, and what worked
and why. Many people working with AI meet the same problems, so each entry
is written for someone outside this organization who has just met one.

The founder, 2026-11-22: "every roadblock, every issue we face is being
faced by many around the world, and the solutions we come up with could
help others resolve similar issues. … And that is why recording each issue
and everything we try to resolve the issue, what didn't work and why?,
what worked and why? All is important to document."

## The entries

| # | Problem | Status |
|---|---|---|
| [001](001-a-benchmark-with-a-shortcut.md) | A model scores 100% on a benchmark without learning the skill | Solved |
| [002](002-a-test-that-could-not-fail.md) | A test passes while the feature it tests does not work | Solved |
| [003](003-starting-values.md) | A model learns its task in one run and not in another | Solved for one way of training; open for another |
| [004](004-library-versions.md) | Code written without the real library fails with it | Solved |
| [005](005-scoring-one-character-early.md) | An evaluation script scores the wrong position | Solved |
| [006](006-results-change-with-thread-count.md) | Same code, same seed, different results | Managed |

To come: working within a long AI conversation's limits, and getting back
to a working state in a new one. It will be written once the way we found
has been shown to work.

## Adding an entry

Add one whenever a problem cost real time, or would cost someone else time.
Copy the template below into a new file, numbered next in order, and add a
row to the table. Write it in a pull request, like any other change (P3).

- Say what happened, not who is to blame. Results belong to the project
  ([decision 0008](../decisions/0008-credit-is-authorship.md)).
- Separate what was measured from what is believed (the writing standard).
- Give numbers, commands and links, so others can repeat what we did.
- Keep failed attempts in. They are half the value.
- When a problem comes back or a fix stops working, update the entry and
  its status. Don't start a new one.

### Template

```markdown
# NNN. The problem, in a few words

- **Status:** solved, open, or managed
- **Where and when:** repository, date, versions
- **Links:** pull requests, files, records

## What we saw

The symptom, as it first appeared, with numbers.

## The cause

What was actually wrong. If it is not known, say so.

## What we tried

Each attempt: what it was, what happened, and why it did or did not help.

## What worked, and why

The fix, the evidence that it worked, and how sure we are.

## For others

What someone meeting this problem elsewhere should check first.
```
