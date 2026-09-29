# House-Call & Mobile Practice Software

**Parent Industry:** [[industries/healthcare-practice-software|Healthcare Practice Software]]
**Category:** Low Digitized
**Contested on:** Every serious competitor selling to house-call and mobile practices is fighting to make a visit charted in a basement with no signal reconcile cleanly — right patient, right place of service, right time, no lost data — and whoever makes the offline round-trip trustworthy takes the account.

## Profile
**Market Size:** ~$400M US software spend across house-call primary care, mobile diagnostics, hospice, home-based palliative care and mobile dentistry and podiatry
**Share of Parent Industry:** ~2% of ambulatory software revenue, and the fastest-growing underdigitised segment
**Digital Adoption:** Low — a large share of house-call practices run a general ambulatory EHR badly, on a laptop, with paper as the real capture medium
**Target Buyer:** Founders and clinical operations leads at house-call groups, hospice agencies and mobile diagnostic providers
**Automation Potential:** High — routing, offline sync, and place-of-service-correct coding are all mechanical problems that are currently solved by people

## What Makes This a Distinct Niche
The setting breaks the assumptions every ambulatory EHR is built on. There is no front desk, so registration and eligibility happen in a car. There is frequently no connectivity — a basement apartment, a rural road, a facility with concrete walls — so the product must function fully offline and reconcile later without losing or duplicating anything. The clinician is driving between encounters, so the documentation window is a parked car, and the charting device is a tablet held in one hand. Billing is place-of-service sensitive in ways that are easy to get wrong and material: a home visit, a visit in an assisted living facility and a visit in a skilled nursing facility carry different codes and different rules, and the distinction is decided by the address the clinician drove to. Meanwhile the population is disproportionately homebound, elderly and complex, which is exactly the population where a missed medication reconciliation matters most.

## Current Tools & Gaps
Home health and hospice have their own software category — Homecare Homebase, WellSky, Axxess — built around the agency model, OASIS assessments and per-episode billing, which does not fit a physician house-call practice billing fee-for-service E/M. Ambulatory EHRs offer mobile apps that are thin clients requiring connectivity, so the first basement visit produces a workaround. The offline story across the category is weak and rarely tested honestly: vendors claim offline support that amounts to caching a schedule. Routing is generally absent or borrowed from a field service tool with no notion of clinical priority. Nothing joins the drive to the chart, so a practice cannot tell what a visit actually cost it.

## Problems
- [[niches/healthcare-practice-software/house-call-practice-software/build|🔨 Build: An Offline-First Clinical Record That Reconciles Honestly]]
- [[niches/healthcare-practice-software/house-call-practice-software/buy|🛒 Buy: Field Service Routing Adapted to Clinical Priority]]
- [[niches/healthcare-practice-software/house-call-practice-software/fix|🔧 Fix: Place of Service Decided by a Dropdown]]
