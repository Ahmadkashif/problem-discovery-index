# Re-Authorisation by Phone in the Middle of a Live Tail

**Niche:** [[niches/investigation-and-screening-firms/claims-investigation-surveillance/profile|Insurance Claims Investigation & Surveillance]]
**Industry:** [[industries/investigation-and-screening-firms|Investigation & Background Screening Firms]]
**Type:** Fix (Pain Point)
**One-liner:** When the claimant finally leaves the house at hour seven of an eight-hour authorisation, the investigator has to reach an adjuster for more time or stop filming.
**Tags:** #decision-trees #logistic-regression #workflow-orchestration #worker-facing #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to put claim-changing evidence on the file before the claim's next decision date — the independent medical exam, the deposition, the hearing or the settlement conference — inside the carrier's hour caps, and whoever produces the most usable activity per billed hour takes the account.

## The Problem
Surveillance is authorised in fixed blocks. The claimant may stay home all morning and then drive to a job site in the late afternoon. If the cap is about to run out, the investigator calls the office, the office calls or emails the adjuster, and the adjuster may be in a meeting. The investigator either keeps filming unauthorised hours the carrier may refuse to pay, or stops at the moment the assignment starts to work.

## Why It's Still Broken
Authorisations are written as fixed numbers because carriers fear open-ended billing, and nobody has written down the conditions under which an extension is obviously worth it.

## What a Fix Looks Like
Conditional extension rules set at ordering: if the subject is mobile and engaged in activity relevant to the claim within the last hour of the cap, extend automatically by up to two hours, logged with the reason and a time-stamped clip; otherwise stop. The adjuster sets the rule once per claim and sees each extension afterward.

## Who Feels the Pain
Field investigators forced to choose between unpaid hours and lost evidence; office coordinators chasing adjusters; adjusters interrupted for decisions they would always approve.

## Impact If Fixed
Fewer assignments end just as the subject becomes active, and carriers keep control of spend through rules rather than phone calls.
