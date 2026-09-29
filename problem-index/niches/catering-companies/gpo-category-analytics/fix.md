# Members Are Told What They Saved Against a Baseline That Was Never Observed

**Niche:** [[niches/catering-companies/gpo-category-analytics/profile|Foodservice GPO Category Analytics]]
**Industry:** [[industries/catering-companies|Catering Companies]]
**Type:** Fix (Pain Point)
**One-liner:** The savings report is the central artefact of the GPO relationship, it is computed against a constructed counterfactual price no one paid, and neither the member nor the category team can say how much of the reported number is real.
**Tags:** #descriptive-statistics #hypothesis-testing #causal-inference #confidence-intervals #revenue-impact

## The Problem
A member joins a purchasing group to buy better than it could alone. The proof of that is a savings report: your spend was this, the reference price was that, you saved the difference.

The reference price is the problem. It is variously a list price the distributor publishes and nobody pays, a prior-year price from before market movement, a benchmark drawn from other members, or a negotiated "off-programme" rate that is itself an estimate. Whichever is used, it is a counterfactual — what this operator would have paid otherwise — and it was not observed.

Everyone involved knows this. Category managers know the baseline is soft, because they chose it. Members treat the percentage with polite scepticism and compare competing GPOs on numbers computed differently by each. Finance directors at member organisations cannot reconcile reported savings against a food cost line that went up.

Two things follow. Members cannot evaluate the programme they are buying, so they switch on relationship and rebate share rather than performance. And the category organisation cannot evaluate itself — it does not know which of its negotiations actually moved prices, so it cannot direct effort at the ones that do.

The second is the more damaging. A team of skilled category managers is negotiating hundreds of agreements a year with no measurement of which ones worked.

## Why It's Still Broken
The savings report is a sales artefact before it is an analysis. It is produced for renewal conversations, it needs to be favourable, and a methodology that produced a smaller honest number would be competitively punished — because the competing GPO's report will not be similarly honest.

There is no standard. No industry body defines how foodservice purchasing savings are computed, so every organisation defines its own and none are comparable. The absence of a standard protects everyone.

The counterfactual is genuinely hard. What an operator would have paid alone is not observable, and the temptation is to conclude that since it cannot be observed exactly, any reasonable proxy is as good as another. That conclusion is wrong — a defensible estimate is available — but it is a comfortable place to stop.

Category managers are also not measured on realised price effect. They are measured on agreements signed, coverage of the basket, and reported savings, all of which they influence directly. Nobody is accountable for whether prices actually moved.

And the analytical capability to do better exists inside the building, pointed at producing the reports rather than at questioning them.

## What a Fix Looks Like
**Build the counterfactual from comparisons, not from list price.** Items and operators outside an agreement, over the same period, in the same markets, are the natural comparison group. Comparing realised prices inside an agreement against that group is a far more defensible estimate than any published reference, and the data for it is entirely internal.

**Report an interval and state the method.** A savings figure with a stated methodology and an honest range is more useful to a member's finance director than a precise number they do not believe. It also becomes a differentiator the moment one organisation does it.

**Separate price effect from mix effect.** Reported savings routinely conflate a genuinely lower price with a shift to a cheaper item, and the second is the operator's own decision rather than the programme's achievement. Decomposing them is elementary and would change many reported figures materially.

**Measure the agreements individually.** Which negotiations produced a detectable price movement, and which did not, is testable across hundreds of agreements. That single table would redirect where the category team spends its year.

**Diagnose leakage instead of counting it.** Off-contract purchasing has causes — unavailability, distributor substitution, operator preference, a better alternative price. Classifying them turns a compliance scolding into an actionable finding, and sometimes reveals that the contracted item was the wrong choice.

**Show the member their own price series.** Operators want to know what they are paying over time versus comparable operators, in units they recognise. That is more useful than a savings percentage and is harder to dispute, because it is observed rather than constructed.

## Who Feels the Pain
The member's finance director, holding a savings report that does not reconcile with a rising food cost line. The category manager, working hard on agreements without knowing which ones mattered. The chef or foodservice director, told to buy on programme without being told why. And the GPO itself, competing on a metric no one believes, which is why the competition has collapsed onto rebate share.

## Impact If Fixed
Purchasing programmes intermediate an enormous share of institutional food spend, and the sole measure of whether they work is computed against a price nobody paid. The data to replace it with a real estimate is sitting in the same warehouse that produces the report.
