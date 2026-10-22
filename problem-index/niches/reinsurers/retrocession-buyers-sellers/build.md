# A Retro-Ready Portfolio Distribution With Its Uncertainty

**Niche:** [[niches/reinsurers/retrocession-buyers-sellers/profile|Retrocession Buyers & Sellers]]
**Industry:** [[industries/reinsurers|Reinsurers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A retro writer prices a reinsurer's catastrophe portfolio from a summary loss curve without knowing how much of it reflects the buyer's own loads, data quality or unfinished renewals.
**Tags:** #monte-carlo-methods #bayesian-inference #gaussian-processes #evaluation-metrics #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to present a reinsurer's whole treaty portfolio as one loss distribution that a retrocession writer can price without seeing the underlying cedents, and whoever's roll-up the retro panel accepts with the fewest data requests takes the account.

## The Problem
The buyer's roll-up passes each treaty's terms over vendor event sets and produces an exceedance-probability curve. The writer receives the curve and some zone aggregates. It cannot tell how far the buyer's view sits from the vendor's, or how much the portfolio will change by 1 January.

## Why Nobody Has Built This
Retro is a small, relationship-driven market, and buyers have little incentive to disclose more than the curve. Vendors model locations, not books of treaties with their own uncertainty.

## What to Build
A portfolio roll-up that produces the loss distribution with explicit uncertainty bands for unfinished renewals, vendor-model disagreement and the buyer's adjustments. It adds a standard retro submission with aggregates by peril region, and a historical comparison of the buyer's past modelled versus reported event losses that a writer can check.

## Target Customer
Retro buyers at mid-sized reinsurers and portfolio managers at ILS funds writing retro.

## Impact If Built
Faster placements with fewer data requests, and retro priced on the buyer's evidence rather than reputation alone.
