# Evaluating a Dataset Before Buying It

**Industry:** [[data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** High Impact
**One-liner:** Every meaningful property of a dataset — coverage of the buyer's population, freshness, accuracy against a reference, whether the important fields are populated — is discoverable only after purchase, which makes the market a lottery with an integration cost attached.
**Tags:** #hypothesis-testing #confidence-intervals #descriptive-statistics #evaluation-metrics #bayesian-inference #k-nearest-neighbors #data-integration #revenue-impact

## The Problem
A buyer needs firmographic data on mid-sized manufacturers, or point-of-interest data for a specific metropolitan area, or consumer transaction panels covering a demographic. Several providers offer something matching the description.

What the buyer needs to know is specific: what fraction of their actual target population appears in this dataset, how accurate the fields are, how stale the records are, whether the fields they depend on are populated for the records they care about or only for the easy ones, and how the dataset overlaps with one they already hold.

What they receive is a description, self-reported coverage statistics, and a sample file. The sample is curated. The statistics are computed by the seller with no standard definition — coverage of what universe, measured how, at what date. Overlap with their existing data is unknowable without a match.

So evaluation happens after purchase. The buyer signs, integrates, and discovers in week six that coverage of their segment is a third of what the headline number implied because the headline counted a different population.

The pattern is well known and buyers respond by demanding pilots, which sellers resist because a pilot is a free copy of the product.

## Why It's Unsolved
The evaluation-versus-disclosure tension is genuine. Assessing a dataset properly requires seeing enough of it to measure, and seeing enough to measure is close to having it. Providers of easily-copied data are correctly worried, and this is the reason the market has settled on curated samples.

The marketplace's incentives compound it. Revenue comes from transactions rather than from buyer outcomes, and publishing comparative quality metrics would make some suppliers unsaleable while antagonising the rest. A marketplace that ranked its own catalogue on measured quality would lose the providers who ranked badly.

There is no standard for what quality means. Coverage, accuracy, freshness and completeness all require a defined universe and a reference, and no convention exists — so even a provider willing to publish honest numbers has no agreed way to state them.

And accuracy specifically requires ground truth, which is the same problem the data was bought to solve. Verifying a firmographic field means knowing the true value, which the buyer does not.

## What a Solution Looks Like
Privacy-preserving overlap and coverage measurement before purchase. A buyer should be able to learn what fraction of their target list appears in a dataset, and how much overlaps with data they already hold, without either party disclosing their records — which is exactly what private set intersection and clean room architectures were built for and which the marketplaces have deployed for advertising and not for evaluation.

Standardised quality reporting computed by the marketplace rather than self-reported. Field population rates, distinct value distributions, update recency and record age are all computable from the dataset without exposing it, and reporting them consistently across a category makes comparison possible for the first time.

Cross-provider agreement as an accuracy proxy. Where several providers cover the same entities, disagreement localises quality problems without needing external ground truth, and the marketplace is the only party positioned to compute it.

Realised outcome signals. Which datasets buyers renew, which they churn, and which fields they actually query are the strongest available quality indicators and the marketplace holds them.

## Impact If Solved
The inability to evaluate before buying suppresses the entire market — buyers overpay for datasets that do not fit, underbuy from providers they cannot assess, and build integrations they discard. Pre-purchase measurement using techniques that already exist would change the basis of competition from marketing claims to measured fit.
