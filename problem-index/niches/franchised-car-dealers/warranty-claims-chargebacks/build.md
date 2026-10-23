# A Claim Checked Against the Policy Manual Before It Leaves

**Niche:** [[niches/franchised-car-dealers/warranty-claims-chargebacks/profile|Warranty Claims & Chargeback Defense]]
**Industry:** [[industries/franchised-car-dealers|Franchised Car Dealers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Claims are edited by the OEM after submission; nothing on the dealer's side applies the same rules first.
**Tags:** #bert #transformers #gradient-boosting #evaluation-metrics #compliance #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to get each warranty repair paid on first submission and kept through the OEM's audit window, and whoever posts the lowest share of warranty dollars rejected or charged back takes the account.

## The Problem
The administrator finds out a claim was wrong when the OEM rejects it or, months later, when an auditor charges it back. The causes are predictable — a story that doesn't show the diagnosis, labour above the guide without authorisation, no photo, part not retained — but each OEM's rules differ and change by bulletin.

## Why Nobody Has Built This
DMS vendors transmit claims for every brand and avoid encoding each OEM's rules; OEMs have no reason to help dealers pass their own edits.

## What to Build
A pre-submission layer with an OEM rule library (labour time limits, prior-authorisation thresholds, retention and photo rules), a story classifier that checks the complaint-cause-correction text against the operation code, and a rejection and chargeback risk score trained on the store's own claim history, with prompts sent to the technician before the car leaves.

## Target Customer
Fixed ops directors at multi-store groups with one administrator per store.

## Impact If Built
Fewer resubmissions and chargebacks; cutting rejected-plus-charged-back dollars by a third on ~$1M a year of warranty labour and parts per store (estimate) keeps tens of thousands a year.
