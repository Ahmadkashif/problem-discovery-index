# Avoidable Days With "Other" as the Reason

**Niche:** [[niches/general-hospitals/case-management-post-acute-placement/profile|Case Management & Post-Acute Placement]]
**Industry:** [[industries/general-hospitals|General Hospitals]]
**Type:** Fix (Pain Point)
**One-liner:** Hospitals count avoidable days but code their causes so loosely that nobody can tell how many were the payer, the facility, the family or the hospital itself.
**Tags:** #large-language-models #bert #descriptive-statistics #quick-win #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to get a medically ready patient accepted and authorised for the right post-acute bed on the day they are ready, and whoever removes the most avoidable days per case manager takes the account.

## The Problem
Case managers log avoidable days with reason codes, often at the end of a busy day, and "other" or "awaiting placement" absorbs most of them. Leadership cannot tell whether the binding constraint is MA authorisation, a weekend admissions gap at nursing homes, a delayed physician discharge order or guardianship paperwork.

## Why It's Still Broken
Coding causes takes time case managers do not have, and nobody uses the codes to change anything, so nobody codes carefully.

## What a Fix Looks Like
Derive delay causes from the timeline the systems already hold: medical readiness note, referral sends and replies, authorisation request and decision times, discharge order time, transport booking. Classify case-management notes into a structured reason taxonomy, and report avoidable days by cause and by payer monthly.

## Who Feels the Pain
Case management directors defending length of stay; CFOs negotiating with MA plans without evidence; patients kept in hospital beds.

## Impact If Fixed
Accurate cause attribution shows which payers and facilities drive avoidable days, the evidence needed for contract terms, preferred-provider networks and weekend admission agreements. Moving "other" from most avoidable days to under ~10% (estimate) makes the monthly report usable for those negotiations.
