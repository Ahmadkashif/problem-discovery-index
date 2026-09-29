# Published Predictions Are Never Scored

**Niche:** [[niches/cloud-infrastructure-consultants/it-research-advisory-firms/profile|IT Research & Advisory Firms]]
**Industry:** [[industries/cloud-infrastructure-consultants|Cloud Infrastructure Consultants]]
**Type:** Fix (Pain Point)
**One-liner:** The firm publishes thousands of dated, checkable predictions a year, the world settles nearly all of them, and no scorecard exists — so a business selling foresight has no evidence about its own.
**Tags:** #evaluation-metrics #time-series-forecasting #hypothesis-testing #confidence-intervals #causal-inference #descriptive-statistics #bert #transformers #data-integration #revenue-impact

## The Problem
Research notes are dense with claims that resolve: market size by a stated year, adoption crossing a threshold, a vendor's trajectory, a technology reaching maturity by a date. Clients make expensive decisions on them. Within a few years most become checkable, and nobody checks. Predictions are published, superseded by the next cycle, and archived. So the firm cannot say which of its analysts, coverage areas, or prediction types are reliable, and cannot answer the question a sceptical procurement officer asks at renewal — how accurate is this, actually. Internally the same absence means analysts get no feedback signal on the only output that distinguishes them from a well-read generalist.

## Why It's Still Broken
Predictions are written as prose, frequently hedged in ways that make resolution ambiguous, and the hedging is not accidental — a claim specific enough to be scored is specific enough to be wrong, and the publishing culture has optimized against that for decades. Resolution also requires ground truth the firm does not always hold, particularly for market sizes it publishes itself, which creates an obvious circularity problem. And the commercial worry is straightforward: a scorecard is a discoverable record of failure in a business whose product is authority. Those pressures have kept the industry's most obvious quality measure unbuilt.

## What a Fix Looks Like
A claim register, built as a by-product of publishing. At publication, each substantive forward-looking claim is recorded with a subject, a direction, a magnitude or threshold, a horizon, and — decisively — the resolution rule agreed at the time rather than argued about afterward. Where ground truth would be the firm's own later estimate, the resolution source is named as external or the claim is marked unscoreable, which is itself an honest and useful category. As horizons pass, claims resolve automatically and accumulate into calibration by analyst, coverage area, claim type, and horizon length. Scoring is internal first: the point is a research organization that learns where it is systematically early, late, or overconfident, which is the most actionable thing a forecasting operation can know about itself. Selective external disclosure becomes a commercial choice made from strength rather than a concession — and in a market where every competitor publishes unscored predictions, being the firm that can show a track record is a genuine differentiator rather than a risk.

## Who Feels the Pain
Analysts who never learn which of their instincts are reliable; research leadership managing quality with no measure of the primary output; sales teams defending renewals on reputation; and clients making capital allocation decisions on forecasts with no accuracy history attached.

## Impact If Fixed
Creates the asset a research business should have and does not. It changes renewal conversations from brand to evidence, it gives the research organization a real feedback loop for the first time, and the claim register itself is proprietary in the strictest sense — only the party that made the predictions can build it, and it accumulates value every year it runs.
