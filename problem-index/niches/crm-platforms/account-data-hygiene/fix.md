# The Merge That Destroys the Evidence

**Niche:** [[niches/crm-platforms/account-data-hygiene/profile|Account Data Hygiene]]
**Industry:** [[industries/crm-platforms|CRM Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Deduplicating accounts means merging records destructively, which loses what was merged and why, so the same duplicate is recreated and re-merged indefinitely and nobody can undo a mistake.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #compliance #data-integration #workflow-orchestration #automation #quick-win
**Contested on:** Every serious competitor in account data is fighting to keep the relationships between accounts correct — parent, subsidiary, duplicate, acquired — rather than the fields inside them, and whoever holds the hierarchy right takes the account.

## The Problem
An operations analyst runs a deduplication pass and merges two hundred account pairs. The merge is destructive: one record survives, the other's identifier is gone, field-level conflicts are resolved by a rule, and the record of what was merged and on what basis is a log entry at best. Three of the merges were wrong — two genuinely distinct subsidiaries collapsed into one, and an account merged into a competitor's record because of a name collision — and unwinding them requires reconstructing from backups. Meanwhile the marketing import that created the duplicates runs again next month and recreates them, because nothing recorded that these two records were considered and judged the same.

## Why It's Still Broken
Merge was implemented as a destructive operation in the CRM data models of the 1990s and has been inherited since. Non-destructive resolution — where records survive and a resolved entity references them — is how the master data discipline solves this and requires a different model than a record with a parent field. Nobody has retrofitted it because merge appears to work, the errors are individually rare, and the party who discovers a bad merge months later is usually a representative who assumes the data was always like that.

## What a Fix Looks Like
Make resolution non-destructive and reversible. Source records persist; a resolved entity references them with the evidence and confidence for each link, which means a merge is an assertion that can be examined and withdrawn rather than an operation that destroys its own inputs. Field-level conflicts record both values with their provenance rather than choosing silently, so a disagreement about employee count between two sources is visible rather than resolved by precedence. Every resolution decision — including the negative ones, that these two records were considered and are not the same — is retained, which is what stops the same duplicate being recreated and re-merged forever and is the single highest-value element. Reversal is a supported operation rather than a restore from backup. And duplicate prevention happens at creation, since the resolution history makes it cheap to check an incoming record against both prior matches and prior non-matches.

## Who Feels the Pain
Operations analysts merging the same pairs repeatedly; representatives who lose account history to a merge they did not know happened; and anyone downstream of a bad merge, who has no way to know the data was ever different.

## Impact If Fixed
Retaining negative resolution decisions alone breaks the recreate-and-remerge cycle that consumes operations time indefinitely. Non-destructive resolution makes structural correction safe to attempt, which is the precondition for the hierarchy work in this niche — nobody will reorganise an account graph on a model where every change is irreversible.
