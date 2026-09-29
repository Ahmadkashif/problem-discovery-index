# Buy: Leave and Benefits Administration Adapted to Sixty Statutory Regimes

**Niche:** [[niches/remote-work-infrastructure/benefits-and-entitlements/profile|Benefits, Leave & Local Entitlements]]
**Industry:** [[industries/remote-work-infrastructure|Remote Work Infrastructure]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** HR systems administer leave and benefits well under one country's rules; here every worker is under different rules and the policy is a floor, not a definition.
**Tags:** #compliance #data-integration #workflow-orchestration #evaluation-metrics #confidence-intervals #descriptive-statistics #automation #worker-facing
**Contested on:** Whether leave and benefits administration built around company policy can enforce sixty statutory floors.

## The Problem

Leave and benefits administration is standard HR functionality. Accrual rules, balance tracking, request and approval workflow, calendar integration, benefit enrolment and carrier connections are all mature in the major HR platforms and in dedicated leave products.

They are configured around a company policy. Accrual is a rate the administrator sets, carryover is a rule the company chooses, benefits are a package the company selects. The legal floor is assumed to be below the policy and is not modelled. Here the floor is jurisdiction-specific, may exceed the policy, and is not optional — which inverts the relationship between policy and system.

## What Already Exists

Leave management in the major HRIS platforms and dedicated leave products. Accrual engines with configurable rules. Benefit enrolment and carrier integration. Absence tracking with calendar integration. Local benefit brokers per market. Statutory leave calculators published by some governments.

## The Customization Gap

**The statutory floor has to be a computed constraint, not a configuration.** Policy is configurable; the floor is not, it varies by jurisdiction and by worker circumstance, and it must override the policy where it is higher. No leave product models a rule it cannot let the administrator change.

**Accrual engines are not expressive enough for the edges.** Carryover with expiry dates that vary, public holiday interaction, sickness during leave converting days back, proration methods that differ by country, and part-time treatment. The configurable accrual models in HR products handle the common cases and fail on the jurisdictional specifics that determine the outcome.

**Benefits are per-jurisdiction packages, not a global plan.** Mandatory coverage differs, brokers differ, carriers differ, enrolment rules differ. The HR product's benefits module assumes a plan design applied across a population, which does not exist here.

**Rule currency is a live obligation.** Statutory entitlements change and the change applies whether or not the configuration was updated. Versioned rules with effective dates, applied retrospectively where required, is not something a leave product supports.

**The worker needs to see their statutory position, not their policy balance.** Two numbers — what the law gives them and what the policy gives them — with the applicable one identified. Every leave product shows one balance.

## Target Customer

Platform benefits and compliance operations running leave administration on an HR product and maintaining the jurisdictional specifics elsewhere. Also the HR and leave product vendors, for whom multi-jurisdiction statutory-floor administration is a real gap as distributed employment grows.

## Impact If Solved

The accrual engine, request workflow, calendar integration and enrolment machinery get reused, and the statutory floor constraint, expressive accrual edges, per-jurisdiction benefits, versioned rules and dual-balance worker view get built. Concretely: a leave balance that reflects the worker's own law rather than the client's policy.
