# ATS Integration & Score Plumbing

**Parent Industry:** [[industries/talent-assessment-platforms|Talent Assessment Platforms]]
**Category:** Highly Automatable
**Contested on:** Whether the score arrives in the hiring system with the context that makes it interpretable, or as a bare number in a field.

## Profile
**Market Size:** ~$160M — 4% of US pre-employment assessment
**Share of Parent Industry:** ~4%
**Digital Adoption:** Moderate — integrations exist and carry almost nothing
**Target Buyer:** Vendors; employers' HR technology teams
**Automation Potential:** Very high — this is entirely integration work

## What Makes This a Distinct Niche

An assessment result reaches the hiring decision through an integration between the assessment platform and the applicant tracking system. What the integration carries determines what the decision-maker sees.

In practice it carries a number, and sometimes a band. The interval, the construct descriptions, the validated range, the administration quality, the accommodation status and the instrument version are all left behind. So the recruiter sees a sortable column of numbers, which is the presentation most likely to be misused, and the guardrails that the assessment platform might provide are on a screen nobody opens.

The niche is distinct because it is pure plumbing with disproportionate consequences: the integration's field list is effectively the specification for how the score will be used.

## Current Tools & Gaps

Standard integrations between the major assessment vendors and applicant tracking systems, typically triggering an assessment on application and writing a score back. Middleware and iPaaS connectors. HR-Open and similar data standards, partially adopted. Status synchronisation for invitation, started and completed.

The gaps are the fields and the retention. The integration writes a score and drops the context. Nothing carries the instrument version, which makes any later validation uninterpretable. Nothing carries administration quality or accommodation status. And on the other side, the score is frequently not written into the employee record at hire, which is the omission that makes local validation impossible.

## Problems
- [[niches/talent-assessment-platforms/ats-integration/build|🔨 Build: An Integration That Carries the Context]]
- [[niches/talent-assessment-platforms/ats-integration/buy|🛒 Buy: HR Integration Platforms Adapted to a Decision Artefact]]
- [[niches/talent-assessment-platforms/ats-integration/fix|🔧 Fix: A Sortable Column of Bare Numbers]]
