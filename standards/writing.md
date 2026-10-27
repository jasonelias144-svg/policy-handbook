# Writing standards

For READMEs, documentation, pull requests, status notes, decision records and
reports. Most of our readers are busy people, and agents arriving with no
memory. Write for them.

## Plain and true

- Plain words, short sentences. Explain a technical term the first time you
  use it, or use a plainer one.
- Say what is true **now**. Delete or correct text the moment it stops being
  true. Out-of-date documentation is worse than none.
- Separate what you verified from what you believe. "Tests pass (ran
  `npm test`, 212 passed)" is a fact; "should work" is a hope, so label it as one.
- Don't pad. No filler, no repeating what the reader just saw.

## READMEs

Open with the answers, in this order:

1. What it is, in one or two sentences.
2. Who it is for.
3. Its state: working, live, paused, complete. Give dates.
4. How to run it and test it.
5. Where to go next: the handbook, `STATUS.md`, deeper documentation.

Put detail (API references, configuration knobs, edge cases) in separate pages,
linked from the README.

## Status notes, pull requests and reports

- Lead with the outcome, then the evidence, then what's left.
- Name things exactly: file paths, commands, pull request numbers, commit SHAs.
- Dates as `YYYY-MM-DD`; times in UTC unless a local time is stated.

## People

- Refer to people by name or role. Use "they" for anyone whose pronouns haven't been stated.
- Name AI contributors by product ("ChatGPT", "Claude", "Grok"), and say when
  something was written by an AI.
