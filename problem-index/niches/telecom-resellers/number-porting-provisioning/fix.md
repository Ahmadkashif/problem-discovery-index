# The Pending Order Nobody Closed

**Niche:** [[niches/telecom-resellers/number-porting-provisioning/profile|Number Porting & Provisioning Desk]]
**Industry:** [[industries/telecom-resellers|Telecom Resellers]]
**Type:** Fix (Pain Point)
**One-liner:** A port is rejected because the losing carrier has an old open order on the account that nobody on either side knew about, and the desk learns of it two weeks after submitting.
**Tags:** #large-language-models #bert #workflow-orchestration #worker-facing #quick-win #automation
**Contested on:** Every serious competitor in this niche (wholesale and CPaaS porting APIs, porting-automation tools and outsourced porting desks) is fighting to get a port order to a firm order commitment on its first submission, and whoever matches the losing carrier's records most reliably before sending takes the account.

## The Problem
Losing carriers reject ports when an order is pending on the account: a feature change from last year never closed, a disconnect in progress, a freeze on the line. The customer doesn't know, the CSR may not show it, and the rejection comes back weeks later. Clearing it takes another call to the losing carrier, sometimes by the customer, and the cut-over date slips again.

## Why It's Still Broken
The pending order lives in the losing carrier's system, which the gaining provider can't see. CSRs vary in whether they show open orders and freezes, and the rejection code that reports it is generic. The desk has no prompt to ask the right question before submitting.

## What a Fix Looks Like
Add a pre-submission step that asks the customer, in plain language, about recent changes, disconnects and freezes, and requests the CSR in a form that shows pending activity where the losing carrier offers one. Classify past rejections so carriers known to sit on orders with pending activity get a pre-check call. When the rejection does come, send the customer a ready-made script for clearing it with the losing carrier.

## Who Feels the Pain
Porting specialists redoing orders; customers whose go-live keeps moving; and installers booked for cut-overs that don't happen.

## Impact If Fixed
A common, avoidable rejection is caught before submission, saving two to three weeks per affected port.
