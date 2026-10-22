# Network Adequacy That Counts Who Actually Sees Members

**Niche:** [[niches/health-insurance-carriers/provider-data-network-adequacy/profile|Provider Data, Directories & Network Adequacy]]
**Industry:** [[industries/health-insurance-carriers|Health Insurance Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Network adequacy filings count contracted providers within time and distance of members, including clinicians who have not billed the plan in a year and are not taking new patients.
**Tags:** #gradient-boosting #survival-analysis #feature-engineering #data-integration #compliance #evaluation-metrics
**Contested on:** Every serious competitor in this niche is fighting to keep each directory entry matching what the provider's office would say on the phone, within the No Surprises Act's 90-day verification cycle, and whoever's directory passes a regulator's secret-shopper sample with the fewest wrong listings takes the account.

## The Problem
Adequacy standards specify how many providers of each type must be within a set travel time and distance of members, by county type. Plans demonstrate them from directory records. A listed psychiatrist who left the practice, or who sees no new plan patients, counts the same as one with open appointments. Regulators increasingly test with secret shoppers and appointment-availability surveys, and state ghost-network laws penalise the gap.

## Why Nobody Has Built This
Adequacy tools take the directory as given. Claims activity, appointment availability and directory records sit in different teams' systems. And a more honest count could show the plan inadequate in counties where it is currently compliant on paper.

## What to Build
An adequacy engine that weights each listed provider by evidence of real availability. Inputs are recent claims volume from plan members at that location, new-patient visits in the last year, verified accepting status, and the predicted probability that the listing is wrong. The engine produces both the regulatory filing and a shadow "effective network", flags counties and specialties where effective adequacy fails, and recommends contracting targets from providers already seeing the plan's members out of network.

## Target Customer
Network management and compliance leaders at MA and Medicaid plans facing secret-shopper audits and EQR network adequacy validation.

## Impact If Built
Plans find their real gaps before regulators or members do, and contracting effort goes to the counties and specialties where members cannot actually get appointments.
