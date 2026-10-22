# The Census File Rebuilt by Hand for Every Valuation

**Niche:** [[niches/pension-funds/small-local-public-plans/profile|Small Local Public Plans]]
**Industry:** [[industries/pension-funds|Pension Funds]]
**Type:** Fix (Pain Point)
**One-liner:** Every year the town's finance office assembles member data for the actuary from payroll, personnel files and last year's spreadsheet, and the actuary sends back a list of questions.
**Tags:** #feature-engineering #evaluation-metrics #data-integration #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to run a small board's whole compliance calendar, from census data for the actuary to GASB 67/68 schedules, state filings and investment monitoring, without the plan hiring staff, and whoever keeps the most small plans off the state regulator's late-filing and non-compliance lists takes the account.

## The Problem
The actuarial valuation needs every active member's dates, pay and service, every retiree's benefit and beneficiary, and every change since last year. A small plan has no administration system, so the data is rebuilt from payroll exports and personnel records. The actuary's data questions take weeks of back-and-forth, delaying the valuation and the GASB schedules that depend on it.

## Why It's Still Broken
The town's payroll system was not built to keep pension history, and nobody owns the member record between valuations. Each year starts from last year's spreadsheet.

## What a Fix Looks Like
A persistent member register updated from each payroll run and personnel change, with the year-over-year checks actuaries apply built in: missing dates, pay jumps, status changes without events, retirees without beneficiary data. The census file is exported in the actuary's format with the exceptions already explained.

## Who Feels the Pain
Municipal finance directors and HR staff; the plan's actuary; the employer's auditor waiting on GASB 68 figures.

## Impact If Fixed
Valuation data takes days rather than weeks, the actuary's questions shrink to the real exceptions, and the employer's financial statements stop waiting on the pension plan.
