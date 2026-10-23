# Field Service Scheduling Adapted to Repossession Runs

**Niche:** [[niches/repossession-services/auto-finance-recoveries/profile|Auto Finance Recoveries]]
**Industry:** [[industries/repossession-services|Repossession Agencies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Field service management software already schedules technicians across hundreds of jobs a day; repossession runs need the same engine with a different idea of what a job is.
**Tags:** #optimization-fundamentals #gradient-boosting #time-series-forecasting #workflow-orchestration #data-integration #automation
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to close more of a lender's auto assignments inside its window without a wrongful-repossession event — but a file with a good address is won at the curb on the first attempt, while a skip is won before the truck moves by finding the car, and the two contests have different inputs, pay and rivals. Decomposed into contested sub-niches below.

## The Problem
An agency's night is a scheduling problem: several trucks, hundreds of open files with several addresses each, hits arriving during the shift, cancellations, and clients with different priorities. Most agencies build run-lists by hand or with a map and the field app's list view.

## What Already Exists
Field service management platforms — ServiceTitan, Salesforce Field Service, Workiz — and route optimisers such as OptimoRoute schedule technicians to appointments with time windows, skills and travel time, and re-plan when jobs change.

## The Customization Gap
A repossession "job" is not an appointment: it is a probability that a car is at an address in a window, worth a fee only if it succeeds, attempted against a client deadline and a legal constraint. The adaptation needs: windows weighted by presence probability rather than customer bookings; several candidate addresses per file; live hits that insert urgent jobs; hold and cancel signals that delete them; agent skill routing for risky files; and output in the field app the agents already use.

## Target Customer
Agencies running three or more trucks across a metro, and multi-state agencies with dispatchers.

## Impact If Solved
More attempts at the right address and hour per truck-night, and less fuel and time spent on files that could not close tonight.
