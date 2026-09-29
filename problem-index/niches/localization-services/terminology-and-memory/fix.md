# The Match Everyone Overwrites

**Niche:** [[niches/localization-services/terminology-and-memory/profile|Terminology & Memory Health]]
**Industry:** [[industries/localization-services|Localization Services]]
**Type:** Fix (Pain Point)
**One-liner:** The same memory segment has been proposed and rejected by every linguist for two years and is still in there.
**Tags:** #quick-win #data-integration #descriptive-statistics #evaluation-metrics #automation #compliance #worker-facing #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to keep the translation memory and glossary trustworthy, because once linguists stop trusting them they work around them and the assets decay unchecked — and whoever maintains them takes the account.

## The Problem
Bad segments persist indefinitely because nothing removes them. A wrong translation approved once is proposed to every subsequent linguist, who overwrites it, and the memory keeps both. Over time the proportion of untrustworthy matches rises, linguists stop reading proposals carefully, and the memory's leverage is lost. The evidence that a segment is bad — that everyone overwrites it — is recorded in the environment and never acted on.

## Why It's Still Broken
Overrides are not fed back — a memory that records what was approved but not what was rejected cannot learn which of its segments are wrong, even though every linguist tells it repeatedly. Removal requires a judgement nobody owns. The memory is append-only by design. And a large memory looks like an asset.

## What a Fix Looks Like
Use the override signal that is already being generated. Track how often each memory segment is proposed and overwritten, which is the fix and is available in every translation environment. Flag segments with a high override rate for review, since a segment everyone rejects is a defect the memory is broadcasting. Demote rather than delete initially, which lowers the stakes of the judgement. Have a linguist review the flagged set periodically rather than the whole memory, which is what makes curation affordable. Remove segments tied to products or features that no longer exist, which is a mechanical filter. Record who approved each segment and when, so provenance informs the review. Check glossary entries against the current product terminology, which frequently finds contradictions. Report the memory's acceptance rate as a health metric, which nobody currently sees. Tell the client, since the asset is theirs and its condition affects their costs. And run the review on a cadence rather than when somebody complains.

## Who Feels the Pain
Linguists overwriting the same wrong segment repeatedly; clients whose asset costs time rather than saving it; agencies whose leverage claims are not met; and the memory itself, growing less trustworthy every month.

## Impact If Fixed
A memory that records what was approved but not what was rejected cannot learn which segments are wrong, though every linguist tells it repeatedly. Tracking override rate uses a signal already being generated.
