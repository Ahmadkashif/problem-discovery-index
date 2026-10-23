# Reliability Scores That Travel With the Clinician

**Niche:** [[niches/skilled-nursing-facilities/per-diem-shift-marketplaces/profile|Per-Diem Shift Marketplaces & Agency Labour]]
**Industry:** [[industries/skilled-nursing-facilities|Skilled Nursing Facilities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A facility filling a same-day shift cannot tell which accepting clinician will actually arrive and do the job well on its unit.
**Tags:** #gradient-boosting #logistic-regression #survival-analysis #evaluation-metrics #worker-facing #automation
**Contested on:** Every serious competitor in this niche is fighting to put a credentialed, reliable CNA or nurse on a same-day open shift, and whoever fills the most shifts inside two hours with the fewest no-shows takes the account.

## The Problem
A shift posted at 5 a.m. may be claimed within minutes and cancelled at 6:30, or claimed by someone who has never worked a dementia unit. Each platform has a star rating, but no-shows, late cancellations and supervisors' notes on performance are scattered across platforms and facilities.

## Why Nobody Has Built This
Platforms compete on supply and keep reliability data to themselves. Facilities do not record per-diem performance systematically. Clinicians resist scores they cannot see or contest.

## What to Build
A facility-side model, trained on the operator's own history across every platform and agency, that predicts show-up and completion probability for each claimant on each shift. Inputs: lead time, distance, shift type, unit, the clinician's history in the building, recent cancellations and supervisor feedback captured in one tap at shift end. Use it to accept claims in ranked order and to book a back-up when risk is high. Clinicians can see their own facility-level record.

## Target Customer
Chains with heavy per-diem use across several platforms; the platforms themselves, which could license the facility-side signal.

## Impact If Built
Cutting no-shows and late cancellations on hard shifts by about a third (estimate) means fewer short-staffed shifts, less double-booking and less last-minute rebooking at peak rates, and a fairer record for reliable per-diem clinicians.
