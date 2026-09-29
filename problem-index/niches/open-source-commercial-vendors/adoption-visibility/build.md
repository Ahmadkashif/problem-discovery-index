# A Build Cache and a Production Cluster Look Identical

**Niche:** [[niches/open-source-commercial-vendors/adoption-visibility/profile|Adoption Visibility]]
**Industry:** [[industries/open-source-commercial-vendors|Open Source Commercial Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The companies deriving the most value from the software are often ones the vendor has never heard of, and every commercial decision is made from download counts that conflate a build cache with a production cluster.
**Tags:** #bert #k-means-clustering #logistic-regression #graph-theory #evaluation-metrics #confidence-intervals #revenue-impact #data-integration
**Contested on:** Every serious competitor in this niche is fighting to tell an open-source vendor who is actually running their software and how — and whoever does that takes the commercial function, because every decision it makes is currently based on download counts.

## The Problem
A vendor's board deck reports forty million downloads last quarter, up eighteen percent. Most of those are continuous integration pipelines pulling the same image repeatedly. Somewhere in the remainder are several hundred organisations running the software in production at meaningful scale, of whom the vendor has identified perhaps thirty. The sales team prospects from inbound interest and conference conversations. The product team prioritises from issue volume, which reflects the loudest users rather than the largest. And the question of whether the open-source strategy is producing commercial value has no answer beyond a correlation between two numbers nobody trusts.

## Why Nobody Has Built This
Telemetry is the obvious answer and is genuinely contentious: the community's suspicion is well founded historically, and a vendor that ships phone-home telemetry badly pays a reputational cost that exceeds the analytical benefit — which has led most to ship it disabled, which produces a biased sample of exactly the users who care least. The public signal route requires assembling a dozen scattered sources and doing entity resolution onto companies, which is real work with no obvious owner. And the category has accepted download counts as the metric for long enough that the inadequacy is background rather than a problem.

## What to Build
Assemble the picture from both routes, and be honest about each. On the telemetry side, design for legitimacy rather than for completeness: an explicit, documented, inspectable payload; opt-in with a clear statement of what is sent and what is returned to the user in exchange; no identifiers that could not be published; and a genuine benefit to the operator, since a telemetry mechanism that gives the user something — version currency, a configuration check, a security advisory relevant to their deployment — is one people enable. On the public side, mine what is already visible: issues and discussions mentioning company context, public repositories depending on the project, job postings requiring it, conference talks, public container manifests and configuration in public code — and resolve them onto organisations, which is entity resolution over noisy text and is the substantial analytical work. Classify by deployment stage, since evaluation, staging and production are entirely different signals and are currently one number. Estimate scale where it is inferable. Then connect signals to commercial outcomes, since the point is to know which signals predict a purchase and nobody has established that. And publish the methodology, because in this category a measurement whose provenance is unclear will be treated as surveillance.

## Target Customer
Commercial and product leadership at open-source companies, foundations seeking to understand their projects' adoption, and the developer analytics vendors serving this market poorly.

## Impact If Built
Every commercial decision in the category rests on a metric that conflates a build cache with a bank, and both a legitimate telemetry path and an abundant public corpus exist. Designing telemetry for legitimacy rather than completeness is what makes the first viable, and deployment-stage classification is what makes any of it commercially useful.
