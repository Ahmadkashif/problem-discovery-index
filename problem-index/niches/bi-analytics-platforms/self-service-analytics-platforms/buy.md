# Usage Analytics the Platforms Do Not Turn on Themselves

**Niche:** [[niches/bi-analytics-platforms/self-service-analytics-platforms/profile|Self-Service Analytics Platforms]]
**Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Product analytics — funnels, cohorts, abandonment, feature adoption — is a mature category that analytics platforms sell the ingredients for and do not apply to their own usage.
**Tags:** #descriptive-statistics #survival-analysis #k-means-clustering #logistic-regression #evaluation-metrics #confidence-intervals #hypothesis-testing #automation
**Contested on:** Every serious competitor here is fighting to let someone who is not an analyst get a correct answer without one — and that contest splits by delivery surface rather than by capability, which is why this niche is not terminal and is decomposed below.

## The Problem
Understanding why users of a product do not complete the thing the product exists for is product analytics, practised by every software company with a growth team and supported by a mature tool category. BI platforms — which supply the infrastructure that product analytics runs on — report their own usage as licence counts and view counts, and cannot say where a user's attempt to answer a question broke down.

## What Already Exists
Funnel and cohort analysis, abandonment measurement, session replay, feature adoption tracking and retention curves are all standard, with commercial products and open implementations. Survival analysis handles time-to-adoption and churn within the estate. Clustering identifies user archetypes. BI platforms log every interaction in detail already, and several expose that log as a queryable dataset. Nothing needs building except the analysis.

## The Customization Gap
The adaptation is to analytical work rather than to a consumer funnel. It requires: (1) a session model built around a question rather than around a visit, since the meaningful unit is an attempt to answer something and it may span several assets, several filters and an export — stitching that into one attempt is the core modelling decision; (2) an outcome definition, which is the hard part and where honesty matters: an attempt that ends in an export to a spreadsheet is not obviously a success, and an attempt followed by a message to an analyst is clearly a failure, and both are observable if the platform is willing to look; (3) archetype segmentation, because an analyst's session and a department head's session are different activities and pooling them hides both; (4) asset-level diagnostics, so the output is which dashboards cause abandonment rather than an aggregate rate, since the aggregate is not actionable; and (5) a willingness to report the uncomfortable number, which is the actual barrier — the analysis is easy and the finding is that the platform is not doing what it was bought for.

## Target Customer
Data leadership running a self-service programme, the BI vendors' own product organisations, and the data observability and catalogue vendors for whom platform usage is an adjacent dataset.

## Impact If Solved
Every technique is mature, the data is unusually complete, and the analysis has not been done because of what it would show. The question-level session model and an honest outcome definition are the two pieces that separate this from another usage dashboard.
