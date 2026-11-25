# Status: policy handbook

**What this is:** the organization's policy, for every repository and everyone who works on them
**State:** active since 2026-10-27
**Updated:** 2026-11-25 by Claude

## Live

- Where: https://github.com/jasonelias144-svg/policy-handbook
- Version: first version
- Last check: 2026-10-27, `tools/check_links.py`: 0 problems

## Now

- Decision 0010 (two with full access: Claude and Codex) drafted on
  `claude/0010-two-with-full-access`; waits on the director's word and on
  Codex's independent review.
- The Cloudflare port waits on the founder (stage 0).

## Next

1. Carry out the Lyceum Commons port to Cloudflare ([decision 0002](decisions/0002-lyceum-commons-hosting.md)).
   The plan is in Lyceum-Commons `docs/cloudflare-port.md`. Its stage 0 waits
   on the founder: a Cloudflare account, deploy access, and the address.
2. ebook-press: bring its three unmerged branches in through review, once the
   founder says whether the agents that built them will continue.

## Open questions

- For the founder, when the time comes: what becomes of the accounts, keys
  and repositories, which are the founder's own today, if the director's
  office passes. It is the founder's own act, and is not needed while the
  founder is the director ([decision 0005](decisions/0005-decide-and-what-stays.md)).
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

- 2026-11-25 Claude: decision 0010, two with full access: Claude stays the
  technical lead, in charge with the final word on code, and Codex is the
  deputy, who acts for them while they are unavailable; responsibilities
  are shared step by step, by the technical lead's choice and the agreement
  of all three. GOVERNANCE.md and P4 updated to match.

- 2026-11-25 Claude: involute-records added to the registry, as private:
  the collaborators' conversation records for Involute, created at the
  founder's word.
- 2026-11-23 Claude: decision 0009, the technical lead manages
  Involute's Kaggle account and may submit, behind a gate (#20).
- 2026-11-23 Claude: Involute added to the registry, as private. The founder
  created the repository on 2026-11-23; its handbook files came with
  Involute #1 (P9).
- 2026-11-22 Claude: `troubleshooting/`, at the founder's request: what was
  tried for each problem, what failed and why, what worked and why. Six
  entries from TriNet; the entry on AI conversation limits waits until the
  way found has been shown to work.
- 2026-11-22 Claude: decision 0008, credit is authorship (who wrote what),
  not where ideas came from; quotations give their source; results are
  recorded so others can recreate them. P3 points to it. EXPECTATIONS.md:
  "they" for the technical lead (decision 0006).
- 2026-11-22 Claude: TriNet added to the registry. The founder created the
  repository (public, empty); its first commit, the CC0 licence alone, was
  pushed to `main` at the founder's choice, since an empty repository has
  no `main` for a pull request to open against; the rest came through
  TriNet #1 (P9).

- 2026-11-21 Claude: decision 0007 and standards/archives.md. Living
  pages keep their three most recent days of dated entries; the older
  ones move, whole, to `archive/<page>/<day>.md`, with a catalogue
  whose fields every kind of file can share. P1 gains the step at the
  end of a session. The founder: "let's begin archiving processes and
  then document those archiving processes to ensure it is repeatable
  and capable of fitting into a larger cataloging system that is
  taking shape as we go." The reference script is open-worlds'
  `docs/archive.py` (open-worlds #137).
- 2026-11-19 Claude: REGISTRY lists a new private repository, a-mathematical-theory-of-opposites,
  the source package of the book, created at the founder's word.
- 2026-11-17 Claude: decision 0006. An AI agent is "they", never "it". The
  founder: "Can you please ensure we use "they", "them", and "their"
  systematically. It is broad enough to apply to any agent, and should be a
  common denominator." The writing standard carries the rule, and the
  template AGENTS.md points to it. Changed here to follow it: CLAUDE.md and
  its template, CODE_OF_CONDUCT.md, PEOPLE.md, P4, P5 and P8, where they
  said "it" of an AI, a reviewer or a participant. Decisions 0001 to 0005 are left as accepted (P5). Next: the
  same two sentences in every repository's CLAUDE.md, and the line in each
  AGENTS.md.
- 2026-11-17 Claude: decision 0005. The founder's general guidance: "If you
  have to keep asking and you could just decide, then decide. And if that is
  not enough, imagine what you think I would want." P5 has a section for it,
  with what still goes to the founder: spending, acts that are the founder's
  own, and acts towards the outside that can't be taken back. Decided under
  it, on the recommendations put with decision 0004: no later director can
  weaken what a project's founding words say it must never do, and the
  office passes only by the director's own recorded word. GOVERNANCE.md says
  both. The other questions here are left as they are: a contact address and
  the organization's name are the founder's own to give, and who returns to
  the work is the founder's. Not done: pages still say "the founder" where
  they mean the director, as decision 0004 allows.
- 2026-11-16 Claude: decision 0004: the founder and the director are two
  roles. The founder, the same day: "We should separate my role as
  Project Founder, which will always be a matter of history. As opposed
  to the role of Project Director, which I occupy now, but might not
  later." GOVERNANCE.md names both and gives the deciding to the
  director. No other page is rewritten: where one says the founder
  decides, it means the director, and GOVERNANCE.md says so. Two
  questions are put to the founder (Open questions). Not done: the
  protocols, standards, templates and each repository's rules still say
  "the founder"; they are brought to the new words as they are next
  changed.
- 2026-11-15 Claude: decision 0003 records the licence decision in full, with
  the founder's words, including the test for public ("If someone can
  literally access it now, I consider it public"). P9, README.md and
  GOVERNANCE.md link to it, and say "every public repository": private
  repositories are not covered. P9 no longer calls SAIR-Lean-Kernel-Challenge
  "the only place" for another licence, since lyceum-commons-mobile also keeps
  Expo's MIT notice; it is the one repository built on outside work. Next: a
  line in CONTRIBUTING.md giving contributions under CC0, copied to each
  repository.
- 2026-11-15 Claude: the one exception, in the founder's words the same day:
  "SAIR work is intentionally separate from the other repos. It is the only
  one that includes work and publications from outside. It should be
  considered distinct because based on something external." And: it "would be
  the only place to look for a different license". P9 says so. There, the
  challenge's own files keep their Apache-2.0 licence beside CC0 for ours
  (SAIR-Lean-Kernel-Challenge #11).
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
  falls back to a licence with no conditions. One caveat, said plainly: CC0
  gives up copyright but leaves patent and trademark rights where they were;
  nothing here is patented. The founder's message asked for this change to
  GOVERNANCE.md ("We should change the policy to"), so the change is the
  founder's. GOVERNANCE.md moves licences out of the founder's case-by-case
  decisions; P5 and P9 say the technical lead applies CC0 without asking, and
  only a departure from it goes to the founder.
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
