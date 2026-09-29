# Researcher Judgment About a Market Becomes a Number

**Niche:** [[niches/insurance-restoration/property-repair-estimating-data/profile|Property Repair Estimating Data]]
**Industry:** [[industries/insurance-restoration|Insurance Restoration]]
**Type:** Fix (Pain Point)
**One-liner:** A researcher knows why one metro's drywall labour runs 20% over the regional model, and the price list records 20%.
**Tags:** #tacit-knowledge-ml #tabular-ml #anomaly-detection #worker-facing #data-integration

## The Problem
Cost researchers covering a region develop real knowledge of it. That this metro's labour market has been tight since a hurricane two years ago and quotes still run well over the model. That a particular county's permitting and inspection regime adds days and therefore cost. That one market's supplier base consolidated and prices moved with it. That a construction style common in a region is systematically mispriced by the national line item definitions.

They apply that knowledge as adjustments. The published price reflects it. The reasoning does not — there is a number, and a researcher who could explain it, and no connection between them recorded anywhere.

So adjustments persist after the reason expires. A surge factor from a 2021 storm is still applied in 2026 because nobody remembers it was a surge factor. And when the researcher who covered that region leaves, their successor inherits multipliers that look arbitrary and either preserves them out of caution or removes them and breaks something.

## Why It's Still Broken
The data model holds prices and factors. An insight can only enter as a number, and its justification has nowhere to live except a working file or a person's memory.

The review process compounds it. Price changes are reviewed for magnitude and downstream impact — appropriately — and never for whether the reasoning was captured. The output of every review is a revised figure and no record of the argument.

And nobody can check. Whether a regional adjustment was correct is answered by what jobs in that market actually settled at, which is data the company holds and does not use for this purpose.

## What a Fix Looks Like
Turn adjustments into dated, evidenced, expiring claims.

**Every adjustment carries a rationale.** The geography, the driver, the evidence, the researcher, the date, and an expected duration. "Post-catastrophe labour tightness, expected 18-24 months" is a claim with a review date. "Regional construction style undercosted by the national line item" is a claim that should hold indefinitely. Today both are the same anonymous multiplier.

**Adjustments expire unless renewed.** This alone fixes the largest recurring error in the system, which is a temporary factor becoming permanent by inattention.

**Wire in the evidence.** Settled job costs in that market, supplier quote histories, and permit values exist inside the company. A researcher asserting a market runs 20% over should be able to point at a distribution, and the system should re-run that comparison as new data arrives.

**Surface where the model and the market disagree.** Markets where observed settlements diverge persistently from the published price are where researcher attention is worth most, and identifying them is a computation nobody runs.

**Make coverage quality visible to the researcher.** Which of their line items rest on recent direct observation and which on extrapolation from three regions away — so effort goes where the price is actually weak.

## Who Feels the Pain
Cost researchers, whose expertise is real, undemonstrable, and lost on departure. The head of research, inheriting a factor table with entries nobody can explain. Contractors and carriers, arguing over a number whose basis nobody can produce. And the company, whose most experienced people are a dependency rather than an asset.

## Impact If Fixed
This price list settles property insurance claims across the entire country, and the parts of it that most depend on local knowledge are exactly the parts nobody can audit. Making that knowledge explicit, dated, and testable against settled outcomes turns regional expertise into something the company owns — and retires the stale adjustments that are quietly wrong in markets nobody has revisited.
