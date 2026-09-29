# A Lottery With an Integration Cost Attached

**Niche:** [[niches/data-marketplace-brokers/pre-purchase-evaluation/profile|Pre-Purchase Evaluation]]
**Industry:** [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every meaningful property of a dataset — coverage of the buyer's population, freshness, accuracy against a reference, whether the important fields are populated — is discoverable only after purchase, which makes the market a lottery with an integration cost attached.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #data-integration #probability-distributions #k-nearest-neighbors #automation
**Contested on:** Every serious competitor in this niche is fighting to let a buyer measure a dataset against their own requirement before paying for it — and whoever does that takes the market, because every purchase in it is currently made blind.

## The Problem
A marketing team buys a consumer dataset described as covering a hundred and eighty million individuals with forty attributes. After a six-week integration they discover it covers eleven percent of their own customer base, three of the five attributes they care about are populated for under a quarter of records, and the refresh they were told was monthly is a quarterly refresh of a subset. Nothing they were shown before purchase was false. Every one of those properties was measurable in advance by a party with access to both datasets, and the market's structure ensured that no such measurement existed.

## Why Nobody Has Built This
Measuring coverage against the buyer's population requires both datasets in one place, which is precisely the thing neither party will do before a contract exists. Marketplaces earn on transactions rather than on outcomes, so a mechanism that prevents bad purchases reduces revenue in the short run. Providers with weak data benefit from opacity and are a substantial share of any catalogue. And no standard exists, so a provider disclosing more looks unusual rather than trustworthy.

## What to Build
Measure before the money moves. Build a matching service that computes overlap between the buyer's population and the provider's dataset without either party seeing the other's records, using privacy-preserving set intersection — which is the enabling technique, is mature, and turns the market's central unanswerable question into a number reported in an afternoon. Report field population rates for every field, since a documented field that is mostly null is the single most common disappointment and the measurement is trivial for the provider and impossible for the buyer. Report freshness as observed rather than as promised: distribution of record ages, actual update cadence, share of records changed per cycle. Measure accuracy against a reference the buyer nominates on the overlapping subset, which is the only credible accuracy claim available. Define a standard evaluation report that every listing carries, since comparability is what converts a catalogue into a market and no individual provider can create it alone. Let buyers run their own evaluation inside a controlled environment before purchase, which is the fully convincing version. Report on the buyer's segment rather than in aggregate, since coverage is rarely uniform and the segment they care about is usually the sparsest. And publish the methodology, because an evaluation the buyer cannot interrogate replaces one trust problem with another.

## Target Customer
Every buyer in the market, the providers whose data is genuinely good and currently indistinguishable, and the marketplaces whose long-run value depends on transactions that succeed.

## Impact If Built
Privacy-preserving overlap measurement turns the market's central unanswerable question into a number computable before a contract exists. Field population rates are trivial for a provider to publish and impossible for a buyer to discover, which makes them the most asymmetric disclosure available.
