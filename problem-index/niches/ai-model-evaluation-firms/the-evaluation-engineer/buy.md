# Build Reproducibility and Bisection Tooling

**Niche:** [[niches/ai-model-evaluation-firms/the-evaluation-engineer/profile|The Evaluation Engineer]]
**Industry:** [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software engineering built bisection, hermetic builds and lock files precisely to answer "what changed between these two runs", and evaluation pipelines pin almost nothing.
**Tags:** #automation #workflow-orchestration #data-integration #evaluation-metrics #compliance #worker-facing #quick-win #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to answer "did the model change or did the measurement change?" without a person spending a day on it — and whoever does that takes the account, because that question consumes most of an evaluation engineer's week.

## The Problem
Finding which change caused a behaviour difference between two points in time is a solved problem with a command. Automated bisection narrows it in logarithmic steps. Lock files pin the whole dependency set so a build is reproducible. Hermetic builds eliminate environmental variation entirely. Evaluation pipelines depend on a remote model that can change without notice, an item set in a shared document, a grader prompt in a config file, and a parser with implicit assumptions — and pin none of them.

## What Already Exists
Automated bisection over commit history with scripted verification; lock files pinning transitive dependencies exactly; hermetic and sandboxed build systems; content-addressed artefact caching with reproducibility checking; and flaky test detection with statistical repetition.

## The Customization Gap
The adaptation is to a pipeline whose most important dependency is a remote service outside anyone's control. It requires: (1) bisection over a multi-dimensional configuration space rather than a linear commit history, since five things changed and the search is over combinations — which is a modest generalisation of the standard algorithm and nobody has written it for this; (2) pinning what can be pinned and monitoring what cannot, because the model provider is not version-controllable and the honest response is a canary that detects when it moved; (3) statistical bisection, since each evaluation is noisy and a single run cannot decide a comparison — the flaky test literature's repetition approach is the right primitive and needs to be built into the search; (4) the item set treated as a locked dependency rather than a living document, which is a governance change more than a technical one and closes a common cause; and (5) cost-aware search, since each bisection step costs model calls and the algorithm should minimise spend rather than steps.

## Target Customer
Evaluation engineering teams, platform vendors, and the developer tooling ecosystem for whom stochastic multi-dimensional bisection is an unserved case.

## Impact If Solved
The tooling for "what changed between these two runs" is mature and assumes a linear, deterministic history. Statistical bisection over a multi-dimensional configuration space is a modest generalisation that nobody has built for this workload.
