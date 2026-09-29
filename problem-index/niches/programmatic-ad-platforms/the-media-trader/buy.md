# Portfolio Trading Practice

**Niche:** [[niches/programmatic-ad-platforms/the-media-trader/profile|The Media Trader]]
**Industry:** [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Financial trading desks automated execution decades ago so traders could work on strategy, and media traders are still executing by hand.
**Tags:** #convex-optimization #time-series-forecasting #automation #evaluation-metrics #workflow-orchestration #confidence-intervals #worker-facing #optimization-fundamentals
**Contested on:** Every serious competitor in this niche is fighting to take the slider-dragging off the trader so they can do the judgement work they were hired for — and whoever does that changes what a trading desk is worth.

## The Problem
Execution in financial markets is automated. Algorithmic execution splits a large order across time and venues against a benchmark, order management systems handle allocation and compliance, transaction cost analysis measures how well execution performed, and the human trader supervises, handles exceptions and decides strategy. The separation between execution and decision is complete and has been for decades. Media trading, which is structurally the same job with the same name, executes manually.

## What Already Exists
Algorithmic execution strategies against stated benchmarks; order and execution management systems; transaction cost analysis; automated allocation across venues; and exception-based supervision workflows.

## The Customization Gap
The adaptation is from a fungible instrument on regulated venues to heterogeneous inventory across proprietary platforms. It requires: (1) execution across vendor platforms with no common protocol, since there is no equivalent of an exchange connection and each platform exposes a different interface — this integration problem is the practical barrier and the reason the pattern has not transferred; (2) an objective that is a delivery-and-outcome trade-off rather than a price benchmark, since there is no reference price for an impression and the benchmark must be constructed; (3) inventory that is not fungible, as two impressions are never the same instrument, which breaks the substitutability every execution algorithm assumes; (4) supervision by someone without a quantitative background, which changes the explanation and control surface entirely; and (5) cost structures suited to agency economics rather than to a trading desk's technology budget.

## Target Customer
Agency trading desks, in-house programmatic teams, demand-side platforms, and execution technology vendors for whom media is an unserved adjacent market.

## Impact If Solved
Finance separated execution from decision decades ago and media never did, despite the same job title. No common protocol across platforms is the practical barrier, and non-fungible inventory breaks the substitutability every execution algorithm assumes.
