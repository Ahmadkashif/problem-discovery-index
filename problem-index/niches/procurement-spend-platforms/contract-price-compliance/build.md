# Contracted Prices as Structured Data, Checked at Payment

**Niche:** [[niches/procurement-spend-platforms/contract-price-compliance/profile|Contract Price Compliance]]
**Industry:** [[industries/procurement-spend-platforms|Procurement & Spend Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An organisation negotiates prices, records them in a contract document, and pays invoices verified against a purchase order that nobody checked against the contract.
**Tags:** #bert #large-language-models #transformers #evaluation-metrics #confidence-intervals #data-integration #compliance #revenue-impact
**Contested on:** Every serious competitor in procurement controls is fighting to check the invoiced price against the contracted price at the moment of payment — and whoever closes that gap takes the savings the organisation already negotiated.

## The Problem
A category manager negotiates a price schedule with a distributor: several hundred items at agreed prices, with volume tiers and an annual rebate. The contract is signed and filed. Ordering happens through a catalogue that was loaded at implementation and has drifted, through purchase orders raised from quotes, and through invoices for items not in the catalogue at all. Some proportion of the spend is at the negotiated price. Nobody knows what proportion, because the contract exists as a PDF in a repository and the systems that order and pay have never seen its contents. A recovery audit firm will find some of the difference in two years and keep a third of it.

## Why Nobody Has Built This
Contract lifecycle management systems store contracts as documents with metadata because that is what the legal function needed, and the price schedule — which is frequently an appendix, a spreadsheet or an attachment — was never extracted as structured data. Loading and maintaining prices in the ordering system is manual work that competes with everything else, and it degrades immediately as prices change. And the recovery audit industry provides a safety net that makes the leakage tolerable: the money comes back eventually, minus a share, which removes the urgency to prevent it.

## What to Build
Price schedules extracted into structured terms and enforced at every point money moves. Extraction pulls the price schedule from the contract and its attachments — item identifiers, units, prices, effective dates, tier and volume breaks, indexation clauses, rebate terms — into a structured term set with provenance to the clause. Those terms flow into the catalogue, into purchase order pricing and into invoice validation, so a price that does not match is flagged before payment rather than after. Indexed and tiered prices are computed automatically as volumes and indices move, which is where most manual administration and most error sits. Non-catalogue spend is checked against the contract even when the order did not use it, which is where a large share of the leakage lives. And the standing metric is price compliance rate — the share of spend transacted at the contracted price — which is a number no procurement organisation currently has and which is the honest measure of whether its negotiations are realised.

## Target Customer
Procurement and contract management vendors, finance and internal audit functions, and the recovery audit firms whose methodology this productises.

## Impact If Built
Recovery audit recovers a meaningful share of spend on a contingent basis, which is direct evidence of how large the leakage is and how much of it is preventable. Checking at payment converts a retrospective recovery, shared with a third party, into a prevented overpayment, and the compliance rate gives procurement a measure of realised rather than negotiated savings — which is the number its credibility with finance actually depends on.
