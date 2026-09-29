# A Confidence Score That Is Not a Confidence Interval

**Niche:** [[niches/real-estate-appraisers/avm-collateral-valuation-analytics/profile|Automated Valuation Models & Collateral Analytics]]
**Industry:** [[industries/real-estate-appraisers|Real Estate Appraisers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every automated valuation ships with a confidence score, almost none of them ship with a calibrated probability that the value is within a stated range, and lenders make waiver decisions on the difference.
**Tags:** #gradient-boosting #bayesian-inference #evaluation-metrics #confidence-intervals #causal-inference

## The Problem
An automated valuation model returns a number and a confidence indicator. The number is used to decide whether a loan is adequately secured, whether a human appraisal can be waived, what a servicer thinks a portfolio is worth, and what an investor will pay for a pool.

The confidence indicator is where the trouble is. Most are ordinal scores or forecast standard deviations produced by heuristics — comparable density, data recency, market volatility, model agreement — rather than by a model of the predictive distribution. A high confidence score does not carry a defensible statement that the true value lies within a given band with a given probability.

This matters more than the point estimate. A lender waiving an appraisal is making a decision under uncertainty, and the entire decision rests on how wrong the number can be. A servicer marking a portfolio needs the tails. And the properties where uncertainty is largest — unusual homes, thin markets, rapidly moving neighbourhoods, properties in poor condition — are exactly the ones where a point estimate with a decorative confidence flag is most dangerous.

Accuracy reporting compounds this. Industry practice reports median absolute percentage error and the share of estimates within ten and twenty per cent of a subsequent sale. Both are computed on properties that sold, which is a selected sample: homes that sell are more standard, more marketable and better maintained than homes that do not, and the model's performance on the sold population systematically overstates its performance on the population it is asked to value.

## Why Nobody Has Built This
Procurement rewards the point estimate. Lenders test vendors on hit rate and median error against sold properties, so vendors optimise for those metrics. A vendor that reported honest wide intervals on hard properties would look worse on a scorecard that does not measure intervals.

The federal quality control rule for automated valuation models pushes toward documented testing and monitoring rather than toward calibrated uncertainty, so compliance can be satisfied without solving the harder problem.

And the selection problem is genuinely hard. Correcting for the fact that only some homes sell requires modelling the sale decision itself, which is a different problem than valuation and one nobody is paid to solve.

## What to Build
A predictive distribution rather than a point plus a flag.

**Model the full conditional distribution.** Quantile regression or a distributional gradient boosting objective yields a value distribution per property directly, at no meaningful cost over a point model, and turns the confidence indicator into an interval with a coverage guarantee that can be tested.

**Validate coverage, not just error.** The right question is whether ninety per cent intervals contain the truth ninety per cent of the time, by property type, price tier, market and condition. Coverage is testable on the sold population and is a far stronger claim than a median error.

**Correct for sale selection explicitly.** Model the probability a property transacts, and use it to reweight validation. This produces an honest estimate of performance on the whole housing stock rather than on the part of it that changed hands, and it is the single most defensible methodological improvement available in this category.

**Model condition as a latent variable.** The dominant unobserved driver of residential value is interior condition, which no public record contains. Permit history, listing photographs and text, sale price residuals for the same property over time, and inspection-derived data where available all carry signal about it. Treating condition as something to infer with uncertainty, rather than as noise, is where the remaining accuracy lives.

**Report where the model should not be used.** A vendor that declines to value a property, with a reason, is more valuable than one that returns a number and a low flag — because the low flag gets ignored and the number gets used.

## Target Customer
Chief Data Officer or Head of Valuation Science at an automated valuation provider. The commercial argument is that point accuracy has converged across the major vendors and is increasingly a commodity, while calibrated uncertainty is unclaimed and is what the waiver decision actually needs.

## Impact If Built
Automated valuations now support waiver decisions on a large share of US mortgage originations and mark trillions of dollars of collateral. Replacing a heuristic confidence flag with a validated predictive interval — and reporting performance on the housing stock rather than on the properties that happened to sell — changes the quality of decisions across the entire residential mortgage system.
