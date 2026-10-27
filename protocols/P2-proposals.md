# P2 Proposals: ideas, experiments, prior art

This is the free and open half of how we work. Anyone may propose anything, and
anyone may try things out. Only `main` is guarded.

## Proposing

Anyone, including visitors, may propose an idea:

- **For any repository:** open an issue with the *Proposal* template.
- **For a product idea in a project that keeps an ideas ledger** (Lyceum Commons
  keeps `docs/ideas.md`): add a row by pull request, with status `idea`.
- **In conversation with the founder:** the founder or the technical lead turns
  it into an issue or ledger entry, so it doesn't evaporate.

A good proposal says what problem it solves, for whom, what already exists, and
the smallest version worth trying.

## Who decides

- An idea that changes **what a project does, for whom, or what it costs** is
  decided by the founder.
- An idea about **how** something is built is decided by the technical lead.
- Unsure which? [P5](P5-decisions.md#intent-or-code) has the test.

## Prior art first

Before designing or building anything new:

1. Search for existing products, open-source projects, standards and papers
   that solve the same or a neighbouring problem.
2. Write down what you found: who, how it works, what we borrow, and what is
   genuinely ours. Projects with a `docs/prior-art.md` keep it there; otherwise
   put it in the proposal.
3. Prefer an existing standard (formats, protocols, state machines, field
   names) to inventing one. Invent only where nothing fits, and say so.

## Experiments

- **Anyone may build a prototype on a branch, without asking.** Name it
  `try/<topic>` ([P3](P3-changes.md#branches)).
- A prototype is not a promise. It reaches `main` only through P3 and P4, and
  usually gets rewritten on the way.
- Note live experiments under "Now" in `STATUS.md`, so they aren't mistaken for
  abandoned work. A `try/` branch with no activity for 90 days is listed in
  `STATUS.md` and then deleted ([P9](P9-repositories.md#branch-hygiene)).

## Status of an idea

`idea` → `prior art checked` → `prototype` → `accepted` → `in use`, or
`dropped` with the reason. A dropped idea stays on record. A "no" is
information, and the reason may change later.
