# The Schema That Grows Until Nobody Fills It In

**Niche:** [[niches/internal-developer-platforms/service-catalogue-accuracy/profile|Service Catalogue Accuracy]]
**Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Every consumer who wants something from the catalogue adds a field, the metadata file reaches forty entries, and teams stop maintaining any of it.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #k-means-clustering #quick-win #worker-facing #automation
**Contested on:** Every serious competitor here is fighting to keep a service inventory correct without anybody maintaining it — and whoever does that takes the foundation of the category, because everything else depends on the catalogue and the catalogue depends on metadata nobody updates.

## The Problem
The catalogue schema began with five fields. Security added data classification and a compliance scope. Finance added a cost centre. Architecture added a tier and a lifecycle stage. Incident management added an escalation path and a criticality. The metadata file now has forty fields, most teams fill in eight, and the rest are empty or wrong — including several of the newer ones that were added precisely because somebody needed them. Each addition was individually reasonable and the aggregate destroyed the thing they were adding to.

## Why It's Still Broken
Adding a field is free for the person adding it and costs every team a little, which is the standard tragedy and produces monotonic growth exactly as it does with alert rules, dashboards and pipeline steps throughout this vault. Nobody owns the schema's total burden, so no one is weighing the addition against the decay it causes. Field completion rates are not reported, so a field that nobody fills in looks identical to one everybody does. And the consumers who added fields do not see that the data they are consuming is empty.

## What a Fix Looks Like
Govern the schema by its cost. Report completion and accuracy per field, which immediately separates the fields that work from those that do not and is a query over the catalogue itself — and which usually shows that the newest fields are the emptiest. Require a case for each new field that identifies who will fill it in and why they would, since most additions fail that test and the exercise prevents them. Derive rather than declare wherever possible, because a derived field costs nobody anything and is the alternative to the request. Retire fields with low completion, since an empty field is worse than no field — it implies an answer exists. Cap the declared set explicitly, which forces the trade-off to be made deliberately rather than by accumulation. Show the consumer of each field who uses it and what for, so a team filling it in knows why. And measure the total maintenance burden the schema imposes, which is the number that would let somebody manage it and which nobody has.

## Who Feels the Pain
Teams asked to maintain forty fields about each of their services; consumers relying on fields nobody fills in; and platform teams whose catalogue accuracy declines with every well-intentioned addition.

## Impact If Fixed
Per-field completion reporting is a query over the catalogue and usually shows that the newest fields are empty, which is the argument against the next addition. Requiring a case identifying who will maintain a field prevents most additions and is the governance that is entirely absent.
