# Application-to-Audit Wait Time Bottleneck

**Niche:** [[niches/energy-auditors/low-income-community-programs/profile|Low-Income Community Programs]]
**Industry:** [[industries/energy-auditors|Energy Auditors]]
**Type:** Fix (Pain Point)
**One-liner:** Low-income households wait 12-24 months from WAP application to energy audit, not because of funding shortages but because eligibility determination and scheduling workflows are manual and sequential.
**Tags:** #automation #workflow-orchestration #compliance #worker-facing

## The Problem
When a low-income household applies for WAP services, the community action agency must: (1) verify household income against 200% of federal poverty guidelines, (2) confirm home ownership or landlord permission, (3) check utility account status, (4) score the application on DOE priority criteria (elderly, disabled, children under 6, high energy burden), (5) rank the application against all pending applications, and (6) schedule the audit when the household reaches the top of the ranked queue. Steps 1-4 require collecting and verifying documentation from the applicant, utility company, and sometimes the landlord — a back-and-forth process managed through phone calls and mail that takes 4-8 weeks. Step 5 requires manually recalculating the priority queue whenever a new application is processed. Step 6 requires coordinating auditor availability with homeowner availability. The total pipeline takes 12-24 months while eligible households endure another heating or cooling season with high energy bills.

## Why It's Still Broken
Eligibility determination requires document verification (tax returns, pay stubs, utility bills, ownership records) that cannot be fully automated without integration with income verification services, utility data-sharing agreements, and property records databases. CAAs are nonprofits with limited IT capacity to build these integrations. The DOE priority scoring formula is straightforward to implement programmatically but CAAs calculate it manually because NEAT/MHEA does not include an intake module. The sequential nature of the pipeline (eligibility must be complete before scheduling) means delays at any step cascade.

## What a Fix Looks Like
A streamlined intake pipeline that: accepts applications online with document upload (tax returns, pay stubs), auto-verifies income against utility LIHEAP records where data-sharing agreements exist, calculates DOE priority scores automatically upon eligibility confirmation, maintains a dynamically ranked wait list visible to both the CAA and the applicant, and triggers audit scheduling automatically when the applicant reaches the queue threshold. The applicant can track their position online rather than calling the CAA monthly for status updates.

## Who Feels the Pain
Low-income households waiting 12-24 months for energy efficiency improvements that would immediately reduce their utility burden, CAA intake staff who spend 50% of their time on eligibility verification phone calls and paperwork, and CAA directors who cannot spend their annual WAP allocation because the intake pipeline is the bottleneck.

## Impact If Fixed
Reduces application-to-audit time from 12-24 months to 3-6 months by parallelizing verification steps and automating priority scoring. Enables CAAs to fully spend their annual WAP allocations, serving 20-30% more households per year.
