# The Roll List Picked by Who Shouted Loudest

**Niche:** [[niches/ocean-shipping-carriers/liner-pricing-and-allocation/profile|Container Liner Pricing & Allocation]]
**Industry:** [[industries/ocean-shipping-carriers|Ocean Shipping Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** When a ship is oversold at cut-off, the boxes rolled to next week are chosen under deadline pressure, often by whose sales rep escalated last rather than by what each box is worth.
**Tags:** #gradient-boosting #evaluation-metrics #workflow-orchestration #revenue-impact #quick-win
**Contested on:** Every serious competitor in this niche is fighting to fill each sailing with the highest-paying cargo that actually turns up, and whoever earns the highest net revenue per available slot across a season of sailings takes the account.

## The Problem
At cut-off the terminal reports more gated-in cargo than the ship's allocation. Someone has to choose which containers wait a week. In practice the list is built from a spreadsheet and phone calls: sales reps defend their customers, operations push for whatever is easiest to stow, and the decision is made in an hour. A high-paying spot box can be rolled while a low-paying booking sails because its customer complained loudest.

## Why It's Still Broken
No system ranks gated-in containers by the value of carrying them now: freight rate, contract penalties, customer importance, cargo urgency (reefer, dated cargo) and the cost of next week's slot. The decision is too fast and too political for anyone to record.

## What a Fix Looks Like
At cut-off, rank every candidate box by its net value of sailing now and the cost of rolling it, with protected accounts flagged, and propose a roll list in seconds. The desk edits and confirms; the system records the final list and the reason for each override, and notifies affected customers with the new sailing.

## Who Feels the Pain
Trade desk managers at cut-off, sales reps whose customers are rolled, customer service agents who deliver the news, and shippers who lose a week.

## Impact If Fixed
Suppose ~300 TEU are rolled from an oversold sailing (estimate). Rolling the lowest-paying boxes rather than whoever escalated least, at a ~$500 per TEU spread between them (estimate), keeps ~$150,000 per sailing. For the first time the roll decisions are recorded and can be checked against what they cost.
