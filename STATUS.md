# Status: policy handbook

**What this is:** the organization's policy, for every repository and everyone who works on them
**State:** active since 2026-10-27
**Updated:** 2026-10-27 by Claude

## Live

- Where: https://github.com/jasonelias144-svg/policy-handbook
- Version: first version
- Last check: 2026-10-27, `tools/check_links.py`: 0 problems

## Now

- Claude: Lyceum-Commons README restructure, then the Cloudflare port plan

## Next

1. Restructure the Lyceum-Commons README so its purpose comes first, with the
   API reference moved to `docs/`. The mobile README is already corrected (#8).
   The leftover branches and the mobile licence are waiting on the founder
   (see Noticed, and lyceum-commons-mobile's STATUS.md).
3. ebook-press: bring its three unmerged branches in through review, once the
   founder says whether the agents that built them will continue.
2. Plan and carry out the Lyceum Commons port to Cloudflare ([decision 0002](decisions/0002-lyceum-commons-hosting.md)).

## Open questions

- For the founder: the licence for this handbook and for each project. The
  Living Pattern Institute README already names a model: CC BY-SA 4.0 for
  writing and Apache 2.0 for software. Should it apply everywhere? (asked 2026-10-27)
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
