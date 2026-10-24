# Diabetic Eye Exam Letters and Plan Gap Credit

**Industry:** [[optometry-practices|Optometry Practices]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** EHRs can print a letter, but nothing turns an optometrist's diabetic eye exam into the result codes, primary-care report and plan submission that let the exam count toward the patient's health plan quality measure.
**Tags:** #large-language-models #transformers #bert #logistic-regression #data-integration #compliance #automation

## The Problem
An optometry practice sees hundreds of patients with diabetes a year for dilated exams. Each exam matters to three parties beyond the patient. The primary care physician needs the result to manage the diabetes. The patient's Medicare Advantage or commercial plan needs proof of the exam for its Eye Exam for Patients With Diabetes measure, a Star Ratings measure that became administrative-only in 2025 (search summary). That means the exam counts only if the result arrives as a claim code or supplemental data, because chart review no longer fills the gap. And the practice itself wants the plan's quality incentive and the referral relationship with the PCP.

In most practices this falls to a medical secretary or scribe. They type or edit a letter to the PCP, fax it, and hope the right CPT II code (with or without retinopathy, documented by an eye care professional) went on the claim. Codes are often missing or wrong, so plans send gap lists in the autumn naming patients the practice has already examined. Then the secretary digs through charts to answer them. Adults with diabetes reported an annual eye exam at only 66.0% in 2023 (Healthy People 2030). Some of that gap is exams that happened but never reached the plan.

## What Already Exists
EHRs ship letter templates and Direct messaging, and some auto-populate a PCP report from the exam. Health plans and their vendors run gap-closure programmes with provider portals and supplemental-data file formats. HEDIS engines on the plan side accept codes but do not chase the eye practice. Autonomous retinal screening at the PCP (CPT 92229) covers some patients before they ever reach an optometrist.

## The Customisation Gap
What's missing is report-back built for eye findings. It should read the exam (retinopathy level by eye, macular oedema, comparison with the prior year) and assign the correct CPT II codes. It should write a short PCP letter in the format that practice wants and send it by Direct or fax. And it should build each plan's supplemental-data submission, reconciling the plan's gap list against exams already done. It also needs to know which plans accept a prior-year negative exam, which require specific eye care professional documentation, and when each plan's data run closes.

## Impact If Solved
A practice examining ~600 patients with diabetes a year that gets 15% more exams credited would close ~90 plan gaps a year (estimate). That strengthens its standing in plans' quality and referral programmes and saves a secretary roughly a week of chart pulls each gap-list season.
