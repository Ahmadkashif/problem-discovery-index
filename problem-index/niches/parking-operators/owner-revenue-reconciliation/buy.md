# Retail Exception Reporting Adapted to PARCS

**Niche:** [[niches/parking-operators/owner-revenue-reconciliation/profile|Owner Revenue Reconciliation & Reporting]]
**Industry:** [[industries/parking-operators|Parking Operators]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Retailers have caught cashier fraud with point-of-sale exception reporting for years; parking cashiers and gate overrides are the same problem in a different system.
**Tags:** #gaussian-mixture-models #feature-engineering #evaluation-metrics #compliance #data-integration
**Contested on:** Every serious competitor in this niche is fighting to account for every dollar a managed facility collects, and whoever shows the smallest unreconciled gap between recorded parking sessions and deposited revenue at the owner's audit takes the account.

## The Problem
Revenue control at an operator samples cashier shifts and reviews gate-override logs by hand. Patterns such as one cashier's lost-ticket waivers on Friday nights surface only when someone happens to look.

## What Already Exists
Point-of-sale exception-based reporting used by retail and restaurant loss-prevention teams, which scores cashiers on voids, refunds, no-sales and discounts and links exceptions to video.

## The Customization Gap
Parking exceptions are different events. They include lost-ticket fees waived, tickets voided, gate arms raised from a booth or by the remote intercom agent, and validations applied without a matching tenant invoice. Monthly cards are used at two facilities at once, and marketplace bookings exit without a scan. The adaptation needs PARCS connectors for each vendor, normalisation for event days, and links to lane video and intercom logs. Reports must go to both the operator and, under some contracts, the owner.

## Target Customer
Operator revenue-control teams; owners and cities auditing their operators.

## Impact If Solved
Moving revenue control from random sampling to ranked exceptions lets one analyst cover ~3–5 times as many facilities (estimate), and catches leakage patterns months before an owner's audit.
