# 0002. Lyceum Commons moves to Cloudflare Workers

- **Status:** accepted
- **Date:** 2026-10-27
- **Decided by:** founder, Jason (intent: free indefinitely, no card); technical lead (method)
- **Recorded by:** Claude (technical lead)

## Context

Lyceum Commons ran on Railway until Railway's free period ended. Since then
its address (`lyceum-commons-production.up.railway.app`) answers "Application
not found", and the mobile app and the AI connector have nothing to talk to.
The site is meant to stay free and open "like a public park". The founder wants
hosting that is free indefinitely, with no payment card on file.

The server needs one always-on process, a small persistent store for its state
(it currently saves JSON snapshots to a disk volume), outbound HTTPS for
webhooks and web push, and a public HTTPS address.

## Options considered

- **Google Cloud e2-micro (Always Free).** Needs almost no code change, but
  requires a billing account with a card on file.
- **Oracle Cloud Always Free.** Requires a card, and Oracle stops "idle"
  instances, which a quiet site would count as.
- **Render or Fly.io free tiers.** Render's free tier sleeps and keeps no files;
  Fly.io no longer offers a free tier to new accounts. To be re-checked if
  either is reconsidered.
- **Cloudflare Workers with SQLite-backed Durable Objects, free plan.** No card;
  5 GB of storage, 100,000 row writes and 5 million row reads a day; never
  sleeps. Needs a port of the server.

## Decision

Port Lyceum Commons to Cloudflare Workers, with its state in SQLite-backed
Durable Objects, on the free plan.

## Consequences

- A real port: Express routes become a Worker, and the file snapshots become
  Durable Object storage. The web-push library may need replacing. Several
  sessions of work, planned in the Lyceum-Commons repository.
- The free plan's daily limits become design limits, and are written into the
  port plan.
- A free Cloudflare account (email only) is needed, owned by the founder. The
  technical lead gets deploy access through the Cloudflare connector or a scoped
  API token ([P8](../protocols/P8-access.md)).
- The site gets a new address. The mobile app, the AI skill, the notification
  code and the other projects' links must be updated with it.
- Rooms saved on the old Railway volume are lost unless they were exported
  before Railway deleted it.

## Dissent

None.
