# Project Failure Prediction From the Draw Record

**Niche:** [[niches/general-contractors/construction-fund-control-inspection/profile|Construction Fund Control & Draw Inspection]]
**Industry:** [[industries/general-contractors|General Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The firm inspects thousands of projects monthly and knows which ones eventually failed, and it uses that history to file reports rather than to predict the next failure.
**Tags:** #survival-analysis #gradient-boosting #time-series-forecasting #evaluation-metrics #cross-validation #confidence-intervals #change-point-detection #feature-engineering #data-integration #revenue-impact

## The Problem
A construction loan goes bad slowly and visibly, and the inspector is the party who sees it happening. Billing outpacing physical progress, cost-to-complete drifting upward, the same trades absent month after month, a schedule that has stopped moving — every one of those is recorded in a monthly report and read by a lender as a status update on one project. Across the firm's book those observations constitute a longitudinal record of project health joined to outcomes, because the firm also knows which loans were ultimately restructured, foreclosed, or completed by a surety. That record is not maintained as a dataset and no model is built on it, so the industry's earliest warning signal is delivered one project at a time as narrative.

## Why Nobody Has Built This
Reports are produced as documents for individual lenders, and the observations inside them — percentage complete by line item, cost-to-complete revisions, trade presence — are captured in inspection forms whose structure varies by client and by inspector. Outcomes arrive months or years later and sit in lender systems rather than the inspector's. And the operating model is per-inspection fee work, where nobody is accountable for what the accumulated file could say.

## What to Build
A structured inspection record with outcomes attached. Each inspection captures the observations in a consistent schema — line-item progress, billing-to-progress divergence, cost-to-complete movement, trade presence, schedule drift — and loan outcomes are captured from lender clients in aggregate. On that base, a project distress model that scores each project monthly against the trajectory of projects that later failed, delivered to the lender as a leading indicator alongside the draw recommendation. That is a materially different product from an inspection report: the lender's actual question is not what percentage complete this project is but whether it is going to finish, and nobody currently answers it. The same record supports contractor-level performance patterns across projects, which is what a lender most wants when underwriting the next loan to the same builder.

## Target Customer
VPs of construction risk at fund control firms running 100-800 inspectors, and the construction lending executives who receive monthly status reports and discover distress when a draw request stops making sense.

## Impact If Built
Moves the product from documentation to prediction, which is a different budget inside the lender and a defensible price. The distress record is also strictly proprietary — only the party performing the inspections across many lenders and thousands of projects can assemble it, and it compounds every month.
