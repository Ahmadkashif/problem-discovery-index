# The Quality Signal the Market Lacks

**Niche:** [[niches/data-marketplace-brokers/marketplace-outcome-intelligence/profile|Marketplace Outcome Intelligence]]
**Industry:** [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A marketplace sees which datasets were evaluated and rejected, bought and churned, and which fields buyers actually use — the exact quality signal the market lacks — and publishes none of it.
**Tags:** #descriptive-statistics #evaluation-metrics #survival-analysis #confidence-intervals #hypothesis-testing #revenue-impact #k-means-clustering #logistic-regression
**Contested on:** Every serious competitor in this niche is fighting to turn what the marketplace already sees — evaluations, rejections, churn, field usage — into the quality signal the market lacks, and whoever publishes it defines how datasets are judged.

## The Problem
A buyer browsing a catalogue sees a description, a price and a provider name. The marketplace knows that this listing has been evaluated forty times and purchased three, that two of those three cancelled inside six months, that buyers who do keep it query four of its thirty fields, and that a competing listing in the same domain has a renewal rate three times higher. None of that reaches the buyer. Every piece of it is a by-product of transactions the marketplace already processes, and its absence is the reason buyers treat the catalogue as a list of claims.

## Why Nobody Has Built This
The marketplace earns on transactions, and a signal that steers buyers away from weak listings reduces near-term revenue while improving long-term market quality — a trade nobody is measured on. Publishing comparative quality makes some suppliers unsaleable, and suppliers are the inventory. Providers would object loudly and buyers cannot demand what they have never seen. And the marketplace can plausibly claim it does not have outcome data, because it does not track outcomes, because it has chosen not to.

## What to Build
Publish what the transactions already reveal. Start with renewal and churn rates per listing, which are pure transaction data, require no new instrumentation, and are the single most informative signal available to a buyer — a dataset two-thirds of buyers abandon within a year is telling you something no description will. Report evaluation-to-purchase conversion, since a listing frequently evaluated and rarely bought is failing a test buyers are running privately. Report field-level usage in aggregate, because which fields buyers actually query is the most direct evidence of what a dataset is worth and providers themselves do not know it. Publish comparative quality within a domain, which is the artefact that converts a catalogue into a market and which no individual provider or buyer can produce. Track outcomes explicitly, asking buyers whether the dataset did what they needed, which is a small instrumentation step and the only way the marketplace learns whether it is intermediating well. Feed field usage back to providers, since a provider told that nobody queries twenty of their fields has a clear improvement path and currently has no signal at all. Anonymise and aggregate so no individual buyer's behaviour is exposed. And accept the supplier attrition, because a marketplace whose signal is trusted attracts better supply than one whose catalogue is complete.

## Target Customer
Marketplaces willing to compete on trust, buyers, providers with genuinely good data, and the industry as a whole.

## Impact If Built
Renewal and churn rates are pure transaction data requiring no new instrumentation and are the most informative signal a buyer could receive. Field-level usage tells providers what is worth maintaining, which even they do not currently know.
