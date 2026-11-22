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
  of the comparison were measured the same way, so the comparison stands.
- **PyTorch's own starting values** (`reset_parameters()` on each layer):
  see below.

## What worked, and why

- **PyTorch's own starting values** (change 5). Trained on the answers
  only: 100% in both seeds, at every length.
- **A side effect.** A weight missing from a saved checkpoint had come
  out as NaN on transformers 5.24.0 and as huge numbers on 4.46.3. It now
  gets a proper starting value too.
- **How sure:** the difference is large (about 70% against 100%), but it
  rests on two seeds.
- **Still open.** Trained on every next character, as the training script
  does, the model learns the task only in part: 34% at best, in one seed of
  three. Starting values helped there in one seed only. What decides it is
  not yet known.

## For others

- If a small model fails to learn, or learns in some seeds and not others,
  compare its starting values with the framework's defaults. A convention
  made for large models may not suit a small one.
- Run more than one seed before believing either a success or a failure.
