# Capacity Planning and Tail Latency Practice

**Niche:** [[niches/vector-search-vendors/dedicated-retrieval-infrastructure/profile|Dedicated Retrieval Infrastructure]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Large-scale serving has mature practice for tail latency, hedged requests, load-aware placement and capacity forecasting, and vector systems report averages on a static load test.
**Tags:** #time-series-forecasting #evaluation-metrics #descriptive-statistics #confidence-intervals #convex-optimization #automation #data-integration #change-point-detection
**Contested on:** Every serious competitor in this sub-niche is fighting to hold a required recall and tail latency at the lowest cost per vector at billion scale — and whoever does that takes the account, because the buyer is running the arithmetic against self-hosting and will act on it.

## The Problem
Serving a latency-sensitive workload at scale is a well-developed discipline: the tail is what matters, hedged and tied requests cut it, placement should follow load, capacity is forecast rather than provisioned by guess, and utilisation targets are set against a latency objective rather than against a hardware number. Vector systems report a benchmark p99 on a uniform load and leave the rest to the customer's platform team, who do have this expertise and use it to justify running it themselves.

## What Already Exists
Tail latency mitigation including hedged requests, tied requests and micro-partitioning; load-aware request routing and replica selection; capacity forecasting with seasonality; autoscaling driven by latency objectives; queueing theory results relating utilisation to latency; and chaos and load testing practice for characterising behaviour under stress.

## The Customization Gap
The adaptation is to a query whose cost varies with the data and whose answer is approximate. It requires: (1) hedging that accounts for approximation, since a hedged query to a different replica may return a different result set and the semantics of that need stating rather than hiding — it is workable and nobody has specified it; (2) routing aware of shard content, because a query's cost depends on where it lands in the vector space and uniform round-robin wastes the locality that would make caching effective; (3) capacity models in vectors and queries rather than in instances, which is how this buyer budgets and what no vendor reports; (4) degradation under pressure that trades recall for latency gracefully, which is an option this workload uniquely has and almost nothing exposes — being able to hold latency by spending recall during a spike is a genuinely valuable and unavailable control; and (5) load testing with skewed and mutating workloads, since the static load test is the one condition that never occurs.

## Target Customer
Platform teams running large retrieval workloads, vector vendors competing with those teams, and the serving infrastructure community.

## Impact If Solved
Tail latency practice is mature and unapplied here. Graceful degradation that trades recall for latency during a spike is a control unique to this workload and exposed by nothing.
