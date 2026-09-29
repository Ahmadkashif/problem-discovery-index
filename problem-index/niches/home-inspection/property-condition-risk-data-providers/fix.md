# The Cost Analysts' Regional Judgment Lives in Spreadsheets

**Niche:** [[niches/home-inspection/property-condition-risk-data-providers/profile|Property Condition & Risk Data Providers]]
**Industry:** [[industries/home-inspection|Home Inspection]]
**Type:** Fix (Pain Point)
**One-liner:** The people who know why rebuild costs in one metro run 18% over the model maintain that knowledge in personal workbooks.
**Tags:** #tacit-knowledge-ml #tabular-ml #data-integration #worker-facing #workflow-orchestration

## The Problem
Replacement cost estimation is one of the highest-stakes numbers these firms produce. It sets coverage limits on millions of policies, and when it is low, homeowners discover it after a total loss.

The estimates come from cost models — materials, labour, regional factors — maintained by a group of analysts who know a great deal that the models do not contain. That this metro's labour market has been tight since a hurricane three years ago and quotes still run well over the index. That a particular county's permitting adds weeks and therefore cost. That a construction style common in one region is systematically mispriced by the national schedule. That demand surge after a catastrophe follows a shape the standard factor does not capture.

Each analyst holds this for their territories, applies it as manual adjustments, and keeps the reasoning in a personal spreadsheet. When they leave, the adjustments remain in the model as unexplained constants that nobody dares change.

## Why It's Still Broken
The model has coefficients, not reasons. Its structure holds regional factors as numbers, so an analyst's insight can only enter as a number, and the justification has nowhere to go except a comment in a workbook or a person's memory.

The review process reinforces it. Cost model updates go through actuarial and product review focused on the magnitude of the change and its effect on the book — which is appropriate — and never on capturing why the analyst proposed it. The output of the process is a new coefficient and no record of the argument.

And the validation problem is the same one that afflicts everything in this niche: whether the adjustment was right is answered by actual rebuild costs, which arrive after a total loss, years later, in claims data the cost team does not routinely see.

## What a Fix Looks Like
Turn adjustments into documented, testable claims.

**Every adjustment carries its rationale**, structured: the geography, the driver, the evidence, the analyst, the date, and an expected duration. "Post-catastrophe labour tightness, expected to persist 18-24 months" is a claim with a review date. "Regional construction style undercosted by national schedule" is a claim that should hold indefinitely. Today both are the same anonymous multiplier.

**Adjustments expire unless renewed.** A demand surge factor from a 2021 hurricane should not still be silently applied in 2026 because nobody remembered it was there. Expiry forces the review the current process never triggers.

**Wire in the evidence.** Contractor quote data, permit values, and claim rebuild costs exist inside these firms, usually in another business unit. An analyst arguing that a metro runs 18% over should be able to point at the distribution rather than at their experience, and the system should re-run that comparison automatically as new data lands.

**Close the loop where it can be closed.** Total loss claims give an actual rebuild cost against an estimate the firm once produced. Even a modest sample per region per year, tracked over time, tells the cost team which adjustments were right — which is a thing nobody in this business can currently say.

## Who Feels the Pain
Cost analysts, whose expertise is real and undocumented and who cannot demonstrate it. The head of the function, who inherits a model with adjustments no living person can explain. Carriers, who receive replacement costs whose regional accuracy they cannot assess. And homeowners, for whom an underestimate becomes visible only after their house has burned down.

## Impact If Fixed
Replacement cost accuracy is a live consumer protection issue and a live regulatory one, and the failures are concentrated exactly where local knowledge matters most. Making that knowledge explicit, dated, and testable turns the firm's most experienced people from a dependency into an asset, and gives the function the one thing it has never had — a way to find out whether it was right.
