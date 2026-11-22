# 004. Code written without the real library fails with it

- **Status:** solved
- **Where and when:** TriNet, 2026-11-22; transformers 4.46.3 and 5.24.0
- **Links:** [TriNet #1](https://github.com/jasonelias144-svg/TriNet/pull/1);
  changes 1 to 4 in `provenance/MANIFEST.json`

## What we saw

The model's code was written by Gemini, in a conversation, in a sandbox
that did not have the transformers library. Gemini tested it against a
stand-in of their own, and said so. Run with the real library, it failed
in several places, differently in each version.

## The cause

The library's interface differs between versions, and from the stand-in:

1. **transformers 5.x** looks for `config.num_hidden_layers`. The model's
   configuration called it `n_layers`, so `generate()` stopped with an
   `AttributeError`.
2. **transformers 5.x** raises `ValueError`, not `TypeError`, when its
   `Cache()` is made with no arguments, so the code's guard did not catch
   it.
3. **transformers 4.x** has a read-only `seen_tokens` on its `Cache`, so the
   model's cache could not set it.
4. **transformers 5.x** passes the cache to the model under a new name.
   This one failed silently (entry 002).

## What we tried

- Running the code with the real library, in both versions we wanted to
  support. Three failures showed at once. The fourth showed only when a
  review watched what the model was given (entry 002).

## What worked, and why

- **The smallest change for each failure,** so the rest stays exactly as
  written. Each change is listed with its reason in
  `provenance/MANIFEST.json`. A test undoes the changes and checks the
  result, byte for byte, against the original.
- **CI runs the tests on both versions** (4.46.3 and 5.24.0), so a change
  that suits one and breaks the other is caught.
- **How sure:** the tests pass on both versions, and each change's test
  fails without it.

## For others

- Code from a model that could not run the real library is untested,
  whatever its own tests say. Run it against the real library, on every
  version you claim to support.
- Pin the versions you test, and test more than one.
- Keep the original and a list of your changes, so anyone can rebuild what
  was given and see exactly what was changed.
