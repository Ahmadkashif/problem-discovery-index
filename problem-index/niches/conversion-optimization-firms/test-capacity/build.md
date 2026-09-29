# Spending the Tests Where They Can Work

**Niche:** [[niches/conversion-optimization-firms/test-capacity/profile|Test Capacity Allocation]]
**Industry:** [[industries/conversion-optimization-firms|Conversion Optimization Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The scarce resource is detectable tests and it is allocated by what is easy to build.
**Tags:** #optimization-fundamentals #confidence-intervals #evaluation-metrics #hypothesis-testing #revenue-impact #descriptive-statistics #bayesian-inference #probability-distributions
**Contested on:** Every serious competitor in this niche is fighting to spend a finite number of tests on the changes most likely to produce a detectable effect, when the selection is currently by ease of building — and whoever allocates it takes the account.

## The Problem
A site can support a limited number of concurrent tests with enough traffic each to detect anything. That capacity is the programme's real constraint. It is allocated from a backlog scored by a framework that weights ease of implementation heavily, so the programme fills with small changes on pages where no realistic effect could be detected, while the high-traffic pages where an effect would show get tested rarely because the changes there are harder to build.

## Why Nobody Has Built This
Prioritisation frameworks in this discipline weight effort and ease explicitly, which biases directly toward undetectable tests. Traffic as a shared constraint is not modelled. Expected value requires an effect size estimate nobody makes. And a full test calendar looks like a productive programme.

## What to Build
Allocate against expected value under a traffic constraint rather than scoring ideas by ease. Model each candidate test's expected value — plausible effect size, traffic available, detectability, implementation cost — which is the core and replaces a scoring framework that biases toward the wrong tests. Treat traffic as the shared constrained resource it is, since concurrent tests compete for it and nobody models the competition. Reject tests that cannot detect a worthwhile effect rather than ranking them lower, which frees capacity immediately. Prioritise pages by traffic and by the size of the change, since those two together determine detectability. Group small changes into larger ones where the mechanism is shared, which converts several undetectable tests into one detectable one. Learn effect size priors from the programme's own history, which is the input everyone lacks and everyone has. Maintain a portfolio rather than a queue, balancing safe incremental tests against larger speculative ones. Report capacity utilisation and the proportion of capacity spent on detectable tests, which is the number that reveals the problem. Sequence dependent tests so one does not invalidate another. And measure the programme's value against capacity rather than against test count.

## Target Customer
Conversion optimisation firms and in-house experimentation teams, programme leadership, testing platform vendors, and optimisation consultancies.

## Impact If Built
The scarce resource is detectable tests and the prioritisation framework explicitly rewards what is easy to build. Expected value under a traffic constraint is what turns a full calendar into a productive one.
