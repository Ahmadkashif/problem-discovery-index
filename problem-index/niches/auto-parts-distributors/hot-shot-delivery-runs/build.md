# Run Consolidation That Knows Shops Reorder

**Niche:** [[niches/auto-parts-distributors/hot-shot-delivery-runs/profile|Hot-Shot Delivery Runs]]
**Industry:** [[industries/auto-parts-distributors|Auto Parts Distributors & Stores]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A shop that orders brake pads at 9:02 orders the rotors at 9:09; a dispatcher that knew that would send one run instead of two, and keep a driver free for the order that would otherwise arrive too late.
**Tags:** #markov-decision-processes #dynamic-programming #time-series-forecasting #optimization-fundamentals #automation #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to get each shop order from the nearest stock to the bay, and whoever loses the fewest shop orders to cancellation because the part arrived after the shop's window takes the account.

## The Problem
Stores dispatch each order as it is picked, because the window starts at the call. Shops order in bursts as technicians tear a car down, so the same street sees three runs in twenty minutes while another shop's order sits on the counter with no driver free; that is the order that arrives after the window and gets cancelled.

## Why Nobody Has Built This
Generic routing tools optimise known stops; they don't forecast the next order from a specific shop, and store systems don't expose order streams to dispatch tools in real time.

## What to Build
A dispatcher whose objective is the fewest orders arriving after the shop's window. It learns each shop's real window from its cancellations and complaints, forecasts each shop's next-order probability from its ordering pattern, the repair it is working (from the parts already ordered) and time of day, and solves a hold-or-go decision for every waiting order: hold a run only when every order on it still lands in time, batch by direction to free drivers, and add core pickups only where they cost no window. Every decision is logged with its outcome (delivered in window, late, cancelled), so the policy learns.

## Target Customer
Commercial operations at chains and warehouse distributors; dispatch software vendors serving parts stores.

## Impact If Built
If late cancellations fell from ~4% to ~2% of shop orders (estimate) at a store taking ~150 shop orders a day, it would keep ~3 orders a day, ~$100K+ of sales a year (estimate), with ~15–25% fewer runs as a by-product (estimate).
