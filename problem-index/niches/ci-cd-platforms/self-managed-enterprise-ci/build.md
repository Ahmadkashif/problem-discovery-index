# The Server Nobody Will Replace

**Niche:** [[niches/ci-cd-platforms/self-managed-enterprise-ci/profile|Self-Managed & Enterprise CI]]
**Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An enterprise runs four thousand accumulated pipeline jobs on a heavily customised legacy server that everyone dislikes, and cannot migrate because nobody can say what the jobs do.
**Tags:** #graph-theory #bert #large-language-models #k-means-clustering #evaluation-metrics #confidence-intervals #compliance #automation
**Contested on:** Every serious competitor here is fighting to give an organisation hosted-grade pipelines inside its own boundary — with the evidence, the hardware and the control it requires — and whoever does that takes the enterprise, because the alternative is that they keep operating it themselves.

## The Problem
A bank runs several thousand build jobs on a server configured over twelve years, with a hundred plugins, jobs created by people who have left, shell steps calling scripts on network shares, and credentials embedded in configurations nobody wants to look at. Everyone agrees it should be replaced. Every migration attempt stalls at the inventory: which jobs are actually used, what do they build, what do they depend on, which are duplicates, and which are load-bearing for a release process nobody has documented. The estimate is two years, the risk is unbounded, and so the server persists and is patched.

## Why Nobody Has Built This
Migration tooling is offered as a job converter — translate this configuration to that syntax — which handles the mechanical part of a problem whose difficulty is entirely in the analysis. Understanding what a job does requires reading imperative scripts with external dependencies, which was not tractable to automate until recently. The vendors selling the target platform have limited incentive to invest in the specifics of the source, and the incumbent has none at all. And the customers are large, slow-moving and deeply risk-averse, which makes this a difficult market that is nonetheless substantial and captive.

## What to Build
Make the migration decidable before it is attempted. Inventory the estate from execution records rather than from configuration: which jobs have run in the last year, how often, triggered by what, producing what — which immediately reveals the large dead fraction these estates always carry, exactly as the legacy code comprehension niche finds. Analyse what each live job does, including the external scripts and shared resources it invokes, and classify it into the small number of patterns most jobs follow. Map the dependency structure between jobs, which is where the release process lives and is documented nowhere. Identify duplicates and near-duplicates, since these estates accumulate copies and consolidating them shrinks the problem substantially before any translation. Translate the mechanical majority automatically and route the genuinely bespoke minority to a person with the analysis attached. Verify equivalence by running old and new in parallel and comparing outputs, which is what makes a risk-averse organisation willing to switch. And sequence the migration by risk and dependency rather than alphabetically, so the estate shrinks continuously rather than in one terrifying step.

## Target Customer
Enterprise platform engineering teams operating legacy CI estates, the vendors selling the target platforms, and the consultancies performing these migrations by hand.

## Impact If Built
These migrations stall at the inventory rather than at the translation, and the inventory is derivable from execution records and job analysis. Parallel-run verification is what converts an unbounded risk into a checkable one for organisations that will not move without it.
