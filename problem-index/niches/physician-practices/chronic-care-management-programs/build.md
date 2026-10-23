# Engagement-Decay Prediction for Care-Managed Patients

**Niche:** [[niches/physician-practices/chronic-care-management-programs/profile|Chronic & Advanced Primary Care Management Programs]]
**Industry:** [[industries/physician-practices|Physician Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Enrolled patients stop answering the monthly call long before the programme notices, and each silent month is both a missed bill and a patient no longer being managed.
**Tags:** #survival-analysis #gradient-boosting #evaluation-metrics #worker-facing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to keep enrolled Medicare patients in monthly care management the practice can bill, and whoever keeps the most patients billable every month with documentation that survives audit takes the account.

## The Problem
A care manager carries ~150–250 enrolled patients (estimate). Each month some do not pick up, some are in hospital, some have moved to another practice. The care manager calls down the list in the same order every month. By the time a patient has been unreachable for three months, they are effectively disenrolled, and their condition has gone unmanaged.

## Why Nobody Has Built This
Care-management vendors are paid per billable patient-month and staff to volume. Engagement data (call outcomes, time of day answered, channel preference) lives in call logs nobody models. Practices running the programme in-house lack analysts.

## What to Build
A survival model of time to disengagement for each enrolled patient. It is trained on call outcomes, answer times, channel responses, recent admissions, refill gaps and RPM transmission gaps. The monthly call list is reordered by risk and best contact window, with channel switches (text, video, family caregiver) suggested before the patient goes silent. Recent hospitalisations trigger an immediate call rather than next month's.

## Target Customer
Directors of care management at primary care groups and ACOs running CCM, APCM or RPM for 500–10,000 patients.

## Impact If Built
Keeping ~10% more enrolled patients billable each month (estimate) is worth ~$50 per patient-month at CCM or APCM rates (estimate). Earlier contact after a gap may also avert some of the admissions the programme exists to prevent.
