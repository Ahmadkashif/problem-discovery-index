# A TRID-Aware Reconciliation Engine

**Niche:** [[niches/title-and-settlement-offices/closing-disclosure-balancing/profile|Closing Disclosure Balancing & Settlement Statements]]
**Industry:** [[industries/title-and-settlement-offices|Title & Settlement Offices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Balancing the CD is a deterministic reconciliation done by people over email, three or four rounds per file.
**Tags:** #large-language-models #transformers #seq2seq #evaluation-metrics #compliance #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to make the lender's Closing Disclosure and the settlement agent's statement agree to the cent in one round inside TRID's three-business-day window, and whoever eliminates the redisclosure round gets onto the lender's preferred settlement-agent list.

## The Problem
The escrow officer and the lender's closer each believe their numbers. Differences arise from late payoff updates, commission changes, HOA transfer fees, prorations computed to different dates and title premiums disclosed under a different rule from the one invoiced. Each round costs hours and risks the closing date.

## Why Nobody Has Built This
The two documents live in different companies' systems, each vendor assumes its side is the truth, and the rules for which differences matter span TRID, state charges and the title rate manual.

## What to Build
Extract both statements into a common schema, match lines, compute expected values where rules determine them (per-diem to funding date, prorations, transfer-tax splits, simultaneous-issue title premium disclosure), and classify each difference: immaterial, correct the lender's side, correct the agent's side, tolerance cure, or redisclosure trigger. Send the lender one annotated list and log every change.

## Target Customer
Escrow departments at agencies with heavy lender-channel volume; lender closing departments.

## Impact If Built
Balancing in one round, fewer delayed closings from redisclosure, and an audit trail both sides can rely on.
