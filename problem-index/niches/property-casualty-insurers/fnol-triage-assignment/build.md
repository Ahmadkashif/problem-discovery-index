# Assignment That Learns From Every Reassignment

**Niche:** [[niches/property-casualty-insurers/fnol-triage-assignment/profile|First Notice of Loss Triage & Claim Assignment]]
**Industry:** [[industries/property-casualty-insurers|Property & Casualty Insurers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Claims are routed by rules written years ago, and every claim that bounces between desks is a label the rules never learn from.
**Tags:** #gradient-boosting #bert #feature-engineering #evaluation-metrics #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to route each new claim to the right path — straight-through payment, desk, field, total loss or fraud referral — at first notice, and whoever cuts reassignments without paying a fraudulent or escalating claim on autopilot takes the account.

## The Problem
A carrier's assignment rules send a claim to a fast-track desk, a field adjuster, a total-loss unit, an injury unit or special investigations on the basis of line, coverage, reported damage and a few keywords. A meaningful share of claims (estimate) are reassigned within the first weeks, when the photos show a total loss, the claimant mentions neck pain, or the facts look staged. Each reassignment costs days of cycle time and an extra handler's ramp-up.

## Why Nobody Has Built This
Assignment logic sits in core-system configuration owned by IT, and reassignment data is rarely analysed. Vendors sell components such as photo estimating, fraud scores and FNOL apps, not the routing decision that combines them.

## What to Build
A routing model trained on final handling paths rather than initial assignments. It uses the FNOL narrative, photos, call transcript, policy and party history, and the outputs of fraud, total-loss and injury models. It sends each claim to the path it ends up needing, sets straight-through thresholds by measured risk, and audits a sample of straight-through payments to keep the thresholds honest.

## Target Customer
Claims operations leaders at personal auto, homeowners and small commercial carriers.

## Impact If Built
Fewer reassignments, shorter cycle times on simple claims, and earlier specialist handling of the claims that need it.
