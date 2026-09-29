# Unit Statistical Data From Carriers Who Reserve Differently

**Niche:** [[niches/insurance-tpa/workers-comp-rating-bureaus/profile|Workers' Compensation Rating Bureaus]]
**Industry:** [[industries/insurance-tpa|Insurance Third-Party Administrators (TPAs)]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Every employer's premium multiplier is computed from claim values that carriers set by their own reserving philosophy.
**Tags:** #anomaly-detection #ml-time-series #data-integration #evaluation-metrics #automation

## The Problem
Unit statistical reporting requires carriers to report every policy and every claim at fixed valuation dates. The experience mod is computed directly from those reported claim values, which means one carrier's reserving practice flows straight into an individual employer's premium.

Carriers differ. One establishes full case reserves early; another develops them upward over time. One carrier's claims administrator closes files aggressively; another leaves them open. A carrier changing claims systems shifts its reporting pattern. A TPA change on a large self-insured account alters reserving overnight. None of these are errors in any single record, and all of them move mods for the employers concerned.

Validation is edits, reasonableness tests, and analysts who know their reporting companies. That last part is the strongest control and it exists entirely in people.

## What Already Exists
Data quality and observability platforms are mature and widely used in insurance data operations, with schema validation, distributional monitoring, anomaly detection, and stewardship workflow all well covered.

## The Customization Gap
Generic tooling assumes a stable definition behind a reported value. Here the definition drifts inside the reporter.

**Reporter-relative baselines.** The question is never whether a claim value is plausible in general; it is whether this carrier's reporting looks like this carrier. That requires a maintained behavioural profile per reporting company, which no generic platform models.

**Development shape is the signal.** Claims are reported at successive valuations, and the pattern of development between them is what the rating plan consumes. An anomaly is a change in that shape — a carrier strengthening reserves looks identical to genuine severity trend, and separating them is the central problem. Nothing off the shelf monitors a development pattern.

**Influence-weighted triage, down to the employer.** Unlike aggregate ratemaking, an error here can land on one identifiable employer's premium. A misreported claim on a small employer with thin experience can move their mod by a large margin, and prioritization must reflect effect on individual mods as well as on class loss costs.

**Definitional drift beats outlier detection.** The costly failures are correct-looking values reported under a shifted convention — a change in what counts as an allocated expense, or in when a claim is deemed closed. These sit inside every range and show only against the reporter's own history and its peers.

**Everything must be reconstructable.** Mods are published, relied on by third parties in contract requirements, and disputed. Each correction and exclusion has to be auditable years later.

## Target Customer
Head of Data Quality or Chief Data Officer at a rating organization, where a fixed analyst team validates growing volume against fixed publication dates.

## Impact If Solved
Errors here do not average out — they land on named employers as a premium multiplier and, in construction, as eligibility to bid. Catching a carrier's reserving shift before it propagates into mods prevents a class of error that is currently invisible until an employer disputes, and it concentrates analyst attention where a submission actually moves someone's number.
