# Classification Disputes Are the Best Signal and Are Resolved One at a Time

**Niche:** [[niches/insurance-tpa/workers-comp-rating-bureaus/profile|Workers' Compensation Rating Bureaus]]
**Industry:** [[industries/insurance-tpa|Insurance Third-Party Administrators (TPAs)]]
**Type:** Fix (Pain Point)
**One-liner:** Every argument about which class an employer belongs in is a report that the classification system does not describe how that business works.
**Tags:** #tacit-knowledge-ml #text-classification #large-language-models #worker-facing #data-integration

## The Problem
Workers' compensation classification assigns an employer to a code describing what its employees do, and the code sets the base rate. The system has hundreds of classes with detailed inclusion and exclusion rules, and it generates constant disagreement — at premium audit, at inspection, and through formal dispute.

Classification specialists resolve those. An inspector visits, or a specialist reads the operations description and the payroll records, and decides. They accumulate real knowledge doing it: which businesses routinely describe themselves into the wrong class, which two classes are chronically confused, which industries have changed so much that no existing class fits, which employers are structuring operations to reach a cheaper code.

The resolution updates the employer's classification. The reasoning, and the pattern the specialist recognized, are not recorded anywhere the organization can use.

So the same disputes recur, the same ambiguities are re-litigated employer by employer, and the strongest available signal about where the classification system is failing — the disputes themselves — is treated as casework rather than as evidence.

## Why It's Still Broken
Classification is administered as a rules function. The output is a decision on an employer, filed against that employer, and the process is measured on turnaround and consistency of application. Nothing asks whether the rule being applied is the right rule.

The rules are also filed and approved, so changing a class is a regulatory undertaking. That makes the institutional posture toward classification change cautious, and cautious has hardened into not collecting the evidence that would inform it.

And the knowledge is genuinely specialist. People who understand the classification system deeply are few and long-tenured, and when they retire their sense of where the system creaks retires with them.

## What a Fix Looks Like
Treat disputes and inspections as measurements of the classification system.

**Structured resolution records.** The classes in contention, the operations facts that decided it, the rule relied on, the outcome, and — critically — whether the specialist thought the rule fitted the business well. That last field is the one nobody has and the one that matters.

**Aggregate the disputes.** Pairs of classes that are chronically confused, industries generating disproportionate disputes, and business types that fit nothing are all computable once resolutions are structured, and each is a specific instruction about where the system needs work.

**Attach knowledge to classes, not to employers.** Interpretation notes, boundary cases, and worked examples belong on the class, so the next specialist facing the same question starts where the last one finished.

**Retrieval at the point of decision.** A specialist opening a dispute should see how the organization has resolved comparable cases, with reasoning. This is the largest single efficiency in the function and it currently depends on asking a colleague.

**Feed it into the classification review.** Once disputes are evidence rather than casework, proposals to split, merge, or redefine a class arrive with a quantified basis instead of an anecdote — which is what makes a regulatory filing defensible.

## Who Feels the Pain
Classification specialists, re-deriving reasoning colleagues worked out. New staff, who need years to learn a system whose interpretation is undocumented. Employers, who receive different answers depending on who handled their case. And the organization, whose classification system is the foundation of every rate it publishes and whose failure points it has no map of.

## Impact If Fixed
Classification decides the base rate for every employer in the system, and the disputes it generates are a free, continuous, expert-generated diagnosis of its defects — currently discarded one case at a time. Capturing them makes the interpretation consistent, compresses the years it takes to develop a specialist, and gives the organization an evidence base for the class changes it has been reluctant to make without one.
