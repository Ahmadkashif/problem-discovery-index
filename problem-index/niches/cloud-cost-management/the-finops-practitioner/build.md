# A Week Spent Chasing and Explaining

**Niche:** [[niches/cloud-cost-management/the-finops-practitioner/profile|The FinOps Practitioner]]
**Industry:** [[industries/cloud-cost-management|Cloud Cost Management]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** FinOps practitioners spend their week asking engineering teams to tag resources and explaining variances they cannot investigate, which is neither the analysis they were hired for nor work that changes anything.
**Tags:** #change-point-detection #gradient-boosting #k-means-clustering #descriptive-statistics #evaluation-metrics #confidence-intervals #worker-facing #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to remove the chasing and the variance archaeology from a FinOps practitioner's week — and whoever does that takes the function, because those two activities are most of what it currently does.

## The Problem
Monday is the variance report: spend is up eleven percent, and establishing why means identifying which resources moved, working out which team owns them, messaging those teams, waiting, and assembling the answers into an explanation by Thursday. Tuesday and Wednesday include the tagging follow-ups: a list of untagged resources, a message to each owning team, a promise, and the same list next month slightly longer. Friday is the report. The analysis the role exists for — architectural opportunities, commitment strategy, unit economics — happens when there is time, which there is not.

## Why Nobody Has Built This
The tools were built to report rather than to act, so everything downstream of the report is a human. Variance investigation requires joining the cost movement to the change that caused it, which is the unmade join that appears throughout this vault — deployment records and configuration changes on one side, billing on the other. Tag chasing exists because ownership is demanded rather than inferred, which the attribution niche addresses. And the practitioner's time is a salary rather than a product cost, so the burden has never appeared in a vendor's roadmap.

## What to Build
Automate the two activities that consume the week. For variance: detect the change point per service and per resource group, join to deployments, configuration changes, scaling events and business events, and produce the explanation automatically — this is the same change-stream join the observability and CI cost niches need, and it converts a four-day investigation into a report that arrives with the variance. For tagging: infer ownership rather than chasing it, which is the attribution capability, and reserve human follow-up for the genuinely ambiguous minority. Then automate the follow-up that remains: route each item to the owning team in their own tools with a specific ask and a deadline, track it, and escalate on a schedule, rather than having the practitioner maintain a spreadsheet of who has not replied. Assemble the recurring reports from the sources automatically, since the practitioner's report is the same shape every month. And measure the function properly — savings identified, savings realised, time to explain a variance, coverage achieved — since a function judged on total spend it does not control cannot demonstrate its own value.

## Target Customer
FinOps and cloud economics functions, cost management vendors whose product ends at the report, and the platform teams who receive the chasing.

## Impact If Built
The two activities consuming the practitioner's week are individually automatable and collectively constitute the job, which leaves no time for the analysis the role exists for. The variance join is the same unmade connection that recurs across this vault, and automating it returns several days a month.
