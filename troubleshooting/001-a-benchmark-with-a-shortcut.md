# 001. A model scores 100% on a benchmark without learning the skill

- **Status:** solved
- **Where and when:** TriNet, 2026-11-22; PyTorch 2.15.0, transformers 5.24.0
- **Links:** [TriNet #3](https://github.com/jasonelias144-svg/TriNet/pull/3);
  [`experiments/README.md`](https://github.com/jasonelias144-svg/TriNet/blob/main/experiments/README.md),
  "A shortcut in Gemini's task"; `experiments/pointer_check.py`

## What we saw

TriNet is a small language model. Its benchmark task generates short texts
such as `d=0;f=2;g=3; … e=f;g=5; … ?e>2;`:
- values are bound to names;
- one name is then made to point to another (`e=f`);
- one name gets a new value (`g=5`);
- queries follow.

To answer `?e>` the model must follow the pointer from `e` to `f`. Two
models scored 99.8 to 100% on the pointer queries.

## The cause

The generator always made the pointer name the **first** name bound, and
always overwrote the **second**. So "answer a pointer query with the first
value bound" was always right. The models had learned that rule, not how to
follow a pointer.

A review of the generator's code noticed the fixed roles. The scores alone
gave no hint.

## What we tried

- **Testing on a variant that breaks the rule.** We trained on the task as
  given, then tested on the same task with the pointer and the overwrite
  placed at random (`pointer_check.py`).
  - Pointer scores fell from 99.8 to 100% to 51.2 / 40.6 / 45.9% at three
    text lengths.
  - They fell to the same figures for both models and both seeds.
  - The rule "give the first value bound" scores exactly that on the same
    test episodes. (It is right when the pointer happens to name the first
    name, or a name with the same value.)
- **Ruling out help from earlier answers.** In these texts, later queries
  can see the answers to earlier ones. Scoring only the first query of
  each episode gave the same picture (53.1 / 41.1 / 45.7%).

## What worked, and why

- **Placing both roles at random in training** (change 6).
  - Trained on answers alone: 100% on pointer queries, at every length.
  - With random roles, no rule based on position can answer a pointer
    query. Only following the pointer can.
- **How sure:** very. The models' scores matched the rule's score exactly,
  in two models and two seeds.
- **The cost:** an earlier result was mostly the shortcut. Trained on whole
  texts, one model had scored 99.7%; on the fair task it reaches 34% at
  best. The claim was withdrawn.

## For others

- For every synthetic benchmark, list what is fixed in how it is built:
  positions, roles, order, lengths. Each fixed thing is a possible rule.
- Work out what the simplest rule would score, and compare. A score that
  matches a rule's score exactly is a warning.
- Keep a test variant that breaks each rule, and report scores on it.
