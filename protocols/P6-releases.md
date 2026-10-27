# P6 Releases: deploys, verification, rollback

A release is anything that changes what users get: a site deploy, an app build,
a published package, a public announcement.

## Rules

1. **Release only from `main`**, and only reviewed changes ([P4](P4-review.md)).
   There are no hotfixes from branches, however small. The one exception is
   stopping harm ([P7](P7-incidents.md)).
2. **The technical lead decides when to release**, within the founder's intent.
   The founder may halt any release.
3. **Nothing that may cost money is switched on without the founder's decision.**
   That includes paid tiers, usage beyond a free allowance, and new paid services.
4. **Each repository's `AGENTS.md` says how it is released:** the command or
   button, where it goes, and the check that shows it worked.

## Steps

1. **Before:** `main` is green; the changes going out are known (list them in the log line).
2. **Release** using the documented method.
3. **Verify** with the documented check: the site answers, the main path works,
   and the logs show no new errors. A release isn't done until it is verified.
4. **Record it** in the repository's `STATUS.md` under "Live": date, commit,
   where it went, the verification result.

## Rollback

If a release breaks something:

1. **Roll back first:** redeploy the last good commit, or revert the change by
   pull request and release that.
2. **Then fix forward** on a branch, through P3 and P4.
3. If people were affected, or data was put at risk, it is an incident: write
   it up ([P7](P7-incidents.md)).

## Environments

Use the free tiers the founder has approved. Keep production and test data
apart. Never test against real people's data when made-up data will do.
