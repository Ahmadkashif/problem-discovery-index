# Structural Attrition Drivers, Not Individual Scores

**Industry:** [[hr-tech-platforms|HR Tech Platforms]]
**Type:** High Impact
**One-liner:** Attrition is predictable months ahead from structural conditions — pay compression, manager span, stalled promotion velocity, absent mobility paths — and the useful product diagnoses the conditions rather than scoring the people.
**Tags:** #survival-analysis #gradient-boosting #causal-inference #hypothesis-testing #confidence-intervals #feature-engineering #evaluation-metrics #revenue-impact

## The Problem
Voluntary attrition is the most expensive recurring event most companies experience. Replacing a professional employee costs a substantial multiple of salary once recruiting, onboarding, lost productivity and the disruption to their team are counted, and the cost is largely invisible because it arrives distributed across budgets.

HR systems report it afterwards. A turnover percentage, quarterly, by department, sometimes with an exit interview summary that is systematically unreliable because departing employees say diplomatic things.

The conditions that produce it are in the same system, months earlier, and are structural rather than personal. A team whose existing members are now paid below the offers being made to new hires for the same role. A manager whose span of control has grown to thirty as the organisation flattened. A job family where nobody has been promoted in two years while an adjacent one promotes annually. A cohort hired together whose tenure is approaching the point where their peers historically leave. A location whose local market has repriced.

Each of those is a condition affecting many people, is measurable from the platform's own records, and is fixable by a decision someone can actually make. None of them requires predicting whether a specific named individual will resign.

## Why It's Unsolved
The category went after the wrong product. Individual flight-risk scoring is the obvious application, several vendors have shipped it, and it fails in practice for reasons that are structural rather than technical. Employees discover they are scored and trust collapses. Managers treat a score as an accusation. The legal exposure is real, since a model trained on who left inherits whatever was in the historical pattern, and acting on individual scores in employment decisions attracts scrutiny under discrimination law. And the score does not say what to do — the manager learns someone might leave and has no lever.

So the honest reading is that the failure of individual scoring has discredited attrition modelling generally, when the structural version was always the better product and was never built.

There are genuine analytical obstacles too. Attrition is a low base rate event with long lead times, and the confounding is severe — pay compression correlates with tenure, tenure correlates with attrition, and separating the structural effect from the demographic one requires care. Sample sizes at the team level are small, which is exactly why pooling across the vendor's whole employer base matters.

## What a Solution Looks Like
Diagnosis at the level of a condition. Which roles, teams, locations and job families are carrying elevated risk, what specifically is driving it, how many people are affected, and what the estimated cost of doing nothing is.

Pay compression is the cleanest case and the most actionable: the platform knows what current employees earn and what new hires in the same role are being offered, and the gap is computable, quantifiable in expected attrition cost, and correctable with a budget decision.

Promotion velocity by job family, manager span against historical thresholds, and internal mobility rates are the next tier — all measurable, all comparable against the vendor's cross-employer base, and all fixable structurally.

The individual level should be deliberately excluded from the product rather than merely discouraged, because a capability that exists will eventually be used.

## Impact If Solved
Attrition costs most organisations more than any software line item and is managed by reporting it after it happens. Diagnosing the structural conditions gives HR leadership something it has never had — a costed, evidence-based case for a specific intervention — and it avoids the surveillance product that has poisoned this territory for a decade.
