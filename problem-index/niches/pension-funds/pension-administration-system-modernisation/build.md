# A Parallel-Calculation Harness That Proves the New System Before Cutover

**Niche:** [[niches/pension-funds/pension-administration-system-modernisation/profile|Pension Administration System Modernisation]]
**Industry:** [[industries/pension-funds|Pension Funds]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A retirement system replacing its PAS tests benefit calculations on samples, then finds the untested edge cases in the first retiree payrolls.
**Tags:** #k-means-clustering #feature-engineering #evaluation-metrics #hypothesis-testing #automation #data-integration
**Contested on:** Every serious competitor in this niche is fighting to move decades of member service, salary and contribution history into a new system that calculates every benefit the old one did, and whoever goes live with the fewest payment errors in the first retiree payrolls takes the account.

## The Problem
A statewide system may have hundreds of thousands of members across multiple tiers, service purchase types, reciprocity agreements, disability provisions and decades of COLA rules (estimate). Conversion testing compares old and new calculations on test cases chosen by staff, who pick the cases they remember. The cases nobody remembers, such as a member with a 1990s break in service, a purchased military credit and a split tier, go live untested.

## Why Nobody Has Built This
Vendors test their own configuration. Oversight consultants test against requirements. Running both systems on every member requires extracting calculation inputs from the legacy system, which is the system being retired and the one nobody wants to touch.

## What to Build
A harness that runs the legacy and new calculations for the entire membership (estimate, final benefit, COLA, option factors) and clusters members by their provision combinations. It reports differences by cluster with the member count affected, so the testing effort follows coverage, not memory. Every difference is classified as a conversion error, a configuration error, or a legacy defect the new system correctly fixes, and that decision is recorded for the board.

## Target Customer
Executive directors and CIOs of systems in PAS replacement; independent oversight consultants; PAS vendors who want to de-risk go-live.

## Impact If Built
Payment errors in the first retiree payrolls fall from "found by retirees" to "found in testing". Legacy defects that underpaid members for years are discovered on purpose rather than by complaint.
