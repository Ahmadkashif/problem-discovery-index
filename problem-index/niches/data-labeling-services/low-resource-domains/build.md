# Consensus Among a Third of Everybody Who Can Do It

**Niche:** [[niches/data-labeling-services/low-resource-domains/profile|Low-Resource Domains]]
**Industry:** [[industries/data-labeling-services|Data Labeling Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The industry's quality machinery assumes a deep substitutable contributor pool, and in a language spoken by a few million people the qualified pool is a few dozen, at which point every mechanism fails at once.
**Tags:** #bayesian-inference #transfer-learning #expectation-maximization #evaluation-metrics #confidence-intervals #hypothesis-testing #compliance #worker-facing
**Contested on:** Every serious competitor here is fighting to produce quality data in languages and specialisms where the contributor pool is small enough that every standard quality mechanism fails — and whoever does that takes the coverage contracts, because nobody can currently deliver them reliably.

## The Problem
A contract requires annotation in a language with perhaps forty qualified potential contributors reachable. Eleven are recruited. Consensus among three of eleven is not the independent replication the statistic assumes — they know each other, several trained under the same people, and their agreement partly reflects a shared background rather than a shared observation. The reviewer is drawn from the same eleven. One contributor leaves and nine percent of the world's available capacity for this task has gone. The vendor's project management, pricing and quality reporting all assume none of this, and the delivered quality is genuinely unknown.

## Why Nobody Has Built This
The category's methods were designed for deep pools and have simply been applied to thin ones, because designing an alternative requires a different quality theory and the contracts are individually small. The pools are also not measured — nobody knows how many qualified people exist for a given language and task, so scoping is guesswork. And the consequence lands on the resulting models' coverage, which is diffuse and is felt by the speakers of those languages rather than by the buyer.

## What to Build
Design for thin pools explicitly. Measure the pool before scoping, since knowing that forty qualified people exist worldwide changes the contract, the timeline and the price, and is currently unknown at signature — pool estimation from professional registries, academic affiliations and community networks is feasible and is the first thing that should happen. Replace independence-assuming consensus with methods that work under correlation: structured adjudication, explicit disagreement resolution with reasoning, and calibration against the small number of strongest available assessors, which the expert-quality niche describes and which applies here with more force. Model the pool's structure, since contributors who trained together are correlated and treating their agreement as independent overstates confidence — and the correlation is knowable from their backgrounds. Use transfer from the well-served languages deliberately, with native speakers validating rather than originating, which multiplies a thin pool's effective capacity and is the practical route to coverage. Treat contributor retention as existential rather than operational, since losing one person is losing a measurable share of world capacity, and pay and schedule accordingly. Build the guidelines with the contributors rather than translating them, which the fix note addresses. And report the quality honestly including its uncertainty, since a customer receiving low-resource data should know it is less certain than their English data rather than assuming parity.

## Target Customer
Model teams needing genuine coverage, the delivery organisations bidding for it, and the language and specialism communities whose representation in these systems depends on it.

## Impact If Built
Every quality mechanism in the category fails simultaneously in thin pools, and the failures are unmeasured because the mechanisms still produce numbers. Measuring the pool before scoping changes the contract, and correlation-aware quality methods give a customer an honest picture of data that is currently reported as though it were equivalent to the well-served case.
