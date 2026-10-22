# A Market-Level Holdover Forecast With the Buyer's Track Record

**Niche:** [[niches/movie-theaters/showtime-and-screen-allocation/profile|Showtime & Screen Allocation]]
**Industry:** [[industries/movie-theaters|Movie Theaters]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Buyers forecast next week from last weekend and memory; nothing forecasts it from each theatre's own history and grades the buyer's overrides.
**Tags:** #tacit-knowledge-ml #gradient-boosting #bayesian-inference #time-series-forecasting #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to forecast each film's next-week demand by theatre and daypart well enough to set screens and showtimes before the mid-week publishing deadline, and whoever gets the holdover calls right most often takes the account.

## The Problem
The holdover call depends on how a film will hold in this town, not nationally. A senior buyer knows that family films hold here and horror collapses there. A junior buyer or an agent covering forty towns applies the national trend and the last weekend.

## Why Nobody Has Built This
Circuits with the data keep it in-house; ticketing vendors haven't built forecasting into scheduling; and the buyer's own expectations, which would let a model learn where their local read beats the trend, are never recorded.

## What to Build
A hierarchical forecast of next-week admissions by theatre, film and daypart, trained on years of point-of-sale history and refreshed with presales. Each Sunday night it proposes holdovers and showtime counts with expected net margin. It records the buyer's one-line expectation per call and grades it the following week, so the buyer's market knowledge becomes a scored, transferable record.

## Target Customer
Directors of programming at circuits of 10–60 theatres; booking agencies serving many independents.

## Impact If Built
Better holdover timing keeps cheap late weeks the theatre would have dropped and frees screens from fading films sooner, a margin gain of perhaps ~1–2% of admissions (estimate), and a retiring buyer's read stays with the circuit.
