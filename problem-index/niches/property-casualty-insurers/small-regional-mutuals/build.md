# Credible Indications for a Thin Book

**Niche:** [[niches/property-casualty-insurers/small-regional-mutuals/profile|Small & Regional Mutual Insurers]]
**Industry:** [[industries/property-casualty-insurers|Property & Casualty Insurers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A small mutual's own losses are too few to price on and too local to ignore, and blending them with bureau loss costs is done once a year by a consultant in a spreadsheet.
**Tags:** #bayesian-inference #bayesian-linear-regression #confidence-intervals #monte-carlo-methods #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to give a mutual with no data-science staff a pricing and catastrophe view its regulator and reinsurer will accept, and whoever turns bureau loss costs, cat models and the mutual's own thin experience into a filed rate change before the reinsurance renewal takes the account.

## The Problem
A mutual writing homeowners in twenty counties has a few years of its own experience, a few thousand policies per territory at best (estimate), and catastrophe years that dwarf everything else. Bureau loss costs reflect the state, not its book. Credibility weighting and catastrophe loading decide its rate change, and both are done annually by an outside actuary.

## Why Nobody Has Built This
Enterprise pricing platforms are priced and staffed for carriers with pricing teams. Consulting actuaries sell hours, not software. The mutuals' associations offer education and benchmarking, not indications.

## What to Build
A hosted indication service built for small books. It blends own experience with bureau loss costs using Bayesian credibility, with uncertainty shown honestly. It separates and loads catastrophe experience from modelled or long-term averages, sets the rate change against the reinsurance cost the broker is quoting, and produces filing-ready exhibits in the format of the mutual's state.

## Target Customer
CEOs, CFOs and sole actuaries of small and regional mutuals, and the consulting actuaries who serve several of them.

## Impact If Built
Rate changes timed to need rather than to consultant availability, and indications a board can follow.
