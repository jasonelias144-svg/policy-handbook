# 0010. The founder's own information is public

- **Status:** accepted
- **Date:** 2026-11-27
- **Decided by:** founder, Jason
- **Recorded by:** Claude (technical lead)

## Context

Until now the pages kept the founder close to anonymous: a first name, the
GitHub account name where links need it, and no email address. On
2026-11-27 the founder ended that, in steps:

> Yeah, username is fine. First name is fine. Last name will be fine soon.
> Going public end anonymity.

> As I mentioned email address is fine. As I said before, anonymity was a
> temporary thing, I will be sending out tons of emails, my email address
> is the publicly available way to contact me. I want my email address to
> be found. Leaving traces here and there is the point. […] And may
> measures are just temporary or change upon meeting some threshold. And
> that is where we are now.

> Both emails are mine and I watch both. They were created for account
> separation because of cloud storage files and other reasons of
> compartmentalization. You can allow personal information from now on.
> Since my goal is to have a public website hosted and available for
> development by the new year. Now is as good a time as any to allow my
> email and name to be leaked or released.

The same day the founder said which pronouns he uses: "'He' works for me."

## Decision

The founder's own personal information may appear anywhere the
organization writes: his full name, written as he gives it; both of his
email addresses; his own account names (GitHub, Kaggle and the like); and
his pronouns, he and him.

Everything else in [P8](../protocols/P8-access.md) stands:
- other people's personal data stays out: contributors', participants' and
  users', and third parties' names beyond what a citation needs;
- secrets are never written anywhere.

## Consequences

- P8 ("People's data") points here.
- The repositories whose `AGENTS.md` spells out an exception for the
  founder (Involute, open-worlds, and the profile repository) point here
  too. The generic line "No secrets or personal data" in the other
  repositories is read with this decision.
- Commits that already carry the founder's email address stay as they
  are; no history is rewritten for it.

## Dissent

None.
