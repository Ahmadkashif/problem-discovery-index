# Provisional Credit Reconciliation Across Safes, Bags and Banks

**Industry:** [[armored-car-services|Armored Car Services]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Account reconciliation is a solved category, but a smart-safe programme has to reconcile three counts — the safe's, the vault's and the bank's credit — across hundreds of stores and dozens of banks, and generic tools model none of them.
**Tags:** #k-nearest-neighbors #gradient-boosting #hypothesis-testing #descriptive-statistics #data-integration #automation #compliance

## The Problem
A store drops cash into a smart safe all day. The safe validates and counts the notes, and the carrier transmits that total so the store's bank can post provisional credit, usually the next business day, before any truck arrives. Loomis says cash validated in a SafePoint safe is guaranteed against loss, robbery or theft once counted. Days later the truck collects the cassette and any manual drops, the vault counts it again, and the bank's provisional credit is settled against the vault count.

Three numbers that should agree often do not. A bill jammed in the validator, a counterfeit the safe accepted, an envelope of coins or cheques dropped manually without validation, a cassette swapped late, a bank that posted credit on the wrong business day. Each mismatch becomes an exception that someone at the carrier, the retailer's cash office or the bank resolves by email with three spreadsheets open. Retailers also pay for the float: a sponsored 2025 trade piece put the cost of a week of provisional credit on $5,000 at $54.66, and late pickups extend it.

## What Already Exists
Account reconciliation platforms such as BlackLine and the reconciliation modules in retail ERPs; banks' own cash-vault reporting; carriers' customer portals showing safe totals and pickups; device makers' dashboards for safes from Tidel (now part of GardaWorld's Sesami), FireKing and others.

## The Customisation Gap
The cash-specific logic is: matching at the level of safe, cassette, bag seal and business day rather than bank account; tolerances that differ by drop type (validated notes are guaranteed by the carrier, manual drops are not); counterfeit and mutilated-note adjustments; bank cut-off calendars that differ by bank, so one chain may face dozens of different provisional credit rules; who bears the loss for each type of mismatch under the carrier contract; and evidence packs — safe event logs, bag scans, vault count video — attached to each exception. A generic matcher can say two numbers differ. It cannot say which party owes the difference.

## Impact If Solved
For a chain of ~300 stores with a mismatch at ~1 store in 20 each day (estimate), the cash office works ~15 exceptions a day at ~30–45 minutes each, ~8–10 staff-hours a day (estimate). Evidence attached automatically and rules that assign each difference to its party could cut that to ~2 hours (estimate), settling disputes with the carrier and banks in days rather than weeks. The float cost of provisional credit also becomes visible store by store, which is the number a retailer needs to decide whether a smart safe is paying for itself.
