# Pre-Need Trust Fund Reconciliation

**Niche:** [[niches/funeral-homes/pre-need-planning/profile|Pre-Need Planning Providers]]
**Industry:** [[industries/funeral-homes|Funeral Homes]]
**Type:** Fix (Pain Point)
**One-liner:** Funeral homes with pre-need trust funds spend days each quarter reconciling trust balances against contract obligations — a manual process prone to errors that can trigger state regulatory action.
**Tags:** #compliance #automation #tabular-ml #data-integration

## The Problem
In many states, pre-need funeral payments must be deposited into state-regulated trust funds rather than insurance policies. The funeral home is responsible for reconciling trust deposits against outstanding contracts quarterly or annually. A funeral home with 500 active pre-need trust contracts must verify that the trust holds sufficient funds to cover every contract, account for interest earned, track withdrawals for completed funerals, and report the reconciliation to state regulators. This is done in spreadsheets, matching bank statements to contract records line by line. Errors in reconciliation can indicate fund mismanagement — a serious regulatory violation.

## Why It's Still Broken
Pre-need trust accounting is a legacy process designed for paper ledgers. The trust bank provides statements in PDF or paper format. Contract records may be in a different system (or in filing cabinets). Matching them requires manual cross-reference. As the number of active contracts grows, reconciliation becomes exponentially tedious. Funeral homes that acquired other firms inherit their pre-need books — often in different formats — compounding the reconciliation challenge.

## What a Fix Looks Like
An automated reconciliation tool that imports trust bank statements (via bank feeds or PDF parsing), matches deposits and interest to specific contracts, flags discrepancies (missing deposits, unexplained withdrawals, contracts with no corresponding trust balance), and generates state-compliant reconciliation reports. The system should handle the common complication of merged pre-need books from acquisitions, mapping legacy contracts to current trust accounts.

## Who Feels the Pain
Funeral home owners and bookkeepers who spend 2-5 days per quarter on trust reconciliation, living in fear that a discrepancy will trigger a state audit that reveals a bookkeeping error from years ago.

## Impact If Fixed
Reduces quarterly reconciliation from 2-5 days to 2-4 hours, catches discrepancies before they become regulatory violations, and provides audit-ready reports that satisfy state regulators on demand.
