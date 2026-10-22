# The Annual Review Tickler in a Spreadsheet

**Niche:** [[niches/community-banks/the-commercial-credit-analyst/profile|The Commercial Credit Analyst]]
**Industry:** [[industries/community-banks|Community Banks]]
**Type:** Fix (Pain Point)
**One-liner:** Which borrowers owe financial statements, which annual reviews are overdue and which covenants were never tested sits in an analyst's spreadsheet, and loan review finds the gaps before the bank does.
**Tags:** #large-language-models #workflow-orchestration #quick-win #compliance #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to get an analyst from a borrower's raw returns to a credit memo the chief credit officer trusts in hours rather than days, and whoever makes every number traceable to its source and every senior edit reusable takes the account.

## The Problem
Credit policy requires annual financial statements and tax returns from commercial borrowers above a threshold, an annual review of each relationship, and quarterly covenant tests on some. The analyst tracks receipt dates and due dates in a spreadsheet, chases lenders who chase borrowers, and the "missing financials" and "past-due reviews" exceptions appear on the board report and in the loan review findings.

## Why It's Still Broken
Requirements sit in loan agreements and policy, receipt is recorded in email, and the core has a tickler field nobody keeps current. The analyst is the integration layer.

## What a Fix Looks Like
Extract reporting requirements and covenants from each loan agreement at booking; generate borrower requests automatically ahead of due dates; recognise documents as they arrive and mark them received; compute covenant tests on receipt; and produce the exceptions report live rather than monthly.

## Who Feels the Pain
Analysts chasing paper; lenders nagged on behalf of analysts; chief credit officers explaining exception counts to the board and examiners.

## Impact If Fixed
Fewer policy exceptions, covenant breaches caught on receipt rather than at review, and hours a week returned to analysis.
