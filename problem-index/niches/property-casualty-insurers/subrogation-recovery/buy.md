# Claims-Fraud Platforms Repointed at Recovery

**Niche:** [[niches/property-casualty-insurers/subrogation-recovery/profile|Subrogation & Recovery]]
**Industry:** [[industries/property-casualty-insurers|Property & Casualty Insurers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Carriers already run every claim through a fraud-scoring platform at intake; the same pipeline could score recovery potential, but it was built to find bad claimants, not liable third parties.
**Tags:** #gradient-boosting #bert #feature-engineering #data-integration #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to flag the recoverable claim at first notice rather than after payment, and whoever files the most recoveries inside each state's limitation period and each arbitration deadline takes the account.

## The Problem
Fraud platforms ingest FNOL data, notes and documents in near real time and route referrals to special investigation units. Recovery screening needs much of the same ingestion and text analysis, but a different target, different rules and a different team at the end.

## What Already Exists
Claims fraud analytics platforms and contributed claims databases (logged in the vault as [[niches/public-adjusters/claims-data-fraud-analytics/profile|🔍 Property Claims Data & Fraud Analytics]]), subrogation modules in core claims systems, and contingency recovery vendors.

## The Customization Gap
The adaptation needs: recovery-type classification (vehicle, product, contractor, landlord or tenant, municipal); state fault, limitation and made-whole rules; waiver-of-subrogation detection in policies and attached contracts; arbitration eligibility checks against the forum's membership and rules; and outcome feedback from recovery units, which fraud models never receive.

## Target Customer
Carriers already licensing a claims-fraud platform that want recovery screening without a new intake integration.

## Impact If Solved
Recovery screening at intake at the marginal cost of a new model on an existing pipeline.
