# Reconciliation Platforms Taught Corporate Actions

**Niche:** [[niches/trust-companies/institutional-custody-asset-servicing/profile|Institutional Custody & Asset Servicing]]
**Industry:** [[industries/trust-companies|Trust Companies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Reconciliation platforms match records well; they do not understand why a corporate action makes two correct records disagree.
**Tags:** #large-language-models #feature-engineering #evaluation-metrics #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to deliver each client's positions, cash and corporate-action entitlements without breaks before the client's own NAV and settlement cutoffs, and whoever has the fewest unresolved breaks at the cutoff takes the account.

## The Problem
A large share of the hardest breaks come from corporate actions: a stock dividend booked on pay date by one party and ex-date by another, an elective event where the manager's election differs from the custodian's record, a cash rate revised after announcement, tax withheld at a rate that differs from the treaty rate expected.

## What Already Exists
Reconciliation and data-matching platforms such as Duco and SS&C's matching products, and corporate-actions data and processing systems from data vendors and the custody banks themselves.

## The Customization Gap
The adaptation needs: event-aware matching that understands record, ex and pay dates, elections and proration; a break reason taxonomy specific to corporate actions and income; reading of the event announcement and the client's instruction to propose which side is right; multi-party views across manager, fund accountant, sub-custodian and depository; and a link from each resolved break to the event record so the next similar event is processed correctly.

## Target Customer
Corporate actions and reconciliation heads at custody banks already licensing a matching platform.

## Impact If Solved
Event-aware matching shortens resolution of corporate-action breaks from hours to minutes (estimate) and reduces client claims for missed or misapplied entitlements.
