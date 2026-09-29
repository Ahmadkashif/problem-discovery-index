# Stock Accuracy & Oversell Prevention

**Parent Industry:** [[industries/dropshipping-suppliers|Dropshipping Suppliers]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in this niche is fighting to know an item is gone before a merchant sells it — and whoever shortens that interval most decides how much of the category's revenue is spent refunding customers.

## Profile
**Market Size:** ~$1.3B US
**Share of Parent Industry:** ~11% of category revenue
**Digital Adoption:** High — polling everywhere, accuracy nowhere
**Target Buyer:** Platform integration engineering
**Automation Potential:** Very High — detection and gating are mechanical

## What Makes This a Distinct Niche
The contest here is latency and reconciliation: how quickly the platform learns that a supplier's stock has changed, and what it does when its own record, the supplier's feed and the observed order outcomes disagree. It is a measurable, closed-loop engineering fight with an unambiguous scoreboard — the oversell rate — and it is entirely separable from whether the resulting listing is any good. A platform that wins this and loses on content still wins the merchants who advertise heavily, because they are the ones an oversell bankrupts.

## Current Tools & Gaps
Scheduled feed polling, stock threshold buffers, manual safety margins set by merchants, and after-the-fact cancellation. The gaps: uniform polling regardless of volatility; no confidence attached to a stock figure; no reconciliation across the three sources of truth; discontinuations detected only as absence; and no gating of advertising spend on stock reliability.

## Problems
- [[niches/dropshipping-suppliers/stock-accuracy-and-oversell/build|🔨 Build: Sold Something That Was Not There]]
- [[niches/dropshipping-suppliers/stock-accuracy-and-oversell/buy|🛒 Buy: Inventory Accuracy Practice]]
- [[niches/dropshipping-suppliers/stock-accuracy-and-oversell/fix|🔧 Fix: The Safety Buffer Everyone Guesses]]
