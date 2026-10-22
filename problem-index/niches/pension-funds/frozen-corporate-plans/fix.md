# Missing Participants Found Only When the Insurer Asks

**Niche:** [[niches/pension-funds/frozen-corporate-plans/profile|Mid-Size Corporate Sponsors With Frozen Plans]]
**Industry:** [[industries/pension-funds|Pension Funds]]
**Type:** Fix (Pain Point)
**One-liner:** Deferred vested participants who left the company decades ago have stale addresses, and the sponsor discovers how many when the insurer's diligence questions arrive.
**Tags:** #k-nearest-neighbors #logistic-regression #data-integration #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to get a frozen plan's participant data, benefit definitions and assets clean enough for a lump-sum window or an annuity buy-out, and whoever brings a plan to insurer bids with the narrowest data-uncertainty loading in the premium takes the account.

## The Problem
A frozen plan may have more deferred members than retirees, many of whom left in the 1990s. Mail is returned, some members have died, and some beneficiaries were never recorded. The DOL treats missing participants as a fiduciary issue. Insurers price them as uncertainty.

## Why It's Still Broken
Searches are bought as one-off projects before a lump-sum window or transaction. Between projects nobody refreshes the records, so the backlog rebuilds.

## What a Fix Looks Like
An annual refresh: address and death searches on all deferred members, scored record linkage against licensed data, and outreach to members whose contact details changed. Results feed the plan's census, and confirmed deaths stop future liabilities from being priced.

## Who Feels the Pain
Benefits managers at sponsors; actuaries valuing liabilities for people who may be dead; members who never receive their benefit.

## Impact If Fixed
The plan enters any transaction with a current census. Members are found while they can still claim, and the premium loading for unknown status falls.
