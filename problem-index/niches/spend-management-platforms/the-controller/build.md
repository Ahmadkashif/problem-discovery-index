# Designing for the Month, Not the Transaction

**Niche:** [[niches/spend-management-platforms/the-controller/profile|The Controller]]
**Industry:** [[industries/spend-management-platforms|Spend Management Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The product is built around the transaction and the controller's life is organised around the month.
**Tags:** #workflow-orchestration #worker-facing #automation #evaluation-metrics #large-language-models #descriptive-statistics #gradient-boosting #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to give the controller back the three weeks a month they spend approving what they were always going to approve — and whoever does it sells to the person who actually chooses the platform.

## The Problem
The platform presents transactions, exceptions and receipts as continuous streams. The controller experiences a cycle: spend accumulates, exceptions arrive, receipts are chased, and then everything must be resolved, coded, reconciled and reported in a compressed window at the end. Nothing in the product understands that cycle, so the controller builds their own checklist in a spreadsheet and lives in a permanent state of catching up on work that is all due at once.

## Why Nobody Has Built This
The product was designed around the card and the transaction, because that is the technical object and the interchange revenue source — the controller's month was never modelled as a first-class entity. Feature development follows the employee experience, which is more visible. Controllers are resourceful and build their own workarounds, which hides the gap. And nobody measures how their time is spent.

## What to Build
Model the month and work backwards from the close. Build a close-oriented view showing what is outstanding, what will block reconciliation, and what can be dealt with now, which is the core and is the organising frame the product lacks. Triage exceptions and receipts so the controller's attention goes where it matters, connecting to the judgement and documentation work. Forecast what the close will look like from mid-month, since problems discovered on the last day were all visible two weeks earlier. Automate the routine approvals with the controller's own configuration, because that is the three weeks and giving it back is the product. Prepare accruals and reconciliation items automatically, as they are derivable and are currently assembled by hand. Detect the transactions that will not reconcile before month end rather than during it. Show the controller where their own time goes, since nobody has told them and they cannot argue for help without it. Benchmark their close against similar companies, which is information only the platform has and which controllers would value greatly. Support the review and sign-off flow, because the responsibility is theirs and the product currently ends before that point. And measure days to close as the product's outcome metric, since it is the number the controller is judged on.

## Target Customer
Controllers and accounting operations leads, CFOs whose close depends on them, product leadership at the platforms, and close management vendors with no spend integration.

## Impact If Built
The product was built around the card and the transaction because that is the technical object and the revenue source, so the controller's month was never modelled. Organising the product around the close is what returns three weeks to the person who chooses the platform.
