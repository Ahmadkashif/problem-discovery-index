# International Transcript Grading Scale Conversion Tool

**Niche:** [[niches/k12-private-schools/international-student-admissions/profile|International Student Admissions Programs]]
**Industry:** [[industries/k12-private-schools|K-12 Private Schools]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Credential evaluation services (WES, ECE) exist for higher education transcripts but charge $150-$300 per evaluation and are not designed for K-12 grading scales — which vary by country, school system, and even individual school.
**Tags:** #multiclass-classification #tabular-ml #data-integration #automation

## The Problem
An admissions committee reviewing an application from a Chinese middle school student sees grades in a 0-100 scale where 85 is considered excellent. A Korean transcript uses a 수/우/미/양/가 grading system. An Indian CBSE transcript uses a different scale than an ICSE transcript from the same country. The admissions director must manually research each country's grading system, determine grade equivalency, and present the committee with a normalized academic profile. At 50-100 international applications per year, this consumes 50-200 hours of research.

## What Already Exists
WES (World Education Services) and ECE (Educational Credential Evaluators) provide official credential evaluations for higher education admissions and professional licensing. SpanTran offers evaluations for K-12 and higher education. These services cost $150-$300 per evaluation, have 2-4 week turnaround times, and are designed for formal credential verification — overkill for private school admissions that need a quick grade equivalency during a 6-week review window.

## The Customization Gap
K-12 international transcript evaluation requires different reference data than higher education: primary and middle school grading in China follows different standards than gaokao-preparation high school grading. The tool must handle dozens of country-specific grading scales, provide age-appropriate equivalencies (converting a Chinese 5th grader's grades to US 5th grade context), and flag non-standard transcripts (homeschool equivalencies, international school curricula like IB PYP/MYP that do not require conversion). The output must integrate with the admissions CRM.

## Target Customer
Admissions directors at schools receiving 50+ international applications per year who spend 1-3 hours per application on transcript interpretation.

## Impact If Solved
Reduces per-application transcript evaluation time from 1-3 hours to 10-15 minutes. Eliminates $7,500-$30,000 in annual credential evaluation service fees. Provides the admissions committee with standardized academic profiles that enable fair comparison of international and domestic applicants.
