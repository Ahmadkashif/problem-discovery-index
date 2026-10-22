# One Record From Qualification to Churn

**Niche:** [[niches/wireless-carriers/wisp-operators/profile|Fixed Wireless ISPs (WISPs)]]
**Industry:** [[industries/wireless-carriers|Wireless Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A WISP predicts an address's signal in one tool, installs from another, monitors experience in a third and bills in a fourth, so it never learns which predictions were wrong.
**Tags:** #gradient-boosting #survival-analysis #feature-engineering #data-integration #revenue-impact #workflow-orchestration
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to deliver advertised speeds to rural homes over fixed wireless, but the contest splits in two. Before the sale it is qualifying a specific roofline correctly; after the sale it is keeping evening-peak experience inside the plan on shared and often unlicensed spectrum. The data, people, clocks and vendors differ, so the niche is decomposed into contested sub-niches below.

## The Problem
Each WISP customer has a predicted signal, an install outcome, a sector, a traffic history, a support history and, eventually, a cancellation date. These sit in separate tools keyed differently. The owner can't ask which towers, sectors or installers produce the customers who leave in the first year, or whether the coverage tool overpromises on wooded lots.

## Why Nobody Has Built This
WISP software vendors each own one step and integrate loosely. The buyers are small and price-sensitive, and nobody has shown them the value of the joined record.

## What to Build
A customer record that joins prediction, install, sector, experience, tickets and billing, with a churn model on top that attributes early cancellations to qualification error, install quality, sector congestion or price. It feeds corrections back into qualification and capacity decisions.

## Target Customer
WISP owners and network engineers with roughly 1,000 to 50,000 subscribers.

## Impact If Built
The WISP finds out where it loses customers and why, and fixes the step responsible instead of discounting to everyone.
