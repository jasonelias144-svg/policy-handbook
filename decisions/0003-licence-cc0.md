# 0003. Everything the founder makes public is CC0 1.0

- **Status:** accepted
- **Date:** 2026-11-15
- **Decided by:** founder, Jason (the policy: one licence, always, with no
  restrictions and no attribution); technical lead (which licence, at the
  founder's request)
- **Recorded by:** Claude (technical lead)

## Context

Most of the founder's public repositories had no licence, so by default all
rights were reserved, or a licence the founder hadn't meant: MIT in
Lyceum-Local, Expo's template licence in lyceum-commons-mobile, and CC BY-SA
4.0 and Apache 2.0 named in the Living Pattern Institute's README beside a CC0
`LICENSE`. Each repository's STATUS.md had asked the founder since 2026-10-27.

The founder, 2026-11-15:

> Consider all free and public and use the license we have been using and
> correct that license when I naively chose the wrong one or none. Always
> consider it all public if in a public repo. If someone can literally access it
> now, I consider it public. Please ensure the right license is chosen that is
> essentially a license that says there is no restrictions and all that. No
> attribution required. Don't care. If it is useful, feel free to use it. We are
> intentionally building something like a public space, like a park or a
> national park, something that is designed to be used freely.

And:

> Please decide if there are more than one options available that meet the
> conditions of what I already said.

> We should change the policy to: "founder always wants this license",
> whichever is the right license that makes sense to you. I don't want to
> decide each time when my decision will be the same.

And on the one exception:

> SAIR work is intentionally separate from the other repos. It is the only one
> that includes work and publications from outside. It should be considered
> distinct because based on something external.

## Options considered

Four licences meet "no restrictions" and "No attribution required":

- **CC0 1.0.** A public-domain dedication for any kind of work, writing and
  code alike. Where a country doesn't let anyone give up their rights entirely,
  it falls back to a licence with no conditions. open-worlds already used it.
  It leaves patent and trademark rights untouched (its section 4(a)), which is
  why some software bodies don't list it for code; to our knowledge nothing
  here is patented.
- **The Unlicense, 0BSD and MIT-0.** Each is written for software, and fits
  writing less well.

## Decision

Every public repository of the founder's is licensed CC0 1.0. The technical
lead adds it, or corrects a wrong licence, without asking the founder; only a
departure from it goes to the founder. Anything not ours to give keeps its own
licence, and the repository's README says which.

SAIR-Lean-Kernel-Challenge is the one repository built on outside work: our
work there is CC0, and the challenge's own files keep their Apache-2.0
licence, listed in its README.

Private repositories are not covered: the founder's words are about what is
public. A private repository that becomes public gets CC0 then.

## Consequences

- Every public repository now has a `LICENSE` with the CC0 1.0 text (Lyceum-Commons
  #69, Lyceum-Local #3, lyceum-commons-mobile #9, Living-Pattern-Institute #2,
  Open-Experiment #3, SAIR-Lean-Kernel-Challenge #11, and this handbook).
  open-worlds already had it.
- GOVERNANCE.md takes licences out of the founder's case-by-case decisions; P5
  and P9 say so.
- CC0 doesn't enforce sharing: anyone may build on the work and close their
  own version. That is the founder's choice ("no restrictions").
- Incoming contributions are not yet covered: CONTRIBUTING.md doesn't say a
  contribution is given under CC0. Until it does, "everything here is CC0" holds
  only for the project's own work. A line in CONTRIBUTING.md, copied to each
  repository, is the next step.

## Dissent

None.
