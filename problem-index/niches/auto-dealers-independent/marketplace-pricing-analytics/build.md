# A Deal Rating Is an Intervention the Platform Controls and Never Measures

**Niche:** [[niches/auto-dealers-independent/marketplace-pricing-analytics/profile|Listing Marketplace Pricing Analytics]]
**Industry:** [[industries/auto-dealers-independent|Independent Auto Dealers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The platform stamps every listing with a rating that moves shopper behaviour and dealer pricing, and has never estimated what the stamp itself does.
**Tags:** #causal-inference #gradient-boosting #survival-analysis #evaluation-metrics #confidence-intervals

## The Problem
The marketplace computes a fair market value per vehicle and labels each listing against it — great deal, good deal, fair, overpriced. Shoppers sort and filter on the label. Dealers reprice to earn a better one. In a large part of the independent used market, that label is the price signal.

It is also a treatment the platform administers. The same vehicle at the same price is presented differently depending on where the model puts the market, and the platform observes what happens next: views, leads, days on lot, price changes, and — for a meaningful share — the eventual sale.

So there is a controlled intervention with observed outcomes, applied millions of times, by the party that decides the treatment. The causal effect of the rating on time-to-sell and realised price is estimable with the platform's own logs, using the discontinuity at each rating boundary, and nobody estimates it.

Two consequences. The platform cannot tell a dealer what a rating change is actually worth — the pitch is that better ratings sell faster, asserted rather than measured. And it cannot tell whether its own labelling is compressing dealer margin across the market, which is the accusation dealers make and neither side can settle.

Underneath that sits an unscored forecast. The market value estimate is a prediction; realised transaction prices are partly observable; and there is no published accounting of accuracy by segment, by vehicle age, by market thinness. Nor is there a per-listing uncertainty, though the model is far more confident about a three-year-old mainstream sedan than about a modified truck with an unusual option set.

## Why Nobody Has Built This
The revenue model points elsewhere. Dealers pay for listings and leads; the analytics are the differentiator that sells the subscription, so investment goes to coverage and shopper engagement rather than to measuring the instrument.

The finding is also commercially awkward in both directions. A large measured effect confirms that the platform materially moves prices, which is exactly the market-power argument dealers make. A small one undercuts the sales pitch.

And nobody asks. Dealers argue about the ratings constantly and have no standing to demand evidence; shoppers do not know the question exists.

## What to Build
Treat the rating as the experiment it already is.

**Estimate the causal effect at the boundary.** Listings just either side of a rating threshold are near-identical vehicles receiving different treatment. That discontinuity gives a clean effect estimate on views, leads, time-to-sell and realised price, from data already in the warehouse.

**Model time-to-sell as a hazard.** Days on lot is a duration with censoring — listings withdrawn, sold off-platform, or still live. Treating it properly is the difference between an average and a usable forecast for a dealer deciding whether to reprice or wholesale.

**Publish accuracy and per-listing uncertainty.** A market value with an honest interval, and a segment-level accuracy record, is a materially stronger product than a point estimate — particularly on the thin-market vehicles where dealers most distrust it.

**Quantify the repricing recommendation.** What a given price change is expected to do to time-to-sell and gross, with an interval. That is the advice a dealer wants and the platform currently gives as a colour.

**Run deliberate holdouts.** A small randomised suppression of the rating on a sample of listings settles every question above permanently and costs almost nothing.

## Target Customer
VP of Data Science or Chief Product Officer at an automotive listing marketplace. The commercial argument is that valuation accuracy is now matched across the major platforms and the defensible claim is a measured one about what the platform does to outcomes.

## Impact If Built
A rating that moves a large share of independent used-vehicle pricing has never had its effect measured by the party that issues it. Measuring it turns an asserted sales pitch into a quantified one, gives dealers a repricing recommendation with an expected value attached, and settles a market-power argument that currently runs on anecdote.
