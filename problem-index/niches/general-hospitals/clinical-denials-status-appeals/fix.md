# The Peer-to-Peer Call Booked Without the Chart Summary

**Niche:** [[niches/general-hospitals/clinical-denials-status-appeals/profile|Clinical Denials & Inpatient Status Appeals]]
**Industry:** [[industries/general-hospitals|General Hospitals]]
**Type:** Fix (Pain Point)
**One-liner:** A hospitalist gets a fifteen-minute peer-to-peer slot with a plan medical director and walks in having skimmed a chart of 200 pages between patients.
**Tags:** #large-language-models #transformers #workflow-orchestration #worker-facing #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to overturn clinical denials of the hospital stay itself (inpatient status, medical necessity and DRG validation) before the payer's appeal window closes, and whoever wins back the most denied dollars per reviewer hour takes the account.

## The Problem
Payers offer peer-to-peer discussions on short notice, often within a day or two of a concurrent denial. The treating physician or a physician advisor takes the call. They need the timeline, the criteria the payer applied, the facts that meet the hospital's criteria, and the policy citation. They usually have a hurried verbal handoff from case management instead.

## Why It's Still Broken
Nobody is staffed to prepare the brief. Case management books the call, the physician takes it between patients, and the outcome is noted in free text, if at all.

## What a Fix Looks Like
An auto-generated one-page brief at booking: admission timeline, criteria met with chart citations, the payer's stated reason and the counter-argument, the applicable rule, and the decision clock. The outcome is captured in two clicks after the call, which feeds the appeal history.

## Who Feels the Pain
Hospitalists pulled off rounds; physician advisors running ten calls a day; case managers who see avoidable days pile up when a call fails.

## Impact If Fixed
Better-prepared peer-to-peers overturn more concurrent denials before the claim drops (estimate: ~10–20 points), saving both the inpatient payment and the downstream written appeal.
