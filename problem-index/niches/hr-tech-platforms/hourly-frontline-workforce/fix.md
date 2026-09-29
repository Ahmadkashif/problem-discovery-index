# Schedule Changes With No Audit Trail

**Niche:** [[niches/hr-tech-platforms/hourly-frontline-workforce/profile|Hourly & Frontline Workforce]]
**Industry:** [[industries/hr-tech-platforms|HR Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A published schedule is edited repeatedly before it is worked, the edits determine predictive scheduling entitlements and a worker's ability to plan, and most systems store only the current version.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #compliance #workflow-orchestration #automation #quick-win
**Contested on:** Every serious competitor in frontline HR software is fighting to make an hourly worker's schedule, hours, accruals and pay visible and provable to the worker themselves — and whoever the workers actually use takes the employer.

## The Problem
A schedule is published two weeks out. Over the following fortnight a shift is shortened, another is moved, a worker is called in with a day's notice, and one shift is cancelled the morning it was due. In covered jurisdictions several of those changes trigger premium pay, and all of them affect a worker whose childcare and second job depend on knowing their hours. The system shows the schedule as it now stands. The version published two weeks ago, and every version since, exist nowhere — so the entitlement cannot be computed, the pattern cannot be examined, and a dispute about what was promised is a disagreement between memories.

## Why It's Still Broken
Schedules were modelled as mutable objects edited in place, which is the natural implementation and the same design error that prevents forecast scoring and policy checking elsewhere in this vault. Predictive scheduling statutes arrived later and were addressed by adding premium pay calculations on top of a data model that does not retain the history the calculation needs, so compliance is computed from whatever the system happened to log. And the party harmed by the absence — the worker — is not the party specifying the system.

## What a Fix Looks Like
Snapshot the schedule at publication and version every change thereafter. Each version retained with a timestamp, the change, who made it, and whether the worker consented — which is the distinction predictive scheduling statutes turn on and which a mutable schedule cannot represent. From that, entitlements compute correctly and automatically rather than approximately. Give the worker their own version history, so what was promised and what changed is a record rather than a recollection. Then produce the analysis no frontline employer currently has: schedule volatility by site, by manager and by week — how much a published schedule changes before it is worked, and who is affected. That number is both a compliance exposure and an operational diagnosis, since high volatility usually indicates a forecasting or staffing problem upstream rather than a manager problem, and it is invisible today. Publish it internally, because a site whose schedules change constantly is imposing a cost on its workers that nobody is currently measuring.

## Who Feels the Pain
Workers whose lives are organised around a schedule that changes without record; managers held to predictive scheduling rules by a system that cannot evidence compliance; and employers whose exposure is computed from incomplete logs.

## Impact If Fixed
Schedule versioning is a schema change that makes predictive scheduling compliance computable rather than estimated, and it gives the worker a record of what they were promised. The volatility metric is the by-product with the broadest value: it locates the sites and weeks where schedule instability is worst, which is where both the compliance risk and the human cost concentrate.
