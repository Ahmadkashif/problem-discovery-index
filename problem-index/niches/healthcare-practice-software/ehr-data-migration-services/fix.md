# Go-Live Day, When the Chart Is Wrong and the Patient Is Waiting

**Niche:** [[niches/healthcare-practice-software/ehr-data-migration-services/profile|EHR Data Migration & Conversion]]
**Industry:** [[industries/healthcare-practice-software|Healthcare Practice Software]]
**Type:** Fix (Pain Point)
**One-liner:** Migration defects surface during the first week of clinic, reported verbally by physicians to whoever is standing nearby, and are triaged by an exhausted consultant with no systematic view of which defects are isolated and which are affecting every chart.
**Tags:** #k-means-clustering #large-language-models #evaluation-metrics #descriptive-statistics #workflow-orchestration #automation #worker-facing #quick-win
**Contested on:** Every serious competitor in EHR migration is fighting to map an unfamiliar legacy database to a target schema with clinical fidelity and without a consultant hand-reading tables — and whoever maps fastest with the fewest post-go-live surprises takes the account.

## The Problem
Go-live week. A physician says the allergy list looks wrong on a patient. Another says an old note will not open. A nurse mentions that immunisation dates seem shifted. Each report reaches a different person — the on-site consultant, a support ticket, a hallway conversation — and each is investigated individually. Nobody realises until Thursday that all three are the same mapping defect affecting every record created before 2016. The consultant, working fourteen-hour days, is triaging by whoever spoke loudest. The practice, already anxious about the switch, is forming its permanent opinion of the vendor during exactly this week.

## Why It's Still Broken
Go-live support is organised as presence rather than as a process: the vendor puts people on site, and the people absorb whatever arrives. Defect reports are unstructured by nature — a physician describes a symptom, not a root cause — and there is no shared queue, so the same defect reported by four people is four conversations. The consultant with the context is the same person doing the triage, the fixing and the reassurance, at the end of an implementation that already ran long. And because every migration is treated as bespoke, nothing learned in this go-live reaches the next one.

## What a Fix Looks Like
Give go-live a queue and a classifier. Every report, from any channel, lands in one place with the patient and record it concerns. Reports are clustered by the record characteristics they share — date ranges, source tables, coded value sets — so that four symptoms with one cause present as one defect with four reporters and a known blast radius, which is the single most useful thing a consultant can be told on a Tuesday morning. Each cluster is checked against the migration's own validation assertions to confirm scope, and the affected record population is enumerated rather than estimated. Confirmed root causes are written back to the mapping corpus so the same defect is prevented at the next migration off that legacy product, which is where this connects to the rest of the niche.

## Who Feels the Pain
Implementation consultants working fourteen-hour go-live weeks and triaging by volume; physicians who reported a problem on Monday and are still seeing it on Thursday; and practice owners who are three days into a decade-long relationship and already doubting it.

## Impact If Fixed
Clustering typically collapses a chaotic first week into a handful of defects with known scope, which changes the consultant's job from investigation to remediation and shortens time-to-resolution from days to hours. The permanent gain is the feedback path: a defect diagnosed once at go-live becomes a pre-migration check thereafter, which is how the fiftieth migration becomes genuinely safer than the first.
