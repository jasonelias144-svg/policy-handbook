# Archives and the catalogue

How a repository keeps its living pages short without losing anything,
and how what it keeps is catalogued, so that the same steps work in
every repository and the catalogues can later be read as one
([decision 0007](../decisions/0007-archives-and-the-catalogue.md)).

## What is archived

A **living page** is a page that grows by dated entries and is read
every session: `STATUS.md`'s dated sections ("Decided", the log, and
any other a repository keeps by date), and pages of dated messages.

Only dated entries of living pages are archived. Pages that describe a
design or a rule are kept current by editing, and are not archived.
Files of record (conversation records, delivered files, works) are
already kept whole; they are catalogued, not archived.

## The rules

- **An entry** is the lines from the one that starts it, with its date
  (`- YYYY-MM-DD ...`, or a `### YYYY-MM-DD ...` heading for a
  message), to its last line before the next entry or the end of its
  section.
- **What stays:** each living page keeps the entries of its three most
  recent days, counted over all its dated sections. A repository may
  choose another number in its `AGENTS.md`, with its reason.
- **What moves:** the older entries, whole and unchanged, a day at a
  time, to `archive/<page>/<YYYY-MM-DD>.md`: one file for each page and
  day, holding that day's entries from each section, under the
  section's own heading, in the order the page had them. Only the blank
  lines between entries are not carried.
- **A day is moved once.** An entry dated on a day already archived
  stops the run: a new entry takes the day it is written.
- **Nothing in the archive is edited again,** except to redact what is
  private. A redaction updates the file's size and hash in the
  catalogue in the same change, and the pull request says what was
  redacted and why.
- **The page points to the archive:** each dated section, once
  anything has moved from it, opens with one line saying where its
  earlier entries are.
- **The pages are committed first,** and the catalogue names that
  commit. A repository that archives merges with merge commits, so the
  commit stays in its history.

## The catalogue

Each repository that archives has `archive/catalog.json`, and
`archive/README.md` written from it for people. Its `items` share
these fields with any other kind of file a catalogue will hold:

| Field | What it is |
|---|---|
| `path` | the file, from the repository's root |
| `kind` | what the file is: `archive` here |
| `title` | a short name: for an archive file, the page and the day |
| `date` | the day the file is about |
| `bytes`, `lines`, `sha256` | its size, its lines, and its SHA-256 |

An archive file adds `source` (the page), `sections` (each section and
how many entries), `moved` (the day it was moved) and `commit` (the
commit the page was at). Other kinds (a conversation record, a file
given to a collaborator, a stage, a work) will keep the shared fields
and add their own, so that every repository's catalogue can be read
the same way, and gathered into one.

## How

The reference script is open-worlds'
[`docs/archive.py`](https://github.com/jasonelias144-svg/open-worlds/blob/main/docs/archive.py):

- `python3 docs/archive.py` says what a run would move, and changes
  nothing;
- `--write` moves it and writes the catalogue;
- `--check` exits 0 if the archive is whole and in step with its
  catalogue and its pages, and a test runs it.

A repository adopts it by copying the script and its test, naming its
own living pages in the script's `PAGES`, and adding the step to its
`AGENTS.md`. It is worth adopting once a living page passes about
100 KB, or sooner.

## When

At the end of a session ([P1](../protocols/P1-sessions.md)), in a
repository that archives: commit the pages, run the script, and when
it lists anything, run it with `--write`, check, and commit again.
