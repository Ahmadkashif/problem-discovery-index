# Inspection and Audit Tooling Turned Continuous

**Niche:** [[niches/field-service-software/multi-site-facilities-service/profile|Multi-Site Facilities Service]]
**Industry:** [[industries/field-service-software|Field Service Software]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Mobile inspection and audit platforms are a mature commodity used across food safety, retail and construction, and facilities contractors use them to record a supervisor's occasional site visit rather than as a sampling instrument.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #k-means-clustering #workflow-orchestration #automation #compliance
**Contested on:** Every serious competitor in multi-site facilities software is fighting to prove that service actually happened, to the standard promised, at a site nobody supervises — and whoever makes verification credible to the client takes the contract.

## The Problem
A supervisor covers thirty sites and inspects each one every few weeks, scoring a checklist. The scores are recorded and averaged into a quality figure. Which sites get inspected is driven by drive routes and by which client complained most recently, so the sample is not random and the resulting score describes the sites that were inspected rather than the contract. A site that has not been visited in two months contributes its stale score to the average, and the contractor's quality metric is a number built from a biased, out-of-date sample and presented to clients as a measurement.

## What Already Exists
SafetyCulture, GoAudits, Lumiform and a dozen equivalents provide mobile inspection with scoring, photo capture, corrective actions and reporting, cheaply and well. Statistical sampling and audit methodology are settled disciplines with a long history in quality management. Facilities-specific inspection standards and cleaning specification frameworks are published. All the pieces are purchasable and most contractors own one of the tools already.

## The Customization Gap
The adaptation is to treat inspections as a designed sample rather than as a supervisor's itinerary. It requires: (1) randomised and risk-weighted inspection scheduling, so the sample supports a defensible estimate of contract-wide quality rather than describing whichever sites were convenient; (2) inspection scores treated as estimates with uncertainty, since a score from one inspection of one floor is not a measurement of a building and presenting it as one is how these numbers lose credibility; (3) stratification by site characteristics and crew, which is what makes the data diagnostic — the interesting finding is almost always that variation concentrates in particular crews, shifts or site types; (4) integration with client-reported issues, so the two independent signals about the same site can be compared and a divergence investigated; and (5) staleness handling, so a site not inspected recently is reported as unknown rather than as its last score, which is the single most misleading feature of current practice.

## Target Customer
Multi-site facilities contractors already using an inspection app, and the facilities management clients who receive quality scores they have no basis to interpret.

## Impact If Solved
A properly sampled quality estimate is defensible to a client in a way an average of convenience inspections is not, and it costs no more inspections than are already being performed — only a different schedule. Stratification is where the operational value is: most contractors have never seen their quality variation decomposed and it usually points somewhere specific and fixable.
