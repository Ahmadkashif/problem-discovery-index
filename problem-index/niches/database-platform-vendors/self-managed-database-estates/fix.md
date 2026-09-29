# The Backup Nobody Has Restored

**Niche:** [[niches/database-platform-vendors/self-managed-database-estates/profile|Self-Managed Database Estates]]
**Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Backups run every night and complete successfully, and nobody has restored one in eighteen months, so the organisation does not know whether it has backups or whether it has files.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #survival-analysis #compliance #quick-win #automation
**Contested on:** Every serious competitor here is fighting to give an organisation running its own databases the operability a managed service provides, without requiring it to move them — and whoever does that takes an enormous installed base that cannot use anything currently on offer.

## The Problem
The backup job reports success every night. The files are the right approximate size and are copied to the expected location. Nobody has restored one since an audit eighteen months ago. When a restoration is eventually required, the discoveries begin: one database's backup has been failing silently because a permission changed and the job reports the copy rather than the dump; another's includes the data and not the roles; a third restores but the point-in-time recovery has a gap because archive shipping stopped in March. Every one of these is detectable by restoring, and restoring is the thing nobody does.

## Why It's Still Broken
Backup success is reported by the backup job, which knows whether it ran rather than whether the result is usable — the same silent-success failure the connector reliability and file transfer niches describe. Restoration testing requires somewhere to restore to, time, and somebody to verify the result, which is a recurring cost with no visible benefit until the day it matters. It is also frequently on a compliance checklist as a procedure that exists rather than as an exercise that is performed, so the paperwork is satisfied. And a failed restoration test creates work, which is a mild but real disincentive.

## What a Fix Looks Like
Restore routinely and automatically. Restore every database's backup to an isolated environment on a schedule, which is the only meaningful test and is entirely automatable given somewhere to put it — this is the whole fix and the rest is refinement. Verify the restored result rather than the fact of restoration: row counts against expectation, checksums on key tables, application-level consistency checks, and the presence of roles, extensions and sequences that backups commonly omit. Test point-in-time recovery specifically, since the continuous archive is a separate mechanism from the dump and fails separately. Measure and report the actual restoration time, since the recovery objective in the plan is an assumption and the measured time is frequently much longer. Detect coverage gaps by reconciling the database inventory against the backup inventory, which regularly finds databases nobody is backing up at all. And report the freshness of the last successful verified restore per database, which is the honest statement of whether the organisation has backups and is the number a board should be shown instead of a job success rate.

## Who Feels the Pain
Database teams discovering during a recovery that their backups are unusable; compliance functions attesting to a capability nobody has exercised; and organisations whose disaster recovery plan rests on an untested assumption.

## Impact If Fixed
Automated restoration with verification is the only test that means anything and is straightforward given an isolated environment. Reconciling the database inventory against the backup inventory regularly finds databases nobody was backing up, which is the finding that most often justifies the whole exercise.
