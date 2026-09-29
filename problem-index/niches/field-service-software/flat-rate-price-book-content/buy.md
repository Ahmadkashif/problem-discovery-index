# Cost Data Feeds Wired to the Book

**Niche:** [[niches/field-service-software/flat-rate-price-book-content/profile|Flat-Rate Price Book Content]]
**Industry:** [[industries/field-service-software|Field Service Software]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Supplier pricing, wage data and materials cost indices are all available as feeds, and flat-rate books are updated on a publication cycle that means a contractor's material cost can move ten percent before the price does.
**Tags:** #time-series-forecasting #change-point-detection #descriptive-statistics #evaluation-metrics #confidence-intervals #data-integration #automation #revenue-impact
**Contested on:** Every serious competitor in price book content is fighting to make a task's price right for this trade in this market with this contractor's cost structure — and whoever needs the least customisation on arrival takes the account.

## The Problem
Copper moves. A supplier's price on a common fitting rises fifteen percent. The contractor's book, which embeds a materials cost from whenever it was last built, continues to price the task as though nothing happened, and the margin on every instance of that task quietly erodes. Nobody notices until a periodic review, or until the year's financials disappoint. The contractor's own purchase records show the increase the week it happened.

## What Already Exists
Supplier catalogues and pricing are available through distributor APIs and EDI for the major suppliers in every trade. Producer price indices and materials cost series are published by federal statistical agencies. Wage data by trade and metropolitan area is published. Distributor invoice capture is already performed by accounting integrations in most of these platforms. The feeds exist and the contractor's own invoices are the most accurate feed of all.

## The Customization Gap
The adaptation is to keep a book's cost basis live rather than periodic. It requires: (1) deriving materials cost per task from the contractor's own actual purchase prices, which are in the accounting integration already, rather than from a catalogue list price nobody pays; (2) mapping supplier items to book tasks — the same entity matching problem that appears in restaurant costing, and solvable the same way, with a pooled mapping corpus; (3) labour cost per task computed from the contractor's realised times and loaded labour rate, since the book's assumed time is a standard and the contractor's actual time is the fact; (4) alerting on margin movement rather than on cost movement, because a five percent materials increase on a labour-dominated task is irrelevant and a small one on a materials-dominated task is not; and (5) separating a decision to reprice from the cost update itself, since a contractor may deliberately absorb an increase and should do so knowingly.

## Target Customer
Price book vendors, field service platforms with accounting integrations already in place, and contractors whose margins are eroding for reasons they cannot locate.

## Impact If Solved
A live cost basis turns flat-rate margin from something reviewed annually into something managed, and the inputs are already flowing into the platform for other purposes. Margin-movement alerting is the part that matters: it directs the contractor's attention to the handful of tasks where cost movement actually threatens the price, which is a much shorter list than the book.
