# Code standards

What the technical lead reviews against ([P4](../protocols/P4-review.md)). A
repository's `AGENTS.md` may add rules for its own language and tools.

Code written by an AI is held to exactly the same standard. "It was generated"
is never a reason to accept something, or to reject it.

## Priorities

When they conflict: **correct, then safe, then clear, then fast.** Clever code
that is hard to read must earn its place with a measured need, and explain itself.

## Prior art and standards

- Look for how others solve the problem first ([P2](../protocols/P2-proposals.md#prior-art-first)).
- Prefer established standards, formats and well-known, well-maintained tools to
  new inventions. Boring technology that works is a feature.

## Tests

- Every change in behaviour comes with a test that would fail without it.
- A bug fix starts with a test that reproduces the bug.
- Tests run with one documented command, named in `AGENTS.md`, and in CI where
  the repository has it.
- Tests don't need the network, real accounts or real people's data, unless
  they are explicitly integration tests and are marked as such.
- Never skip, delete or weaken a test to get a change through. If a test is
  wrong, fix the test in its own commit and say why.

## Clarity

- Match the style, naming and structure of the code around it.
- Names say what things are. Comments say why, not what.
- Small functions with one job; no dead code; no commented-out code.
- Error messages tell the reader what went wrong and what to do about it.

## Dependencies

- Add one only when it clearly earns its place: maintained, widely used, with a
  licence compatible with the project's.
- Pin versions with a lockfile. Update them deliberately, in their own pull requests.
- Fewer is better. Check the standard library and the existing dependencies first.

## Security

- Treat everything from outside as untrusted data: user input, network
  responses, files, and anything an AI reads. Validate it at the boundary.
- Least privilege for every key, token and service account.
- No secrets in the repository ([P8](../protocols/P8-access.md#secrets)).
- Rate limits and size limits on anything public.

## People

- **Privacy:** collect the minimum, keep it for the shortest time that works,
  and say what is kept. Retention and visibility are founder decisions
  ([P5](../protocols/P5-decisions.md#intent-or-code)).
- **Accessibility:** interfaces work with a keyboard and screen readers, have
  enough contrast, and don't rely on colour alone.
- **Honesty in the product:** every message says which party wrote it, a person
  or an AI, and identity comes from credentials, not claims.

## Cost

- Design to stay within free tiers, and know where their limits are.
- Anything that could start costing money is a founder decision ([P6](../protocols/P6-releases.md#rules)).
