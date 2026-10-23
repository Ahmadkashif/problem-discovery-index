# Crew-Level Exposure Pricing From Payroll and Job Data

**Niche:** [[niches/professional-employer-organizations/high-hazard-blue-collar-clients/profile|High-Hazard & Blue-Collar Clients]]
**Industry:** [[industries/professional-employer-organizations|Professional Employer Organizations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A PEO prices a contractor's comp from the class codes on its payroll, while the actual exposure, how many hours each crew spent on roofs, ladders or trucks, sits in job and timekeeping data nobody joins to it.
**Tags:** #gradient-boosting #survival-analysis #feature-engineering #evaluation-metrics #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to write roofing, trucking and light-manufacturing clients that mainstream PEOs decline, and whoever prices their workers' comp to each crew's actual exposure and enforces safety at the worksite well enough to keep retained losses under the comp premium charged takes the account.

## The Problem
A general contractor's payroll shows carpenters, laborers and a clerical class. The rates assume the split is honest and stable. In practice an "office" employee runs jobs on site, a crew moves from residential remodelling to commercial roofing mid-year, and a slow season pushes everyone into whatever work exists. The PEO finds out at premium audit or after a fall. Meanwhile the client is priced as its class mix looked at onboarding.

## Why Nobody Has Built This
Small contractors' job data lives in estimating tools, scheduling apps and paper. The PEO sees payroll, not jobs. Comp rating rules are class-based, and the incentive to look closer than the rules require is weak until losses arrive.

## What to Build
An exposure model that joins payroll by employee to job, site and task data from the client's timekeeping or field apps. It estimates hours by hazard type (height, vehicles, heavy equipment) and flags class drift monthly. A loss model learns which exposure patterns precede claims across the PEO's construction book, and the output feeds class corrections, safety requirements and renewal pricing for each client.

## Target Customer
Specialty PEOs serving construction and transport clients, and regional PEOs whose construction book drives most of their retained comp losses.

## Impact If Built
Pricing that tracks the work actually being done, fewer audit surprises, and safety effort aimed at the crews and tasks that produce the claims.
