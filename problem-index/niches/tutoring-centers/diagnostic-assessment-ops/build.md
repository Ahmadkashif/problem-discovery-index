# Error Pattern Recognition for Root-Cause Diagnosis

**Niche:** [[niches/tutoring-centers/diagnostic-assessment-ops/profile|Diagnostic Assessment Operations]]
**Industry:** [[industries/tutoring-centers|Tutoring Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A system that classifies student errors by type (computational, conceptual, procedural, reading comprehension) and traces them to root-cause prerequisite gaps — performing the diagnostic reasoning that experienced tutors do tacitly but new tutors can't replicate.
**Tags:** #bayesian-network #gradient-boosting #multiclass-classification #tabular-ml #tacit-knowledge-ml

## The Problem
When a student gets a math problem wrong, the answer alone doesn't diagnose the issue. An experienced tutor looks at how the student solved it: Did they set up the equation correctly but make an arithmetic error (computational)? Did they apply the wrong operation (conceptual)? Did they follow the right steps but in the wrong order (procedural)? Did they misinterpret the word problem (reading comprehension)? Each error type points to a different root cause and requires different remediation. New tutors — who constitute 40-60% of most centers' staff — classify all errors as "didn't understand the topic" and reteach the entire concept, missing the specific gap that would enable targeted, efficient remediation.

## Why Nobody Has Built This
Error classification requires structured data that tutoring centers don't collect: not just right/wrong answers but the student's specific incorrect answer, the work shown, and the reasoning attempted. Training a classification model requires experienced tutor annotations on hundreds of error examples per skill area, linking each error pattern to a root-cause diagnosis. This annotation effort hasn't been undertaken because no infrastructure captures the data, and no market incentive has justified the investment. The closest analog is educational research on misconception taxonomies (e.g., Brown & VanLehn's "repair theory"), which provides theoretical frameworks but not operational diagnostic tools.

## What to Build
An error classification engine for K-12 math and reading: (1) students enter answers through a digital interface that captures their specific response (not just correct/incorrect); (2) for multiple-choice items, the system recognizes which wrong answer was selected and matches it to known error patterns (e.g., selecting "24" instead of "42" for 6x7 indicates a reversal error, not a random guess); (3) for open-response items, the system accepts the student's answer and classifies the error type using a trained model; (4) error patterns are aggregated across problems and traced backward through the prerequisite graph to identify the most probable root-cause gap. Output: "This student's algebra errors are 70% procedural (step ordering) — likely root cause is weak understanding of inverse operations from 6th grade."

## Target Customer
Center directors and academic directors at tutoring centers with 50+ active students and 40%+ annual tutor turnover who want diagnostic accuracy independent of individual tutor expertise.

## Impact If Built
Provides new tutors with diagnostic capability that currently requires 2-3 years of experience to develop. Reduces misdiagnosis rates from 30-40% (typical for new tutors) to 10-15% (matching experienced tutor accuracy). Accelerates student remediation by 30-40% through accurate root-cause targeting from the first session.
