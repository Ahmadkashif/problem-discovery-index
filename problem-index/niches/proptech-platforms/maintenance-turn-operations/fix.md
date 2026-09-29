# The Reopened Work Order Counted as Two

**Niche:** [[niches/proptech-platforms/maintenance-turn-operations/profile|Maintenance & Turn Operations]]
**Industry:** [[industries/proptech-platforms|Proptech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** When a repair does not hold and the resident submits another request, the platform records two completed work orders and a satisfied portfolio, and the single most important maintenance quality signal is destroyed at the moment it is created.
**Tags:** #k-nearest-neighbors #bert #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #automation #quick-win
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
A resident reports a leaking sink. A vendor attends and closes the order. Nine days later the resident reports a leaking sink again. A new work order is created, possibly categorised differently, possibly sent to a different vendor. The system's record is two work orders, both completed, both within service level. The operator's dashboards show completion rates and average close times that look healthy. The fact that matters — that the first repair failed — is nowhere, and it is the fact on which vendor quality, technician training, parts decisions and resident satisfaction all depend.

## Why It's Still Broken
Linking requires matching a new request to a prior one on unit, component and description, which is a fuzzy match rather than a key, and no vendor has implemented it because no customer has asked. Customers have not asked because their reporting looks fine without it — which is precisely the problem. There is also a mild disincentive: an operator that starts measuring reopen rate will find it higher than expected and will have to explain the change to an owner, so the metric is unwelcome in a way that a completion rate is not.

## What a Fix Looks Like
Detect the reopen. A new request for the same unit, concerning the same component or system, within a window, is identifiable from data the platform already holds, and the match can carry a confidence with the borderline cases surfaced rather than assumed. Publish the definition and let the operator set the window so the metric is stable and comparable. Separate the categories that behave differently — a repair that failed, a related but genuinely new problem, and a resident-caused recurrence are three different things — because lumping them makes the vendor conversation unwinnable. Then report reopen rate by vendor, by work type, by property and by technician with volume-appropriate uncertainty. Everything else in this niche depends on it: vendor scorecards, triage accuracy and preventive maintenance all need a definition of a repair that worked.

## Who Feels the Pain
Residents living with a problem that was reported as fixed; site managers whose dashboards say the property is performing; and good vendors, who are indistinguishable from bad ones in a system that counts completions.

## Impact If Fixed
Reopen detection is the missing quality signal in rental maintenance and costs a fuzzy match on existing data. Operators who compute it for the first time typically find it concentrated in particular vendors and work types, both of which are immediately actionable, and every other measurement in this niche becomes meaningful once it exists.
