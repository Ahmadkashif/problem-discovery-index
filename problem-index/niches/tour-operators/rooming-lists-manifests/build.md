# Confirmations Read and Compared Automatically

**Niche:** [[niches/tour-operators/rooming-lists-manifests/profile|Rooming Lists, Manifests & Supplier Reconfirmation]]
**Industry:** [[industries/tour-operators|Tour Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Suppliers confirm rooming lists and manifests by email in their own formats and languages, and a coordinator checks every line by eye.
**Tags:** #large-language-models #transformers #seq2seq #evaluation-metrics #automation #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to get every hotel, coach company, restaurant and guide the final names, rooms, numbers and needs without a discrepancy on arrival, and whoever delivers the most departures with zero arrival-day manifest errors takes the account.

## The Problem
A hotel replies to a rooming list with its own reservation printout, a PDF in Italian, or a one-line "confirmed" that hides a twin changed to a double. A coach company returns a manifest with one name missing. Coordinators read each confirmation against what they sent, under deadline, across dozens of departures.

## Why Nobody Has Built This
Before capable document models, extracting structured data from arbitrary supplier formats was not reliable enough to trust. Tour-operations systems generate outgoing documents but treat incoming replies as email.

## What to Build
A service connected to the operations mailbox. It recognises supplier confirmations, extracts every name, room type, date, number and special request in any format or language, and matches them to the departure record. It produces a discrepancy list per departure and supplier, drafts the correction request, and sets the departure's confirmation status. Recall on discrepancies is the binding metric.

## Target Customer
Operations managers at multi-day, group and educational operators, and tour-operations software vendors as a module.

## Impact If Built
Checking time per departure cut sharply and arrival-day surprises largely eliminated (estimate). Coordinators work exceptions instead of reading every line.
