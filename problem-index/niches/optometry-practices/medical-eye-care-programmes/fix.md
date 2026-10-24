# Medical Patients Lost Between Annual Exams

**Niche:** [[niches/optometry-practices/medical-eye-care-programmes/profile|Medical Eye Care Programmes (Glaucoma & Dry Eye)]]
**Industry:** [[industries/optometry-practices|Optometry Practices]]
**Type:** Fix (Pain Point)
**One-liner:** Medical patients told to return in three or six months are recalled like annual vision patients, so many never come back until their next yearly exam.
**Tags:** #survival-analysis #logistic-regression #automation #worker-facing #quick-win
**Contested on:** *Not terminal as stated.* The honest partial sentence is "Every serious competitor in this niche is fighting to keep medically managed eye patients in the optometry practice", but glaucoma and dry eye are won by different things. Glaucoma is won by catching progression at the visit it first shows, with imaging and field analysis across devices and co-management with ophthalmology. Dry eye is won by turning a diagnosis into a completed, mostly cash-paid series of in-office treatments. Vendors, buyers' metrics and the cost of failure differ. Decomposed into contested sub-niches below.

## The Problem
The doctor says "come back in four months for a field and pressure check". The front desk books the next annual exam, or nothing. The recall system sends a generic reminder at twelve months, and the four-month check never happens.

## Why It's Still Broken
Recall tools key on appointment type, not on the doctor's ordered interval. The interval sits in free text in the plan section of the note. Nobody reviews who missed a medical follow-up.

## What a Fix Looks Like
Extract the ordered interval and tests from each note. Create a medical recall with its own due date, and send a disease-specific message that explains why the visit matters. List overdue medical patients for a weekly call.

## Who Feels the Pain
Patients whose glaucoma or dry eye goes unmonitored, and owner ODs whose medical revenue leaks without anyone noticing.

## Impact If Fixed
Recovering ~5 missed medical follow-ups a week at ~$120 a visit (estimate) is ~$30,000 a year for one practice, and earlier detection for those patients.
