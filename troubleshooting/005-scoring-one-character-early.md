# 005. An evaluation script scores the wrong position

- **Status:** solved
- **Where and when:** TriNet, 2026-11-22
- **Links:** [TriNet #2](https://github.com/jasonelias144-svg/TriNet/pull/2),
  its review; [`experiments/README.md`](https://github.com/jasonelias144-svg/TriNet/blob/main/experiments/README.md),
  "Corrected after review"; `tests/test_experiments.py`

## What we saw

An experiment script trained models to answer queries like `?g>5`, and
scored the predicted answer. Scores came out lower than expected:
- one model at about 70%;
- a prototype at 70.7 and 74.7% after 450 training steps. Gemini, who
  wrote it, had reported 100% after 250.

We wrote that the prototype "learns more slowly" than reported.

## The cause

The script read each answer one character too early.
- It took the prediction made at the query's name (`g`), not at the `>`.
- At the name, the model has not yet seen the `>` that asks for the
  answer.

All the models were trained and scored the same way, so their ranking held.
But the scores were too low, and the story built on them was wrong.

## What we tried

- **Taking the scores at face value.** We explained the gap as slower
  learning. That was a plausible story, and wrong.
- **An independent review of the script.** It found the position.

## What worked, and why

- **Scoring at the `>`.** One line in the script changed:
  `cols.append(pos - 1)` became `cols.append(pos)`.
- **A test that builds an episode with a known answer position** and checks
  that the script reads exactly that position.
- **The results run again:**
  - the first model reached 78.6 to 92.5% on the task as it then stood;
  - the second reached 99.4 to 100% after 250 steps, about as reported.

  The "learns more slowly" claim was withdrawn, and the page says so.
- **How sure:** very. The test fixes the position, and every number was
  run again.

## For others

- Test the scoring code itself, with a hand-made example whose right answer
  and position you know.
- When your results disagree with someone else's, check your evaluation
  before you explain the gap.
- An off-by-one in evaluation does not crash anything. It gives plausible
  numbers.
