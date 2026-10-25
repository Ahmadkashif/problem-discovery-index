# A Drum Planner for Lab-Pack Inventories

**Niche:** [[niches/hazardous-waste-firms/lab-pack-hhw-collection/profile|Lab Pack & Household Hazardous Waste Collection]]
**Industry:** [[industries/hazardous-waste-firms|Hazardous Waste Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Two chemists packing the same stockroom ship it in noticeably different numbers of drums, and the customer pays for the difference.
**Tags:** #optimization-fundamentals #combinatorics-and-counting #large-language-models #worker-facing #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to clear a laboratory's or a collection event's chemical inventory into compliant shipments, and whoever ships each inventory in the fewest drums takes the account.

## The Problem
Grouping is constrained by DOT hazard classes, segregation rules, waste codes, the receiving facility's acceptance by drum type and the operator's own packing procedures. An experienced chemist finds groupings that fill drums; a newer one opens a fresh drum whenever in doubt. Drum count drives the invoice and the receiving facility's workload.

## Why Nobody Has Built This
Inventories are not captured as data until after packing, so there is nothing to plan from. Operators treat packing as craft, and the rules sit in procedures and in senior chemists' heads.

## What to Build
Once the inventory is captured (label photos matched to safety data sheets), a planner proposes drum groupings that satisfy the operator's segregation and acceptance rules, written as explicit constraints, and minimise drum count and disposal cost by outlet. The chemist edits and approves; the plan writes the drum inventories and manifest lines.

## Target Customer
Lab-pack operations managers at national and regional hazardous waste firms; university EHS departments that pack their own waste for pickup.

## Impact If Built
Cutting drum count by ~10% (estimate) on a clean-out of 60 drums at ~$300–600 a drum (estimate) saves the customer ~$2,000–3,500 per job, which wins the next bid.
