# 002. A test passes while the feature it tests does not work

- **Status:** solved
- **Where and when:** TriNet, 2026-11-22; transformers 5.24.0 (not 4.46.3)
- **Links:** [TriNet #1](https://github.com/jasonelias144-svg/TriNet/pull/1),
  its review; change 4 in `provenance/MANIFEST.json`; `tests/test_model.py`

## What we saw

A language model keeps a cache, so that each step of text generation reads
only the new token. A test generated text twice, once with the cache and
once without, and checked that the outputs were the same. They were, so the
test passed.

## The cause

On transformers 5.x the cache was never used.
- The library hands the cache to the model's
  `prepare_inputs_for_generation` under the name `cache=`.
- The model's code read only `past_key_values=`, so the cache was dropped.
- Every step then read the whole text again from the start.

Reading the whole text again gives the right answer, only more slowly. So
the outputs matched, and the test could not tell.

## What we tried

- **The equality test.** It could not fail: a model that ignores its cache
  and one that uses it correctly give the same output.
- **Watching what the model is given.** The review used a spy that records
  the length of each input the model receives during generation:
  - 6, 7, 8, 9, 10 tokens on transformers 5.24.0: the whole text each time;
  - 6, 1, 1, 1, 1 on 4.46.3: one new token each time, as intended.

## What worked, and why

- **Reading the cache under both names** (change 4).
- **A test of the mechanism, not just the output.** It asserts that after
  the first step, generation feeds the model one new token at a time.
- **Proof that the test can fail.** We undid the fix and watched the test
  fail on 5.24.0. Later fixes there were checked the same way, where the
  record shows it: the fixes from the review of TriNet #2, and the tests
  for change 6.
- **How sure:** very. The spy's numbers and the failing test agree.

## For others

- When a test compares two ways of computing something, ask whether they
  can differ at all. If not, the test checks nothing.
- For a speed or memory feature, such as a cache, batching or streaming,
  test the mechanism: what the model is given at each step, or how much it
  stores.
- Undo each fix once and watch its test fail. A test you have never seen
  fail is not yet a test.
