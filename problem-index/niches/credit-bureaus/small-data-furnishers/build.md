# Metro 2 Mapping Inferred From the Ledger

**Niche:** [[niches/credit-bureaus/small-data-furnishers/profile|Small Data Furnishers]]
**Industry:** [[industries/credit-bureaus|Credit Bureaus]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Onboarding a new furnisher means a consultant hand-mapping its ledger fields to Metro 2, and the mapping is never tested against what the ledger actually contains.
**Tags:** #large-language-models #decision-trees #feature-engineering #evaluation-metrics #data-integration #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to turn a small furnisher's loan or rent ledger into an accepted, accurate Metro 2 file every month without a data-reporting specialist, and whoever drives the furnisher's reject and dispute rates lowest takes the account.

## The Problem
A landlord, a small finance company or a credit union starting to report must map its system's fields — payment status, days late, charge-off, payment plan, bankruptcy, co-borrower — to Metro 2 base and segment fields. A consultant or the vendor does it once from a spreadsheet of field names. Edge cases that exist in the ledger but not in the spreadsheet are discovered as rejects or disputes months later.

## Why Nobody Has Built This
Each core and servicing system is different, the market for small-furnisher onboarding is fragmented, and the bureaus fund onboarding only for furnishers large enough to matter to coverage.

## What to Build
A mapping assistant that reads a sample of the furnisher's actual ledger, infers what each status and transaction pattern means, proposes Metro 2 mappings with the CRRG rule cited, generates test files that exercise every account state found, and runs them through bureau-equivalent edits before the first live submission.

## Target Customer
Bureaus' furnisher onboarding teams; rent reporting services and property-management software vendors bringing landlords to the bureaus; credit union service organisations.

## Impact If Built
Onboarding in days rather than weeks (estimate), and new furnishers whose first files are right rather than corrected in the dispute queue.
