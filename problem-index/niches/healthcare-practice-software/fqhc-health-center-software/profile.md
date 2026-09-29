# FQHC & Community Health Center Software

**Parent Industry:** [[industries/healthcare-practice-software|Healthcare Practice Software]]
**Category:** Underserved Audience
**Contested on:** Every serious competitor selling to health centers is fighting to make the UDS report, the sliding-fee determination and the 340B claim all derive from the same encounter record without a parallel data collection exercise — and whoever removes that second exercise takes the account.

## Profile
**Market Size:** ~$900M US software spend across 1,400 federally qualified health centers and look-alikes and their 15,000 delivery sites
**Share of Parent Industry:** ~5% of ambulatory software revenue, almost entirely grant- and payer-funded
**Digital Adoption:** Medium — health centers were early meaningful-use adopters and are among the most reporting-burdened providers in ambulatory care
**Target Buyer:** Health center CIOs and quality directors; on the vendor side, product leads with HRSA-facing implementation teams
**Automation Potential:** High — the reporting, eligibility and pharmacy-claim work is rule-governed and is currently performed by analysts with spreadsheets

## What Makes This a Distinct Niche
A health center is an ambulatory practice carrying an obligation structure nobody else has. It must report the Uniform Data System annually — a detailed census of patients, services, clinical quality measures and payer mix with definitions that do not align with any commercial quality programme. It must determine each patient's sliding-fee discount from household income and size, and defend those determinations. If it participates in 340B, it must maintain patient and provider eligibility for discounted drugs and survive an audit that looks specifically for ineligible dispensations. And it serves a population with high uninsured rates, language diversity and social needs that it is also expected to screen for and report on. None of this fits the commercial EHR's model of a visit, so it is done alongside the EHR — by analysts, in spreadsheets, in a season that consumes the first quarter of every year.

## Current Tools & Gaps
Epic's community offering, athenahealth, eClinicalWorks, NextGen and Azara's analytics layer serve most of the segment, and a handful of vendors specialise. The specialists understand UDS; the generalists supply a report that must be reconciled by hand. The gap is consistent across both: the data the reports require is collected twice. Income and household size are gathered for the sliding fee at the front desk and gathered again for UDS from a different field; social needs screening is captured in a questionnaire that does not map to the reporting taxonomy; 340B eligibility is determined by a third-party administrator reading claims after the fact rather than by the record at the point of prescribing. Every one of these is the same encounter, recorded in parallel systems that disagree.

## Problems
- [[niches/healthcare-practice-software/fqhc-health-center-software/build|🔨 Build: One Encounter Record That Yields UDS, Sliding Fee and 340B]]
- [[niches/healthcare-practice-software/fqhc-health-center-software/buy|🛒 Buy: Social Needs Screening Wired to the Referral That Follows]]
- [[niches/healthcare-practice-software/fqhc-health-center-software/fix|🔧 Fix: The UDS Season]]
