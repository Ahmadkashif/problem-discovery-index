# Care-Drift Detection Between Reassessments

**Niche:** [[niches/assisted-living-communities/acuity-level-of-care-billing/profile|Resident Acuity Assessments & Level-of-Care Billing]]
**Industry:** [[industries/assisted-living-communities|Assisted Living Communities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A resident's needs grow week by week; her care fee changes when the nurse next gets round to her.
**Tags:** #gradient-boosting #change-point-detection #large-language-models #feature-engineering #revenue-impact #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to bill each resident for the care staff actually deliver, and whoever turns caregivers' daily documentation into an evidenced level-of-care change before the next invoice takes the account.

## The Problem
After a hospital stay or a slow decline, a resident needs two-person transfers, more prompting and night-time help. Aides give it. The care level stays where it was until the quarterly reassessment, and sometimes past it, because the wellness nurse covering 60–80 residents (estimate) has not seen the change herself.

## Why Nobody Has Built This
Care logs are task checkboxes without time, incidents sit in a separate module, and the assessment tool is a form. Nobody has joined them to detect a change in need, partly because the honest label (care minutes delivered) is not measured.

## What to Build
A weekly model per resident that reads task logs, call-light patterns, incident notes, medication changes, hospital returns and, where installed, room-sensor time. It detects change points in care need and proposes a reassessment with the evidence: the documented tasks, the incidents and an estimated care-time increase. The nurse confirms, and the system drafts the family notice in the community's required form.

## Target Customer
Clinical and finance leaders at chains of 10–200 communities; billing service providers such as Sunbound.

## Impact If Built
Re-scoring under-billed residents a month or two sooner (estimate) recovers ~$300–500 a month for each of ~10–15 residents in an 80-unit building, ~$40,000–90,000 a year (estimate), and gives aides' extra work a voice.
