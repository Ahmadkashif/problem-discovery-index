# Combinatorial Test Design, Forty Years Old

**Niche:** [[niches/qa-test-automation-vendors/browser-device-grids/profile|Browser & Device Grids]]
**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Combinatorial test design has established methods for covering an interaction space with a small number of configurations, and grid matrices are chosen by listing the popular ones.
**Tags:** #combinatorics-and-counting #optimization-fundamentals #dynamic-programming #evaluation-metrics #confidence-intervals #hypothesis-testing #cross-validation #automation
**Contested on:** Every serious competitor here is fighting to offer the combinations that actually matter, on environments that behave like real ones, at a price per parallel session that beats running a lab — and whoever does that takes the grid account, because the alternative is self-hosting.

## The Problem
Covering a large configuration space with a small number of test configurations is combinatorial test design, with established methods, published tooling and empirical evidence that most defects involve interactions between few factors. A browser and device matrix is exactly such a space — engine, version, operating system, screen size, input mode — and is covered by choosing the combinations with the largest market share, which is not a covering design and leaves interaction gaps while duplicating coverage elsewhere.

## What Already Exists
Combinatorial interaction testing with covering array generation tools; the empirical work establishing that defects predominantly involve interactions between a small number of factors; constrained covering array methods for handling infeasible combinations; and the selection and prioritisation literature. All published and several implementations are free.

## The Customization Gap
The adaptation is to browser and device configurations with unequal importance. It requires: (1) weighting by the customer's own user distribution, since a covering array treats all factor values as equal and real exposure is enormously skewed — an untested combination used by nobody is not a gap; (2) a factor model that reflects how these environments actually differ, since engine and version are the factors that determine behaviour and device model frequently is not, which means the naive factor set produces a matrix that is large and not more informative; (3) empirical validation against observed failures, because the theory says few-factor interactions dominate and the category can check that directly from its own failure history and has not; (4) constraint handling for infeasible combinations, which are numerous here; and (5) cost as an explicit budget, since the practical question is the best matrix for a given spend rather than the smallest covering array.

## Target Customer
Grid vendors, quality engineering functions with large matrices, and the test design tooling community.

## Impact If Solved
A forty-year-old design discipline addresses exactly this selection problem and the practice is to list popular combinations. Weighting by the customer's own user distribution and using the right factor model are the two adaptations that make the resulting matrix both smaller and better.
