# Capacity & Utilisation

**Parent Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Category:** High Market Share
**Contested on:** Every serious competitor in this niche is fighting to hold its latency guarantees at the highest achievable utilisation of depreciating hardware — and whoever does that takes the market, because that single ratio is the entire margin.

## Profile
**Market Size:** ~$1.6B US attributable to the capacity decision rather than the serving
**Share of Parent Industry:** ~27% of category revenue
**Digital Adoption:** Low — the gap is managed by judgement
**Target Buyer:** The providers themselves, their finance functions and their investors
**Automation Potential:** Very High — forecasting and allocation are both well-posed

## What Makes This a Distinct Niche
An accelerator bought or leased on a long commitment depreciates whether or not it serves a request. Demand arrives in spikes driven by a customer's product launch, a viral moment, or a batch job somebody scheduled without telling anyone. Overprovision and the margin goes to idle silicon; underprovision and the latency guarantee fails, which is the only thing the customer is buying. Every provider in this market lives or dies on the ratio between provisioned and used, and almost none of them forecast, arbitrate or price against it systematically — the gap is managed by capacity planners' judgement and by absorbing spikes with headroom. This is the industry's defining problem and it is an optimisation problem wearing a procurement costume.

## Current Tools & Gaps
Long-term commitments, reserved instances, spot and preemptible capacity, autoscaling on utilisation, and manual capacity planning. The gaps: no per-customer demand forecasting, though the signal is strong and the data is complete; no arbitrage model across the commitment, reserved and spot tiers despite the spread being where the margin lives; no pricing that reflects the cost of the headroom a guarantee requires; and no measure of the fleet's genuinely necessary size, so nobody knows how much of it is insurance.

## Problems
- [[niches/ai-inference-providers/capacity-and-utilisation/build|🔨 Build: The Margin Is the Gap Between Provisioned and Used]]
- [[niches/ai-inference-providers/capacity-and-utilisation/buy|🛒 Buy: Revenue Management and Capacity Markets]]
- [[niches/ai-inference-providers/capacity-and-utilisation/fix|🔧 Fix: The Spike Nobody Was Told About]]
