# The Same Degree Evaluated Ten Thousand Times From Scratch

**Niche:** [[niches/immigration-law/credential-evaluation-services/profile|Foreign Credential Evaluation Services]]
**Industry:** [[industries/immigration-law|Immigration Law Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A four-year engineering degree from one Indian university is the same degree every time, and each report is written as though the analyst had never seen that institution before.
**Tags:** #text-classification #word-embeddings #large-language-models #named-entity-recognition #workflow-orchestration

## The Problem
Credential evaluation answers a narrow question with wide consequences: is this foreign qualification equivalent to a US degree at a given level. An H-1B beneficiary's eligibility for a specialty occupation turns on it, as does a professional licence and a graduate admission.

The volume is enormous and enormously repetitive. A handful of countries and a few hundred institutions account for the bulk of it, and within those, the same degree programmes recur constantly. The determination for a four-year Bachelor of Technology from a particular recognized Indian university is the same determination this year as last, unless the institution's recognition status or the programme's structure changed.

Each one is nonetheless produced as an individual analysis. An analyst identifies the institution, checks its recognition, reads the transcript, maps the credits, and writes the report. Throughput is people, throughput is the constraint, and cap season concentrates demand into weeks where a delayed evaluation loses a filing window entirely.

## Why Nobody Has Built This
The evaluation is a professional judgment and the field has treated it as unautomatable on principle — a defensible instinct, since the hard cases genuinely require expertise and the consequence of error falls on an applicant's immigration status.

The instinct is applied to the whole distribution rather than to the tail. Most of the work is not hard cases; it is the same institution and the same programme structure recurring, where the difficulty is entirely in reading a transcript accurately and applying a determination the firm has already made hundreds of times.

There is also no knowledge base to reuse. Institution recognition research and programme equivalency determinations are embedded in the reports they were written for, not maintained as a reference. So even the parts that could obviously be reused are not, because reuse would mean finding the last report on that institution.

## What to Build
An institution and programme knowledge base, with the report assembled from it.

**Make institutions and programmes first-class records.** Recognition status by country authority, accreditation history, degree structures with durations and credit systems, and the firm's own prior determinations with dates. Mining this from decades of completed reports is the foundational work and the asset it produces is the company's real inventory.

**Match incoming documents to known programmes.** Institution and programme identification from a transcript — across transliteration, name changes, and inconsistent formatting — is the first bottleneck and is well-posed given a reference base of prior evaluations.

**Assemble a draft from the determination that exists.** Where the institution and programme are known and the transcript is consistent with the recorded structure, the analyst reviews and signs rather than composes. Where anything deviates — an unrecognized institution, an unusual duration, a programme structure that does not match the record — it routes to full analysis, which is where the expertise belongs.

**Flag what has changed.** Institution recognition changes; countries reform degree structures; the Bologna transition reshaped an entire continent's qualifications. A determination made four years ago may no longer hold, and today nothing tells an analyst that except their own knowledge.

## Target Customer
President or VP of Evaluation Services at a credential evaluation organization. The constraint is analyst capacity against demand that spikes on the immigration calendar, and turnaround is what applicants and attorneys choose on.

## Impact If Built
Evaluation delays cost people filing windows, and a missed cap season costs a year. Concentrating analyst expertise on the cases that need it — while the recurring institution-and-programme work is assembled from determinations the firm has already made — improves both turnaround and consistency, since the same institution currently gets slightly different treatment depending on who picked it up.
