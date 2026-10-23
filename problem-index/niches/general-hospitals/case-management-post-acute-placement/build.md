# Acceptance Prediction for Every Post-Acute Referral

**Niche:** [[niches/general-hospitals/case-management-post-acute-placement/profile|Case Management & Post-Acute Placement]]
**Industry:** [[industries/general-hospitals|General Hospitals]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Case managers send referrals to the family's list of facilities in the order the family wrote it, without knowing which facilities ever accept patients like this one.
**Tags:** #gradient-boosting #logistic-regression #large-language-models #evaluation-metrics #workflow-orchestration #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to get a medically ready patient accepted and authorised for the right post-acute bed on the day they are ready, and whoever removes the most avoidable days per case manager takes the account.

## The Problem
A patient on a ventilator wean, or one with a behavioural history, IV antibiotics, bariatric needs or a Medicaid-pending payer, is hard to place. Facilities decline these patients silently or slowly. The hospital's referral platform holds years of sends, views, accepts and declines, but nobody uses them to choose where to send next.

## Why Nobody Has Built This
Referral platforms are paid per transaction and are neutral by design. Patient-choice rules make steering sensitive, and decline reasons are rarely recorded in structured form.

## What to Build
A model that predicts acceptance probability and time-to-accept per facility, from patient clinical features, payer, required services and each facility's own history with the hospital. It presents the family's choices with expected wait times and suggests similar-quality alternatives with better acceptance odds, keeping choice with the family. It drafts facility-specific packets with the documents each intake team asks for, and reads replies to update status.

## Target Customer
Directors of case management at hospitals with high avoidable-day counts and MA-heavy payer mixes.

## Impact If Built
Cutting time-to-acceptance for hard-to-place patients by a day or more (estimate) saves thousands of bed-days a year at a 400-bed hospital and shortens ED boarding.
