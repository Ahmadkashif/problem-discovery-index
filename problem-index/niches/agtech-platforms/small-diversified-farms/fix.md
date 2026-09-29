# The Audit Reconstructed From a Notebook

**Niche:** [[niches/agtech-platforms/small-diversified-farms/profile|Small & Diversified Farms]]
**Industry:** [[industries/agtech-platforms|Agtech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Organic certification and food safety audits require records that were supposed to be kept all season, and on most small farms they are assembled in the fortnight before the inspection from a notebook, a memory and a stack of receipts.
**Tags:** #descriptive-statistics #evaluation-metrics #compliance #workflow-orchestration #automation #worker-facing #quick-win #data-integration
**Contested on:** Every serious competitor selling to small diversified farms is fighting to make recordkeeping and compliance work for an operation with twenty crops, five sales channels and nobody in the office — and whoever gets the record-keeping burden lowest takes the segment.

## The Problem
The organic inspection is in two weeks. The farm needs seed sources and organic status for everything planted, field histories, input applications with dates and rates, harvest records, sales records reconciling to production, and a traceability chain from lot to buyer. Some of it is in a notebook, some on receipts in a drawer, some in the crop plan, some in a point of sale, and some in the owner's memory. Two weeks of evenings go into assembling it, on top of a farm in full production. Food safety certification adds its own set with its own format. The records were mostly generated during the season; they were not captured in a form anyone could compile.

## Why It's Still Broken
Compliance recordkeeping is designed around what an auditor needs to see rather than around how a farm actually works, so it is experienced as a separate documentation task rather than as a by-product of the work. The certification bodies provide paper templates, which is helpful and assumes the farm will complete them contemporaneously, which nobody does in July. And the software that exists addresses either the farming or the compliance, so the farm maintains both.

## What a Fix Looks Like
Derive the compliance records from the operating records rather than maintaining them separately. If the planting-keyed record described in the build note exists, most of what an audit requires is already there — seed source, field history, applications, harvests, sales — and the audit package is a report rather than a project. The specific additions are small: seed source and organic status captured at ordering, when the invoice is in hand and it takes seconds; applications recorded at the time with the lot and rate, which is a voice note in the field; and cleaning and sanitation logs in the wash-pack shed, captured with a tap on a device that is already there. Generate the certifier's own forms in their format, since every certifier wants something slightly different and reformatting is a real part of the burden. Flag gaps continuously through the season, when they can still be closed, rather than in the fortnight before, when they cannot.

## Who Feels the Pain
Farm owners losing a fortnight of evenings in the middle of a season; certifiers reviewing reconstructions rather than records; and the farms that drop certification entirely because the paperwork is not worth the premium, which is a common and consequential outcome.

## Impact If Fixed
Compliance as a by-product rather than a project removes a burden that is a genuine factor in whether small farms maintain certification at all. The continuous gap flagging is the element that changes the outcome most, since a record that is missing in July can still be created and one missing in October cannot.
