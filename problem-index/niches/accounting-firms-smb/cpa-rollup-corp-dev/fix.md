# Post-Close Integration Learnings Never Reach the Next Diligence
**Niche:** [[niches/accounting-firms-smb/cpa-rollup-corp-dev/profile|CPA Rollup Platform Corporate Development]]
**Industry:** [[industries/accounting-firms-smb|SMB Accounting Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The integration team learns exactly which diligence assumptions were wrong — and there is no path for that knowledge to reach the corp dev team before they make the same assumption on the next deal.
**Tags:** #logistic-regression #gradient-boosting #feature-engineering #evaluation-metrics #data-integration #workflow-orchestration #tacit-knowledge-ml

## The Problem
Diligence produces a set of explicit predictions: this partner will stay, this client base is sticky, this firm can be on the common tech stack in six months, these synergies are achievable. Integration then discovers the truth over the following eighteen months. The two teams are different people with different systems and different incentives, and no mechanism compares the prediction to the outcome. Corp dev moves on to the next deal; integration absorbs the variance as operational reality. The consequence is that a platform can acquire thirty firms and never systematically learn that its partner retention assumptions are optimistic by twenty points, or that firms above a certain size consistently take twice the projected time to migrate.

## Why It's Still Broken
Diligence assumptions live in deal models built for a decision, not for later measurement — they are stated as inputs in a spreadsheet, not as tracked claims. Once the deal closes the model is archived and the target becomes a portfolio company tracked in an entirely different reporting stack, with no key linking the post-close entity back to the pre-close assumption set. Nobody owns the comparison: corp dev is measured on deals closed, integration on operational milestones, and neither scorecard includes forecast accuracy. Reconstructing the comparison manually across thirty deals is expensive enough that it never rises above other priorities.

## What a Fix Looks Like
A thin but strictly enforced layer that captures the diligence assumption set as structured, testable claims at LOI — retention by named partner, revenue attrition by year, integration milestones with dates, synergy targets with amounts — and carries that record forward against the post-close entity. Integration reporting then automatically scores actuals against the original claims, and the platform accumulates a calibration record: which assumption classes are systematically optimistic, by how much, and under what target characteristics. That record feeds forward into diligence as adjusted priors, so the next model starts from the platform's demonstrated forecasting accuracy rather than from the analyst's judgment alone. The requirement is not more analysis but a durable identity for each assumption and an owner for the comparison.

## Who Feels the Pain
Integration leads who inherit plans built on assumptions they know to be wrong; corp dev analysts who repeat errors nobody told them about; and the sponsoring PE firm, which underwrites returns on models with unmeasured bias.

## Impact If Fixed
Turns thirty completed acquisitions into a calibrated forecasting instrument instead of thirty anecdotes. Improves bid accuracy on the assumptions that most move price — partner retention and revenue attrition — and gives the platform a defensible, evidence-based underwriting story for its own investors and lenders.
