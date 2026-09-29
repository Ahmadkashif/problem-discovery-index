# Alert Quality & Thresholds

**Parent Industry:** [[industries/observability-vendors|Observability Vendors]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor here is fighting to replace thresholds somebody guessed with numbers backtested against the organisation's own incidents — and whoever does that takes the reliability account, because alert fatigue is the most cited operational complaint in the category.

## Profile
**Market Size:** ~$740M US attributable to alerting, anomaly detection and alert management
**Share of Parent Industry:** ~6% of category revenue
**Digital Adoption:** None for quality — alerting is universal and unevaluated
**Target Buyer:** Site reliability and platform teams
**Automation Potential:** Very High — backtesting against incident history requires no new data

## What Makes This a Distinct Niche
Alert thresholds are numbers an engineer guessed when a monitor was created, on services whose normal behaviour nobody characterised, and never revisited as the service changed underneath them. The result is the two failure modes everyone recognises: alerts that fire constantly and get muted, and alerts that never fire and are mistaken for health. No platform reports which alerts have ever led to action. This is a distinct contest because the remedy is unusually well defined — model the metric's real structure and backtest candidate thresholds against the organisation's own incident history — and because the descriptive half needs no modelling at all: an inventory of alerts in four classes would let most teams prune in an afternoon and does not exist in any product.

## Current Tools & Gaps
Threshold and rule-based alerting in every platform, anomaly detection features of varying quality, alert grouping and suppression, and escalation policies. The gaps: no platform reports alert outcomes, so quality is unmeasurable; generic anomaly detection flags every Monday morning because it does not model seasonality, deploy-related step changes or genuinely multi-modal regimes, which makes it worse than a static threshold; thresholds are never backtested against the incidents that actually occurred; coverage gaps — incidents that happened with no alert — are invisible; and alerting on causes rather than symptoms is a design principle the tooling does not encourage.

## Problems
- [[niches/observability-vendors/alert-quality-and-thresholds/build|🔨 Build: A Number Somebody Guessed in 2021]]
- [[niches/observability-vendors/alert-quality-and-thresholds/buy|🛒 Buy: Seasonality and Regime Modelling, Properly Applied]]
- [[niches/observability-vendors/alert-quality-and-thresholds/fix|🔧 Fix: The Alert Inventory Nobody Has]]
