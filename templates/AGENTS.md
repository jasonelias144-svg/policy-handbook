# Working in <repository>

This repository follows the handbook at
https://github.com/jasonelias144-svg/policy-handbook. Read its orientation (README.md)
before your first session here. The rules below add to the handbook; they never
loosen it.

## Every session

1. Read `STATUS.md` and the open pull requests (handbook P1).
2. Work on a branch; never push to `main` (P3).
3. End by pushing, updating `STATUS.md` on your branch, and opening or updating
   the pull request (P1).

## Who decides

The founder decides what this project is for and who works on it. The technical
lead (Claude) decides everything about the code, and records an approval on
every pull request before it merges (P4). Intent questions go to the founder (P5).

## This repository

- **What it is:** <one line>
- **Run:** `<command>`
- **Test:** `<command>` (must pass before a pull request is marked ready)
- **Other checks:** `<lint / typecheck commands, or "none">`
- **Merge method:** squash
- **Release:** <how it is deployed, where, and the check that shows it worked (P6)>
- **Data:** <where state lives; what must never be lost>

## Rules specific to this repository

- <rule, and why>

## Always

- Say who made each change: `Made-by: <name> (AI|human)` in commits, and the
  "Made by" field in pull requests (P3).
- No secrets or personal data anywhere in the repository (P8).
- Report outcomes honestly: what you checked, and what you did not.
