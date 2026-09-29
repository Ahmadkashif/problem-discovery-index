# Scorecards That Mark Teams Down and Fix Nothing

**Niche:** [[niches/internal-developer-platforms/golden-path-drift/profile|Golden Path Drift]]
**Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Maturity scorecards measure how far a service has drifted from the standard, present it as a score, and leave every team to fix it themselves — which is why they are resented.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #logistic-regression #worker-facing #quick-win #automation
**Contested on:** Every serious competitor here is fighting to make a platform improvement reach the services that already exist — and whoever does that takes the platform, because a golden path that only applies at creation improves nothing after the first month.

## The Problem
The platform introduces maturity scorecards. Each service receives a score against a set of standards. Teams see a red mark for something they did not know was a standard, that was introduced after their service was built, that would take a day to fix, and that they were not asked about. The scorecard is accurate and the response is resentment, because it transfers work to the team while presenting itself as an assessment. Adoption of the platform declines slightly, the scores improve marginally among teams with capacity, and the platform team concludes the estate is immature.

## Why It's Still Broken
Scorecards are easy to build — the checks are simple and the data is available — and they produce a satisfying dashboard, which is why they became a standard feature. They measure conformance without providing remediation, which is the asymmetry that makes them resented: the platform team gets visibility and the application team gets work. The standards are also frequently introduced without consultation and applied retroactively, which is experienced as a rule change after the fact. And the resentment is not measured, so the cost to the platform's relationship is invisible.

## What a Fix Looks Like
Ship the fix with the finding. Provide automated remediation for every check that can be remediated automatically, which is most of them, and open the change rather than reporting the gap — this is the single change that converts a scorecard from an assessment into a service. Where automation is not possible, provide the specific steps rather than the standard's name. Consult before introducing a standard, and apply new ones prospectively with a stated window for existing services, since retroactive rules are the specific thing that generates the resentment. Weight by consequence, so a security gap and a missing documentation link are not presented identically — a scorecard that treats them equally teaches teams to ignore all of it. Show the platform team's own score, since the platform's components are services too and exempting them is noticed. Measure the response: whether scores improve, whether the improvement is the platform's automation or the team's effort, and whether adoption of the platform changes — which is the honest assessment of whether the scorecard is helping. And frame it as the platform's backlog rather than the team's, because a standard that most services fail is a platform problem rather than four hundred team problems.

## Who Feels the Pain
Application teams handed work by a dashboard; platform teams whose relationship erodes for a feature that was easy to build; and organisations whose estate conformance does not improve despite being measured continuously.

## Impact If Fixed
Automated remediation converts a scorecard from an assessment into a service and is available for most checks. Prospective application of new standards removes the specific grievance, and treating a widely-failed standard as the platform's backlog is both accurate and the framing that makes it work.
