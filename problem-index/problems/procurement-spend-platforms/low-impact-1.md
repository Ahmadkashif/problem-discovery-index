# Contract Price Compliance at Invoice

**Industry:** [[procurement-spend-platforms|Procurement & Spend Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Three-way match is a solved, universal control that verifies quantity and total, and nobody checks whether the price on the line is the price that was negotiated in the contract.
**Tags:** #large-language-models #bert #transformers #word-embeddings #hypothesis-testing #evaluation-metrics #compliance #revenue-impact

## The Problem
A company negotiates a contract with a supplier: unit prices by item or category, volume tiers, rebates, freight terms, price adjustment mechanisms, payment terms. The negotiation is careful and consumes a category manager's quarter.

Then invoices arrive and are paid. The three-way match verifies that the invoice matches the purchase order and the receipt — quantity received, total billed, correct supplier. It does not verify that the unit price matches the contract, because the contract is a document in a repository and the matching engine has never read it.

So contracted prices erode. A supplier raises a price and the increase flows through. A volume tier is reached and the lower price is never applied. A rebate accrues and is never claimed. Freight is billed that the contract said was included. Each is small per invoice and substantial per year, and it is discovered, if at all, by an outside recovery audit firm that takes a share of what it finds.

That recovery audit industry exists entirely because this control is missing, which is the clearest possible evidence of the gap.

## What Already Exists
Three-way match is standard in every procure-to-pay system and works well for what it checks. Contract lifecycle management systems store agreements and increasingly extract metadata. Invoice capture and OCR is reliable. Catalogue-based purchasing enforces contracted prices at the point of requisition, where it is used. Recovery audit firms perform this analysis retrospectively as a service.

## The Customisation Gap
Catalogue purchasing solves this for catalogue items and covers a minority of spend. Everything bought outside a catalogue — services, projects, non-catalogue materials, anything ordered by email — has no price control at all.

The contract terms are the missing input. Extracting unit prices, tiers, rebate structures, freight terms and adjustment mechanisms from executed agreements into a machine-checkable form is a document task on documents the company already holds, and once done the check at invoice is trivial arithmetic.

Tier and rebate tracking is the piece with the most money attached and the least attention. A volume tier reached in month seven should trigger a price change and frequently does not, and a rebate accrued across a year has to be claimed by someone who remembers it exists.

Cross-customer price benchmarking is the third layer and only the platform can do it: an invoice priced above what comparable enterprises pay the same supplier for the same item is a negotiating fact, not just a compliance exception.

## Impact If Solved
Contract leakage is a well-documented and routinely large share of contracted spend, and an entire recovery audit industry profits from the fact that nobody checks. Enforcing the contract at the invoice converts a retrospective, commission-based recovery into a prevented overpayment.
