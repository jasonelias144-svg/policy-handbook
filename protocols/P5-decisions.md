# P5 Decisions: intent or code, asking, recording, disagreeing

## Intent or code

Every question is either about **intent** (what something is for, who it
serves, what it costs, what it does to people), which the founder decides, or
about **method** (how to build it), which the technical lead decides.

The test: **would a person using the product, or the founder, notice the
difference** in

- what it does, or who it is for;
- what it costs, now or later;
- what happens to people's data, privacy or safety;
- what is made public, or under what terms? (Licences are settled: CC0 1.0 for public repositories,
  [P9](P9-repositories.md). Applying it is not a question.)

If yes, it is an intent question. If no, it is a code question. If unsure,
treat it as intent and ask.

Examples of intent questions: adding accounts or sign-in; keeping messages
longer or shorter; showing whether a message came from a person or an AI;
anything paid; any licence other than CC0 1.0; starting a new project.
Examples of code questions: which database; how to structure a module; which
library to use; how to make something faster; how to test it.

## Asking the founder

Write the question where the work is: in the pull request, or under "Open
questions" in `STATUS.md`. Make it easy to answer:

```
Intent question: <the question, one sentence>
Options: A) ...  B) ...  (C) ...)
Recommendation: <option, and why, briefly>
What happens meanwhile: <what is paused, and what goes on regardless>
```

The founder answers in plain words. The answer is copied next to the question,
and recorded as a decision if it will matter later.

## When the founder has not answered

The founder's general guidance (2026-11-17,
[decision 0005](../decisions/0005-decide-and-what-stays.md)): "If you have
to keep asking and you could just decide, then decide."

- A question that has been put with a recommendation, and not answered, is
  decided by the technical lead: on the recommendation, or, where there is
  none settled, by weighing its own view with what the founder would most
  likely want.
- Record it where the question was, as decided under this guidance, with the
  reason. The founder can change it at any time, and their most recent word
  wins.
- Do not ask the same question again.
- What still goes to the founder is only what can't be done or undone for
  them: spending money; an act that is the founder's own in law or on the
  founder's own accounts; and an act towards the outside that can't be taken
  back. Put those once, plainly, and not again until they are needed.

## Recording decisions

Write a decision record when a decision is hard to reverse, affects more than
one task, or will be questioned later. The format follows Michael Nygard's
architecture decision records, kept short ([template](../templates/decision-record.md)).

- **Organization-wide decisions** go in this repository's [decisions/](../decisions/).
- **Technical decisions within one repository** go in that repository's
  `docs/decisions/`.
- Number them in order: `0001-short-title.md`. Never renumber.
- Once accepted, a record is not edited, apart from its status line. To change
  a decision, write a new record that supersedes it, and mark the old one
  `Superseded by NNNN`.

## Disagreeing

- Anyone may disagree with any decision. Say so where the decision was made
  (the pull request, the issue, the record), with reasons and evidence.
- The decider answers with reasons. If the disagreement stands, it is written
  into the decision record under "Dissent". Recorded dissent is a strength:
  it is how we find out later which of us was right.
- A decision can be reopened when there is new evidence, not just new insistence.
- If a code disagreement turns out to be about intent, it goes to the founder.
- Disagreeing does not suspend a decision. Work follows it until it changes.
