# Cache Configuration

**Parent Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Category:** High Market Share
**Contested on:** Every serious competitor in this niche is fighting to derive what is genuinely cacheable from the traffic rather than from a rule somebody wrote in 2019 — and whoever does that takes the account, because caching decisions determine both performance and origin cost and are the category's oldest unsolved problem.

## Profile
**Market Size:** ~$1.6B US attributable to caching configuration, optimisation and origin offload
**Share of Parent Industry:** ~18% of category revenue
**Digital Adoption:** Low — configuration is manual and rule sets accumulate
**Target Buyer:** Platform engineering and whoever owns the CDN configuration
**Automation Potential:** Very High — the traffic that answers every question flows past continuously

## What Makes This a Distinct Niche
What to cache, for how long, keyed on what, and when to invalidate are the decisions that determine both how fast a site is and how much origin capacity it needs. They are made once, by hand, in a rule set that then accumulates for years as exceptions are added and nothing is removed. Meanwhile the traffic that would answer every one of them flows past the provider's network continuously: which responses are actually identical across requests, which vary only by a header nobody keyed on, which are marked uncacheable by an origin default nobody chose, how long each resource genuinely remains valid, and which cache keys are fragmenting the cache into single-use entries. The contest is deriving the configuration from the observed traffic, and the reason it has not happened is that the category sells bandwidth and rule sets rather than decisions.

## Current Tools & Gaps
Rule engines with increasingly expressive configuration languages, cache hit ratio reporting, purge mechanisms, and origin shielding. The gaps: hit ratio is reported as a single number for the whole property, which conceals that a small set of resources accounts for most of the misses; nothing identifies what could be cached and is not, which is the actionable question; cache key fragmentation — a key including a parameter that varies per user — is a common and invisible cause of poor hit rates; time-to-live values are chosen by convention rather than derived from how long content actually remains unchanged; and the rule set has no lifecycle, so it only grows.

## Problems
- [[niches/edge-cdn-providers/cache-configuration/build|🔨 Build: Rules Written Once While the Answer Flows Past]]
- [[niches/edge-cdn-providers/cache-configuration/buy|🛒 Buy: Cache Analysis Is a Solved Discipline]]
- [[niches/edge-cdn-providers/cache-configuration/fix|🔧 Fix: One Hit Ratio for the Whole Property]]
