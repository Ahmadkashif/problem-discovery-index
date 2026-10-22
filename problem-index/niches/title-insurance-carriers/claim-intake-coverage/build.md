# An Intake Read With Precedents and a Score

**Niche:** [[niches/title-insurance-carriers/claim-intake-coverage/profile|Claim Intake & Coverage Determination]]
**Industry:** [[industries/title-insurance-carriers|Title Insurance Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Experienced counsel can read a claim at intake and predict its path and cost, but no system captures that read, offers precedents beside it or grades it when the claim closes.
**Tags:** #tacit-knowledge-ml #gradient-boosting #survival-analysis #large-language-models #k-nearest-neighbors #evaluation-metrics #compliance
**Contested on:** Every serious competitor in this niche is fighting to turn a title claim notice into an acknowledged claim with a coverage position and a first reserve inside the statutory deadline, and whoever gets coverage and reserve right on the first read, with the fewest later reversals, takes the account.

## The Problem
At intake, counsel decide coverage and set a first reserve on a thin file. Good counsel form an accurate read quickly, drawing on servicers, counties, defect types and fraud signals. Newer counsel do not have that experience. Nobody measures who is calibrated, and the read itself is never recorded.

## Why Nobody Has Built This
Labels are slow (claims close over years), counsel disagree, and coverage carries bad-faith exposure, so carriers are wary of any model near the decision.

## What to Build
At intake: automatic assembly of the policy, exceptions, commitment, approval and recorded documents; a model prediction of resolution path, severity band and time to close with intervals; the ten most similar closed claims; and a one-click capture of counsel's own read. When each claim closes, both reads are scored, and counsel see their own calibration by claim type. The model never decides coverage.

## Target Customer
Chief claims counsel at the four families and regional underwriters.

## Impact If Built
Faster, more consistent coverage positions within the statutory window, better first reserves, and a measured path for newer counsel to reach senior judgement.
