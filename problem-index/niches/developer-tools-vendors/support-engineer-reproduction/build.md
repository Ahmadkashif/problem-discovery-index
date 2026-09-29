# Reproducing a Failure in an Environment You Cannot See

**Niche:** [[niches/developer-tools-vendors/support-engineer-reproduction/profile|Support Engineer Reproduction]]
**Industry:** [[industries/developer-tools-vendors|Developer Tools Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Developer tool support engineers spend their days trying to recreate a failure in an environment they cannot see, described by a developer who has already worked around it.
**Tags:** #descriptive-statistics #k-means-clustering #bert #logistic-regression #evaluation-metrics #confidence-intervals #worker-facing #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to let a support engineer see the environment a failure happened in rather than imagining it — and whoever does that takes the support organisation, because reproduction is where the entire cost of developer tool support sits.

## The Problem
A ticket says the extension stops responding on large projects. The support engineer asks for versions and receives three of the eight that matter. They build a large project locally and cannot reproduce it. They ask for logs and get the last two hundred lines, which begin after the failure. They ask for a sample project and are told it is proprietary. Four days elapse. The developer, who worked around it on day one by disabling a feature, stops replying. The ticket is closed as cannot reproduce, and the same failure arrives from another customer a fortnight later.

## Why Nobody Has Built This
Diagnostic capture was designed as a support afterthought — a command the user runs when asked — rather than as something the product does at the moment of failure, which is the only moment the relevant state exists. Capturing environments raises real privacy and proprietary-code concerns, which are solvable with redaction and have instead been treated as a reason not to try. Support tooling in this industry is the generic ticketing stack, which knows nothing about environments. And the cost lands on support engineers rather than on a product line, so it has never competed for roadmap attention.

## What to Build
Capture the environment at the moment of failure, safely. Structured environment capture triggered by the failure rather than requested afterwards: operating system, runtime and tool versions, the full dependency graph with resolved versions, extension and plugin inventory, relevant configuration, resource state, and the log window around the event — assembled automatically, presented to the developer for review, and redacted by default for anything resembling a credential, a path containing a customer name, or proprietary source. Make it one action for the developer, since every additional step loses a proportion of them. On the support side, reconstruct a comparable environment automatically from the capture, which is what containers exist for and which turns four days of guessing into a starting point. Cluster captures across tickets, so that an environment-specific failure affecting many customers is recognised as one incident rather than diagnosed independently forty times — this is the same cross-tenant aggregation the connector-drift niche describes and it is equally unused here. Surface similar prior tickets with their resolutions at triage. And analyse the cannot-reproduce population in aggregate rather than closing it, because that is where the systematic capture gaps show up.

## Target Customer
Developer tool vendors' support organisations, the engineering teams receiving escalations that are really reproduction requests, and the support platform vendors for whom developer tooling is an underserved vertical.

## Impact If Built
Time to reproduce dominates the cost of support in this category and the state needed to remove it exists only at the moment of failure, which nothing captures. Cross-ticket clustering converts a stream of individual mysteries into a small number of identified environment problems.
