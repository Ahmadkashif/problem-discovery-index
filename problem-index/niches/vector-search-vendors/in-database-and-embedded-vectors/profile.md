# In-Database & Embedded Vectors

**Parent Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in this sub-niche is fighting to be good enough inside the system the developer already runs — and whoever does that takes the market, because the buyer's real alternative is not another vendor, it is not adopting one.

## Profile
**Market Size:** ~$140M US and structurally commoditising
**Share of Parent Industry:** ~12% of category revenue
**Digital Adoption:** High and increasingly default
**Target Buyer:** Application developers and small platform teams
**Automation Potential:** Very High — the whole value is not having to operate anything

## What Makes This a Distinct Niche
Most applications with retrieval have a corpus in the hundreds of thousands rather than the billions. At that scale the index structure barely matters — a mature relational database's vector extension, or an embedded library inside the application process, performs adequately. The buyer's decision is not which vector database but whether to run one at all, and the honest answer is frequently no. That makes this a market where the winner is whoever removes the most operational surface, where transactional consistency with the rest of the application data is worth more than index sophistication, and where a separate system must justify itself against a dependency the developer already trusts and already backs up.

## Current Tools & Gaps
Vector extensions in mature relational databases, embedded vector libraries, and lightweight managed offerings. The gaps: no guidance on when a dedicated system is actually warranted, so the decision is made on marketing; scaling and migration paths are undocumented, so teams either over-provision early or hit a wall late; keeping vectors consistent with the source rows is left to the application and is done wrong routinely; and the embedding step is outside the transaction, which is where most correctness bugs in these deployments originate.

## Problems
- [[niches/vector-search-vendors/in-database-and-embedded-vectors/build|🔨 Build: The Vectors and the Rows That Disagree]]
- [[niches/vector-search-vendors/in-database-and-embedded-vectors/buy|🛒 Buy: Extension and Embedded Database Practice]]
- [[niches/vector-search-vendors/in-database-and-embedded-vectors/fix|🔧 Fix: Nobody Will Say When You Actually Need One]]
