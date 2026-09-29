# Reserving Methodology Brought to the Individual Claim

**Niche:** [[niches/insurtech-platforms/claims-core-systems/profile|Claims Core Systems]]
**Industry:** [[industries/insurtech-platforms|Insurtech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Actuarial reserving has a century of method for estimating how claims develop, all of it applied at portfolio level, and the adjuster setting a reserve on an individual claim has a table.
**Tags:** #survival-analysis #bayesian-inference #probability-distributions #maximum-likelihood-estimation #confidence-intervals #evaluation-metrics #monte-carlo-methods #hypothesis-testing
**Contested on:** Every serious competitor in claims systems is fighting to reserve a claim correctly and route it to the right adjuster at first notice — and whoever improves reserve accuracy and cycle time most takes the account.

## The Problem
Actuaries estimate ultimate losses with development triangles, Bornhuetter-Ferguson methods and stochastic reserving, producing portfolio estimates with distributions. Two floors away, an adjuster reserving a specific claim uses an average by claim type, adjusted by feel as the claim develops. The two never meet, so the portfolio estimate is built on case reserves whose individual quality nobody measures, and the adjuster has none of the methodology that exists to answer exactly their question.

## What Already Exists
Loss reserving methodology is among the most developed quantitative disciplines in insurance, with an extensive literature, professional standards and mature software. Individual claim reserving has a growing academic literature and some commercial implementation. Survival and development modelling tooling is commodity. Every method needed is documented; the barrier is organisational rather than technical.

## The Customization Gap
The adaptation is to the individual claim and to the adjuster's workflow. It requires: (1) development modelling per claim rather than per cohort, which the individual reserving literature addresses and which most carriers have not implemented; (2) updating as the claim develops, so the estimate incorporates what the investigation has revealed rather than remaining anchored to first notice — this continuous revision is what an adjuster does by feel and what a model does well; (3) the estimate delivered as decision support in the claims system rather than as an actuarial report, since the adjuster is the user and a quarterly analysis reaches nobody; (4) explicit separation of the model's estimate from the adjuster's case reserve, with both recorded, because the difference between them is itself the most informative measurement the carrier could make and collapsing them destroys it; and (5) governance appropriate to a number that flows into financial statements, with the actuarial function owning calibration and the claims function owning the decision.

## Target Customer
Carriers and third-party administrators, claims system vendors, and the actuarial organisations who would benefit from better case reserves feeding their own estimates.

## Impact If Solved
Individual claim reserving is a developed method that has not crossed an organisational boundary, and bringing it to the adjuster improves both the claim-level decision and the portfolio estimate built on top of it. Recording the model estimate and the adjuster's reserve separately is the small design choice that makes everything afterwards measurable.
