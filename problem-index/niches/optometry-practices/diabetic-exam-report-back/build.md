# Exam-to-Credit Pipeline

**Niche:** [[niches/optometry-practices/diabetic-exam-report-back/profile|Diabetic Eye Exam Report-Back & Plan Gap Credit]]
**Industry:** [[industries/optometry-practices|Optometry Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A pipeline that turns each diabetic eye exam into result codes, a PCP report and a plan submission, then confirms the plan credited it.
**Tags:** #large-language-models #bert #transformers #data-integration #compliance #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to get each diabetic eye exam the practice performs counted by the patient's health plan, and whoever gets the highest share of completed exams credited in the plan's eye-exam measure takes the account.

## The Problem
The exam happens, but the plan never learns the result. Codes are missing or wrong, letters go only to the PCP, and plans list the patient as a gap months later.

## Why Nobody Has Built This
Plans build gap closure from their side, around their own members. Optometry EHR vendors treat the diabetic exam as one more encounter. The measure's shift to administrative-only data is recent, so the value of getting codes right from the eye practice has only just become obvious.

## What to Build
Extract retinopathy status by eye and compare it with the prior year. Assign the correct CPT II result codes to the claim. Write the PCP letter and send it by Direct or fax. Build each plan's supplemental-data file. Then reconcile the plan's gap lists against what was submitted and chase anything uncredited.

## Target Customer
Multi-OD groups and rollups with large Medicare Advantage panels, and plans that want a cleaner channel from eye practices.

## Impact If Built
A group examining ~5,000 patients with diabetes a year that lifts credited exams by 10% closes ~500 more plan gaps a year (estimate), the basis for plan incentive and preferred-provider arrangements.
