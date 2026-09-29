# Product Analytics, Pointed Inward

**Niche:** [[niches/internal-developer-platforms/platform-as-product/profile|Platform as Product]]
**Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Funnel analysis, activation measurement and retention curves are standard product analytics, deployed in the same building by the company's own product teams, and the platform team counts onboarded services.
**Tags:** #survival-analysis #logistic-regression #k-means-clustering #hypothesis-testing #confidence-intervals #evaluation-metrics #descriptive-statistics #automation
**Contested on:** Every serious competitor in this niche is fighting to make a platform team behave like a product team — measuring adoption, abandonment and what developers do instead — and whoever does that takes the platform account, because the category error explains most of its failures.

## The Problem
The company's product organisation runs a mature analytics practice: funnels, cohorts, activation definitions, retention curves and experiments. The platform team, two floors away, building a product used by several hundred internal developers, reports the number of services onboarded. The tooling, the practice and the practitioners are all in the same organisation, and the distance between them is a framing error rather than a capability gap.

## What Already Exists
Product analytics platforms with funnel, cohort and retention analysis; activation metric methodology; survival analysis for time-to-adoption and retention; experimentation infrastructure; and the product management practice itself, staffed and operating in the same company.

## The Customization Gap
The adaptation is to a captive, small, identifiable user base. It requires: (1) small-sample methods, since the population is hundreds rather than millions and conventional significance testing will find nothing — which argues for qualitative follow-up on every abandonment rather than statistical inference, and is a genuine advantage since every user is reachable; (2) a captive-audience correction, because internal users may adopt under mandate rather than preference and an adoption metric that cannot distinguish the two is measuring compliance; (3) identifiable users, which permits direct follow-up — a platform team can simply ask the three teams that abandoned at step four, which no consumer product team can do and which is the most efficient research available here; (4) alternatives as an observable, since the competing option is the team building it themselves and that is visible in their repository, which has no analogue in consumer analytics; and (5) an ethical posture, since measuring identifiable colleagues' usage is different from measuring anonymous users and should be transparent to them.

## Target Customer
Platform engineering teams, developer experience functions, and the platform tooling vendors who could ship this instrumentation by default.

## Impact If Solved
The practice, the tooling and the practitioners are all in the same organisation and the platform team is not using any of them. The identifiable user base makes qualitative follow-up the efficient method here, and observing what teams built instead is a signal consumer analytics never has.
