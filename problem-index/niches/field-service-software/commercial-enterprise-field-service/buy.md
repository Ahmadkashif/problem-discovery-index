# Reliability Engineering Methods Applied to Service Contracts

**Niche:** [[niches/field-service-software/commercial-enterprise-field-service/profile|Commercial & Enterprise Field Service]]
**Industry:** [[industries/field-service-software|Field Service Software]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Reliability engineering has a century of mature method for exactly this problem — time-to-failure distributions, censoring, repairable systems, spares provisioning — and service operations organisations price contracts by intuition next door to the department that teaches it.
**Tags:** #survival-analysis #probability-distributions #maximum-likelihood-estimation #confidence-intervals #evaluation-metrics #hypothesis-testing #monte-carlo-methods #revenue-impact
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
A service organisation asks how often a particular model of machine, eight years old, running two shifts, will need attention next year. The answer comes from a service manager's recollection. Two floors away, the reliability engineering group models time-to-failure distributions for the same machines using standard methods, for design and warranty purposes, and the two groups do not exchange anything. The service business prices risk without using the discipline that exists to price it.

## What Already Exists
Survival and reliability analysis is among the most settled quantitative disciplines available: Weibull and other lifetime distributions, censoring handling, repairable-system models, competing risks, and spares provisioning methods are all standard, taught, and implemented in mature open-source and commercial packages. Warranty analytics practice in manufacturing is directly adjacent. Nothing needs inventing; it needs importing across an organisational boundary.

## The Customization Gap
The adaptation is to service data rather than to test data, and service data is messier. It requires: (1) treating installed machines as repairable systems with recurrent events rather than as units with a single time-to-failure, which is the usual modelling error when reliability methods are first applied to service; (2) handling the heavy censoring and the selection in service records — a machine only generates a record when someone calls, and machines under contract are called about differently from those out of contract; (3) covariates that service data has and reliability testing does not, above all duty cycle, environment and site-level maintenance quality, which explain more variance than machine age; (4) translating failure forecasts into the quantities the service business actually decides on — contract price, technician capacity by region, and spares stocking levels — since a hazard curve is not a decision; and (5) validating against the service organisation's own realised costs rather than against engineering expectations, which is the check that keeps the modelling honest.

## Target Customer
Manufacturers with service businesses, commercial service providers, and the enterprise field service vendors who could embed reliability modelling rather than leave it to spreadsheets.

## Impact If Solved
Importing a mature discipline is far faster than developing one, and the methods arrive with known assumptions and known failure modes. Spares provisioning alone — stocking levels derived from modelled demand rather than from historical consumption — typically frees working capital while improving parts availability, which is the constraint on first-visit resolution in this segment.
