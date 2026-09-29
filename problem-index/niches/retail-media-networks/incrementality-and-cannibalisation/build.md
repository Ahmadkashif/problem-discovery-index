# Counting Sales That Were Going to Happen

**Niche:** [[niches/retail-media-networks/incrementality-and-cannibalisation/profile|Incrementality & Cannibalisation]]
**Industry:** [[industries/retail-media-networks|Retail Media Networks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The retailer shows the ad and rings the sale in the same system, and still reports a ROAS that counts shoppers who searched the brand by name and subtracts nothing for the organic sale the ad displaced.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #bayesian-inference #revenue-impact #monte-carlo-methods #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to report what a sponsored placement actually caused, net of the organic sale it displaced — and whoever brands trust to produce that number sets the terms on which the category's spend is renewed.

## The Problem
A shopper types a brand name into the retailer's search box. A sponsored result for that brand appears at the top. They click it and buy. The system records an attributed sale and a spectacular return on spend. The shopper was going to buy that product; the organic result was directly beneath the advertisement; the retailer charged the brand for a sale it was about to make anyway and displaced a listing that would have produced it for free. Multiply by a category and the reported return is substantially an accounting of pre-existing demand. Every party knows this. The instrument that could settle it — one company, one database, one identity — is the best-equipped measurement apparatus in advertising and is pointed at a proxy.

## Why Nobody Has Built This
The honest number is smaller, and the reported number funds a profit pool that has become load-bearing for a public company's earnings — this is the entire explanation and it is commercial rather than technical. Brands have historically accepted retailer-reported figures as a condition of shelf relationships. No standard methodology exists, so each retailer's number is incomparable and none is falsifiable. And the party that could measure it is the party that would lose from the result.

## What to Build
Build the honest measurement layer, positioned to be trusted by the side that wants it. Run continuous holdout experiments as infrastructure rather than as occasional studies, since the retailer's identity graph makes shopper-level holdouts trivially implementable — the capability exists and is simply not switched on. Subtract displaced organic sales explicitly, which is the central omission: measuring what the sponsored placement added over the organic listing it replaced is the actual question and is answerable by suppressing the advertisement and observing the same shopper cohort. Separate branded from unbranded query intent, which is the fix note's subject and is most of the inflation. Measure at the category level as well as the brand level, because a brand's incremental gain that came entirely from another brand in the same category is worth nothing to the retailer and is currently invisible. Report incremental margin rather than incremental revenue, since a placement that shifts shoppers to a lower-margin product can raise sales and lower profit. Handle the long-run effects, as a shopper who bought a different brand once may have changed habit, which is a real effect and cuts both ways. Establish a standard methodology through an industry body, since incomparable retailer-specific numbers are how the current situation persists. Position the product to the brand rather than only to the retailer, because the brand is the party who wants the truth and has the budget. Give retailers a path to adopt it without a cliff, since an abrupt restatement is unmanageable and a phased disclosure is not. And publish the gap between attributed and incremental return, because that single ratio is the category's real state of play.

## Target Customer
Brand media and finance teams, independent measurement vendors, and the retailers who conclude that credible measurement is a durable position rather than a threat.

## Impact If Built
The best-equipped measurement apparatus in advertising is pointed at a proxy for a commercial reason, not a technical one. Suppressing the advertisement for a matched cohort measures what it added over the organic listing it displaced, which is the actual question and is switchable on today.
