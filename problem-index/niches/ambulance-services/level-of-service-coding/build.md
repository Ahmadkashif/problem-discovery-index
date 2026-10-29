# Pre-Bill Level and Necessity Checker on Every ePCR

**Niche:** [[niches/ambulance-services/level-of-service-coding/profile|Level-of-Service Coding & Medical-Necessity Review]]
**Industry:** [[industries/ambulance-services|Ambulance Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every ambulance claim's level is a reading of a narrative, done by a coder who sees the chart days later; a model can read it at chart close, recommend the level, price it and say what is missing.
**Tags:** #bert #transformers #logistic-regression #evaluation-metrics #compliance #revenue-impact #quick-win
**Contested on:** Every serious competitor in this niche is fighting to code each transport at the level its chart supports, and whoever keeps the most collected dollars per transport after denials and audit recoupments takes the account.

## The Problem
The level decision drives most of an ambulance claim's value and most of its audit risk, and it is made by reading. Coders differ, crews document differently, and the billing firm finds out which charts were weak only when a denial or recoupment arrives.

## Why Nobody Has Built This
Ambulance billing is a niche inside healthcare revenue cycle, served by specialist firms whose software predates modern language models. Large revenue cycle AI vendors target hospitals and physician groups, where the dollars are bigger.

## What to Build
The two-week MVP first. On synthetic NEMSIS v3.5 ePCRs with narratives, a rule layer encodes Medicare's level definitions and a transformer classifier judges whether the narrative supports medical necessity. Each run gets a recommended level among A0426–A0429 with the sentences behind it, a PCS check for scheduled runs, and a price from the CY2026 Ambulance Fee Schedule PUF for its locality. Then a production version trained on a billing firm's claims and outcomes, adding A0433, A0434 and mileage checks, and sending "will not support" flags back to the crew's QA queue while the run is fresh.

## Target Customer
Ambulance billing firms and the revenue-cycle directors of operators that bill in house.

## Impact If Built
For a billing firm handling 500,000 transports a year at ~$470 average Medicare payment, reducing recoupments by 0.5% of billed value (an estimate) keeps ~$1.2M a year.
