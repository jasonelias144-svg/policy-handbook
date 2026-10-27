# P9 Repositories: create, set up, maintain, retire

## Creating a repository

1. **The founder decides the project should exist**, and what it is for.
2. **The technical lead sets it up**: the required files below, the settings,
   and a [REGISTRY.md](../REGISTRY.md) entry.

## Required files

| File | What it holds |
|---|---|
| `README.md` | What the project is, for whom, its state, how to run and test it, and a link to this handbook |
| `AGENTS.md` | The rules for working in this repository, for any contributor ([template](../templates/AGENTS.md)) |
| `CLAUDE.md` | Loads `AGENTS.md` for Claude, and states the technical lead's role ([template](../templates/CLAUDE.md)) |
| `STATUS.md` | Now, next, open questions, what's live, and the session log ([template](../templates/STATUS.md)) |
| `LICENSE` | Chosen by the founder. Until then, the README says the licence is undecided. |
| Tests, and CI to run them | For anything with code |

`AGENTS.md` is the shared format that many coding agents read. Claude reads
`CLAUDE.md`, which imports it, so the rules are written once.

Each repository also carries unchanged copies of three files from the
handbook: `CONTRIBUTING.md`, `SECURITY.md` and `.github/PULL_REQUEST_TEMPLATE.md`
(the issue templates in `.github/ISSUE_TEMPLATE/` too, where issues are used).
They link back to the handbook, so contributors who only ever see one
repository still find the rules. When the handbook's copies change, the
technical lead updates them in every repository.

## Settings

On every repository:

- **Protect `main`:** require a pull request before merging; require the CI
  checks to pass where they exist; block force-pushes and deletion.
- **Automatically delete branches** after their pull request is merged.
- Allow only the repository's chosen merge method (squash by default).
- On public repositories, **turn on private vulnerability reporting**, so
  security reports don't have to be public ([SECURITY.md](../SECURITY.md)).

GitHub can't require the technical lead's approval, because everyone pushes
through one account. That rule is kept by the approval record ([P4](P4-review.md)).

## Branch hygiene

- Merged branches are deleted.
- A branch with no activity for 90 days is listed in `STATUS.md` under
  "Noticed", then deleted, unless someone says why it should stay. Deleting a
  branch whose pull request was closed unmerged loses nothing that matters: the
  pull request keeps its commits.
- No branch may be named after a Git keyword or remote (such as `origin` or `HEAD`).

## Retiring a repository

When a project is finished or stopped (the founder decides):

1. Final `STATUS.md`: what was achieved, the final state, and anything someone
   would need to revive it.
2. The README's first lines say it is complete or retired, and since when.
3. [REGISTRY.md](../REGISTRY.md) is updated.
4. Archiving it on GitHub (read-only) is the founder's choice. It can be undone.
