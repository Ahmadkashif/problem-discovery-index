# Forecast Accountability Against Retail Sell-Through

**Niche:** [[niches/alterations-tailoring/apparel-trend-forecasting/profile|Apparel Trend Forecasting Services]]
**Industry:** [[industries/alterations-tailoring|Alterations & Tailoring]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A forecasting house publishes thousands of directional calls a year and scores none of them, so its most valuable possible asset — a track record — is the one thing it cannot produce.
**Tags:** #time-series-forecasting #causal-inference #evaluation-metrics #gradient-boosting #feature-engineering #bert #transformers #data-integration #revenue-impact

## The Problem
The product is prediction, and the accuracy of the prediction is never measured. A season's forecast contains hundreds of specific claims — this silhouette rises, this colour family expands, this fabrication moves from premium into mid-market — each of which becomes checkable eighteen months later when the assortment data is in. Nobody checks. Analysts move to the next season, the published forecast becomes archive, and the firm's confidence in its own calls rests on reputation and the persistence of subscriptions rather than on evidence. The commercial cost is direct: a subscriber deciding whether to renew has no way to evaluate the product except by impression, and the firm has no way to argue the case except by citing the calls that happened to be memorable.

## Why Nobody Has Built This
Forecasts are written as editorial prose and imagery, not as scoreable claims, and prose is where the ambiguity hides — a call phrased as "a softer, more relaxed shoulder gains traction" cannot be marked right or wrong, which is partly why it is phrased that way. Making calls scoreable means committing to specificity, and specificity creates the possibility of being visibly wrong, which the editorial culture has organized itself to avoid. There is also a genuine measurement problem: the firm's own retail scraping shows what got made and merchandised, not what sold, so proving a call correct requires sell-through data the firm does not hold and would have to acquire or trade for.

## What to Build
An engine that turns published forecasts into a structured claim register and scores it. At publication, each directional call is recorded as a claim with a defined subject — attribute, category, market, price tier — a direction, a magnitude band, and a horizon. As assortment scrapes and, where obtainable, sell-through and pricing data accumulate, the claim resolves automatically against a stated measurement rule fixed at publication rather than argued afterward. The register then supports what the firm currently cannot do at all: report calibration by attribute type, category, market, and analyst; identify where the house is systematically early or late, which is the most actionable finding a forecasting operation can have about itself; and feed resolved history back as an input to the next season's calls, so the process compounds rather than resetting annually. Scoring is internal by default — the point is to make the operation self-correcting, with selective external disclosure as a commercial decision rather than an obligation.

## Target Customer
Heads of content and chief product officers at trend forecasting services running 100-400 analysts, and the merchandising and buying directors at subscriber brands who currently have no basis for evaluating a forecast except whether it sounded plausible.

## Impact If Built
Creates the single asset a forecasting business should have and does not: a measured track record. That changes renewal conversations from taste to evidence, and it changes the internal conversation more — analysts learn which of their instincts are reliable, and the house learns where its process is structurally biased. The claim register is also a genuinely proprietary dataset, since it can only be built by the party that made the calls, and it is exactly the thing a new entrant with better scraping technology cannot replicate.
