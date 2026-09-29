# The On-Call ML Engineer

**Parent Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Category:** Underserved Audience
**Contested on:** Every serious competitor in this niche is fighting to make the page arrive with a diagnosis instead of a log file — and whoever does that takes the account, because the platform already recorded everything needed to produce one.

## Profile
**Market Size:** ~$180M US in loaded on-call cost and attrition
**Share of Parent Industry:** ~6% of category revenue equivalent
**Digital Adoption:** None — the page is a link to logs
**Target Buyer:** ML engineering leaders, who feel it as retention
**Automation Potential:** High — the diagnostic signals are all recorded

## What Makes This a Distinct Niche
Machine learning pipelines fail at night, and the person paged is an ML engineer who did not sign up for an operations rota and is not supported by one. The page says a task failed. The platform recorded the exception, the resource state, the upstream task outcomes, the input data statistics and the last successful run of the same pipeline — and presents a link to a log file. The engineer reads logs, works out that an upstream table was empty because a source system was late, and reruns the job. That sequence repeats across organisations nightly, and roughly half of these pages resolve to a small number of recurring causes that the platform could identify. This is the category's own users being served worst by it.

## Current Tools & Gaps
Orchestrator alerting on task failure, log aggregation, retry policies, and generic incident tooling. The gaps: no diagnosis attached to the page; no distinction between a failure that needs a person now and one that a retry or a morning fix resolves; no awareness of upstream data readiness, which is the most common cause; no memory of how the same failure was resolved last time; and no measure of on-call load, so the burden is invisible to the people who could reduce it.

## Problems
- [[niches/mlops-platforms/the-on-call-ml-engineer/build|🔨 Build: Paged at Three to Read Logs]]
- [[niches/mlops-platforms/the-on-call-ml-engineer/buy|🛒 Buy: Incident Response Practice From Site Reliability]]
- [[niches/mlops-platforms/the-on-call-ml-engineer/fix|🔧 Fix: The Page That Did Not Need a Person]]
