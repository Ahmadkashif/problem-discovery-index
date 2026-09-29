# Build: Attrition Prediction and Screening Validation

**Niche:** [[niches/digital-bpo-operations/hiring-and-attrition/profile|Hiring, Onboarding & Attrition]]
**Industry:** [[industries/digital-bpo-operations|Digital BPO Operations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Predict who is about to leave from the daily operational signal, and test whether the screening assessments predict anything at all.
**Tags:** #survival-analysis #gradient-boosting #logistic-regression #confidence-intervals #evaluation-metrics #hypothesis-testing #revenue-impact #worker-facing
**Contested on:** Whether attrition can be predicted early enough to act, and whether anyone will act on it.

## The Problem

Attrition is the industry's dominant cost and is managed by recruiting harder. The prediction problem is unusually favourable — hundreds of thousands of individuals, daily behavioural data, a short horizon, and abundant labels — and it is not solved anywhere.

The signals are visible. Adherence slipping. Absence pattern changes. Schedule swap requests rising. Break behaviour shifting. Quality score trajectory. Handle time drift. Login timing. Load exposure from difficult contacts. Team leader changes. Most people who leave signal it in their operational data for weeks first.

The screening side is worse. Assessment instruments are applied to every applicant and determine who is hired, and essentially nobody has tested whether the scores predict tenure or performance in the role. An instrument that gates employment for hundreds of thousands of people, never validated against outcomes, is both an analytical failure and a fairness problem.

## Why Nobody Has Built This

Attrition is planned for rather than fought. The recruiting machine is sized to replace, training cohorts are scheduled to match, and the operational model works. Predicting an individual's departure raises the question of what to do about it, and the answers — better scheduling, load management, pay, progression — cost money in a business competing on price.

There is also a real concern about misuse. A model predicting departure could be used to reduce investment in the people it flags, which is worse than not having it. That is a governance problem and it has served as a reason not to build.

And validating screening instruments risks finding that the assessment everyone has used for a decade predicts nothing, which would be awkward for whoever selected it.

## What to Build

A survival model on operational data and a validation study on the screening.

**Model time to attrition with the operational covariates.** Adherence and its trend, absence, schedule changes and swaps, quality trajectory, handle time drift, difficult-contact exposure, tenure, team, site, commute proxy, shift pattern and pay band. Survival framing because the timing matters as much as the event, and because censoring is heavy.

**Find the structural drivers, not just the individuals.** The more valuable output is which teams, shifts, sites, programmes and managers have elevated hazard after controlling for composition. A specific shift pattern or a specific programme's contact mix driving attrition is actionable at scale, whereas an individual flag is actionable one person at a time.

**Concentrate on the first ninety days.** Early attrition is a large share of the total, is the most expensive because training is sunk, and has distinct causes — training quality, nesting support, shift allocation, expectation mismatch at hiring. Modelling it separately from tenured attrition is worth doing because the interventions are completely different.

**Govern the individual predictions tightly.** Use for support, never for adverse action. Visible to the team leader as a prompt to check in, not to the operation as a ranking. Written into policy and enforced in access control. Without this the model is a liability.

**Validate the screening instruments properly.** Correlate assessment scores against ninety-day survival, twelve-month survival and quality performance. Report by subgroup, because an instrument that predicts nothing while producing disparate pass rates is a legal exposure as well as a waste. If a component does not predict, remove it — which usually widens the funnel in a labour market where that is worth a great deal.

**Test the training.** Cohort-level outcomes by trainer, curriculum version and nesting approach, against ninety-day survival and early quality. This is the most controllable lever in the whole system and is almost never evaluated.

## Target Customer

BPO people and operations leadership, where attrition is the dominant controllable cost and where the structural findings — a shift pattern, a programme, a site — are actionable without any individual intervention at all.

## Impact If Built

The structural drivers of attrition become visible and addressable at the level where they can be fixed. Early attrition, which is the most expensive kind, gets its own model and its own interventions. And the screening instruments gating employment for hundreds of thousands of people get tested against whether they predict anything — which is both an efficiency question and a fairness one.
