# Minutes by Repository Is Not a Decision

**Niche:** [[niches/ci-cd-platforms/build-spend-attribution/profile|Build Spend Attribution]]
**Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Usage dashboards exist at every CI vendor and show minutes by repository, which is not a unit anyone can act on, so build spend is optimised by whoever happens to notice the invoice.
**Tags:** #descriptive-statistics #gradient-boosting #change-point-detection #k-means-clustering #evaluation-metrics #confidence-intervals #revenue-impact #automation
**Contested on:** Every serious competitor here is fighting to say where build spend actually goes in units somebody can act on — and whoever does that takes the cost conversation, because minutes by repository is not a unit anyone can act on.

## The Problem
A platform lead is asked to reduce build spend. The dashboard shows minutes by repository: the monolith is the largest, which everybody already knew and nobody can do anything with. What they need is that the integration test step accounts for a third of it, that a quarter of all runs are re-runs of identical changes, that the nightly job that nobody reads costs more than the entire front-end estate, and that a commit six weeks ago added a step consuming four hundred hours a month. All of that is computable from the platform's own records, which attribute every minute to a job, a step, a trigger and a commit.

## Why Nobody Has Built This
Usage reporting was built for billing and plan limits, where the repository and the workflow are the relevant units, and it has not been revisited for optimisation. Finer attribution requires no new data at all — the minutes are already attributed to steps and commits — but it produces a report that shows customers how to spend less, which is a weak commercial incentive for a vendor billing by the minute. And on the customer side, build cost sits between platform engineering and finance with no single owner, so nobody has asked.

## What to Build
Report in units that correspond to decisions. Cost by pipeline step and by test, which is where the reduction actually happens and immediately identifies the small number of steps consuming most of the budget. Cost by trigger type — pull request, merge, scheduled, manual — which regularly reveals that scheduled jobs nobody reads are a large share of the total. Re-runs separated from first runs and attributed to their cause, since in a flaky estate re-runs are a substantial and entirely avoidable cost and are currently indistinguishable from useful work. Redundant work: minutes spent on steps whose inputs had not changed, which quantifies the caching opportunity concretely. Cost per change delivered and per merged pull request, which is the unit a leader can compare across teams and over time and which no vendor reports. Attribution of increases to the commit that caused them, using change-point detection per step so a cost rise is traced to a configuration change rather than discovered as a variance. And a projection, so a proposed pipeline change comes with its cost before it is merged rather than after.

## Target Customer
Platform engineering teams and finance functions facing build spend, and the cost management vendors for whom the incumbents' billing incentive is the opportunity.

## Impact If Built
Every minute is already attributed and the reporting stops one level above where action is possible, which makes this a reporting change with a direct financial return. Re-run separation and redundant-work quantification are usually the two largest and most surprising findings.
