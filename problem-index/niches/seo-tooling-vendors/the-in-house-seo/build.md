# A Day to Explain Which of Four Things Happened

**Niche:** [[niches/seo-tooling-vendors/the-in-house-seo/profile|The In-House SEO]]
**Industry:** [[industries/seo-tooling-vendors|SEO Tooling Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Organic traffic falls, the algorithm changed, a competitor moved, the site shipped a release, and the SEO has a day to explain which — with tools that show correlation and nothing else.
**Tags:** #worker-facing #causal-inference #change-point-detection #confidence-intervals #evaluation-metrics #hypothesis-testing #time-series-forecasting #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to give the in-house SEO an answer when traffic drops rather than four charts that correlate — and whoever does that changes whether the role can defend itself inside a business.

## The Problem
Traffic is down twenty-two percent week on week. Leadership wants an explanation tomorrow morning. In that week the search engine confirmed an update, a competitor relaunched their category pages, the engineering team shipped three releases, and a seasonal pattern would predict some of the decline anyway. The SEO opens four tools, each showing a line that fell, and assembles a narrative. They will present it with more confidence than they have, because the alternative is saying they do not know, and in most organisations that is not an available answer.

## Why Nobody Has Built This
The vendors' products were built to report state rather than to explain change, which is a different discipline and a different product — the line chart is the deliverable and always has been. The data needed spans the vendor's corpus, the customer's analytics and the customer's deployment history, and nobody joins them. Causal inference on observational data is hard and vendors prefer to ship a correlation. And the SEO absorbs the failure personally, which keeps it off the roadmap.

## What to Build
Build the diagnosis. Decompose every traffic change into its candidate causes — algorithm, competitor movement, own-site change, demand shift, seasonality, result-page composition — with an estimated contribution and a confidence for each, which is the product and is the difference between four charts and an answer. Use the longitudinal corpus as a control group, since millions of comparable sites experienced the same update and the ones that did not change anything are the natural control, which is the vendor's unique asset and the fix note's subject. Ingest the customer's own deployment and content changes, which is the most important missing input and the most common actual cause. Detect competitor movement specifically, as a competitor gaining is a different situation from the site losing and the two look identical in a traffic chart. Separate demand from visibility, because a category whose search demand fell is not a ranking problem and is currently diagnosed as one constantly. Produce the explanation in a form that can be presented, with the evidence attached, since the deliverable is a meeting rather than an analysis. Distinguish a recoverable cause from a structural one, which determines whether the response is a fix or a strategy change. Alert on the change when it starts rather than when it is noticed, so the SEO is ahead of the question. Say when the answer is uncertain, which protects the SEO more than a confident wrong story does. And measure diagnostic accuracy over time, since a diagnosis product that is not checked is just a more elaborate correlation.

## Target Customer
In-house SEO teams and their leadership, agencies accountable for client organic performance, and vendors whose products end at a line chart.

## Impact If Built
Tools report state and the SEO is asked to explain change, so they present a narrative with more confidence than they have. Decomposing the change with the corpus as a natural control group is the vendor's unique asset and the difference between four charts and an answer.
