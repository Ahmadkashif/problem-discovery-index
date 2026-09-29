# The Refresh That Wiped Two Weeks of Work

**Niche:** [[niches/saas-implementation-partners/environment-management/profile|Environment & Sandbox Management]]
**Industry:** [[industries/saas-implementation-partners|SaaS Implementation Partners]]
**Type:** Fix (Pain Point)
**One-liner:** Somebody refreshed the sandbox and a fortnight of unmerged configuration went with it.
**Tags:** #quick-win #automation #workflow-orchestration #compliance #evaluation-metrics #data-integration #descriptive-statistics #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to keep development, test and production environments consistent across hundreds of client tenants, and whoever automates that takes the account.

## The Problem
A sandbox refresh overwrites the environment with production. Anyone whose work had not been migrated out loses it. This happens because the refresh is requested by one person, the work is being done by another, and there is no record of what is in the environment that has not been deployed elsewhere. It is entirely preventable and it happens on a meaningful fraction of engagements.

## Why It's Still Broken
Nothing knows what is unmerged — an environment that does not track which of its changes exist elsewhere cannot warn anybody before being overwritten, and the refresh is a single button. Configuration is not version controlled. Refreshes are requested informally. And the loss is absorbed as rework.

## What a Fix Looks Like
Record what is in the environment and require a check before overwriting it. Track configuration changes made in each environment and whether they have been deployed elsewhere, which is the fix and is what makes a warning possible. Require an explicit confirmation listing unmerged work before a refresh proceeds. Announce refreshes on a schedule rather than on request, so people can protect their work. Export the environment's configuration before every refresh as a matter of course, which makes the loss recoverable. Keep configuration in version control where the platform permits, which solves this and several other problems. Restrict who can trigger a refresh to people who know what is in the environment. Keep a per-environment log of what was changed and by whom. Standardise a working practice of deploying out of a sandbox frequently rather than accumulating. Review the incident each time it happens rather than treating it as bad luck. And make the safe path the default rather than a discipline people must remember.

## Who Feels the Pain
Consultants redoing a fortnight of work; delivery schedules absorbing avoidable rework; clients paying for it twice; and whoever pressed the button.

## Impact If Fixed
An environment that does not track which of its changes exist elsewhere cannot warn anybody before being overwritten, and the refresh is a single button. Tracking unmerged changes and requiring a confirmation prevents the whole class.
