# Making the Test Routine

**Niche:** [[niches/game-user-acquisition-firms/incrementality-operations/profile|Incrementality Operations]]
**Industry:** [[industries/game-user-acquisition-firms|Game User Acquisition Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The only measurement that establishes causation is run twice a year because each one is a project.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #automation #workflow-orchestration #revenue-impact #monte-carlo-methods
**Contested on:** Every serious competitor in this niche is fighting to run incrementality tests often enough to know what their spend is actually buying, when each one is currently a project — and whoever makes them routine takes the account.

## The Problem
Attributed installs are not caused installs, and the gap is large and varies by channel. Incrementality testing closes it, and it is run rarely because each test requires design, a power calculation, a negotiated holdout, weeks of waiting, a bespoke analysis and a presentation. Between tests, every allocation decision is made on attributed numbers that the last test showed were wrong, and nobody knows by how much any more.

## Why Nobody Has Built This
Each test is designed from scratch because no standing infrastructure exists. Holdouts mean deliberately not spending, which is uncomfortable. Networks offer their own lift studies, which are convenient and not independent. And the analysis requires care that a UA team is not staffed for.

## What to Build
Build standing test infrastructure rather than running projects. Maintain continuous holdouts across channels as standing infrastructure, which is the core — a permanent small holdout produces a continuous incrementality estimate rather than an occasional one. Automate test design and power calculation so a test can be launched in an hour rather than designed over a fortnight. Standardise the readout so results are comparable across tests and over time. Size holdouts against the decision's value rather than using a fixed percentage. Accumulate results into a standing view of each channel's incrementality, which is what actually informs allocation. Run tests independently of the networks, since a network measuring its own lift has an obvious interest. Detect when a channel's incrementality changes, as it does and nobody notices between annual tests. Report the cost of the holdout alongside the value of the information, which is how the practice gets approved. Apply the same machinery to creative and geography, where it is equally applicable and even less used. And feed the incrementality estimates directly into bidding rather than leaving them as a slide.

## Target Customer
UA teams and agencies, mobile publishers, measurement and attribution vendors, and experimentation platform providers.

## Impact If Built
The only measurement that establishes causation is run twice a year because each one is a project. Standing holdouts with automated design turn an occasional study into a continuous estimate that can drive bidding.
