# Build: Prevalence, Not Takedowns

**Niche:** Enforcement Effectiveness Measurement
**Industry:** [[industries/brand-protection-firms|Brand Protection Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Measure the infringing population over time by sampling, track re-emergence after action, and join to the brand's own market signals — so the report says whether the problem shrank.
**Tags:** #evaluation-metrics #confidence-intervals #causal-inference #survival-analysis #hypothesis-testing #time-series-forecasting #descriptive-statistics #revenue-impact
**Contested on:** Whether anyone can show that enforcement reduced counterfeit sales, or only that it produced takedowns.

## The Problem

A brand spends heavily on enforcement and receives a monthly count. Four thousand listings removed. Up from three thousand six hundred.

The brand's actual question is whether there are fewer counterfeits of their product being sold than there were a year ago. The count does not answer it and cannot, in either direction: a rising count is equally consistent with a growing problem, better detection, or the same operators cycling accounts faster.

The measurement that would answer it is a prevalence estimate. Sample a category on a platform, count what fraction of listings are infringing, repeat monthly. It is a survey, the methodology is ordinary, and it produces a trend that means something.

The second measurement is re-emergence. After an operator-level action, how long before that operator is selling again and at what scale. This is the difference between disruption and inconvenience and is computable from the firm's own records once operators are identifiable.

The third is the brand's own market signal. Warranty claims on non-genuine units, customer complaints about fakes, grey-market observations, seizure data. These sit with the client, are collected for other purposes, and are never joined to enforcement activity.

None of the three is exotic. All three are absent.

## Why Nobody Has Built This

**The count is what the contract is priced on.** A measurement that contextualises the headline downward has no commercial constituency on the supply side.

**Prevalence sampling costs money and produces a worse number.** It is real expenditure whose output may show that a rising takedown count accompanies a rising infringing population.

**Attribution is genuinely hard.** Prevalence changes with seasonality, platform policy, product launches and economic conditions. Attributing a change to enforcement requires a comparison the industry has never constructed.

**Re-emergence requires operator attribution.** Measuring whether the operator came back needs the clustering described in [[niches/brand-protection-firms/operator-attribution/profile|🟠 Operator Attribution]].

**Brand-side signals sit in other functions.** Warranty, customer service and legal hold the outcome data, and the brand protection manager may not have access to any of it.

**Nobody is measured on the outcome.** The manager reports takedowns upward, the firm reports takedowns to the manager, and counterfeit sales are measured by nobody in the chain.

## What to Build

**Sample prevalence monthly.** A defined category on a defined platform, a random sample of listings, assessed for infringement, tracked over time with confidence intervals. This is a survey and it produces the trend line the industry lacks.

**Construct a comparison.** Categories or platforms with lower enforcement intensity as a natural control, so a change in prevalence can be partly attributed rather than merely observed. Enforcement intensity varies enormously between a brand's categories and markets already, which supplies the variation.

**Measure re-emergence as the primary enforcement outcome.** Time to return, scale on return, and the proportion of actioned operators who return at all. This is the measure that distinguishes disruption from inconvenience.

**Join to the brand's own signals.** Warranty claims on non-genuine goods, customer complaints, seizure volumes, grey-market observations. Each is independently noisy and together they bound the real trend.

**Measure search-surface exposure.** For high-intent brand searches on each platform, what fraction of the first results are infringing. This is what a consumer actually encounters, it is cheap to measure, and it is a better consumer-harm proxy than the total population.

**Report the trend, not the count.** Prevalence with its uncertainty, re-emergence rate, and exposure — alongside activity rather than instead of it, because activity is operationally useful and is not an outcome.

**Publish the methodology.** A firm that publishes how it measures effectiveness, including unflattering results, establishes a standard competitors must answer — which is the only route to the metric changing across the industry.

## Target Customer

Brand leadership and finance, who authorise the spend and receive a count they cannot interpret, and who would immediately use a prevalence trend.

Brand protection firms willing to compete on effect, for whom a measured outcome is the first non-volume differentiator available in this category.

Industry bodies and anti-counterfeiting coalitions, who are well placed to publish a prevalence measurement methodology that individual firms would be penalised for adopting alone.

## Impact If Built

The brand gets an answer to the question it is actually asking, which it currently cannot get from any vendor in the market.

Prevalence sampling is an ordinary survey, is cheap relative to the enforcement spend, and would produce the first trend line anyone in this industry has had.

And measuring re-emergence would reveal how much of the takedown count represents the same operators cycling — which practitioners describe privately and no report has ever quantified.
