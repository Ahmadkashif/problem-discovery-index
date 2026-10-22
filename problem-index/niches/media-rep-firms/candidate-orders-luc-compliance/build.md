# A Lowest-Unit-Charge Engine With the Working Shown

**Niche:** [[niches/media-rep-firms/candidate-orders-luc-compliance/profile|Candidate Orders & Lowest-Unit-Charge Quoting]]
**Industry:** [[industries/media-rep-firms|Media Representative Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The lowest unit charge moves every time a commercial advertiser buys the same class cheaper during the window, and reps recompute it by hand for each station.
**Tags:** #large-language-models #descriptive-statistics #compliance #workflow-orchestration #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to quote every candidate order at each station's true lowest unit charge for the class, and turn the disclosure paperwork around in hours, inside the 45- and 60-day windows, and whoever does it without a rebate claim or a political-file gap gets the national political buyer's next order.

## The Problem
A candidate's buyer asks the rep for rates on fifteen stations for the last three weeks of a general election. For each station and each class (preemptible, fixed, by daypart) the LUC is the lowest rate any commercial advertiser paid for that class and time in the period. It changes when a commercial order clears lower mid-window. A candidate who paid more is owed a rebate. The rep's political coordinator rebuilds the calculation from each station's rate history, often in a spreadsheet emailed by the station.

## Why Nobody Has Built This
Traffic systems compute LUC for their own station; the rep needs it across hundreds of stations on several systems. The work recurs only in even years, so internal tools decay between cycles.

## What to Build
An engine that ingests each represented station's cleared commercial rates by class and period and computes the current LUC per class and window date. It quotes candidate orders from it, saves the calculation with every quote, monitors for lower commercial clearances that trigger a rebate obligation, and produces the disclosure statement of classes and preemption likelihood the rule requires.

## Target Customer
Heads of political sales at rep firms; station group political directors who want the rep's quotes to match their own records.

## Impact If Built
Quotes become defensible line by line, rebates are caught before the campaign's auditor finds them, and a coordinator can quote in minutes what used to take an afternoon.
