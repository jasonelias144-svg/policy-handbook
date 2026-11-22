# 006. Same code, same seed, different results

- **Status:** managed: the cause is understood and the runs are controlled
  for it
- **Where and when:** runs of a two-part TriNet model (BicameralTriNet) on
  a CPU, 2026-11-22; PyTorch 2.15.0, transformers 5.24.0
- **Links:** TriNet's
  [`experiments/README.md`](https://github.com/jasonelias144-svg/TriNet/blob/main/experiments/README.md),
  which records the threads and versions for each table. The runs
  themselves are not yet kept in a repository.

## What we saw

Two training runs with the same code, the same seed and the same data gave
different results.
- One TriNet model's score on pointer queries was 41.0% in one run and
  22.9% in the other.
- Its overwrite score was 52.8% and 36.8%.
- Its scores moved by up to 18 points.

The only difference between the runs was the number of CPU threads: 2 in
one, 4 in the other.

## The cause

With a different number of threads, PyTorch adds numbers up in a different
order. Floating-point addition gives slightly different results in
different orders.
- In a recurrent model trained for hundreds of steps, those small
  differences grow.
- TriNet's training losses drifted apart from about step 50.
- In the same runs, a Transformer's losses matched exactly. How much a
  model is affected depends on the model.

PyTorch does not promise the same results on a different number of
threads, or on a different machine or version.

## What we tried

- **Comparing the logs step by step,** to see where the runs parted:
  about step 50, with no error and no warning.

## What worked, and why

- **Fixing the thread count.** The experiment scripts default to
  `--threads 2`, and the training script runs with `OMP_NUM_THREADS=2`.
- **Recording it with every result.** Each result table gives:
  - the machine;
  - the number of threads;
  - the versions of Python, PyTorch, transformers and NumPy.
- **Treating single runs with care.** A difference between two models
  smaller than the difference between two runs of one model means nothing.
  Use several seeds.
- **How sure:** the cause is standard and well understood. The size of the
  effect here is from one pair of runs.

## For others

- Record the thread count, the library versions and the machine with every
  result, as carefully as the seed.
- Before comparing models, run one model twice and see how far its results
  move.
- PyTorch's notes on reproducibility say what it does and does not promise.
