# Working in the handbook

This repository *is* the handbook. Read its [orientation](README.md) before your
first session. The rules below add to it.

## Every session

1. Read `STATUS.md` and the open pull requests (P1).
2. Work on a branch; never push to `main` (P3).
3. End by pushing, updating `STATUS.md` on your branch, and opening or updating
   the pull request (P1).

## Who decides

Changes to GOVERNANCE.md and EXPECTATIONS.md are decided by the founder.
Protocols, standards and templates are decided by the technical lead (Claude).
Every change is merged only with the technical lead's recorded approval (P4).
See [GOVERNANCE.md](GOVERNANCE.md#changing-this-handbook).

## This repository

- **What it is:** the organization's policy, for every repository on the account
- **Run:** nothing to run; it is Markdown
- **Test:** `python3 tools/check_links.py` (every relative link and anchor must resolve; CI runs it on every pull request)
- **Merge method:** squash
- **Release:** merging to `main` publishes it. When `CONTRIBUTING.md`, `SECURITY.md` or the templates in `.github/` change, update the copies in every repository (P9)
- **Data:** none

## Rules specific to this repository

- Keep the protocol numbers P1-P9 stable; other repositories and records cite
  them. Add new protocols at the end rather than renumbering.
- Decision records are never edited after acceptance, except their status line
  ([P5](protocols/P5-decisions.md#recording-decisions)).
- Write for a reader with no context and no memory ([standards/writing.md](standards/writing.md)).

## Always

- Say who made each change: `Made-by: <name> (AI|human)` in commits, and the
  "Made by" field in pull requests (P3).
- No secrets or personal data anywhere in the repository (P8).
