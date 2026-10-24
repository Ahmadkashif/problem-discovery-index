# The Class Forecast Built on Two Spreadsheets

**Niche:** [[niches/colleges-and-universities/enrollment-and-net-tuition-revenue/profile|Enrollment Management & Net Tuition Revenue]]
**Industry:** [[industries/colleges-and-universities|Colleges & Universities]]
**Type:** Fix (Pain Point)
**One-liner:** Admissions forecasts deposits in one spreadsheet, aid forecasts the discount in another, and the two are reconciled by hand every week of April.
**Tags:** #time-series-forecasting #logistic-regression #data-integration #workflow-orchestration #quick-win #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is "every serious competitor is fighting to raise net tuition revenue from the next entering class", but it holds two contests with different winners: filling the funnel with students likely to enroll, won on enrolled students per recruitment dollar, and pricing each admit, won on the discount rate at target class size. Decomposed into contested sub-niches below.

## The Problem
In the weeks before the deposit deadline, the dean of admissions tracks deposits against last year by day. The aid director tracks committed aid against budget. The CFO wants net tuition revenue. Each number lives in a different extract, refreshed at different times, and a Monday meeting spends its first half reconciling them.

## Why It's Still Broken
The CRM, the aid system and the SIS each report on their own records, and the person who could build a shared daily view is usually the same institutional researcher doing IPEDS.

## What a Fix Looks Like
One daily snapshot that joins admits, deposits, awards and appeals; a deposit forecast by aid band calibrated on prior years' daily curves; and a projected class size, discount rate and net tuition revenue with intervals, refreshed overnight.

## Who Feels the Pain
Enrollment VPs, aid directors, CFOs and the institutional researcher pulled into every reconciliation.

## Impact If Fixed
Decisions about the waitlist, late aid and appeals are made on one number the whole cabinet trusts, and the weekly reconciliation that takes ~4–6 staff hours each week from February to May disappears (estimate).
