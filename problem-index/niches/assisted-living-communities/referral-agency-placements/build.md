# A First-Contact Ledger Both Sides Accept

**Niche:** [[niches/assisted-living-communities/referral-agency-placements/profile|Referral Agency Placements & Fee Disputes]]
**Industry:** [[industries/assisted-living-communities|Assisted Living Communities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Communities and referral agencies argue over who found a family first because each side trusts only its own records.
**Tags:** #large-language-models #logistic-regression #feature-engineering #data-integration #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to decide which move-ins a referral agency is owed a fee for, and whoever holds the timestamped first-contact record that both the community and the agency accept takes the account.

## The Problem
A move-in lands, an agency invoices a fee of about a month's rent and care, and the sales director believes the family called on its own two weeks earlier. The business office pays rather than fight, or fights and strains a relationship the community needs.

## Why Nobody Has Built This
Each side's system is built to prove its own case. CRMs record a single lead source, often typed in late. Agencies' portals record their referral time. Nobody has built the neutral record, because it needs household-level matching and acceptance by agencies that benefit from ambiguity.

## What to Build
An append-only ledger that captures every contact event the community sees (calls, forms, chats, walk-ins, agency notifications) with system timestamps. Household matching resolves names, phone numbers and addresses, and an LLM reads call transcripts for "who told you about us." For each move-in it produces a first-contact report under each agency's registration rules, shareable with the agency as evidence.

## Target Customer
Revenue cycle and sales leaders at chains paying hundreds of agency fees a year; agencies that want fewer disputes.

## Impact If Built
If ~5–10% of agency fees are paid on families who were already known (estimate), a 30-community chain paying ~300 fees a year at ~$6,000 recovers ~$90,000–180,000 a year, with documented disputes instead of arguments.
