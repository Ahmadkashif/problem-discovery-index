# Statistical Data Quality Against Carriers Who Report Differently

**Niche:** [[niches/independent-insurance-agents/advisory-loss-cost-forms-bureaus/profile|Advisory Loss Cost & Policy Form Bureaus]]
**Industry:** [[industries/independent-insurance-agents|Independent Insurance Agents]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Hundreds of carriers report premium and loss data on their own systems under a common standard they each interpret slightly differently, and every published loss cost inherits the difference.
**Tags:** #anomaly-detection #data-integration #ml-time-series #evaluation-metrics #automation

## The Problem
The statistical plan tells carriers what to report and how. Carriers implement it on systems of varying age, with their own claim handling conventions, their own timing for establishing and revising reserves, and their own interpretation of the edges of the definitions.

The result is data that is nominally uniform and practically heterogeneous. A carrier changes its claims system and its reporting pattern shifts. A company's case reserving philosophy alters and its development pattern changes with it, mimicking a real trend. A class is coded differently by two carriers in the same state. Any of these propagates into a loss cost that will be filed and used to price thousands of policies.

Validation is edits, reasonableness checks, and analysts who know their companies. Analysts recognize when a carrier's numbers look unlike that carrier — which is the strongest signal available and is entirely in their heads.

## What Already Exists
Data quality and observability platforms — the enterprise data quality suites, Monte Carlo, Great Expectations, and their peers — do schema validation, distributional monitoring, anomaly detection, and stewardship workflow well, and are widely used in financial services.

## The Customization Gap
The generic products assume a source whose meaning is stable. Here the meaning drifts inside the reporter.

**Reporter-relative baselines.** The question is never whether a value is plausible for the industry; it is whether it is plausible for this carrier given how this carrier has reported for the last decade. That requires a maintained behavioural profile per reporter, which no generic tool has a concept of.

**Development patterns are the data.** Losses are reported at successive maturities and the pattern of development is what actuarial estimation runs on. An anomaly here is a change in the *shape* of development, not in a value — a carrier strengthening reserves looks exactly like emerging severity trend, and separating them is the central problem. Nothing off the shelf monitors a triangle.

**Influence-weighted triage.** A questionable submission matters in proportion to its weight in the published loss cost for that class and state. In a thin class one carrier can be most of the data. Prioritizing by effect on the published number, rather than by size of the discrepancy, is the correct allocation and requires the system to reason about the output.

**Silent definitional drift.** The failures that matter most are not outliers but correct-looking values reported under a shifted interpretation — a change in what counts as an allocated expense, a reclassification of a coverage. These sit inside every range and are detectable only against the reporter's own history and its peers.

**An auditable record of every adjustment.** Published loss costs are filed with regulators and used to price policies. Every correction and exclusion must be reconstructable years later, which makes lineage a regulatory requirement rather than a nice-to-have.

## Target Customer
Head of Statistical Data Quality or Chief Data Officer at the advisory organization, where a fixed analyst team validates a growing volume from hundreds of reporters against a filing calendar that does not move.

## Impact If Solved
Every filed rate in commercial insurance descends from these numbers. Catching a reporter's definitional drift before it enters a loss cost prevents an error that propagates into thousands of policies and persists for years, and concentrating limited analyst attention where a submission actually moves a published figure is the difference between validating everything shallowly and validating what matters properly.
