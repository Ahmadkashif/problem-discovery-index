# Skilled Trades Staffing

**Parent Industry:** [[industries/staffing-agencies|Staffing Agencies]]
**Category:** Low Digitized

## Profile
**Market Size:** $10-15B
**Share of Parent Industry:** ~6%
**Digital Adoption:** Low-Medium — Bullhorn serves the segment but candidate records often lack structured skill data; credential verification is manual and fragmented
**Target Buyer:** Branch manager at an industrial or trades staffing firm placing welders, electricians, machinists, and pipefitters
**Automation Potential:** Medium — the matching problem is more complex than light industrial due to specialized certifications and skill hierarchies, but the compliance documentation is more structured

## What Makes This a Distinct Niche
Skilled trades staffing places workers whose qualifications are defined by specific certifications, code endorsements, and demonstrated competencies — not just "warehouse experience" but "AWS D1.1 structural steel certified welder with TIG/MIG/FCAW processes, OSHA 30, and TWIC card." The matching problem is fundamentally different from light industrial: a welder certified in stick welding (SMAW) is not interchangeable with one certified in TIG welding (GTAW), even though both appear as "welders" in the ATS. Clients require specific certifications documented on the candidate's profile, and sending an under-qualified worker to a petrochemical site or power plant can create safety hazards and regulatory violations.

## Current Tools & Gaps
Bullhorn and generic ATS platforms store credential information as text fields or attached PDFs, but do not understand certification hierarchies (an AWS D1.1 6G certification implies competency in 1G through 5G positions). Search is keyword-based: searching for "welder" returns thousands of results without distinguishing between certified structural welders and entry-level shop hands. Credential verification is manual — a recruiter calls the certifying body or checks a PDF certificate. No system matches the multi-dimensional skill requirements of a job order (welding process + base metal + position + code + safety certifications) against structured candidate qualifications.

## Problems
- [[niches/staffing-agencies/skilled-trades-staffing/build|🔨 Build: Structured Skill Taxonomy and Certification Matching Engine]]
- [[niches/staffing-agencies/skilled-trades-staffing/buy|🛒 Buy: Trade Credential Verification and Expiration Tracking]]
- [[niches/staffing-agencies/skilled-trades-staffing/fix|🔧 Fix: Candidate Skill Assessment Inconsistency Across Recruiters]]
