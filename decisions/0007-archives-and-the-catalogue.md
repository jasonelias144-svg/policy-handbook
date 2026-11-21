# 0007. Archives and the catalogue

- **Status:** accepted
- **Date:** 2026-11-21
- **Decided by:** founder, Jason (that there is an archive, repeatable
  and ready for a larger catalogue); technical lead (how)
- **Recorded by:** Claude (technical lead)

## Context

In open-worlds, `STATUS.md` had reached 455 KB and
`docs/COLLABORATING.md` 169 KB. Both grow one dated entry at a time and
are read at the start of every session, by people and by AI
collaborators. The technical lead proposed moving the older entries
into dated archive files. The founder, 2026-11-21:

> Yes, let's begin archiving processes and then document those
> archiving processes to ensure it is repeatable and capable of fitting
> into a larger cataloging system that is taking shape as we go.

## Options considered

- **Leave the pages long.** Nothing to build, and every reader pays for
  it every session; long pages are already cut into parts for readers
  who are shown only a page's start.
- **Delete old entries and rely on git history.** Short pages, but what
  was decided becomes hard to find, and a reference by date leads
  nowhere.
- **Move old entries to an archive, a file for each month.** Few files,
  but a month here holds hundreds of entries.
- **Move old entries to an archive, a file for each page and day, with
  a catalogue.** A reference by page, section and date, the form the
  pages already cite, leads to one file; each file is checked by its
  hash, and the catalogue's fields can be shared by every other kind of
  file.

## Decision

The last option, as set out in
[standards/archives.md](../standards/archives.md). Living pages keep
their three most recent days of dated entries; the older ones move,
whole and unchanged, to `archive/<page>/<day>.md`, listed in
`archive/catalog.json`. open-worlds' `docs/archive.py` is the
reference script (open-worlds #137).

## Consequences

- Living pages stay short, and nothing is lost: every moved entry is
  in one file, by its date, and can be checked against the commit it
  was taken from.
- A repository that archives merges with merge commits, so the commits
  its catalogue names stay in its history.
- An archived entry is not edited again, except to redact; a decision
  that changes is changed by a new entry, as before.
- Each repository adopts it when its living pages grow; the catalogues
  share their fields, so they can later be read as one.

## Dissent

None.
