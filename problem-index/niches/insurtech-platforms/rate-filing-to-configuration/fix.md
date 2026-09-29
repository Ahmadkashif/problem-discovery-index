# Nobody Verifies Production Against the Filed Rate

**Niche:** [[niches/insurtech-platforms/rate-filing-to-configuration/profile|Rate Filing to Configuration]]
**Industry:** [[industries/insurtech-platforms|Insurtech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A carrier's obligation is to charge the rate it filed, its production configuration is a hand-built interpretation of that filing, and no carrier runs a standing check that the two still agree.
**Tags:** #descriptive-statistics #hypothesis-testing #evaluation-metrics #confidence-intervals #compliance #automation #quick-win #workflow-orchestration
**Contested on:** Every serious competitor in rating technology is fighting to turn an approved filing into working, verified configuration across fifty states without a specialist retyping it — and whoever shortens filing-to-production most takes the account.

## The Problem
Configuration was built correctly from the filing two years ago. Since then there have been eleven changes: three filed amendments, two defect corrections, four adjustments made during other product work, and two that nobody can now account for. Whether the production rating configuration currently matches the filed rate in every state is unknown, and the way a carrier finds out is a market conduct examination, a regulator's inquiry, or a customer complaint. The exposure applies to every policy written under the divergence, which is the whole population of that product in that state.

## Why It's Still Broken
Verification would require comparing a document to a configuration, which is the translation problem this niche exists to describe, so the check has been as hard as the original work. Carriers have therefore managed it with process — change control, review, and the institutional memory of the specialists — which is a legitimate control and depends entirely on those people and those processes not slipping. Nobody has built the standing check because nobody had a machine-readable filing to check against, which is what the build note supplies.

## What a Fix Looks Like
Run the comparison continuously and make it a report. With the filing represented in a comparable form, production configuration can be decompiled and diffed against it on every change and on a schedule, per state, per product, per effective date. Divergences are reported with the specific element and the magnitude — a factor that differs by a small amount in one state is a different matter from an entire table that is stale. Every configuration change is linked to the filing that authorises it, so an unauthorised change is detectable rather than merely discouraged. Historical verification matters too: knowing when a divergence began determines the population affected and therefore the remediation, and is currently established by archaeology. Where a carrier cannot yet represent its filings formally, the interim version of this check is a premium regression against independently computed expected values from the manual — which is weaker and still far better than nothing.

## Who Feels the Pain
Compliance officers who cannot attest to something they are responsible for; product teams remediating a divergence that ran for a year; and policyholders charged a rate the carrier did not file.

## Impact If Fixed
This is the compliance control the rating function lacks, in an area where the obligation is unambiguous and the current assurance is process discipline. A standing diff converts an exposure that surfaces at examination into one that surfaces on the day it is introduced, and the historical version determines the size of any remediation before a regulator asks.
