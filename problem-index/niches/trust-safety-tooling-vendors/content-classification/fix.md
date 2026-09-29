# Fix: The Aggregate Hides the Languages That Fail

**Niche:** Content Classification
**Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** A platform serving forty markets buys a classifier on one accuracy figure, and the figure describes the two languages the training data was strongest in.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #descriptive-statistics #compliance #worker-facing
**Contested on:** Whether a classifier works where the harm actually concentrates, or only in the aggregate.

## The Problem

A platform with substantial user bases across South and Southeast Asia evaluates two classifiers. Both report accuracy in the low nineties. They choose on price and integration effort.

Neither figure describes their users. Both are computed on test sets drawn from the vendor's training distribution, which is weighted toward the languages where labelled data was available. The performance in the languages this platform actually operates in — where the users are, where the growth is, and where the offline consequences of a moderation failure are frequently most severe — is not in the number and is not published.

The platform discovers the gap slowly. Review queues in some markets are dominated by false positives while genuinely harmful content circulates uncaught. Local teams report that the classifier does not understand how people actually write, which in practice means code-switched, transliterated, dialect-heavy text. And the aggregate accuracy figure continues to look fine.

The disaggregation exists in the vendor's own evaluation. They know which languages perform well. Publishing it is a decision, not a project.

## Why It's Still Broken

**The aggregate sells better.** A single strong number is a better sales artefact than a table showing weak segments, and the buyer is comparing numbers.

**Buyers do not know to ask.** A platform evaluating classifiers asks for accuracy because that is what is offered, and does not know the figure describes a different population.

**Test sets follow training data.** Evaluation is built from the same distribution as training, so the segments that are weak are also under-represented in the measurement of their weakness.

**Language coverage is claimed and not measured.** Supporting a language and performing well in it are different claims, and the marketing does not distinguish them.

**The affected users have no channel.** Over-removal and under-detection in a lower-resource language affects people with no route to the vendor's product team.

**The consequences are geographically distant from the buyer.** A platform's headquarters teams evaluate the classifier and the failures land in markets they do not observe directly.

## What a Fix Looks Like

**Ask for per-language performance before buying.** A buyer requesting a breakdown by the languages they actually operate in would change the evaluation immediately, and vendors who cannot supply it have said something.

**Build your own evaluation set.** A platform can label a sample of its own content in its own markets and measure the classifier on it. This is a few thousand items per market and it is the only measurement that describes the deployment.

**Weight evaluation by user distribution.** The accuracy figure that matters is weighted to where the users are, not to where the training data was.

**Monitor per-market queue composition.** False positive rates and review volumes by market are computable from the review outcomes and would reveal the disparity within weeks.

**Give local teams a channel.** The people who can tell you the classifier does not understand how their market writes are frequently in the organisation and have no route to the vendor.

**Require disaggregated reporting in procurement.** A platform making per-segment disclosure a purchasing condition changes what vendors publish, and a few large buyers doing it would change the market.

**Report it to regulators honestly.** Where a platform reports moderation accuracy, an aggregate that does not describe its user base is a partial account, and the disaggregation is what a regulator actually needs.

## Who Feels the Pain

Users in markets outside the high-resource languages, who experience both more harmful content and more wrongful removal, and who are frequently in the places where the offline consequences are most severe.

Local trust and safety teams, who know the classifier does not work well in their market and have no way to demonstrate it.

The platform, which believes it has deployed a capable classifier and has deployed one that is capable in two languages.

And the vendor, whose genuine weakness in a market is invisible to them because nobody reports it back.

## Impact If Fixed

Asking for per-language performance is a procurement question that costs nothing and would immediately reveal which vendors have measured it and which have not.

A platform labelling a few thousand items of its own content per market produces the only accuracy measurement that describes its actual deployment, and it is achievable within weeks.

And monitoring per-market queue composition is computable from data the platform already generates and would surface the disparity without waiting for anyone to publish anything.
