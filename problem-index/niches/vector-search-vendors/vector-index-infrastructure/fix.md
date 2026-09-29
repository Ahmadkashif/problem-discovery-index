# Benchmarks Run on Corpora Nobody Has

**Niche:** [[niches/vector-search-vendors/vector-index-infrastructure/profile|Vector Index Infrastructure]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Published vector benchmarks use static academic datasets with uniform query distributions, and every real deployment is mutating, filtered and skewed, so the numbers do not predict anything a buyer will experience.
**Tags:** #evaluation-metrics #descriptive-statistics #hypothesis-testing #probability-distributions #confidence-intervals #k-nearest-neighbors #quick-win #monte-carlo-methods
**Contested on:** Not terminal — the contest differs by whether the buyer is acquiring capacity or avoiding a system, and the decomposition is recorded in the profile.

## The Problem
A buyer compares vendors on published benchmarks: recall against queries per second on a standard dataset, a few million vectors, loaded once and queried. Their actual deployment inserts continuously, deletes on a retention policy, filters most queries by tenant and date, and has a query distribution where a small number of patterns dominate and the rest is a long tail. Every one of those differences changes the ranking, several of them substantially. The benchmark is honest, carefully run, and predicts almost nothing about the system the buyer will operate.

## Why It's Still Broken
Static benchmarks are reproducible and comparable, which is what a benchmark is for, and adding mutation and filtering makes results harder to compare across vendors. The academic datasets are free and familiar. Vendors have no incentive to publish results under the conditions where their system is weakest. And buyers accept the benchmarks because constructing a realistic one themselves is a project they do not have time for.

## What a Fix Looks Like
Benchmark the conditions people actually run. Add a mutation workload as a standard dimension — continuous insert, update and delete at realistic rates — since every deployment has one and it is the condition under which approximate indexes degrade most and are measured least. Add filtered queries as a standard dimension, because most production queries carry a metadata filter and the interaction between filtering and approximate search is where systems differ most dramatically. Use skewed query distributions drawn from realistic access patterns rather than uniform sampling from the dataset, which is the assumption that flatters caching behaviour most. Report recall over time under mutation rather than at load, which is the number that predicts what an operator will live with. Include cost in the reported frontier, since recall against queries per second omits the axis the buyer is actually optimising. Publish a harness a customer can run on their own corpus, which is the only fully honest answer and is cheap to provide. And report the variance across runs, since these systems are sensitive to build order and single-run comparisons between close competitors are frequently meaningless.

## Who Feels the Pain
Buyers who chose on benchmarks and discovered the ranking inverts under their workload; vendors whose strength under mutation goes unrewarded; and operators living with a recall number nobody predicted.

## Impact If Fixed
Mutation and filtering are universal in production and absent from every published benchmark, and they are exactly where systems diverge. Recall over time under mutation is the number that predicts what an operator will actually live with.
