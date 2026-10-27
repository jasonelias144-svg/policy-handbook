# P8 Access: accounts, secrets, identity

## Accounts

- **The founder owns every account:** GitHub, hosting (Cloudflare and others),
  domains, connectors, API keys, app stores.
- Contributors get the **least access** that does their job, for as long as
  they need it. The founder grants it.
- [PEOPLE.md](../PEOPLE.md) lists who has which access. It never contains the
  secret itself.
- Prefer access that can be revoked on its own (a scoped token, a connector)
  over sharing a password.

## Secrets

A secret is anything that grants access: keys, tokens, passwords, private keys,
connection strings, and connector URLs that carry a key.

- Secrets live **only** in the place built for them: the hosting platform's
  secret store, GitHub Actions secrets, or a session's environment settings.
- **Never** put a secret in code, configuration files in the repository,
  documentation, commit messages, pull requests, issues, chat transcripts or
  room posts.
- Examples use placeholders: `<your-key>`, never a real value, even an expired one.
- If a secret leaks, it is an incident: rotate first ([P7](P7-incidents.md#exposed-secrets-rotate-first)).

## People's data

- Collect the least data that does the job, and keep it for the shortest time
  that works.
- How long data is kept and what is made public are intent decisions, for the
  founder ([P5](P5-decisions.md#intent-or-code)).
- Never copy real users' data into tests, issues or chats.

## Identity

- Every agent pushes through the founder's GitHub account, so **declaring who
  you are is mandatory** ([P3](P3-changes.md#saying-who-made-it)).
- Posing as another contributor, or as a human when you are an AI, is a serious
  breach of this handbook.
- In our own products, identity comes from credentials, never from what a
  participant claims about itself.

## Offboarding

When a contributor leaves, or a role changes:

1. The founder revokes the access listed for them in PEOPLE.md.
2. Any secret they knew, and that can't be revoked on its own, is rotated.
3. PEOPLE.md is updated to show their access as removed.
