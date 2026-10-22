# Carrier Commission Statement Reconciliation

**Industry:** [[wireless-retail-agents|Wireless Retail Agents]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Commission reconciliation software exists for every sales channel, but a wireless dealer's month-end means matching each carrier's own statement format, line by line, to activations under a comp plan that changed last month, before the dispute window closes.
**Tags:** #large-language-models #feature-engineering #random-forests #evaluation-metrics #data-integration #automation #revenue-impact #quick-win

## The Problem
Every month each carrier, master agent or brand sends the dealer what it believes it owes: activation commissions, upgrade and feature payments, spiffs, residuals and bonuses, less chargebacks for lines that cancelled, went unpaid or were flagged. The statement arrives as a portal export, a CSV in the carrier's own layout, or a PDF. The dealer's back office has to match every line to the activation in its own point-of-sale system by phone number, IMEI, SIM or order number. Then it has to work out what should have been paid under that month's comp plan, find lines missing or short-paid, and file disputes with evidence before the carrier's window closes. A chain with hundreds of doors processes tens of thousands of lines a month (estimate). An owner-operator with four prepaid stores does it at the kitchen table, or doesn't, and simply accepts the deposit.

Unmatched lines are where the money leaks. A missed feature payment because the rep added protection after activation; a spiff that applied to one SKU colour and not another; a chargeback for a line that was in fact exchanged, not cancelled. Each is small. Across a month of statements they add up to a few percent of commission revenue (estimate).

## What Already Exists
iQmetrix ReconcilePro matches RQ sales to carrier commission files with configurable rules and templates per carrier format. Telecom commission tools (Modero, Commission Tracker) and general incentive-compensation software (QCommission, Xactly) handle statement import and ledgers. Outsourced reconciliation shops work the files by hand for smaller dealers. Spreadsheets fill every gap.

## The Customisation Gap
The generic tools assume a stable plan and a clean feed. A wireless dealer needs: parsers for each carrier's statement and PDF layout that survive the carrier changing a column; expected-commission rules generated from the current month's comp plan and spiff bulletins, including effective dates, SKU lists and tier multipliers; matching that tolerates the identifiers changing across an exchange, a port or a SIM swap; chargeback reason mapping across carriers, so "deactivation" and "non-pay" mean the same thing in every report; and a dispute tracker that knows each carrier's evidence requirements and window length. Without the comp-plan logic, a reconciliation tool can tell you a line was paid, but not whether it was paid correctly.

## Impact If Solved
For a chain, closing the month in days rather than weeks and recovering short-paid commissions that currently expire; ~1–3% of commission revenue recovered is plausible (estimate). For a prepaid owner-operator, it is the difference between knowing the month's income and trusting the deposit.
