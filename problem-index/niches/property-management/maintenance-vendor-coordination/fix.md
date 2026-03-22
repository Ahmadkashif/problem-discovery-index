# Vendor Invoice Verification

**Niche:** [[niches/property-management/maintenance-vendor-coordination/profile|Maintenance & Vendor Coordination]]
**Industry:** [[industries/property-management|Property Management]]
**Type:** Fix (Pain Point)
**One-liner:** Property managers approve vendor maintenance invoices by comparing them against the original work order scope and their memory of agreed-upon rates — missing overcharges, scope creep, and billing errors on 15-25% of invoices because manual review doesn't catch charges that don't match the agreed terms.
**Tags:** #bert #automation #revenue-impact #dbscan

## The Problem
A property management company processing 400-800 vendor invoices per month must verify each one: does the charged amount match the agreed rate for this type of work? Does the scope on the invoice match the original work order? Are material markups within the agreed percentage? Was the work actually completed (confirmed by tenant or inspection)? This verification is done by the maintenance coordinator or bookkeeper, who reviews each invoice against the work order and their memory of vendor rate agreements. The review takes 3-5 minutes per invoice — at 600 invoices per month, that's 30-50 hours of invoice review time. Despite this effort, 15-25% of invoices contain errors or overcharges that slip through: a plumber who charges 3 hours for a 1-hour repair, an HVAC vendor who marks up a $150 filter to $350, a handyman who invoices for work on a unit they weren't dispatched to, or a vendor who charges their "emergency" rate for a routine dispatch.

## Why It's Still Broken
Vendor rate agreements are stored in the coordinator's head, a filing cabinet, or a spreadsheet that's never updated. When the coordinator changes (turnover is high in PM operations), the institutional knowledge of vendor rates walks out the door. AppFolio and Yardi store historical invoice amounts but don't compare them against agreed rates or flag anomalies. No tool automatically checks whether today's invoice is consistent with what this vendor has historically charged for this type of work at this property.

## What a Fix Looks Like
An invoice verification system that: (1) maintains vendor rate agreements in a structured database — agreed hourly rates, material markup limits, trip charges, and after-hours premiums per vendor per trade; (2) compares each incoming invoice against the rate agreement and the original work order — flagging discrepancies ("Invoice: 3 hours at $125/hr = $375. Work order description suggests a 30-minute job. Historical average for this task type: 1.2 hours"); (3) uses anomaly detection on the vendor's historical pricing — flagging invoices that are significantly above the vendor's own historical average for the same type of work; (4) checks for common billing errors — duplicate invoices, charges for canceled work orders, material markups exceeding the agreed percentage; and (5) presents flagged invoices for coordinator review with the specific discrepancy highlighted, enabling informed approval or dispute.

## Who Feels the Pain
Maintenance coordinators who approve 20-30 invoices per day under time pressure, catching obvious errors but missing subtle overcharges. Property owners who absorb inflated maintenance costs because the PM didn't catch vendor overbilling. PM company owners whose margins are eroded by maintenance cost overruns that should have been caught at the invoice review stage.

## Impact If Fixed
Identifies 15-25% of invoices with errors or overcharges, recovering $30K-100K annually for a 500-unit PM company. Reduces invoice review time from 3-5 minutes to 30 seconds for invoices that pass automated verification. Creates accountability in vendor pricing by establishing documented rate agreements and automated enforcement. Protects the PM's margin by ensuring maintenance costs stay within budgeted ranges.
