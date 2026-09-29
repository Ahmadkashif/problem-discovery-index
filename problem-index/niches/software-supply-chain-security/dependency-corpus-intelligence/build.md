# Three Questions, One Corpus, No Answers

**Niche:** [[niches/software-supply-chain-security/dependency-corpus-intelligence/profile|Dependency Corpus Intelligence]]
**Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** These vendors observe dependency graphs, fixes, dismissals, exploitations and upgrade outcomes across a large share of commercial software, and ship a severity score computed by somebody who has never seen the application.
**Tags:** #gradient-boosting #graph-theory #survival-analysis #k-means-clustering #evaluation-metrics #confidence-intervals #cross-validation #transfer-learning
**Contested on:** Every serious competitor that gets here is fighting to use a fleet-wide record of dependency graphs, dismissals, fixes and upgrade outcomes — and whoever does that can estimate real exploitability, real upgrade risk and real remediation effort, which are the three questions every finding raises.

## The Problem
Every finding raises three questions — does it matter, what will the fix break, how long will it take — and the tools answer none of them. The vendor holding the finding also holds: the dependency graphs of thousands of commercial applications, the record of which findings each customer fixed and which they dismissed with what reasoning, which components have been implicated in actual incidents, and how long the upgrade took in the projects that performed it. Those are the three answers. They are used to compute a severity score sourced from a public database.

## Why Nobody Has Built This
Cross-customer analysis has not been articulated as a governed capability, so it is avoided — although the useful representation here contains no customer code, only which public components are present and what the customer decided, which is a materially easier governance position than most corpus opportunities in this vault. Dismissal reasoning is captured inconsistently or not at all, because the tools treat a dismissal as a suppression rather than as a labelled observation. Upgrade outcomes are not instrumented. And the analytical investment competes with feature work whose value is demonstrable in a sales cycle.

## What to Build
Turn the fleet into the three answers. Collect dismissal reasoning as structured labels rather than as free-text suppressions, since a dismissal is an expert saying this finding does not apply and thousands of them across customers are the best available estimate of real-world applicability — this is the instrumentation change everything depends on and is cheap. Learn applicability: for a given component, vulnerability and usage pattern, what proportion of expert assessors concluded it did not apply, which is a far better prior than a published severity and is directly usable in prioritisation. Learn upgrade outcomes: how long this upgrade took, what proportion reverted, what broke — collected from the fleet and from the public corpus together, which answers the risk question the remediation niche needs. Learn real exploitation association, joining components to incidents where customers will share, which is sparse and is the most valuable label available. Represent everything structurally — public component identities and outcomes, never customer code — which makes the governance position statable publicly. Benchmark customers against comparable organisations on exposure and remediation, which is a question asked constantly. And publish the general findings, since a vendor that establishes what is actually exploitable has a position no competitor can reach from the same public database.

## Target Customer
The supply chain security vendors, primarily; and security leadership, who would buy the benchmarking and receive the improved prioritisation.

## Impact If Built
The three questions every finding raises are answerable from a corpus the vendors already hold and use to render a public score. Structured dismissal capture is the cheap instrumentation change that produces the applicability label, and the content-free representation makes the whole thing governable.
