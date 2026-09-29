# The Spike Nobody Was Told About

**Niche:** [[niches/ai-inference-providers/capacity-and-utilisation/profile|Capacity & Utilisation]]
**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Type:** Fix (Pain Point)
**One-liner:** Customers launch products, run viral campaigns and schedule enormous batch jobs without telling their inference provider, and the provider absorbs the consequence with headroom nobody is paid for.
**Tags:** #time-series-forecasting #change-point-detection #confidence-intervals #revenue-impact #descriptive-statistics #evaluation-metrics #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to hold its latency guarantees at the highest achievable utilisation of depreciating hardware — and whoever does that takes the market, because that single ratio is the entire margin.

## The Problem
A customer ships a feature on Tuesday morning and their request volume goes up eleven-fold within an hour. Another schedules a hundred-million-document embedding job to start at midnight. Neither told anyone, because no channel exists and nothing in the relationship suggested it would matter. The provider's fleet absorbs both, degrading every other tenant or burning emergency on-demand capacity at a loss. The information that would have made both events trivial to handle existed on the customer's side days in advance, and nothing asked for it.

## Why It's Still Broken
Self-service is the category's product promise, and asking customers to forecast feels like a step backwards from it. There is no incentive for a customer to disclose, since they pay the same either way and disclosure sounds like an invitation to be throttled. Account teams learn about launches socially and irregularly, and nothing routes that into capacity planning. And absorbing the spike is treated as the service working, which is exactly the framing that keeps it unpriced.

## What a Fix Looks Like
Make disclosure worth something. Offer a concrete discount for advance notice of a spike, which converts a one-sided absorption into a trade, is trivial to implement, and is the single change most likely to surface the information — a customer with a launch date will happily share it for a rate reduction. Provide a scheduled-capacity product for batch jobs, so a customer with a hundred million documents books a window instead of arriving unannounced, which is better for both parties and is not currently on offer. Detect ramping demand early from the request stream, since the first minutes of a spike are distinguishable from noise and buy time even without disclosure. Route account intelligence into capacity planning systematically, because sales teams frequently know about a launch weeks ahead and nothing connects that to the fleet. Publish what the provider does under contention, so a customer knows whether they are the one being degraded — the current silence makes every capacity event a trust event. Offer an interruptible tier priced accordingly, giving flexible customers a reason to self-identify. And report absorbed spike cost per customer internally, since the cross-subsidy is invisible today and naming it is what makes any of the above fundable.

## Who Feels the Pain
Reliability engineers absorbing unannounced events; the tenants degraded so another's launch succeeds; and the providers whose margin funds a service level nobody is paying for.

## Impact If Fixed
The information exists days ahead on the customer's side and nothing asks for it. A discount for advance notice turns one-sided absorption into a trade, and a scheduled-capacity product removes the batch spikes entirely.
