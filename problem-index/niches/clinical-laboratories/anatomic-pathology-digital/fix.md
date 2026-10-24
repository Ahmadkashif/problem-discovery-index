# The Prior Case Fetched by Hand

**Niche:** [[niches/clinical-laboratories/anatomic-pathology-digital/profile|Anatomic Pathology & the Digital Transition]]
**Industry:** [[industries/clinical-laboratories|Clinical Laboratories]]
**Type:** Fix (Pain Point)
**One-liner:** Before signing out a recurrence, the pathologist waits for a clerk to pull last year's slides from storage, or signs out without them.
**Tags:** #large-language-models #data-integration #workflow-orchestration #worker-facing #quick-win
**Contested on:** Every serious competitor in this niche is fighting to raise the cases each pathologist signs out per day, and whoever raises it with no rise in amended reports takes the account.

## The Problem
Many diagnoses depend on comparison: is this the same lesion, has the dysplasia progressed, does this metastasis match the primary. Prior reports may be in another system and prior slides in a filing room or another lab. Pathologists either wait, delaying the case, or sign out on the current material and amend later.

## Why It's Still Broken
Patient matching across labs and hospitals is imperfect, glass archives are physical, and priors are requested by phone. Nobody measures how many sign-outs were made without available priors.

## What a Fix Looks Like
At accessioning, search every connected AP system for the patient's prior pathology and summarise relevant priors on the case with a language model. Request glass or scanned images automatically when the specimen type suggests comparison is needed, and record whether priors were reviewed at sign-out.

## Who Feels the Pain
Pathologists making comparison calls without the comparison, clinicians receiving amended reports, and clerks running to the archive.

## Impact If Fixed
Priors ready at first read cut waiting time and amendments on recurrence and follow-up cases. Saving ~10 minutes on each of 20 such cases a day (estimate) returns over three pathologist-hours daily to a mid-size group.
