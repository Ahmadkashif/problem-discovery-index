# The Demurrage Clock Nobody Is Watching

**Niche:** [[niches/freight-tech-platforms/ocean-intermodal-visibility/profile|Ocean & Intermodal — Milestone Reconciliation]]
**Industry:** [[industries/freight-tech-platforms|Freight Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Demurrage and detention free time starts on an event, runs on a schedule that differs by carrier and terminal, and is tracked by importers in a spreadsheet — so the charges arrive as an invoice rather than as a deadline anyone could have acted on.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #time-series-forecasting #compliance #workflow-orchestration #automation #revenue-impact
**Contested on:** Every serious competitor in ocean and intermodal visibility is fighting to reconcile milestones reported by carriers, terminals, customs brokers and drayage providers into one true container timeline — and whoever produces the earliest correct availability and pickup signal takes the account.

## The Problem
A container discharges on the 3rd. Free time is four calendar days at this terminal under this carrier's tariff, with a different clock for the equipment detention that starts when the container leaves the terminal. Customs holds it until the 6th. The importer, who is tracking free time in a spreadsheet updated when someone remembers, books drayage for the 9th and receives a demurrage invoice. The charge was avoidable and the deadline was knowable, and the only reason it was missed is that nobody was watching a clock that nobody built.

## Why It's Still Broken
Free time terms live in carrier tariffs and terminal schedules that differ by port, by carrier, by equipment type and sometimes by contract, and encoding them is content work that no platform has undertaken. The start event is itself disputed, which is the reconciliation problem of this sub-niche appearing again. And the charges land on the importer, who is the least equipped party to fight them and frequently does not know the terms well enough to know whether the invoice is correct — a meaningful share of demurrage invoices contain errors that are never challenged.

## What a Fix Looks Like
Build the clock. Encode free time terms per carrier, per terminal and per contract as maintained content, and start the clock from the reconciled milestone rather than from whichever report arrived first. Show the deadline continuously against the current best availability estimate, with an alert when the two are converging — which is the moment expediting drayage is worth paying for and is the decision the importer is currently making blind. Validate incoming demurrage invoices against the platform's own timeline and flag discrepancies with evidence, since a meaningful share are wrong and essentially none are checked. And report the aggregate: how much demurrage this importer paid, by port, by carrier, by cause — customs hold, no appointment, drayage capacity, internal delay — which is a decomposition no importer has and which points directly at what to change.

## Who Feels the Pain
Importers paying charges they could have avoided and cannot verify; logistics coordinators tracking free time in spreadsheets; and drayage providers blamed for delays that were customs or appointment constraints.

## Impact If Fixed
Demurrage is large, growing, avoidable and poorly checked. A clock built on reconciled milestones with an alert before the deadline converts a category of invoice into a category of decision, and invoice validation alone recovers charges that are currently paid without review.
