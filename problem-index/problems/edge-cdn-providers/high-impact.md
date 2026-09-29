# Cache Configuration Decided by Rules Nobody Revisits

**Industry:** [[edge-cdn-providers|Edge & CDN Providers]]
**Type:** High Impact
**One-liner:** What to cache, for how long, keyed on what — the decisions that determine both performance and origin cost — are made once in a rule set that then accumulates for years, while the traffic that would answer them flows past every second.
**Tags:** #gradient-boosting #time-series-forecasting #k-means-clustering #causal-inference #confidence-intervals #hypothesis-testing #feature-engineering #evaluation-metrics

## The Problem
A CDN's value is determined by its cache hit ratio, and the hit ratio is determined by configuration: which responses are cacheable, for how long, keyed on which request attributes, and when they are invalidated.

Those decisions are made by a solutions engineer during onboarding, encoded in rules, and left. Over years the rule set grows as exceptions are added for specific paths, specific customers, specific incidents. Nobody removes anything, because removing a rule requires knowing why it was added and the person who added it has gone.

The result is systematically conservative. Content that is genuinely static is cached for an hour because someone was cautious. Cache keys include headers or query parameters that do not affect the response, which fragments the cache and multiplies misses. Vary headers are set broadly. Personalisation is assumed where it does not exist. Purges are issued site-wide because targeted invalidation is harder to reason about.

Every one of these decisions is measurable from the traffic. The provider sees which responses actually vary by which request attributes, which content actually changes and how often, and what the hit ratio would be under a different key. It computes hit ratio as a metric and never as a function of the configuration that produced it.

## Why It's Unsolved
The failure modes are asymmetric and one of them is severe. Caching something that should not be cached can serve one user's personalised or authenticated response to another, which is a security incident. Not caching something merely costs money and latency. Faced with that asymmetry every engineer chooses caution, permanently, and no vendor has offered evidence that would justify anything else.

The provider also does not know what the content means. Whether a response is personalised, or contains anything sensitive, is a property of the customer's application that the CDN can only infer from response characteristics — which is exactly the inference nobody has been willing to make automatically.

Rule sets are also load-bearing and undocumented. A rule added during a past incident may be preventing a recurrence nobody remembers, so touching it feels dangerous even when the traffic suggests it is inert.

And the incentive is mildly wrong: origin requests are the customer's cost, and cache misses generate delivery volume the provider bills for.

## What a Solution Looks Like
Cacheability inferred from observed response behaviour. Whether a response actually varies by a header, a cookie or a query parameter is directly measurable across the traffic, and a key that includes an attribute the response never varies on is pure fragmentation with a computable cost.

Content change frequency measured rather than assumed. The correct time-to-live for a resource is a function of how often it actually changes, which the provider observes, and setting it from evidence rather than from caution is the largest single hit ratio improvement available to most customers.

Safety established rather than assumed in either direction. Responses that vary by an authentication credential, contain personal data patterns, or differ between clients for the same key are exactly what must never be cached, and detecting them is a classification problem the provider is uniquely positioned to run — with a bias that is explicitly conservative.

Rule set analysis: which rules have matched traffic in the last ninety days, which are dead, and which overlap or contradict.

And counterfactual measurement, so a configuration change is evaluated on what it did to hit ratio, origin load and real user latency rather than on whether it felt safer.

## Impact If Solved
Cache configuration determines the value the customer receives and the origin cost they pay, and it is set once by a cautious engineer and never revisited. Inferring cacheability and change frequency from observed traffic is available only to the party carrying the traffic, and the safety classification is what makes acting on it defensible.
