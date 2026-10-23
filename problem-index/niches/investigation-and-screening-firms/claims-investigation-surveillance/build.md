# Panel Allocation by Yield, Not by Rotation

**Niche:** [[niches/investigation-and-screening-firms/claims-investigation-surveillance/profile|Insurance Claims Investigation & Surveillance]]
**Industry:** [[industries/investigation-and-screening-firms|Investigation & Background Screening Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Carriers split investigation work among panel vendors by rotation, geography and price, and cannot compare vendors' yield because claim mix differs from vendor to vendor.
**Tags:** #causal-inference #gradient-boosting #hypothesis-testing #evaluation-metrics #revenue-impact #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to put claim-changing evidence on the file before the claim's next decision date — the independent medical exam, the deposition, the hearing or the settlement conference — inside the carrier's hour caps, and whoever produces the most usable activity per billed hour takes the account.

## The Problem
A carrier's special investigation unit may use a dozen investigation vendors across its states. Assignments are spread by rotation, adjuster preference and territory. The vendor scorecard shows turnaround, invoice accuracy and a raw "activity obtained" rate. A vendor with a high rate may simply get the easier claims; a vendor with a low rate may be sent the claimants who never leave home. The carrier cannot tell which vendor actually produces more usable evidence per dollar.

## Why Nobody Has Built This
Assignment data sits in the claims system, results sit in vendor reports and invoices, and outcomes sit in claim closure data; nobody joins them. Vendors have no incentive to propose a comparison that might show them losing.

## What to Build
A yield model that adjusts each vendor's results for the claims it was given — claim type, restrictions, timing relative to exam or hearing, address confidence, prior surveillance — and estimates usable activity per billed hour and, where the carrier records it, effect on claim outcome. Feed it back into allocation: send each new assignment to the vendor with the best adjusted record for that claim profile and territory, with exploration so newer vendors get a fair test.

## Target Customer
SIU directors and claims vendor managers at carriers and TPAs spending millions a year on investigations.

## Impact If Built
Spend shifts toward vendors that produce evidence rather than hours, vendors are rewarded for planning and skill, and the carrier can defend its surveillance budget with numbers.
