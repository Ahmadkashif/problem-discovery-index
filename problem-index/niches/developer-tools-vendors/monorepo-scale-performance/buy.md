# Incremental Computation and Tail Latency Discipline

**Niche:** [[niches/developer-tools-vendors/monorepo-scale-performance/profile|Monorepo & Scale Performance]]
**Industry:** [[industries/developer-tools-vendors|Developer Tools Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Incremental computation frameworks, content-addressed caching and tail latency engineering are all developed disciplines, and most developer tools recompute from scratch and report means.
**Tags:** #dynamic-programming #graph-theory #time-series-forecasting #descriptive-statistics #evaluation-metrics #confidence-intervals #automation #optimization-fundamentals
**Contested on:** Every serious competitor here is fighting to keep navigation, search and build responsive past the repository size where everything degrades — and whoever does that keeps the largest accounts, because the customers who cross that line are the most valuable and the least able to switch.

## The Problem
Doing only the work that a change invalidates is incremental computation, with mature frameworks and a clear theory. Not recomputing what somebody else already computed is content-addressed caching, standard in modern build systems. Making the ninety-ninth percentile acceptable rather than the mean is tail latency engineering, a well-developed discipline in serving systems. Most tooling in this category recomputes whole indexes, caches nothing across users, and reports averages.

## What Already Exists
Incremental computation frameworks with demand-driven recomputation; content-addressed storage and remote caching, proven in large build systems; distributed build execution; index sharding and partial loading techniques from search infrastructure; and the tail latency literature with its hedging and replication patterns. All published and much of it open.

## The Customization Gap
The adaptation is to code analysis over a changing repository. It requires: (1) correct dependency tracking at fine granularity, since incremental analysis that invalidates too much gains nothing and one that invalidates too little produces wrong answers, and code dependencies are subtle enough that both errors are easy; (2) cross-user caching, because in a monorepo most developers are analysing mostly the same code and the vendor is recomputing it per person — this is the single largest available saving and requires a shared, verifiable cache rather than a local one; (3) partial and lazy loading, so the editor is responsive on the part of the repository in use rather than after the whole thing is indexed, which is a design change rather than an optimisation; (4) degradation that is graceful and legible, since at sufficient scale something must give and a tool that says this operation is unavailable at this scope is far better than one that hangs; and (5) percentile reporting throughout, because the mean of a distribution dominated by small repositories describes nobody's experience of the problem.

## Target Customer
Developer tool vendors, build system and code search vendors, and the platform teams at large engineering organisations currently building this themselves.

## Impact If Solved
The techniques are mature and the largest customers are reimplementing them privately at considerable expense, which is a clear signal. Cross-user caching is the largest single saving and legible degradation is what makes the limits survivable.
