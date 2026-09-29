# Dedicated Retrieval Infrastructure

**Parent Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in this sub-niche is fighting to hold a required recall and tail latency at the lowest cost per vector at billion scale — and whoever does that takes the account, because the buyer is running the arithmetic against self-hosting and will act on it.

## Profile
**Market Size:** ~$280M US
**Share of Parent Industry:** ~23% of category revenue
**Digital Adoption:** High
**Target Buyer:** Platform and infrastructure teams with large dedicated retrieval workloads
**Automation Potential:** High — parameter selection and placement are both optimisable

## What Makes This a Distinct Niche
At hundreds of millions to billions of vectors, retrieval becomes an infrastructure line with its own budget, its own capacity planning and its own reliability requirements. The buyer is a platform team that can and will run an open index themselves, and does the arithmetic every renewal. What they need is a cost structure that beats their own operations cost, a predictable tail under load and skew, and the ability to hold a recall target rather than to hit a peak number in a benchmark. The competition is partly other vendors and substantially the customer's own engineering team, which is an unusual and disciplining dynamic.

## Current Tools & Gaps
Graph and quantisation-based indexes, sharding and replication, tiered storage, and managed operations. The gaps: no explicit recall-cost frontier for the customer's own data, so operating points are chosen by trial; quantisation's accuracy cost is rarely reported against its memory saving; tail latency under skew and mutation is not characterised; and multi-tenant filtering — the dominant query shape at this scale — interacts badly with approximate search in ways that are not documented.

## Problems
- [[niches/vector-search-vendors/dedicated-retrieval-infrastructure/build|🔨 Build: An Operating Point Chosen by Trial]]
- [[niches/vector-search-vendors/dedicated-retrieval-infrastructure/buy|🛒 Buy: Capacity Planning and Tail Latency Practice]]
- [[niches/vector-search-vendors/dedicated-retrieval-infrastructure/fix|🔧 Fix: Filtered Search That Falls Off a Cliff]]
