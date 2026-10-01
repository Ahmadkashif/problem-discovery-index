# The Read of the Print Has No Memory

**Niche:** [[niches/sell-side-equity-research/earnings-coverage/profile|Earnings Coverage]]
**Industry:** [[industries/sell-side-equity-research|Sell-Side Equity Research]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Each quarter the analyst reconstructs, from memory, how this management team guides and which number this stock trades on — information the department's own archive already contains.
**Tags:** #tacit-knowledge-ml #gradient-boosting #feature-engineering #causal-inference #evaluation-metrics #large-language-models #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to get a correct read of the print — which number the stock will trade on and whether the beat or miss is real — to clients before the open, and whoever does that best owns the morning call and the vote.

## The Problem
On report morning the analyst has minutes to decide what matters. The decision draws on years of pattern: this company's guide is reliably conservative by a few percent; this stock ignores revenue and trades on subscriber adds; this CFO changes definitions when a metric worsens. That pattern is held by the analyst and nowhere else. A newer analyst, an associate covering for a holiday, or a successor after a departure has none of it and the department's first take is visibly weaker for several quarters.

## Why Nobody Has Built This
The data is fragmented across the estimate archive, transcripts, releases and price history, and the "what it trades on" judgment is never labelled. Vendors sell consensus and transcripts to everyone, so nobody sells the department its own history joined to outcomes. Analysts have little incentive to externalise what makes them hard to replace.

## What to Build
A per-company earnings memory built from the department's own record: guidance versus result by line item and quarter (a guidance-bias profile per management team); the department's estimate versus result history; price reaction on report days regressed on the surprise in each line item, giving an empirical "what it trades on" ranking that updates each quarter; and the department's past first-take emphasis compared with which surprise the price actually followed. Delivered inside the preview template and the first-take draft, with track records attached to every suggestion, so the analyst can overrule it in seconds.

## Target Customer
Directors of research and sector heads at bulge-bracket and mid-tier brokers; independent research providers with earnings coverage.

## Impact If Built
The earnings read becomes a departmental asset rather than a personal one: faster first takes from less experienced staff, a defensible hand-over when an analyst leaves, and a measured answer to which coverage actually anticipates the market's reaction.
