# AI Agents & Platform Opportunities — Crypto Exchanges

**Industry:** [[crypto-exchanges|Crypto Exchanges]]

---

## 1. Screening Accountability Platform
#ai-platform #graph-neural-networks #gradient-boosting #causal-inference #confidence-intervals #evaluation-metrics #compliance #data-integration

**Concept:** A platform that measures the control an exchange's entire compliance posture rests on. It assembles the scarce set of genuinely confirmed outcomes — law enforcement confirmations, subpoena correlations, verified source-of-funds, later confirmations in either direction — into a curated register, then estimates the precision of each vendor score at each operating threshold on the exchange's own population, with the selection bias stated rather than hidden. It re-runs historical screening under proportional, poison and haircut propagation to show how much of the flagged population is an artefact of a taint model nobody chose. It decomposes flag volume by hop distance, separating direct exposure from indirect exposure four hops removed. And it supports graduated responses — documentation request, withdrawal restriction to the originating address, enhanced monitoring — so that a full asset freeze stops being the only available instrument.

**Inputs:** Screening decisions with full vendor score breakdowns and hop distances; analyst dispositions and reasoning; source-of-funds evidence and its verification status; confirmed outcomes from any source; subsequent customer behaviour; multiple vendors' scores on the same addresses where available.

**Outputs / Actions:** Precision intervals per vendor per threshold, with assumptions about the unresolved majority made explicit. Propagation model sensitivity analysis. Hop-distance decomposition of flag volume. Graduated response recommendations. Customer-facing explanations to the extent the law permits, which is considerably further than current convention.

**Why now:** This control freezes lawful customers' assets at an unmeasured rate and the regulatory frame creates no pressure to measure it, so the measurement has to come from inside. Exchanges are also the origin of the attribution data they buy back as a scored feed, which puts them in an unusually strong position to evaluate it.

**Market:** Licensed exchanges, custodians, crypto-native banks and payment firms, and the blockchain analytics vendors themselves, for whom a defensible published precision figure would be a genuine differentiator. The buyer is the chief compliance officer; the argument is that an unmeasured control is not a managed one.

---

## 2. Investigation Agent
#ai-agent #graph-neural-networks #graph-theory #large-language-models #bert #k-means-clustering #worker-facing #compliance

**Concept:** An agent that does the mechanical half of a blockchain investigation. It performs the backward trace automatically, ranking candidate paths from the deposit address to attributed entities rather than requiring an analyst to click hop by hop, and it leaves the graph fully explorable so the analyst can disagree. It classifies the case into a named typology — peel chain, mixer withdrawal structure, chain-hop through a bridge, scam consolidation — at alert time, so the analyst knows what they are looking at before they begin. It drafts the suspicious activity narrative from the structured trace, which is the single largest time saving in the role. And it searches the exchange's own investigation history, so the institution can finally answer whether anyone here has seen this counterparty, this pattern or this customer archetype before.

**Inputs:** Chain transaction graphs; vendor entity attributions; the exchange's own address-to-identity knowledge at deposit and withdrawal; sanctions lists; the corpus of historical investigations with their traces, conclusions and filed narratives.

**Outputs / Actions:** Ranked trace paths with the evidence for each. Typology classification with abstention permitted. Drafted narratives in the required form. Retrieval over prior internal cases. Routing of whatever outcome feedback does arrive — law enforcement responses, subpoena correlations — back to the analysts who filed, since scarce feedback that is delivered is worth far more than abundant feedback that is not.

**Why now:** The graph is public and complete, the typologies are few and recognisable, the narratives are formulaic, and every historical investigation is a labelled example. Analysts are currently spending investigative skill on clicking and composition.

**Market:** Exchanges, custodians, blockchain analytics vendors and financial institutions with crypto exposure. It sells on analyst capacity and on report quality, and its quieter value is that it stops an institution from losing everything its investigators know when they leave.

---

## 3. Market Operations Agent
#ai-agent #change-point-detection #time-series-forecasting #gradient-boosting #large-language-models #evaluation-metrics #workflow-orchestration #worker-facing

**Concept:** An agent for a market that never closes. It learns what normal looks like per asset and per chain instead of applying a global threshold, so ordinary crypto volatility stops generating pages and genuinely unusual movement becomes visible. It monitors chain health semantically — block production, finality lag, mempool depth, reorg depth, validator participation — rather than treating a node as up or down, which is where most chain incidents are visible before customers feel them. It forecasts withdrawal demand from price movement and market events so hot wallet sizing stops being a pure judgement call under a security-versus-service tradeoff. And when it does page someone, it hands them the last three occurrences of this incident type with what was done and what worked.

**Inputs:** Per-asset price, volume and volatility history; order book and liquidity state across venues and pairs; chain-level health telemetry per network; deposit and withdrawal queues; hot and cold wallet balances; historical incidents with their responses and outcomes; chain upgrade schedules.

**Outputs / Actions:** Per-asset anomaly alerts calibrated to that asset's own distribution. Chain health degradation warnings ahead of customer impact. Withdrawal demand forecasts and hot wallet rebalancing recommendations. Triaged pages with retrieved runbooks assembled from incident history. Automatic handling of the transient node issues that need no human at all.

**Why now:** Continuous markets make this function permanently staffed by a small group whose knowledge is not easily handed over, and the alerting that exists cannot distinguish a market event from a defect, so it has been loosened until it barely fires. Both halves of that are fixable with data the exchange already collects.

**Market:** Exchanges, custodians, staking operators, market makers and crypto payment processors. The argument is operational risk in an industry where an error at three in the morning can mean a permanent loss of customer assets, and secondarily the sustainability of a rotation that currently depends on a handful of individuals being reachable indefinitely.
