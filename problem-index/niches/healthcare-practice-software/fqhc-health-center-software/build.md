# One Encounter Record That Yields UDS, Sliding Fee and 340B

**Niche:** [[niches/healthcare-practice-software/fqhc-health-center-software/profile|FQHC & Community Health Center Software]]
**Industry:** [[industries/healthcare-practice-software|Healthcare Practice Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Health centers collect the same facts three times for three obligations because no vendor has modelled the encounter richly enough to derive all three, so every health center runs a parallel data operation staffed by analysts.
**Tags:** #feature-engineering #evaluation-metrics #descriptive-statistics #confidence-intervals #compliance #data-integration #workflow-orchestration #automation
**Contested on:** Every serious competitor selling to health centers is fighting to make the UDS report, the sliding-fee determination and the 340B claim all derive from the same encounter record without a parallel data collection exercise — and whoever removes that second exercise takes the account.

## The Problem
A patient arrives. The front desk collects household income and size to set the sliding-fee discount, entering it in a registration screen. The same facts are needed for UDS, where the definitions differ slightly and the data comes from a different extract, so the quality analyst reconciles them in February. The patient is prescribed a drug that the health center dispenses under 340B; eligibility for that discount depends on whether this was a qualifying encounter with a qualifying provider at a qualifying site, which is determined weeks later by a third-party administrator matching claims against an eligibility file. Three obligations, one visit, three data paths, three sets of disagreements, and three separate audit exposures.

## Why Nobody Has Built This
Commercial EHR vendors built for the commercially insured, where none of these obligations exist, and health centers are a small enough share of seats that the model was never extended. The specialists that did serve the segment built reporting layers on top of the commercial model rather than changing it, because changing it meant re-architecting registration, encounter and pharmacy at once. There is also a genuine definitional problem: UDS, sliding-fee guidance and 340B eligibility use overlapping but non-identical definitions of patient, encounter, provider and site, and a single record that satisfies all three has to hold the differences explicitly rather than choosing one. That is unglamorous modelling work with no demo value.

## What to Build
An encounter model that carries the attributes all three obligations need, as first-class dated facts rather than as report-time derivations: household composition and income with an effective date and a documentation reference; the encounter's qualifying status by site, provider and service type, evaluated at the time of service rather than retrospectively; and the patient's relationship to the health center expressed in the way each programme defines it. From that record, UDS tables, sliding-fee determinations and 340B eligibility all fall out as views with their differences visible. The essential property is that a disagreement between the three becomes a data question answerable in the chart, not a reconciliation project, and that any determination can be traced to the facts and effective dates that produced it — which is what every one of these audits asks for.

## Target Customer
Health center controlled networks and the larger multi-site FQHCs with analyst teams, plus the vendors serving the segment who currently ship a reporting layer and inherit the reconciliation as support load.

## Impact If Built
Removing the parallel data operation is worth one to three analyst FTEs at a mid-size health center and, more significantly, collapses the first quarter of the year from a reporting season into a report. Determinations that trace to dated facts also change the character of an audit from reconstruction to retrieval, which is the difference between a week and an afternoon.
