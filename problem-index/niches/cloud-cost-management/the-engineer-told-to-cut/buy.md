# Shift-Left Patterns From Security and Testing

**Niche:** [[niches/cloud-cost-management/the-engineer-told-to-cut/profile|The Engineer Told to Cut]]
**Industry:** [[industries/cloud-cost-management|Cloud Cost Management]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Security, testing and policy all moved into the pull request a decade ago with mature tooling and an established practice, and cost is still reported monthly to a portal.
**Tags:** #graph-theory #gradient-boosting #descriptive-statistics #evaluation-metrics #confidence-intervals #workflow-orchestration #worker-facing #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to show an engineer the cost of their own decisions at the moment they make them — and whoever does that takes the engineering organisation, because the alternative is a periodic instruction to cut something with no way to know what is safe.

## The Problem
Static analysis, dependency vulnerability scanning, infrastructure policy checks and test results all appear as comments on the pull request, at the moment the decision is being made, with a clear pass or fail and a specific remedy. This transformation happened across the industry over a decade and is now unremarkable. Cost has not made the journey: it remains a monthly report in a separate tool, describing decisions made weeks ago by people who have moved on.

## What Already Exists
Pull request annotation frameworks and check APIs; infrastructure-as-code parsers; policy-as-code engines; published price lists from every provider with programmatic access; cost estimation tools for infrastructure definitions, which exist in open source and are not integrated into the cost platforms; and the whole shift-left practice with its established conventions.

## The Customization Gap
The adaptation is to a cost estimate that depends on usage rather than only on configuration. It requires: (1) usage assumptions made explicit, since an instance's price is determinate and a data transfer or request charge depends on traffic the change does not specify — the honest approach is a range with the assumption stated, derived from the service's current behaviour; (2) the delta rather than the total, because the reviewer needs to know what this change costs rather than what the system costs, and the delta is the actionable number; (3) materiality thresholds, since annotating every pull request with a trivial figure trains people to ignore it, which is exactly how security scanning failed before it learned to suppress noise; (4) a policy layer for the cases that warrant blocking, such as an unbounded retention setting or a cross-region transfer in a hot path, expressed as rules rather than as warnings; and (5) attribution after the fact, comparing the estimate to what actually happened, which both improves the estimates and closes the loop for the engineer.

## Target Customer
Cost management vendors, developer platform teams, the infrastructure-as-code tooling ecosystem, and the policy-as-code vendors whose engines this would ride.

## Impact If Solved
An established delivery pattern moved security and testing into the moment of decision and cost has not followed, despite the infrastructure definition being right there in the change. Delta rather than total, with explicit usage assumptions, is the adaptation that makes the number useful to a reviewer.
