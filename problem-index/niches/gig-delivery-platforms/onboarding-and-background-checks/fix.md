# Fix: The Dispute Nobody Finishes

**Niche:** [[niches/gig-delivery-platforms/onboarding-and-background-checks/profile|Onboarding, Background Checks & Identity]]
**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** An applicant excluded by a wrong record is told they may dispute it, and the dispute requires them to obtain court documents they have no idea how to get.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #compliance #large-language-models #workflow-orchestration #worker-facing #quick-win
**Contested on:** Whether the dispute process can be made completable by the people it is ostensibly for.

## The Problem

An applicant is rejected. They receive a pre-adverse action notice and a copy of the report, as required, with instructions that they may dispute inaccurate information. The report contains a record belonging to someone with a similar name, or a charge that was dismissed and never updated, or a matter that was expunged years ago.

To dispute it, they must identify which entry is wrong, understand the difference between disputing with the screening company and with the platform, and typically obtain certified documentation from the county court that holds the record — a process involving a physical clerk's office, a fee, and a form. Most people do not complete this. Many do not open the email. The abandonment rate is high and unmeasured, and every abandonment is recorded as an uncontested accurate result.

## Why It's Still Broken

The process is compliant. The obligations are notice, a copy of the report, and an opportunity to dispute, and they are met. Completability is not an obligation, so nobody owns it, and the outcome — most disputes abandoned — reads as confirmation that the reports were right.

The two parties who could fix it each have a reason not to. The screening vendor's dispute costs it money and produces no revenue. The platform has already moved on to the next applicant, and supply is abundant in most markets. Neither is measured on the population that vanishes at this step.

And the applicant has no advocate. Unlike an employment candidate who spoke to a recruiter, the gig applicant has no relationship with anyone at the platform, frequently no phone support, and no route to a human who could look at the report with them.

## What a Fix Looks Like

Make the dispute completable, and measure how many people complete it.

Start with the number. What share of applicants receiving a pre-adverse notice open it, start a dispute, complete one, and prevail. No platform reports this and it is the metric that makes the problem real. If completion is in the low single digits, the process is not functioning regardless of its legal adequacy.

Explain the report in plain language. The report itself is dense, jurisdictional and full of docket language. A plain-language explanation of each adverse entry — what it says, where it came from, what it would take to challenge it, and specifically whether it looks like a possible identity mismatch given the name and date of birth — is a language-model summarisation task over a structured record with a human-reviewed template, and it converts an impenetrable document into something a person can act on.

Take on the record retrieval. A substantial share of disputes fail because the applicant cannot obtain a court document. Many courts have electronic access, and the platform or the vendor can retrieve records at a fraction of the difficulty an individual faces. Doing the retrieval on the applicant's behalf, with their authorisation, removes the step where most disputes die.

Provide a human. One reachable person for adverse-action questions, in the applicant's language. The volume is smaller than it appears because most people never get this far, which is the problem.

Hold the application open. An applicant disputing a record should not have to reapply from scratch weeks later, which is a common design and a strong deterrent.

And route the systematic errors upstream. A screening source that repeatedly produces misattributions in a particular county is a data quality problem the vendor can fix, and the pattern is only visible to whoever aggregates dispute outcomes — which is the platform.

## Who Feels the Pain

Applicants wrongly excluded from an income source by a records error they cannot practically contest, disproportionately people with common names, people with expunged records who believed the matter closed, and people for whom English is a second language. And the platform, which loses supply it wanted, has an FCRA exposure it has not measured, and cannot state how many of its rejections were wrong.

## Impact If Fixed

The dispute process starts working for the population it exists for, which turns a legal formality into an actual remedy. The platform gets a measured completion rate and, through it, its first real estimate of screening error. And people excluded by a clerical mistake get back a route to an income — which for a large number of them is the entire consequence of the error.
