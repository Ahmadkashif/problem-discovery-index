# Search Volume and Difficulty Sold as Facts

**Industry:** [[seo-tooling-vendors|SEO Tooling Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Monthly search volume is an extrapolation from a clickstream panel with enormous tail error, displayed as an integer, and customers build annual content budgets on it.
**Tags:** #bayesian-inference #confidence-intervals #probability-distributions #maximum-likelihood-estimation #gradient-boosting #hypothesis-testing #evaluation-metrics #descriptive-statistics

## The Problem
Every keyword tool shows a monthly search volume — 2,400, 880, 170 — and a difficulty score out of 100. Both are estimates. Volume comes from a clickstream panel of browser and app users, weighted and extrapolated to a national population, or from Google's own ad-planner buckets which are themselves rounded and intent-biased toward advertisers. Difficulty is a vendor-composite of backlink and authority metrics with no external referent at all.

At the head of the distribution the volume estimates are reasonable. At the tail — where the majority of distinct queries live, and where most content strategies now operate — panel counts are single-digit or zero and the extrapolation multiplies noise by a large constant. Two vendors will report volumes differing by an order of magnitude for the same tail keyword, and both display an exact number.

Customers do not treat these as estimates, because nothing in the interface suggests they are. Content calendars, budget cases and agency proposals are built on summed volume projections, and a projected traffic figure from a tool becomes a target someone is measured against.

## What Already Exists
Semrush, Ahrefs, Moz and Similarweb all run panels and publish volume; Similarweb's panel is the largest commercial one. Google Keyword Planner provides bucketed advertiser-facing volumes free. Google Search Console gives true impression counts for the customer's own site, which is the only ground truth anyone has, and is thresholded and sampled in a way that hides the tail. Several vendors publish accuracy studies about themselves. Clickstream panel providers sell the underlying data to the tool vendors.

## The Customisation Gap
The gap is not a better estimate, it is an honest one, and then a calibrated one. A volume with a credible interval — wide at the tail, narrow at the head — changes how a customer plans, because a keyword whose volume is somewhere between 20 and 900 is a different decision from one that is 170. The estimation machinery to produce that interval already exists inside these vendors; what is missing is the willingness to show it, because a competitor's confident integer looks better in a sales demo.

The calibration opportunity is the interesting one. Every customer has Search Console data for their own site: true impressions for queries where they ranked. That is a per-customer labelled sample from the same distribution the panel is estimating, and it can be used to fit a correction specific to that customer's vertical, market and language — precisely where panel extrapolation is weakest, since a panel weighted for a national population is badly wrong for a specialist B2B vocabulary or a non-English market.

Difficulty needs replacing rather than refining. What a customer wants to know is whether *they specifically* can rank for this, given their site's history, topical coverage and authority in that subject — not a universal composite. That is a per-customer prediction with a per-customer answer, and the vendor has the data to make it.

## Impact If Solved
These numbers drive resource allocation across the whole discipline: which content gets written, what a campaign is projected to deliver, what an agency promises. Intervals turn a false-precision plan into a portfolio decision, and customer-calibrated volumes fix the error exactly where planning now happens. A site-specific difficulty model replaces a number customers already distrust with one they could act on, which is a rare case where the honest version is also the more valuable product.
