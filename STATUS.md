# Status: policy handbook

**What this is:** the organization's policy, for every repository and everyone who works on them
**State:** active since 2026-10-27
**Updated:** 2026-10-27 by Claude

## Live

- Where: https://github.com/jasonelias144-svg/policy-handbook
- Version: first version
- Last check: 2026-10-27, `tools/check_links.py`: 0 problems

## Now

- Claude: rolling the handbook out to the remaining repositories

## Next

1. Roll the handbook files out to the remaining repositories: ebook-press,
   SAIR-Lean-Kernel-Challenge, Open-Experiment and Living-Pattern-Institute.
   Done: Lyceum-Commons (#65), lyceum-commons-mobile (#8), Lyceum-Local (#2).
2. Restructure the Lyceum-Commons README so its purpose comes first, with the
   API reference moved to `docs/`. The mobile README is already corrected (#8).
   The leftover branches and the mobile licence are waiting on the founder
   (see Noticed, and lyceum-commons-mobile's STATUS.md).
3. Plan and carry out the Lyceum Commons port to Cloudflare ([decision 0002](decisions/0002-lyceum-commons-hosting.md)).

## Open questions

- For the founder: the licence for this handbook and for each project (asked 2026-10-27).
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

- 2026-10-27 Claude: handbook files adopted by Lyceum-Commons (#65),
  lyceum-commons-mobile (#8) and Lyceum-Local (#2); REGISTRY.md updated.
- 2026-10-27 Claude: CI uses actions/checkout@v7 (Node 24 runtime).
- 2026-10-27 Jason: approved GOVERNANCE.md and EXPECTATIONS.md, and named the
  repository `policy-handbook`.
- 2026-10-27 Claude: first version of the handbook, written at the founder's
  request, published by pull request like every later change.
