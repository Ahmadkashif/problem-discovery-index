# Alerting That Knows the Market

**Niche:** [[niches/crypto-exchanges/market-operations-on-call/profile|Market Operations On Call]]
**Industry:** [[industries/crypto-exchanges|Crypto Exchanges]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The monitoring cannot tell a violent market from a broken system, so it pages for both and the engineer learns to assume the market.
**Tags:** #change-point-detection #gaussian-mixture-models #time-series-forecasting #hidden-markov-models #evaluation-metrics #worker-facing #confidence-intervals #automation
**Contested on:** Every serious competitor in this niche is fighting to page a human only when the market's behaviour is actually a system fault — and whoever separates a violent but ordinary market from a broken exchange makes a permanently staffed function survivable.

## The Problem
Order rate spikes tenfold, latency rises, the withdrawal queue lengthens, spreads widen, a price feed diverges from its peers. Every one of those is a symptom of a system problem and every one is also what a normal violent day looks like in this asset class. The alerting was configured with static thresholds and cannot tell the difference, so it fires during every significant market move — which is exactly when the on-call engineer is least able to absorb noise and most needed for a real fault.

## Why Nobody Has Built This
Monitoring was adopted from general software practice, where the workload is not adversarially volatile, and nobody adapted the model because the thresholds appeared to work in calm periods. Market regime is a trading concept and alerting is an engineering system, and the two teams do not share a model. The noisiest days are the days nobody has time to fix the alerting. And on-call pain is absorbed by individuals.

## What to Build
Condition the alerting on the market. Model market regime explicitly — calm, trending, volatile, dislocated — and evaluate system signals relative to it, which is the core and is what turns an unusable alert stream into an informative one. Predict expected system load from market activity, since order rate following volume is normal and order rate without volume is a fault. Compare against other venues, because a price divergence that every exchange shows is a market event and one only this exchange shows is a bug — the single most decisive check available and one nobody runs automatically. Separate the market-caused symptom from the system-caused symptom in the alert itself, so the page says which it is. Alert on the relationship breaking rather than on the level, as the level is uninformative in this asset class. Model withdrawal and deposit queue behaviour against network conditions, since chain congestion is an external cause that looks identical to an internal one. Suppress the alerts that are known consequences of a detected market event, which removes the storm at the worst moment. Escalate differently for market and system causes, because the responders differ. Give the on-call engineer market context on the page, since they currently open three dashboards to establish it. Measure page precision and on-call load honestly, as an unmeasured rota degrades silently. And design the rota for a market with no quiet hour, which is the part that is a staffing problem rather than a software one.

## Target Customer
Exchange engineering and market operations leadership, the on-call engineers themselves, and observability vendors whose products have no concept of an external regime.

## Impact If Built
Monitoring was adopted from general software practice where workload is not adversarially volatile. Conditioning system signals on market regime — and comparing against other venues — separates the fault from the Tuesday.
