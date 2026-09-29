# Licensure, Credentialing & Capacity Matching

**Parent Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Category:** Highly Automatable
**Contested on:** Whether the right licensed clinician is available in the right state at the right hour, at an acceptable cost of idle capacity.

## Profile
**Market Size:** ~$3.0B — 10% of US virtual care delivery
**Share of Parent Industry:** ~10%
**Digital Adoption:** Moderate — a rules engine and a staffing spreadsheet
**Target Buyer:** Platform workforce operations and credentialing teams
**Automation Potential:** Very high — this is a forecasting and assignment problem

## What Makes This a Distinct Niche

A clinician can only see patients in states where they hold a licence, demand varies by state and hour, and matching the two is done with a rules engine and a staffing spreadsheet.

This is the operational constraint that shapes the entire economics of virtual care. A platform operating nationally needs, at every hour, enough clinicians licensed in each state to meet that state's demand — and those clinicians are contractors choosing their own hours. Over-staff and you pay for idle capacity; under-staff and wait times rise in one state while clinicians sit idle because their licences do not cover it.

The niche is distinct because it is a genuinely hard and well-posed operations research problem — stochastic demand, a supply pool with per-state eligibility, self-scheduling workers and a service level target — being solved with spreadsheets.

## Current Tools & Gaps

Credentialing and licensure tracking systems, increasingly with compact participation handled. Rules engines enforcing state eligibility at routing time, which work. Shift scheduling tools and staffing spreadsheets. Some platforms fund additional state licences for clinicians, which is the main lever on the supply constraint.

The gaps are forecasting, portfolio planning and incentives. Demand by state and hour is highly predictable and is forecast crudely where at all. The decision about which clinicians should be licensed in which additional states is a portfolio optimisation that nobody treats as one, though each licence costs real money and takes months. And the mechanism for getting contractors to work the hours that are short is a blunt rate bump rather than anything targeted.

## Problems
- [[niches/telehealth-platforms/licensure-and-capacity/build|🔨 Build: Demand Forecasting and Licence Portfolio Optimisation]]
- [[niches/telehealth-platforms/licensure-and-capacity/buy|🛒 Buy: Workforce Management Adapted to State-Constrained Contractor Supply]]
- [[niches/telehealth-platforms/licensure-and-capacity/fix|🔧 Fix: Clinicians Idle in One State, Queues in Another]]
