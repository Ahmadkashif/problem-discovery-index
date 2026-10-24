# Contract-Vehicle Price Lists Kept in Spreadsheets

**Industry:** [[it-value-added-resellers|IT Distributors & Value-Added Resellers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Quoting tools and catalogue feeds already price IT products; none of them knows which SKUs are on which government or cooperative contract, at what ceiling price, after which modification, so the reseller's contracts desk keeps that in spreadsheets and finds the errors when an order is rejected.
**Tags:** #large-language-models #word-embeddings #k-nearest-neighbors #descriptive-statistics #compliance #data-integration #workflow-orchestration #automation

## The Problem
A reseller selling to government and education holds several contract vehicles at once: a GSA Multiple Award Schedule, a seat on NASA's SEWP (whose sixth generation named 2,115 winners and opens for orders on 1 November 2026), state cooperative contracts such as NASPO ValuePoint, education vehicles such as E&I and cooperative purchasing agreements such as Sourcewell or OMNIA Partners. Each has its own list of awarded SKUs, its own ceiling or discount-off-list price, its own process for adding products (a contract modification that can take weeks), and its own sales-reporting obligation and fee.

The contracts administrator keeps each price list current by hand. When a vendor changes SKUs — Microsoft renaming Copilot offers in October 2026, a server generation reaching end of sale, a switch vendor replacing a bundle — the reseller's quote may contain items that are not yet on the vehicle, or at prices above its ceiling. An agency's contracting office rejects the order, a cooperative flags it in a quarterly report, or an audit years later finds sales that should have been reported. The work is repetitive and the consequence of a slip is a lost order or a compliance finding.

## What Already Exists
Channel CPQ tools (ConnectWise CPQ, QuoteWerks, Kaseya Quote Manager) price from distributor feeds; content syndicators supply product data; GSA's eBuy and Advantage, NASA's SEWP portal and the cooperatives publish catalogues; GovSpend and Deltek GovWin sell bid intelligence; buyer-side procurement suites are mapped under [[niches/procurement-spend-platforms/public-sector-procurement/profile|Public Sector Procurement]].

## The Customisation Gap
The missing layer is a contract-aware catalogue on the reseller's side: every quoted SKU checked against each vehicle's awarded list and ceiling price as of the current modification; vendor SKU changes mapped to the contract line they replace, with a draft modification request when a new SKU must be added; eligibility rules (which agencies, states and schools can order off which vehicle); and sales reporting assembled from invoiced lines in each vehicle's format. Generic CPQ treats a price as a number from a feed; here a price is a legal commitment with an expiry, a ceiling and a reporting duty, and the matching between vendor SKUs and contract lines is the hard part.

## Impact If Solved
A reseller with five vehicles could cut the contracts desk's price-list upkeep by ~half (estimate), quote public-sector deals the same day instead of waiting for a manual compliance check, and reduce orders rejected or modified for off-contract items from an estimated ~3–8% of public-sector orders to under 1% — on a $100M public book, a few million dollars of orders that stop slipping into the next quarter.
