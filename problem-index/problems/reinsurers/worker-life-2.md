# The Technical Accountant Chasing Ceded Balances

**Industry:** [[reinsurers|Reinsurers]]
**Type:** Worker Life Changing
**One-liner:** A reinsurance technical accountant spends each quarter reconciling cedents' statements of account, reinstatement premiums and cash calls against contract terms by hand, then chasing the differences by email before the balances age into penalties.
**Tags:** #large-language-models #k-nearest-neighbors #feature-engineering #descriptive-statistics #worker-facing #automation #workflow-orchestration

## The Problem
Every treaty generates accounts. Cedents send quarterly statements of account, often as spreadsheets or PDFs in their own layout, showing premium, commission, losses paid, reserves, reinstatement premiums and the net balance. Large losses bring cash calls outside the quarterly cycle. The technical accountant checks each statement against the contract: the cedent share, the commission scale, whether the losses fall inside the treaty's period and terms, and whether reinstatement premium is calculated on the right basis. They then book it, agree differences with the cedent or broker, and track collateral where the reinsurer posts it, through Reg 114 trusts, letters of credit or funds withheld. A technical accountant may own hundreds of contracts across dozens of cedents (estimate).

Differences are routine and small, and resolving them is slow. A misapplied commission, a loss booked to the wrong underwriting year, or a reinstatement calculated on paid rather than incurred loss turns into an email thread through a broker. Meanwhile the balance ages. On the cedent's side, Schedule F has since the early 1990s charged surplus 20% of paid-loss reinsurance recoverables more than 90 days overdue, so both parties are under pressure to clear disputes before the quarter-end.

## Why It Matters to the Worker
The work is detailed, repetitive and invisible until it goes wrong. Quarter-ends and the post-event cash-call wave bring the same compressed weeks every time, and the accountant is judged on aged balances they cannot clear alone, because every difference needs a reply from someone else. The skill that makes them valuable, knowing how each cedent's statements are usually wrong, is spent on spotting the same errors again rather than fixing why they recur.

## What a Solution Looks Like
Statements of account read automatically into a standard structure and checked against the contract terms held in the administration system. Each difference is labelled by type (share, commission, period, reinstatement basis, currency), with the contract clause and the expected figure attached. Draft queries go to the broker or cedent with the evidence. Each cedent's recurring error pattern is visible, so the accountant can fix it at source with the cedent's own team rather than query it every quarter.

## Impact If Solved
Most quarter-end reconciliation becomes review rather than recomputation, saving an estimated ~1–2 days per accountant per quarter-end and per major event (estimate). Aged balances fall before they reach the 90-day line, and the accountant gets back the part of the job that requires judgement: disputed losses and collateral.
