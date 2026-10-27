# P7 Incidents: stopping harm, then reporting

An incident is harm happening now, or about to happen:

- a secret (key, token, password) exposed anywhere;
- a site or service broken or down for its users;
- data lost, corrupted, or exposed, or at risk of it;
- abuse, illegal content or harassment on something we run;
- a security hole being exploited, or easy to exploit.

## Anyone may act first

When there is an incident, **anyone** (founder, technical lead, any
contributor) may immediately take **the smallest step that stops the harm**,
without asking for approval:

- take the site or feature offline;
- revoke or rotate the exposed key;
- revert the last change, or redeploy the last good version;
- hide or remove the harmful content.

Do not use an incident as a reason to ship a new feature or a large fix. Stop
the harm; the real fix goes through P3 and P4.

## Exposed secrets: rotate first

A secret that has appeared anywhere public (a commit, a pull request, a chat, a
room post, a log) is compromised, **even after it is deleted**, because the
history keeps it. Rotate or revoke it first; clean up afterwards.

## Then report

1. **Tell the founder** as soon as the harm is stopped.
2. **Write an incident report** within the same session, or the next one, in
   the handbook's `incidents/` folder (in this repository, whichever project it
   concerns) as `YYYY-MM-DD-short-title.md`, using
   the [template](../templates/incident-report.md): what happened, the impact,
   what was done and when, the cause, and what will prevent it next time.
3. **The technical lead reviews** what was done in a hurry and opens follow-up
   work through the normal process.

## No blame

Incident reports describe causes and fixes, not culprits. Mistakes reported
early and honestly are how we get better. Hiding one is the only real failure.
