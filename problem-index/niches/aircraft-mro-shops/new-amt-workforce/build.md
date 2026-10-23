# A Senior-Mechanic Judgement Library by Task

**Niche:** [[niches/aircraft-mro-shops/new-amt-workforce/profile|Newly Certificated A&P Mechanics]]
**Industry:** [[industries/aircraft-mro-shops|Aircraft MRO & FBO Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** When a new mechanic hits a fault the manual doesn't settle, the answer is "go find Dave", and Dave retires next year.
**Tags:** #tacit-knowledge-ml #large-language-models #k-nearest-neighbors #cnns #worker-facing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to get a newly certificated A&P signing off work alone on a type in months rather than years, and whoever shortens time to independent sign-off without raising QA findings takes the account.

## The Problem
Senior mechanics carry thousands of fixes: which connector on this type always corrodes, what a particular vibration on a run-up means, how much coating loss on that blade row is normal. The manuals give procedures and limits but not the order to check things in or the borderline calls. New mechanics learn by asking, which pulls seniors off their own work, or by trial and error, which costs parts and time.

## Why Nobody Has Built This
Fixes are recorded as compliant logbook entries that say what was done, not why or what was ruled out first. Seniors don't write down reasoning, and nobody pays them to. Confirmed-fix databases exist for cars (see [[niches/auto-repair-shops/confirmed-fix-databases/profile|🔍 Confirmed-Fix Diagnostic Knowledge Databases]]) but not for aircraft at the shop level, where each OEM controls technical data.

## What to Build
A capture-and-retrieve library inside the shop. Seniors record a 30-second voice note or photo at the end of a job ("checked the sensor first, it's always the connector at P12 on this type"); it is attached to the work order, the fault and the outcome. New mechanics search by fault message, symptom or task and see the shop's own past fixes, ranked by how often they held. For visual calls (corrosion, borescope findings), pair the images with the senior's disposition. The library records which entries new mechanics used and whether their work passed QA, which shows when each is ready to sign alone.

## Target Customer
Training directors and directors of maintenance at MROs, airline bases and FBO chains hiring large cohorts of new A&Ps.

## Impact If Built
Cutting time to independent sign-off on a type from ~18–24 months to ~12 months (estimate) is worth ~$20,000–$40,000 per new mechanic in senior supervision time and rework. For a base hiring 30 a year, that is ~$0.6–1.2M a year.
