# Buy: Background Screening Adapted to Gig Onboarding at Volume

**Niche:** [[niches/gig-delivery-platforms/onboarding-and-background-checks/profile|Onboarding, Background Checks & Identity]]
**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Screening vendors were built for employment hiring with a recruiter in the loop; gig onboarding runs millions of fully automated decisions with nobody reading the report.
**Tags:** #compliance #descriptive-statistics #evaluation-metrics #confidence-intervals #data-integration #workflow-orchestration #automation #worker-facing
**Contested on:** Whether screening products designed for a recruiter's judgement can carry a fully automated adjudication at gig volume.

## The Problem

Background screening is a mature purchased service. Criminal records, motor vehicle records, identity verification and continuous monitoring are available through well-established vendors with broad jurisdictional coverage and FCRA-compliant workflows.

The product assumes an employment hire: a recruiter receives a report, reads it, applies judgement, and follows the adverse action process with a candidate they have spoken to. Gig onboarding has no recruiter, no conversation and no judgement — a matrix adjudicates the report automatically, at a volume of millions a year, for a role where the applicant may never interact with a human at the platform at all.

## What Already Exists

Checkr, Sterling, HireRight and the screening category, with API-first delivery, continuous monitoring, adjudication matrix configuration and FCRA adverse action workflows including pre-adverse notice, report delivery and dispute intake. Identity verification vendors. Motor vehicle record monitoring. The coverage and the compliance scaffolding are genuinely good.

## The Customization Gap

**Adjudication is fully automated and the matrix is the entire judgement.** With no human reading the report, the matrix carries all the weight a recruiter would have carried, including the individualised assessment that fair-chance laws in several jurisdictions require. Vendor matrix configuration is a rules table; what is needed is a versioned, auditable policy with jurisdictional variation and a documented evidence basis — which the platform has to own.

**Nobody measures accuracy and the vendor will not.** The vendor's product is the report. Whether the report is right about a specific person is the platform's exposure, and measuring it requires auditing against primary sources — a programme with no place in the vendor relationship and no line in the contract.

**The adverse action flow assumes a candidate who is engaged.** FCRA pre-adverse notice, report copy and dispute opportunity are implemented as email sequences designed for a job applicant in an active process. A gig applicant who downloaded an app on a Tuesday may not open the email, may not read English fluently, and has no recruiter to ask. Compliance in form with total failure in substance is the normal outcome, and fixing it is product work on the platform's side.

**Continuous monitoring turns onboarding into a permanent condition.** Re-screening on new records means a courier can be deactivated mid-shift by a third-party data update, including an arrest without conviction. The policy for what triggers what, and what due process attaches, is a platform decision the vendor's alert stream does not make.

**Volume changes the economics of everything.** Millions of checks a year makes per-check cost dominant, which pushes toward cheaper, less accurate database searches over county-level verification — a trade-off with a direct accuracy consequence that the procurement decision rarely surfaces.

## Target Customer

Platform trust and safety and procurement teams selecting or renewing a screening vendor, who need to know what the contract does not cover. Also the screening vendors, for whom automated high-volume gig adjudication is a distinct segment whose accuracy and due-process requirements their employment-shaped product does not meet.

## Impact If Solved

The vendor keeps supplying records and the compliance scaffolding, and the platform owns the adjudication policy, the accuracy programme and a dispute experience built for someone who is not in a hiring process. The practical result is that an automated exclusion is measured, evidence-based and actually contestable rather than compliant on paper.
