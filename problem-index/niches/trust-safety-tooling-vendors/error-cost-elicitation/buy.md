# Buy: Preference Elicitation From Decision Science

**Niche:** Error Cost Elicitation
**Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Health economics and decision science built rigorous methods for eliciting preferences over incommensurable outcomes, and content moderation asks nobody anything.
**Tags:** #bayesian-inference #evaluation-metrics #confidence-intervals #probability-distributions #hypothesis-testing #descriptive-statistics #worker-facing
**Contested on:** Whether a platform will state what it costs to miss a piece of harmful content against what it costs to remove a legitimate one.

## The Problem

Getting people to state preferences over outcomes they cannot naturally quantify is a mature methodological field.

Health economics needs to compare a year of life in one health state against a year in another, which are not commensurable, in order to allocate resources. It developed standard gamble, time trade-off and discrete choice experiments to elicit those preferences rigorously, at population scale, with established validity checks.

Environmental economics values goods with no market price through contingent valuation and choice experiments. Public policy elicits preferences over regulatory trade-offs through deliberative methods and citizens' assemblies. And decision analysis provides the framework that turns elicited preferences into a decision.

The common insight is that people cannot state an exchange rate directly and can consistently choose between scenarios, from which the rate is derivable.

Content moderation faces exactly this problem, sets the exchange rate by having an engineer type a number, and consults nobody.

## What Already Exists

Health economics: standard gamble, time trade-off, discrete choice experiments and the quality-adjusted life year framework, with decades of methodological development and validity research.

Environmental valuation: contingent valuation and stated preference methods for goods with no market price.

Deliberative methods: citizens' assemblies and deliberative polling, used for contested public policy trade-offs and designed for exactly the situation where a values judgement affects a population.

Decision analysis: the framework converting elicited preferences into an optimal decision, with sensitivity analysis.

Content moderation: policy documents with qualitative principles and a configuration field.

## The Customization Gap

**Nobody has applied any of it.** This is the gap. The methods are mature, documented and implementable, and the field has not reached for them.

**The population is global and heterogeneous.** Health economics elicits from a national population. A platform's users span jurisdictions, languages and cultural contexts with genuinely different preferences, which makes a single elicited rate inadequate and a per-community one necessary.

**Both harmed parties must be included.** Health elicitation asks patients. Here the two error types affect different populations — those experiencing harm and those experiencing removal — and both must be in the elicitation or the result is one-sided.

**Deliberative methods fit best and are slowest.** A deliberative process on moderation trade-offs would produce the most legitimate result and is expensive and slow, which argues for using it on the categories where the judgement matters most.

**The platform has an interest in the outcome.** Health elicitation is conducted by parties without a stake. A platform eliciting preferences about its own moderation has an interest, which argues for independent conduct.

**Scale is achievable.** Discrete choice experiments run at population scale routinely, and a platform has direct access to its users — which makes large-scale elicitation more feasible here than in most of the source domains.

## Target Customer

Platform policy and research teams, who have the population access that makes large-scale elicitation feasible and have never attempted it.

Regulators and civil society organisations, who could commission independent elicitation and would produce a more credible result than a platform doing it internally.

Academic health economists and decision scientists, for whom this is a well-posed application of established methods to a domain with abundant access and no prior work.

## Impact If Solved

Mature, validated methods for exactly this problem exist across several fields and have never been applied to a judgement affecting billions of people.

Discrete choice experiments at population scale are routine in health economics and are unusually feasible here, because a platform can reach its users directly at a scale no health system can.

And independent conduct — by a regulator, a research body or a civil society organisation — would produce a result with legitimacy that a platform's internal exercise could not, which is the arrangement the source disciplines converged on for the same reason.
