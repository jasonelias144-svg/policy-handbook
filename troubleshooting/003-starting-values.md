# 003. A model learns its task in one run and not in another

- **Status:** solved when training on the answers only; open when training
  on every next character
- **Where and when:** TriNet, 2026-11-22; PyTorch 2.15.0, transformers 5.24.0
- **Links:** [TriNet #2](https://github.com/jasonelias144-svg/TriNet/pull/2);
  change 5 in `provenance/MANIFEST.json`;
  [`experiments/README.md`](https://github.com/jasonelias144-svg/TriNet/blob/main/experiments/README.md)

## What we saw

The packaged TriNet model learned its in-context task (entry 001) in one
random seed and stalled in the other.
- On the fair task, trained on the answers only: 99.8 to 99.9% with seed 0,
  and about 70% with seed 1, at every text length.
- A smaller prototype of the same design, written earlier, learned the task
  in both seeds.

## The cause

The starting values of the weights.
- The packaged model drew every linear, embedding and convolution weight
  from a normal distribution with spread 0.02. This is the usual convention
  for large Hugging Face models.
- The prototype used PyTorch's own defaults, which are much larger for
  small layers. A linear layer with 32 inputs starts with a spread of about
  0.10. An embedding starts with 1.0.

Which layer's starting values matter most, and why, has not been shown.

## What we tried

- **Letting the gates also see the local context.** It changed nothing:
  69 to 71%, two seeds. This was measured before the fixes in entries 001
  and 005, so the figures are not comparable with those above. Both arms
  were measured the same way, so we believe the comparison holds, but it
  was not repeated.
- **PyTorch's values, first version: it broke loading.** The first version
  of change 5 left every layer but TriNet's own untouched in
  `_init_weights`, relying on the values PyTorch gives a layer when it is
  built.
  - That works for a new model.
  - But when a saved checkpoint lacks a weight, transformers builds the
    model without starting values and calls `_init_weights` to set the
    missing ones. So that weight was never set at all.
  - It came out as NaN on transformers 5.24.0, and as numbers around 1e35
    on 4.46.3.
  - Gemini's original code had set such weights for the linear, embedding
    and convolution layers.
  - The independent review of TriNet #2 found this.
- **PyTorch's values, second version:** calling `reset_parameters()` on
  each layer in `_init_weights`. See below.

## What worked, and why

- **PyTorch's own starting values** (change 5). Trained on the answers
  only: 100% in both seeds, at every length.
- **A missing linear, convolution, embedding or norm weight now gets
  PyTorch's starting value,** tested on both versions. TriNet's own layer
  parameters still do not, as in Gemini's code (TriNet `STATUS.md`,
  "Noticed").
- **How sure:**
  - With Gemini's values, one seed of two stalled (about 70%). With
    PyTorch's, neither did (100%).
  - On the task before entry 001's fix it was the same: 78.6 to 92.5%
    against 100%, in both seeds.
  - The difference is large, but it rests on two seeds.
- **Still open.** Trained on every next character, as the training script
  does, the model learns the task only in part: 34% at best, in one seed of
  three. Starting values helped there in one seed only. What decides it is
  not yet known.

## For others

- If a small model fails to learn, or learns in some seeds and not others,
  compare its starting values with the framework's defaults. A convention
  made for large models may not suit a small one.
- Run more than one seed before believing either a success or a failure.
