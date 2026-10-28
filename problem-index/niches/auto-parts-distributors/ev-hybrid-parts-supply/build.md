# A Coverage-Gap Map by Local Parc

**Niche:** [[niches/auto-parts-distributors/ev-hybrid-parts-supply/profile|EV & Hybrid Repair Parts Supply]]
**Industry:** [[industries/auto-parts-distributors|Auto Parts Distributors & Stores]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Distributors don't know which hybrid and EV repairs around each store the aftermarket can already supply, which it can't, and which are about to matter.
**Tags:** #survival-analysis #bayesian-inference #gradient-boosting #feature-engineering #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to supply the parts independent shops need to keep hybrids and EVs out of the dealer, and whoever fills the largest share of hybrid and EV repair-part requests from aftermarket stock takes the account.

## The Problem
A category manager deciding whether to stock remanufactured hybrid packs or inverter pumps in a region has scattered evidence: national sales, supplier pitches, and the odd shop request. The parc is small per store but growing fast, and the failure ages of these parts are poorly known outside the vehicle makers.

## Why Nobody Has Built This
Vehicle-in-operation data, catalog coverage and lookup logs sit in different hands, and lookups that ended "dealer only" are not stored as demand.

## What to Build
A map that joins hybrid and EV counts by ZIP and configuration (licensed VIO) to catalog coverage by part type, flags configurations where the aftermarket has no listing, estimates failure timing from early returns and warranty-expiry dates, and records lookups that ended in "dealer only." Output: per region, the top uncovered repairs, expected demand, and which suppliers could fill them.

## Target Customer
Category managers at chains, warehouse distributors and programme groups; suppliers deciding which EV and hybrid lines to develop.

## Impact If Built
If a distributor filled ~15% more of its hybrid and EV requests from aftermarket stock (estimate) on ~$50M of such requests a year (estimate), it would add ~$7.5M of sales that now go to dealers.
