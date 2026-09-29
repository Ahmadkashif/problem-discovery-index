# Nobody Measures Schedule Survival

**Niche:** [[niches/restaurant-tech-platforms/labor-scheduling-availability/profile|Labour Scheduling & Availability]]
**Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A restaurant publishes a schedule and then modifies it all week, and no product reports what share of published shifts were worked as published — which is the only number that describes whether scheduling is working.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #change-point-detection #worker-facing #quick-win #compliance
**Contested on:** Every serious competitor in restaurant scheduling is fighting to produce a schedule that respects who can genuinely work, so the manager stops spending the week on the phone finding cover — and whoever gets the share of shifts that survive the week highest takes the account.

## The Problem
Monday's published schedule and Sunday's actual timesheet are different documents. Shifts were swapped, cut, extended, covered and no-showed. The manager knows the week was chaotic and cannot quantify it. The scheduling product reports hours and labour cost, which come from the timesheet, so the published schedule — the thing the product actually produced — is never evaluated against what happened. Nobody at the vendor or the restaurant knows whether schedules are getting better or worse, or which employees, shifts or stations generate the churn.

## Why It's Still Broken
Comparing the two requires keeping the published version as an immutable artefact, and most systems treat the schedule as a mutable object that is edited in place — so by Sunday, the Monday version no longer exists. That is a one-line design decision made years ago in every product in the category, with the consequence that the category cannot measure its own output. There is also no demand from customers, because managers experience schedule churn as the normal texture of the job rather than as a metric that could improve.

## What a Fix Looks Like
Snapshot the schedule at publication and compare. Report the share of published shifts worked as published, and decompose the rest into swaps, cuts, extensions, call-outs and no-shows — each of which has a different cause and a different remedy. Break it down by employee, by day, by station and by how far in advance the shift was published, since notice is the variable most under the manager's control and the one predictive scheduling statutes are built around. Show the manager where the churn concentrates, which is usually a small number of people and a small number of shift patterns. Give employees their own view too, because a worker who can see their own swap and call-out pattern has information about their own reliability that nobody currently gives them. In covered jurisdictions the same snapshot is the compliance record, which makes this a requirement rather than a nicety.

## Who Feels the Pain
Managers who lose hours a week to churn they cannot characterise; employees covering shifts for a rota that never matched their lives; and vendors who cannot demonstrate that their scheduling product produces better schedules than a spreadsheet.

## Impact If Fixed
Schedule survival is the category's missing metric, and it costs a snapshot to compute. It identifies where churn concentrates, gives predictive scheduling compliance its evidence for free, and provides the evaluation signal that every other improvement in this niche — including the inferred availability model — needs in order to be shown to work.
