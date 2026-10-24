# Root-Cause Linking From Round Test Failures to Build Records

**Niche:** [[niches/defense-systems-manufacturers/all-up-round-acceptance-test/profile|All-Up-Round Assembly & Acceptance Test]]
**Industry:** [[industries/defense-systems-manufacturers|Defense Systems Manufacturers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A missile that fails acceptance test is debugged in isolation, though the cause often sits in a supplier lot, a build station or a rework step shared with other rounds.
**Tags:** #gradient-boosting #causal-inference #k-nearest-neighbors #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to get finished rounds through acceptance test the first time, and whoever raises first-pass yield at all-up-round acceptance test takes the account.

## The Problem
When a round fails a functional or environmental test, a test engineer reads the failure log, a technician troubleshoots, and the failing section is reworked or replaced. The failure report records the fix. What it rarely records is whether the same test signature appeared on other rounds built with the same supplier lot, harness, connector batch or technician, so the same fault returns weeks later on another round.

## Why Nobody Has Built This
Test data, build genealogy and failure reports live in three systems owned by three departments, on classified or ITAR networks. Each programme has built its own automated test software, so there is no common data model to sell into, and yield has been treated as a manufacturing engineering problem rather than a data one.

## What to Build
An on-premises correlation layer that joins every round's test measurements and failure signatures to its as-built genealogy (supplier lots, serial numbers, build stations, operators, rework history). For each new failure it retrieves rounds with similar signatures, ranks shared build attributes by how strongly they separate failing from passing rounds, and proposes the probable cause and containment scope for the failure review board.

## Target Customer
Directors of final assembly and test, and failure review board chairs, on high-rate missile and interceptor lines.

## Impact If Built
Raising first-pass acceptance yield by a few points on a line delivering hundreds of rounds a year frees test-station hours and rework labour equivalent to weeks of output (estimate), at a time when rate is the constraint.
