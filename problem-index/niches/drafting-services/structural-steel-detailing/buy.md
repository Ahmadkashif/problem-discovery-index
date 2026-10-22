# Connection Automation Turned Into a Checker

**Niche:** [[niches/drafting-services/structural-steel-detailing/profile|Structural Steel Detailing]]
**Industry:** [[industries/drafting-services|Drafting Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Connection automation already knows how to design and model a connection to AISC rules; pointed the other way, it could check every connection a detailer modelled by hand.
**Tags:** #decision-trees #graph-neural-networks #evaluation-metrics #automation #quick-win #compliance
**Contested on:** Every serious competitor in this niche is fighting to deliver checked, approval-ready shop and erection drawings inside the fabricator's schedule with the fewest errors reaching the shop floor, and whoever can prove the lowest field-fix rate per ton takes the fabricator's account.

## The Problem
Many connections in a steel model are placed manually or adjusted after automation, especially at skews, slopes, transfer conditions and where the engineer's design reactions are incomplete. Checking them means opening each one or reading its shop drawing. Checkers sample instead of checking every one, and the errors hide in the ones they skip.

## What Already Exists
Qnect's QuickQnect designs and models connections inside Tekla to AISC and CISC requirements; SDS2 designs connections inside the detailing package; Tekla's components and clash checks flag geometric interference. These are built to create connections, not to audit ones already in the model.

## The Customization Gap
The adaptation needs: (1) a check mode that reads every existing connection and compares it to what the automation would have produced for the same members and reactions; (2) fabricator-specific fit-up rules — preferred bolt gauges, clip angle sizes, shop standard connections — layered over the AISC rules; (3) flags prioritised by fabrication and erection consequence, not just by code failure; (4) output as a review list in the checker's PDF or model, not a report; and (5) per-client configuration that a small bureau can set up in hours.

## Target Customer
Steel detailing bureaus already licensing Tekla or SDS2, and fabricators with in-house detailing who want consistent checking across vendors.

## Impact If Solved
Every connection checked instead of a sample, at almost no checker time, removing the single largest category of fit-up errors before submittal.
