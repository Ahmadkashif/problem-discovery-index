# History: Online Marketplaces

**Industry:** [[industries/online-marketplaces|Online Marketplaces]]
**Primary Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**Secondary Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**Origin Parent:** [[origins/online-travel-agencies/profile|Online Travel Agencies]]
**Episode Tier:** 1
**Transferable Pattern:** A matching engine that aggregates identical units and a matching engine that aggregates unique units are different products wearing the same interface — and most of the money gets made solving the first while most of the pain sits in the second.

## Before the Listing

A seller with something to sell and a buyer with money to spend found each other through channels that were local, slow, or both: a classified ad in a newspaper, a swap meet, a specialist auction house, a dealer's showroom, a rolodex of known contacts. Distribution — getting the item in front of anyone at all — was the binding constraint, and it scaled with how much you could afford to advertise, not with how good the item was.

Trust was solved the same way distribution was: locally, through reputation that did not travel. A buyer at a swap meet could see the seller's face. A buyer answering a newspaper ad could not, and had almost no protection if the transaction went wrong. This is the condition [[origins/online-travel-agencies/profile|Online Travel Agencies]] describes one layer up, for a narrower kind of inventory — a retail layer sitting between a traveller and a supplier the traveller could not otherwise reach at a fair price. Marketplaces generalise the same problem to every category of good a person might want to buy from a stranger.

## The Origin Event — a cluster, not a moment

Three dated events, eighteen months apart, define three structurally different answers to the same problem.

**September 3 1995.** Pierre Omidyar launches **AuctionWeb** — renamed **eBay** in September 1997 — as a side project. Its first recorded sale was a broken laser pointer for $14.83; when Omidyar queried the winning bidder about the item's condition, the buyer replied that he collected broken laser pointers. The detail is trivial. The mechanism underneath it is not: eBay solved stranger-to-stranger trust with a **feedback and reputation system** that travelled with the seller across every future transaction, making a rating computed once usable everywhere, for anything, for the first time.

**1995**, the same year, **Craigslist** (Craig Newmark) digitised the classified ad directly, with none of eBay's auction mechanics — free listings, no reputation system, no escrow, matching left almost entirely to the two parties' own judgement. It is worth naming as a second, deliberately minimal answer to the same problem, because its persistence for three decades on essentially unchanged infrastructure argues that a marketplace does not need to solve trust computationally to survive — it can also just externalise the risk onto the user and stay out of the way.

**November 6 2000.** **Amazon Marketplace** launches, letting third-party sellers list against Amazon's own product pages. This followed a public failure worth recording rather than skipping: Amazon had tried to beat eBay directly with **Amazon Auctions** (1999) and then **zShops** (1999), and neither displaced eBay's auction-based peer-to-peer model. Marketplace won by refusing the fight on eBay's terms. Instead of a unique listing per seller, Amazon matched multiple sellers' offers of the *same* product to a *single* catalogue page and let algorithmic rules decide who gets the **Buy Box** — the default "Add to Cart" seller. *(I could not independently re-verify the 1999 Auctions/zShops dates this session against a primary source; treat them as approximate and confirm before quoting precisely.)*

**June 18 2005.** **Etsy** (Robert Kalin, Chris Maguire, Haim Schoppik, Jared Tarbell) launches as a marketplace exclusively for handmade and vintage goods — a return to eBay's one-of-a-kind listing model, deliberately narrowed to a category where fungibility was structurally impossible.

Four models, one problem. That plurality is itself the finding: there is no single correct architecture for a marketplace, because "marketplace" describes at least two different mechanisms wearing one word.

## What Became Cheap

**Reaching a buyer beyond your own geography or social network.** Before 1995, the cost of finding a customer for a used bicycle or a specialty ceramic bowl fell entirely on the seller — a classified ad bought by the week, a table rented at a fair. After 1995, listing became free or near-free at the margin, exactly as [[series/eras/wave-05-commercial-web|Wave 5]] made distribution cheap across every category it touched.

What did **not** become cheap, and this is the whole story: **discovery** — the buyer finding the *right* listing among millions of others, and the platform knowing which listing to show which buyer. Distribution answers "can this be found." Discovery answers "will this be found by someone who wants it," and that second question turned out to be a much harder computational problem than the first.

## How It Was Actually Solved — and where it wasn't

Amazon's Buy Box is the cleanest instance of the discovery problem being solved, and it is worth stating precisely why it worked: **when every seller is offering the identical SKU**, ranking sellers against each other reduces to a small, well-behaved optimisation over price, shipping speed, and seller reliability metrics. It is a search problem with almost no ambiguity in what "the same item" means, because the catalogue page defines sameness for you.

eBay and Etsy do not get this simplification, because their core inventory is **unique by construction** — a single vintage coat, a single handmade ring, a single collectible. There is no canonical catalogue page to match a listing against, because there is no second unit of the same thing. Search has to work on descriptions written by amateurs, against a taxonomy someone else designed, for items that have never been sold before and may never be sold again. This vault's own hub note for the industry states the consequence directly: matching "works when a thousand sellers offer the same product and breaks when every listing is one of a kind — which is precisely the inventory marketplaces exist to serve."

**Reputation was solved once, in 1995, and has needed comparatively little re-invention since.** Discovery for fungible goods was solved by 2000, by refusing to treat listings as unique. Discovery for unique goods remains, thirty years on, the unsolved problem underneath a mature, well-funded, extensively engineered transactional layer — a split this vault's own tech-landscape note describes without naming its age: "mature transactional layer, primitive matching."

## The Contest

**eBay versus Amazon, on the specific question of what a listing is.** eBay bet the unit of the marketplace was the unique item, individually described, individually bid on. Amazon bet the unit was the SKU, with sellers competing underneath a catalogue page they did not control. Amazon's model won the larger share of e-commerce gross merchandise value — third-party sales reached roughly **54% of paid units on Amazon by 2020** — but it did not make eBay's model obsolete. It made clear that the two were never actually competing for the same inventory. Fungible commodity goods flowed to the catalogue-page model; one-of-a-kind and long-tail goods stayed with the listing-based model, and a new generation of vertical marketplaces (Etsy in 2005, and later Poshmark, Reverb, StockX, Faire) built specifically around that second category, where Amazon's mechanism cannot function at all.

## What's Still Open

The vault's own problem notes for this industry sit exactly on the seam this file has been describing:

- [[problems/online-marketplaces/high-impact|🔴 Liquidity for Unique Inventory]] — the Buy Box has no answer for this, structurally, and thirty years of search engineering has not closed the gap
- [[problems/online-marketplaces/low-impact-1|🟡 Category Taxonomy and Search Relevance]] — search built for described-once, amateur-written listings
- [[problems/online-marketplaces/low-impact-2|🟡 Seller Onboarding and Listing Quality]] — new sellers write their worst listings during the exact window that decides whether they stay
- [[niches/online-marketplaces/unique-item-discovery/profile|Unique Item Discovery]] and [[niches/online-marketplaces/liquidity-engineering/profile|Liquidity Engineering]] — the two niches built directly around the unresolved half of the problem
- [[niches/online-marketplaces/unmet-demand-intelligence/profile|Unmet Demand Intelligence]] — the vault's own analysis notes that every failed search and every unsold listing is a direct, currently unused measurement of exactly where matching is failing

## The Transferable Pattern

> **Ask what "the same item" means before building the ranking system. If two listings can be exactly the same thing, aggregate them and rank sellers underneath a shared page — the Amazon answer. If no two listings can ever be the same thing, ranking sellers is the wrong problem; the actual problem is ranking a search query against a description written by someone with no incentive to write it well — the eBay and Etsy answer, and the one nobody has solved.**

An FDE walking into any two-sided marketplace should establish, before anything else, which of these two worlds the inventory belongs to. Commodity-goods marketplaces have spent two decades optimising an already-solved shape. Unique-inventory marketplaces are still solving 1995's problem with 2026's tools, and that gap is where the vault's own high-impact note, and the niches built around it, actually live.

**Sources:** Wikipedia, *eBay*, *Etsy*, *Amazon Marketplace*, *Fulfillment by Amazon* (via direct article retrieval, Sept 2026); company-reported third-party seller share statistics cited in the Amazon Marketplace Wikipedia article (54% of paid units, 2020); this vault's `industries/online-marketplaces.md` and `origins/online-travel-agencies/legacy.md`.
