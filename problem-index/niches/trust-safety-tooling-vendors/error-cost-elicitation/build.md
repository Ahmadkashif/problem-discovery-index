# Build: A Stated Exchange Rate

**Niche:** Error Cost Elicitation
**Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A structured process that makes a platform state, per category, how much legitimate content it accepts removing to catch a given amount of harm — recorded, reviewable and consulted with the affected populations.
**Tags:** #bayesian-inference #evaluation-metrics #confidence-intervals #probability-distributions #hypothesis-testing #compliance #worker-facing
**Contested on:** Whether a platform will state what it costs to miss a piece of harmful content against what it costs to remove a legitimate one.

## The Problem

A platform's moderation policy says it balances user safety with freedom of expression. Everyone says this. It commits to nothing and guides no decision.

The actual balance is a number in a configuration file, chosen without a framework, which encodes an exchange rate nobody has stated. At that threshold, for every piece of harmful content caught, some number of legitimate posts are removed. The platform has decided that trade is acceptable, implicitly, without anyone articulating it.

Making it explicit is uncomfortable in a specific way. The output is a sentence like: in this category, we accept removing this many legitimate posts to catch one instance of this harm. Written down, that sentence can be quoted, criticised and compared against other platforms.

Which is precisely why it should exist. A platform that has stated its position has made a decision that can be reviewed; one that has not has made the same decision invisibly.

The elicitation methods are mature. Decision analysis has spent decades making people state preferences over outcomes that cannot be naturally quantified — paired comparisons, scenario ranking, standard gamble — and none of it has been applied here.

## Why Nobody Has Built This

**The output is quotable.** A stated exchange rate is a sentence a journalist or a regulator can use, which is a strong reason for a platform not to produce one.

**Vendors will not lead it.** A vendor providing this framework is taking a position on the relative weight of over- and under-removal, which every vendor avoids for good commercial reasons.

**The affected parties are not consulted anywhere.** The people harmed by missed content and the people wrongly removed are the ones whose preferences matter and neither is asked.

**Over-removal harm has no magnitude.** Half the trade has no measured quantity, because a wrongly removed post produces an appeal rather than a metric.

**Costs differ by community and the differences are politically charged.** Over-removal falls unevenly — reclaimed speech, minority language use and marginalised communities are documented to be affected disproportionately — and acknowledging that in an elicitation is uncomfortable.

**No regulator requires it.** Regulatory regimes ask about processes and reporting, not about the stated values underlying the threshold.

## What to Build

**Elicit per category using structured methods.** Paired comparison and scenario ranking rather than asking for a number directly. People cannot state an exchange rate and can consistently rank scenarios, and the rate is derivable from the rankings.

**Consult the affected populations.** The elicitation should include the users on both sides — those experiencing the harm and those experiencing removal — rather than being a policy team's internal exercise. This is where it differs most from the medical analogue and where it is most valuable.

**Differentiate by community where the evidence supports it.** Where over-removal demonstrably falls more heavily on particular communities or language groups, the cost is higher for them and the elicitation should say so.

**Record the judgement with its basis.** Who was consulted, what was stated, when, and what threshold followed. This is what makes the decision reviewable and is what a regulator will eventually ask for.

**Run sensitivity analysis.** Show how much the resulting threshold depends on the elicited values. In some categories the answer is barely, which is worth knowing and would redirect attention to the parameters that do matter.

**Revisit it on a cycle.** Values change, platforms change, and a judgement made three years ago is still governing today's threshold.

**Publish it.** A platform that publishes its stated exchange rates has done something no competitor has and has invited exactly the scrutiny that would improve the field.

## Target Customer

Platform policy leadership, who make this judgement implicitly and would gain a defensible, documented basis for a decision they currently cannot explain.

Regulators and civil society, for whom a stated exchange rate is the artefact that would make a platform's values inspectable rather than embedded in a configuration file.

Academic and research collaborators, for whom eliciting preferences over moderation trade-offs at population scale is a well-posed and unexplored problem.

## Impact If Built

The most consequential values judgement in content moderation becomes explicit, where it currently exists only as a number nobody has justified.

Consulting the affected populations is what distinguishes this from an internal exercise, and it is the element that would most improve the legitimacy of the resulting threshold.

And publishing the stated rates would create the first basis on which platforms could be compared on their actual moderation values rather than on their policy language, which is currently identical everywhere.
