# A Model Version Change Moves Billions and Nobody Can Say Which Assumption Did It

**Niche:** [[niches/public-adjusters/catastrophe-modelling-firms/profile|Catastrophe Modelling Firms]]
**Industry:** [[industries/public-adjusters|Public Adjusters]]
**Type:** Fix (Pain Point)
**One-liner:** A new model version raises a carrier's hurricane loss estimate by thirty per cent, and the explanation is a change document rather than a decomposition.
**Tags:** #evaluation-metrics #causal-inference #compliance #automation #workflow-orchestration

## The Problem
Catastrophe models are updated every few years. A new version incorporates revised hazard science, updated vulnerability functions, new event sets, changed demand surge assumptions, and refreshed engineering research. When it ships, clients' modelled losses move — sometimes by tens of per cent.

Those movements have enormous consequences. Reinsurance is bought against them. Capital is held against them. Rate filings are built on them, and a regulator will ask why the number changed. Rating agencies ask. Boards ask.

The answer arrives as documentation: a description of what changed in the model, often running to hundreds of pages, plus aggregate impact analysis by region and peril. What is generally not available is an attribution — for this client's portfolio, this much of the change came from the hazard update, this much from vulnerability, this much from the event set, this much from demand surge.

Without attribution, a client cannot tell whether a thirty per cent increase reflects better science about their specific exposure or a conservative global assumption they might reasonably question. They cannot form a view about whether to adopt the new version, blend it, or argue with it. And the modelling firm's own scientists, who understand each change individually, often cannot answer the composite question quickly for a specific portfolio either.

The same problem appears inside the firm during development. When a candidate version produces an unexpected result on a validation portfolio, tracing which change caused it means rerunning combinations by hand.

## Why It's Still Broken
Model components are interdependent. Vulnerability functions are recalibrated against the new hazard, so decomposing the change into independent contributions is not simply a matter of toggling one at a time — the components are not separable in the way clients want them to be. This is a real technical objection, and it has served as a reason not to attempt an approximation that would still be far more informative than nothing.

Computation is expensive. Running a large portfolio through a catastrophe model is costly, and attribution requires many runs. That was a stronger constraint a decade ago than it is now.

And there is a commercial edge to it. A firm that could show a loss increase was driven mainly by a conservative demand surge assumption rather than by hazard science would invite an argument it currently does not have to have.

## What a Fix Looks Like
**Build attribution into the release process.** Run a standard set of reference portfolios through ordered component swaps, and publish the decomposition alongside the version. Even with interdependence — handled by averaging over orderings, the standard approach to exactly this attribution problem — the result is vastly more informative than a change log.

**Make it available per portfolio.** Clients care about their own exposure, not a reference portfolio. Offering attribution as a service at version transition is a product, not just a disclosure.

**Version and date every assumption as data.** Demand surge factors, vulnerability curves, event rates and secondary uncertainty parameters should be addressable, comparable objects rather than descriptions in a document, so that any two versions can be diffed mechanically.

**Give scientists the same tool.** The internal development question — which change caused this — is the same computation. Building it for internal use first is how it gets built at all, and it pays for itself in development cycle time.

**Report which components dominate uncertainty.** For a given portfolio, saying that vulnerability contributes most of the spread tells a client exactly where to invest in better exposure data. That is genuinely useful advice and no vendor currently gives it.

## Who Feels the Pain
Chief risk officers explaining a moved number to a board and a regulator; reinsurance buyers deciding whether to adopt a version mid-programme; the modelling firm's own client-facing scientists, answering the question portfolio by portfolio from intuition; and the development teams, who cannot cheaply trace an unexpected result to its cause.

## Impact If Fixed
Model version transitions are the most disruptive recurring event in this business and the largest source of client friction. Turning an opaque revaluation into an explained one changes the relationship from a negotiation into a technical discussion — and it is the prerequisite for the forecast validation work, which cannot proceed without a versioned, comparable record of what each model version actually assumed.
