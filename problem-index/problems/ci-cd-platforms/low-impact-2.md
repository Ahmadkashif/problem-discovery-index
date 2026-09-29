# Build Compute Cost Attribution

**Industry:** [[ci-cd-platforms|CI/CD Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Usage dashboards exist at every CI vendor and show minutes by repository, which is not a unit anyone can act on — so build spend is optimised by whoever happens to notice the invoice.
**Tags:** #gradient-boosting #k-means-clustering #time-series-forecasting #optimization-fundamentals #confidence-intervals #evaluation-metrics #revenue-impact

## The Problem
CI compute is billed by the minute and consumed by pipelines that grew by accretion. For an organisation of any size the total is substantial, and it rises steadily as repositories, branches and matrix dimensions multiply.

Nobody owns it. The platform team pays the bill and does not control the pipelines. Product teams write the pipelines and never see a cost. So the spend is optimised episodically, when someone senior notices the invoice, by asking teams to cut something — with no information about which changes would actually help.

The waste is largely structural and identifiable. Matrix builds running combinations nobody looks at. Full test suites on documentation-only changes. Long-running jobs on oversized runners chosen once and never revisited. Caches that never hit. Pipelines that run on every push to every branch including abandoned ones. Retried jobs from flaky tests.

Each is visible in the execution data. None is reported in a form that reaches the team that could fix it.

## What Already Exists
Usage dashboards showing minutes by repository, workflow and job are standard. Runner size selection is configurable. Concurrency limits and queue controls exist. Self-hosted runners let organisations trade platform cost for infrastructure cost. Spot and preemptible instance support is available in several products. Cost allocation tags exist in the cloud-native services.

## The Customisation Gap
Minutes by repository is not an actionable unit. What a team needs is spend attributed to the decisions that produced it — this matrix dimension, this test suite, this runner size, this trigger rule — with the saving from changing each.

Right-sizing is measurable and unmeasured. A job's actual CPU and memory utilisation determines whether the runner is oversized, and the utilisation data exists while the recommendation does not.

Waste identification is a set of straightforward queries nobody runs: pipelines triggered by changes that could not affect their outcome, matrix combinations whose results are never examined, jobs that always pass and have never caught anything, caches with near-zero hit rates.

Chargeback or at least showback is the organisational fix, and it requires attribution the platforms do not produce. A team that sees its own build spend behaves differently from one that does not, and every platform team knows this and cannot implement it.

## Impact If Solved
Build compute is a growing, unowned cost optimised by whoever notices the bill, and the waste is structural and identifiable in execution data. Decision-level attribution puts the information in front of the team that can act on it, which is the only mechanism by which this ever improves.
