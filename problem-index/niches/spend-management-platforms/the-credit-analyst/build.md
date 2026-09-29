# What Happened to Companies Like This

**Niche:** [[niches/spend-management-platforms/the-credit-analyst/profile|The Credit Analyst]]
**Industry:** [[industries/spend-management-platforms|Spend Management Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The analyst has seen a thousand companies and can recall a dozen, and the platform has the outcomes for all of them.
**Tags:** #k-nearest-neighbors #survival-analysis #gradient-boosting #worker-facing #evaluation-metrics #confidence-intervals #tacit-knowledge-ml #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to tell the analyst what happened to the last five hundred companies that looked like this one — and whoever closes that loop turns a judgement made in the dark into one made on evidence.

## The Problem
The file in front of the analyst is a twelve-month-old company with rising revenue, a large recent raise, high burn and a founder with one prior exit. The question is what limit to extend. The relevant evidence — what happened to the several hundred structurally similar companies the platform has already underwritten — exists in the database and is unavailable to them. So they decide from personal recall, general heuristics and the pressure to approve quickly.

## Why Nobody Has Built This
The outcome data sits in collections and churn systems with no path back to the credit desk, so the analyst was never a consumer of it — the role's information environment was defined by the intake systems rather than by the outcome ones. Analysts are measured on throughput. Nobody captured decision reasoning in a form that supports retrieval. And the portfolio was small enough, early on, that recall felt sufficient.

## What to Build
Give the analyst the portfolio's memory. Retrieve comparable past cases with their outcomes at decision time, which is the core and converts recall into evidence. Define similarity on the dimensions that matter — stage, sector, burn profile, revenue trajectory, funding pattern — rather than on superficial attributes, since that definition is the substance of the feature. Show what happened: repayment, delinquency, shutdown, growth, with base rates and not just anecdotes. Capture the analyst's reasoning in a structured form, because it is the input to every later improvement and is currently free text nobody reads. Feed outcomes back to the analyst who made the decision, since it is the only way expertise develops and the role currently offers none. Measure consistency between analysts on similar files, as the spread is unknown and is a quality signal. Surface the factors that historically predicted trouble in similar profiles, which is what the analyst is trying to recall under time pressure. Flag the file that has no close comparables, because that is where judgement is genuinely required and where a model should not be trusted. Keep the analyst's decision authority, since the tooling should inform rather than replace and the cases are genuinely hard. And measure decision quality by outcome cohort, which is the metric the function has never had.

## Target Customer
Credit leadership, the analysts themselves, portfolio and capital stakeholders, and commercial credit tooling vendors with no comparable-case capability.

## Impact If Built
The role's information environment was defined by intake systems and the outcomes live in collections, so the analyst was never a consumer of them. Comparable-case retrieval at decision time replaces personal recall with the portfolio's actual history.
