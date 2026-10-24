# One Deal Record From Configurator to Install

**Niche:** [[niches/it-value-added-resellers/datacenter-networking-solution-quoting/profile|Data-Centre & Networking Solution Quoting]]
**Industry:** [[industries/it-value-added-resellers|IT Distributors & Value-Added Resellers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A solution deal's configuration, approved price, shipment, install and claims each live in a different system, so no reseller can say which deals made money and why.
**Tags:** #feature-engineering #gradient-boosting #causal-inference #evaluation-metrics #data-integration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche is fighting to turn a customer's infrastructure requirement into a priced vendor bill of materials that wins, but that splits into two contests with different winners: a configuration that installs as quoted at the customer's site, scored after delivery in change orders and returns, and a price the vendor's deal desk approves at a level that beats the competing reseller, scored at award. Decomposed into contested sub-niches below.

## The Problem
A reseller's finance team knows each solution deal's booked gross profit. It does not know the realised profit after change orders, returns, unbilled site visits and incentive claims that were or weren't paid, and it cannot trace a loss back to its cause: a missing optic, an unapproved discount, a registration that lapsed. The configuration sits in the vendor's tool, the price approval in a portal, the order in the ERP, the install in the PSA, the claim in a spreadsheet.

## Why Nobody Has Built This
Each vendor builds for its own step: configurators for valid configurations, CPQ for the quote, PSA for the project, PRM for the programme. The join requires the reseller's own data, and resellers have treated the quote as a document, not a record.

## What to Build
A deal ledger keyed on the quote: every line from configurator export through approved price, distributor order, serials shipped, install ticket, change order or return, and incentive paid. On top, realised margin per deal and per cause, which feeds both sub-niches' models — the fit checker and the pricing model — with labels.

## Target Customer
VPs of solutions and CFOs at resellers with $100M+ of solution sales and their own pre-sales teams.

## Impact If Built
Seeing realised rather than booked margin typically moves ~1–2 points of gross profit on solution deals once the leading causes are fixed (estimate) — ~$1–2M a year on $100M of solution sales.
