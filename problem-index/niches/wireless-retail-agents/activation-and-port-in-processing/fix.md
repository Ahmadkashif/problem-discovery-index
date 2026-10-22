# The Port-In That Fails After the Customer Leaves

**Niche:** [[niches/wireless-retail-agents/activation-and-port-in-processing/profile|Activation & Port-In Processing]]
**Industry:** [[industries/wireless-retail-agents|Wireless Retail Agents]]
**Type:** Fix (Pain Point)
**One-liner:** A wrong account number or port-out PIN means the customer leaves with a new phone on a temporary number, and the line becomes an unhappy call-back or a cancellation.
**Tags:** #logistic-regression #evaluation-metrics #automation #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche (the carriers' own activation tools, iQmetrix's multi-carrier activation and device-setup vendors) is fighting to take a new line from ID check to a working, ported phone with its data moved in ~20 minutes without raising fraud, and whoever cuts the most counter minutes per activation takes the dealer's counter.

## The Problem
Customers rarely know their old carrier's account number or port-out PIN. Reps take a best guess, the port request is rejected later, and the customer has to come back or call. Some give up and cancel inside the window.

## Why It's Still Broken
Each losing carrier has its own way to look up the account number and generate a PIN, the rep can't see it, and nobody checks the details before the customer reaches the counter.

## What a Fix Looks Like
A pre-visit text or QR prompt that walks the customer through getting their account number and port-out PIN from their current carrier's app, with screenshots of where to find them. At the counter, a quick check that the details are well-formed. Port rejections are then tracked by losing carrier and rep to show where the guidance fails.

## Who Feels the Pain
Customers left without their number; reps who repeat the work; stores that lose the line.

## Impact If Fixed
Fewer failed ports and repeat visits, from guidance that costs almost nothing to send.
