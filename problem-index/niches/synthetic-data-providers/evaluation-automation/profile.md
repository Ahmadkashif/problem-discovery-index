# Evaluation Automation

**Parent Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to make evaluation a standard, reproducible run that a customer can execute themselves — and whoever does that takes the category's credibility, because a claim the buyer cannot reproduce is a claim they have to take on faith.

## Profile
**Market Size:** ~$190M US
**Share of Parent Industry:** ~13% of category revenue
**Digital Adoption:** Low — evaluations exist and are run ad hoc by the interested party
**Target Buyer:** Generation vendors and their customers jointly
**Automation Potential:** Very High — every component is a deterministic computation

## What Makes This a Distinct Niche
Every metric the category needs already exists in the literature: fidelity comparisons, downstream task performance, constraint violation rates, membership and attribute inference attacks, linkage attacks. What does not exist is a standard harness that runs all of them the same way every time, on any dataset, by any party. Instead each vendor implements a subset, chooses the configuration, runs it themselves, and reports selectively. Two vendors' numbers cannot be compared, a customer cannot reproduce either, and nothing is tracked across generator versions. The entire content is automatable — it is computation over two datasets — and the reason it has not been is that standardising evaluation removes the freedom to report favourably.

## Current Tools & Gaps
Open-source evaluation libraries with partial metric coverage, vendor-internal evaluation code, and research implementations of the attacks. The gaps: no common protocol, so results are incomparable; evaluation is run by the vendor rather than by or for the buyer; attack strength is a free parameter and the interested party sets it; results are not versioned, so a generator regression is invisible; and nothing runs continuously, so a model drifting away from a changing source goes unnoticed.

## Problems
- [[niches/synthetic-data-providers/evaluation-automation/build|🔨 Build: Every Metric Exists and No Two Runs Are Comparable]]
- [[niches/synthetic-data-providers/evaluation-automation/buy|🛒 Buy: Benchmark Harnesses and Continuous Evaluation Infrastructure]]
- [[niches/synthetic-data-providers/evaluation-automation/fix|🔧 Fix: The Attack Run by the Party Selling the Result]]
