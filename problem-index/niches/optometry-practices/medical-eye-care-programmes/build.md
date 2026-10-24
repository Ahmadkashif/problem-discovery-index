# One Medical-Patient Ledger Across Diseases and Devices

**Niche:** [[niches/optometry-practices/medical-eye-care-programmes/profile|Medical Eye Care Programmes (Glaucoma & Dry Eye)]]
**Industry:** [[industries/optometry-practices|Optometry Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A ledger that lists every medically managed patient, their diagnosis, next due test and treatment status, so an optometry practice can see and keep its medical panel.
**Tags:** #survival-analysis #logistic-regression #large-language-models #data-integration #workflow-orchestration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is "Every serious competitor in this niche is fighting to keep medically managed eye patients in the optometry practice", but glaucoma and dry eye are won by different things. Glaucoma is won by catching progression at the visit it first shows, with imaging and field analysis across devices and co-management with ophthalmology. Dry eye is won by turning a diagnosis into a completed, mostly cash-paid series of in-office treatments. Vendors, buyers' metrics and the cost of failure differ. Decomposed into contested sub-niches below.

## The Problem
An owner OD cannot answer a simple question: how many glaucoma suspects, glaucoma patients and dry-eye patients does the practice manage, and how many are overdue? Patients are recalled for the annual vision exam, so the medical schedule depends on the doctor's memory and a note in the chart.

## Why Nobody Has Built This
EHRs organise by encounter, devices by scan, and recall tools by appointment type. Each sees part of the patient. Medical eye care was a small part of optometry until scope laws and dry-eye products changed that in the last decade.

## What to Build
A ledger built from diagnosis codes, orders, device exports and notes. It lists each medical patient, their disease, the date their next test or visit falls due, their treatment and adherence, and their churn risk from a survival model. It feeds disease-specific recall and gives the owner a monthly panel report. The sub-niches show the disease-specific contests built on top.

## Target Customer
Medically oriented independent practices and the clinical directors of multi-OD groups.

## Impact If Built
A practice managing ~800 medical patients that brings back 10% more on schedule would add ~80 retained patients and ~$25,000–$45,000 a year of testing and visit revenue (estimate).
