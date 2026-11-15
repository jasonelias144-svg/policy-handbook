# Status: policy handbook

**What this is:** the organization's policy, for every repository and everyone who works on them
**State:** active since 2026-10-27
**Updated:** 2026-10-27 by Claude

## Live

- Where: https://github.com/jasonelias144-svg/policy-handbook
- Version: first version
- Last check: 2026-10-27, `tools/check_links.py`: 0 problems

## Now

- Nothing in progress. The Cloudflare port waits on the founder (stage 0).

## Next

1. Carry out the Lyceum Commons port to Cloudflare ([decision 0002](decisions/0002-lyceum-commons-hosting.md)).
   The plan is in Lyceum-Commons `docs/cloudflare-port.md`. Its stage 0 waits
   on the founder: a Cloudflare account, deploy access, and the address.
2. ebook-press: bring its three unmerged branches in through review, once the
   founder says whether the agents that built them will continue.

## Open questions

- For the founder: a private contact address for conduct reports, to replace
  the interim route in CODE_OF_CONDUCT.md (asked 2026-10-27).
- For the founder: the organization's name. "Open Project" is the working
  name, taken from the name on recent commits (asked 2026-10-27).
- For the founder: should ChatGPT, Grok, or the agents from the other app return? If so, when and with what scope?

## Noticed

- The P9 repository settings (protecting `main`, required checks, deleting
  merged branches, squash only, private vulnerability reporting) need the
  founder in GitHub's settings, in every repository. Sessions can't change
  repository settings.
- Sessions can't delete branches either: the git proxy refuses. Leftover
  branches need deleting from GitHub's branch pages.

## Log

- 2026-11-15 Claude: licences become a standing rule. The founder, the same
  day: "I do not care to even learn the difference. I expressed my opinion. I
  hoped that would limit it to a single choice. Please decide if there are
  more than one options available that meet the conditions of what I already
  said." And: "We should change the policy to: "founder always wants this
  license", whichever is the right license that makes sense to you. I don't
  want to decide each time when my decision will be the same." The technical
  lead's choice: CC0 1.0. Of the licences with no restrictions and no
  attribution (CC0 1.0, the Unlicense, 0BSD, MIT-0), it is the one that covers
  writing as well as code, and where rights can't be given up entirely it
  falls back to a licence with no conditions. GOVERNANCE.md moves licences out
  of the founder's case-by-case decisions; P5 and P9 say the technical lead
  applies CC0 without asking, and only a departure from it goes to the
  founder.
- 2026-11-15 Claude: licence: CC0 1.0 (`LICENSE`), a public-domain
  dedication, by the founder's decision of 2026-11-15: "Consider all free
  and public and use the license we have been using and correct that license
  when I naively chose the wrong one or none. Always consider it all public
  if in a public repo." And: "Please ensure the right license is chosen that
  is essentially a license that says there is no restrictions and all that.
  No attribution required." This handbook and every project: wherever one
  has the wrong licence or none, it gets CC0. P9 says so. The open question
  on the licence (asked 2026-10-27) is closed.

- 2026-10-27 Claude: Lyceum-Commons README restructured (#66); Cloudflare
  port plan written (Lyceum-Commons #67).
- 2026-10-27 Claude: handbook files adopted by every repository: also
  SAIR-Lean-Kernel-Challenge (#9), ebook-press (#1), Open-Experiment (#2) and
  Living-Pattern-Institute (#1).
- 2026-10-27 Claude: handbook files adopted by Lyceum-Commons (#65),
  lyceum-commons-mobile (#8) and Lyceum-Local (#2); REGISTRY.md updated.
- 2026-10-27 Claude: CI uses actions/checkout@v7 (Node 24 runtime).
- 2026-10-27 Jason: approved GOVERNANCE.md and EXPECTATIONS.md, and named the
  repository `policy-handbook`.
- 2026-10-27 Claude: first version of the handbook, written at the founder's
  request, published by pull request like every later change.
