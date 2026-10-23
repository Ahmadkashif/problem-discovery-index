# Every Deal Checked Against Its State's Rules Before Funding

**Niche:** [[niches/franchised-car-dealers/deal-jacket-compliance/profile|Deal-Jacket Compliance Review]]
**Industry:** [[industries/franchised-car-dealers|Franchised Car Dealers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Dealer compliance is audited by sample after the fact; nothing checks every deal jacket against the rules for that state, vehicle and price before it funds.
**Tags:** #large-language-models #transformers #autoencoders #compliance #workflow-orchestration #evaluation-metrics
**Contested on:** Every serious competitor in this niche is fighting to catch a defective deal jacket — a missing add-on consent, a price that doesn't match the total first quoted, an unsigned disclosure — before the contract is funded, and whoever catches the highest share of defective deal jackets before funding takes the account.

## The Problem
A compliance auditor reviews a sample of jackets each month and finds defects weeks after the customer left. Under California's CARS Act a missing optional-product acknowledgement or a used sale under $50,000 without the cancellation notice is a violation on every affected deal, and the store must hold two years of proof.

## Why Nobody Has Built This
Compliance vendors sell training and policies; e-contracting platforms check signatures, not state retail rules; the documents mix e-signed and scanned paper.

## What to Build
Extraction of every document in the jacket, joined to the CRM's first written quote and the deal record, tested against a rule set keyed to state, new or used, price and products, with defects flagged to the business manager before the customer leaves and an anomaly model for unusual deal structures. Evidence packets are retained automatically.

## Target Customer
F&I directors and compliance officers at dealer groups with California stores first, then other states as they legislate.

## Impact If Built
Every deal checked instead of a sample; a group selling ~20,000 deals a year (estimate) that catches defects before funding avoids exposure at up to $2,500 per violation under California's UCL.
