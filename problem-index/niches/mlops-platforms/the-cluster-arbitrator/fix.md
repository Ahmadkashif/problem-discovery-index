# Reserved Eight, Using Two

**Niche:** [[niches/mlops-platforms/the-cluster-arbitrator/profile|The Cluster Arbitrator]]
**Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Researchers request accelerators by the number that once worked, jobs run for days using a fraction of what they hold, and the cluster is simultaneously fully allocated and half idle.
**Tags:** #descriptive-statistics #evaluation-metrics #time-series-forecasting #automation #revenue-impact #confidence-intervals #quick-win #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to schedule accelerators on what a job will actually need and be worth rather than on what its author requested — and whoever does that takes the account, because the cluster is the largest line in the budget and it is allocated by negotiation.

## The Problem
The cluster shows one hundred percent allocated and the utilisation telemetry shows accelerators averaging under thirty percent. Jobs requested eight because eight was what the example used, or because a previous job with a larger batch size needed eight, or because requesting more felt safer than being throttled. One job has held four accelerators for two days while its data loader starves them. Nobody is doing anything wrong and the organisation is buying capacity it already owns and is not using. Every fact needed to see this is in the telemetry.

## Why It's Still Broken
There is no feedback to the researcher — a job that over-reserves runs perfectly well, so nothing corrects the request. Utilisation is reported at cluster level, where the average conceals which jobs are responsible. Right-sizing a request requires knowing what the job will need, which the researcher genuinely does not. Asking for less carries a real risk of a failure or a slower run, while asking for more carries no cost to the person asking. And the platform engineer who can see the waste has no mechanism to act on it that does not become an argument.

## What a Fix Looks Like
Close the feedback loop, gently and with data. Report actual utilisation against reservation to the job's author when it completes, which is a small change, is not punitive, and on its own corrects a meaningful share of the over-requesting because most people simply do not know. Recommend a right-sized request for the next run of the same job, derived from what it used, so the researcher is given an answer rather than a criticism. Detect starved accelerators — high memory, low compute — and attribute the cause, since a data loading bottleneck is the most common reason a job wastes what it holds and it is fixable by the author in an afternoon once identified. Report waste in currency and in queue time imposed on others, because that is the framing that motivates and it is the honest cost. Make reservations elastic where the framework allows, so a job can release what it is not using. Rank teams by utilisation rather than by consumption, which changes what the leaderboard rewards. And set the default request from the job's own history rather than from a template, since the template is where the over-request originates.

## Who Feels the Pain
Researchers queueing for capacity that is allocated and idle; platform engineers who can see the waste and have no lever; and the finance functions buying accelerators to relieve a shortage that is partly an accounting artefact.

## Impact If Fixed
Nothing currently tells a researcher what their job actually used, and simply telling them corrects much of it. Reporting waste as queue time imposed on colleagues is the framing that moves behaviour where a utilisation percentage does not.
