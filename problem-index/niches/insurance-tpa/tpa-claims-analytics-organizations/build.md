# Reserves Set by Examiner Judgment on Millions of Resolved Claims

**Niche:** [[niches/insurance-tpa/tpa-claims-analytics-organizations/profile|TPA Claims Analytics Organizations]]
**Industry:** [[industries/insurance-tpa|Insurance Third-Party Administrators (TPAs)]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An examiner carrying 200 claims sets each reserve by judgment, and the company holds millions of claims that show what those judgments should have been.
**Tags:** #survival-analysis #gradient-boosting #ml-time-series #evaluation-metrics #revenue-impact

## The Problem
Every open claim carries a reserve — the estimate of what it will ultimately cost. Reserves drive the client's financial statements, their collateral requirements, and their funding. They are set at intake by an examiner and revised as the claim develops, and Pass 1 puts that examiner's caseload at 150-200 claims a month.

Reserve accuracy is one of the things clients evaluate a TPA on, and it is measured after the fact in aggregate — development triangles showing whether the book as a whole developed up or down. That tells the actuary something and tells the examiner nothing about the claim in front of them.

The company holds millions of closed claims with their full history: the facts known at intake, the reserve set, every revision, the litigation path, the return-to-work outcome, and the final paid amount. That is a large, cleanly labelled dataset for predicting ultimate cost from what was knowable at day one — and it is used to produce triangles rather than predictions.

## Why Nobody Has Built This
Reserving is a claims discipline with a strong professional identity. Examiners are trained to set reserves, the practice is documented in handling guidelines, and clients audit whether examiners followed them. A model that proposes a reserve reads as second-guessing a role, and there is a genuine regulatory sensitivity about reserves being set by anything other than informed judgment.

That sensitivity is manageable and is not what has stopped this. What has stopped it is that reserve accuracy has no owner at the claim level. Actuaries own it in aggregate, examiners own individual claims, and nobody owns the question of whether examiners are systematically wrong in identifiable ways.

The SLA does the rest. Everything about the operation is built around meeting 15-30 day decision deadlines at volume, and improving the quality of a judgment does not show up in that measurement.

## What to Build
Ultimate cost prediction from intake, as a decision support layer under the examiner.

**Predict ultimate incurred from day-one facts.** Injury type and body part, jurisdiction, employer and industry, wage, age, tenure, attorney involvement, prior claim history, and reporting lag. Every one of these is captured at intake, and the label is the closed claim.

**Model the trajectory, not just the endpoint.** Claim cost is driven by duration, and duration is a survival problem with covariates that arrive over time — a treatment escalation, an attorney retention, a failed return-to-work attempt. The valuable output is a hazard that moves when the claim moves.

**Flag divergence, do not replace judgment.** Present the model's estimate alongside the examiner's reserve and surface the gap. An examiner who disagrees keeps their reserve and says why — which is both the right professional posture and the mechanism that generates the next training signal.

**Predict litigation and escalation early.** Attorney involvement transforms a claim's cost, and its precursors are visible in the file weeks before it happens. This is where intervention actually changes the outcome rather than just the estimate.

**Measure examiner-level calibration.** Some examiners run consistently high, some low, some are noisy. That is a coaching input and a caseload allocation input, and it exists in the data now.

## Target Customer
Chief Analytics Officer or Chief Data Officer at a large TPA platform. The commercial case is the client relationship: reserve accuracy and cost containment are what renewals turn on, and a TPA that can demonstrate its reserves are better calibrated than its competitors' is arguing on ground nobody else in the market occupies.

## Impact If Built
Reserve error is expensive in both directions — over-reserving locks up client collateral and capital, under-reserving produces adverse development that damages the relationship. And a claim identified early as heading toward litigation or long duration is a claim where intervention still works, which is the difference between predicting a cost and preventing one.
