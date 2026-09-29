# Ticket Volume Measured, Correctness Not

**Niche:** [[niches/hr-tech-platforms/employee-facing-hr-tools/profile|Employee-Facing HR Tools]]
**Industry:** [[industries/hr-tech-platforms|HR Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** HR service desks are measured on ticket volume, resolution time and satisfaction surveys, and nothing measures whether the answers employees received were right.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #compliance #workflow-orchestration #quick-win #worker-facing
**Contested on:** Every serious competitor building employee-facing HR software is fighting to let an employee answer a question about their own employment without asking a person — and whoever answers accurately from the employee's own record takes the deployment.

## The Problem
An employee asks about their equity vesting on termination and receives an answer from an HR generalist that is confidently wrong, because the generalist applied the standard policy without noticing this employee's grant predates a plan amendment. The ticket is closed, the satisfaction survey is positive because the reply was prompt and friendly, and the employee makes a decision about leaving on incorrect information. The service desk's metrics record a good outcome. Nothing in the system checks the answer, and the error surfaces months later or never.

## Why It's Still Broken
Correctness is harder to measure than speed, so service desks measure speed — a pattern common to every support function. In HR the consequences are more personal than in most: answers concern pay, leave, benefits and employment terms, where an error affects someone's finances or their entitlements. Sampling for quality is standard practice in contact centres and is rare in HR service delivery, and where it exists it usually assesses tone and process compliance rather than whether the answer was right.

## What a Fix Looks Like
Sample answers and check them against the record. A random sample of closed tickets is reviewed for factual correctness by someone with the authority and the record access to determine it — which is ordinary quality assurance practice and is the missing control. Classify errors by cause: policy misapplied, record misread, jurisdictional variation missed, plan version wrong. Report the error rate as a standing metric alongside volume and resolution time, because what gets measured is what gets managed and this function currently measures everything except the thing it exists to do. Feed confirmed error patterns into the knowledge base and into the answering system, so the same mistake is not made repeatedly by different generalists — which is the compounding benefit. And where an error is found, correct it with the employee, which is uncomfortable and is plainly the right thing to do.

## Who Feels the Pain
Employees who made decisions on incorrect information about their own employment; HR generalists doing their best with policy documents and no verification; and the organisation, whose service quality is measured on everything except accuracy.

## Impact If Fixed
Answer sampling is inexpensive and is the only way an HR function can know whether it is telling people the truth about their own entitlements. The error taxonomy typically concentrates in a small number of causes — jurisdictional variation and policy versioning above all — which are exactly the things the automated answering in this niche is designed to handle correctly.
