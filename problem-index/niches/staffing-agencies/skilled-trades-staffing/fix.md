# Candidate Skill Assessment Inconsistency Across Recruiters

**Niche:** [[niches/staffing-agencies/skilled-trades-staffing/profile|Skilled Trades Staffing]]
**Industry:** [[industries/staffing-agencies|Staffing Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** Two recruiters interviewing the same welder will rate their skill level differently because there is no standardized assessment process — leading to mismatched placements and client complaints.
**Tags:** #tacit-knowledge-ml #gradient-boosting #multiclass-classification #tabular-ml #worker-facing

## The Problem
When a skilled trades candidate walks into a staffing office, the recruiter assesses their skill level through a combination of resume review, verbal interview, and sometimes a practical test. But the assessment is highly subjective: one recruiter rates a welder as "journeyman-level" based on years of experience, while another recruiter would rate the same welder as "advanced apprentice" based on the range of processes they have actually used. These inconsistent assessments lead to mismatched placements — a candidate rated too high gets sent to a job they cannot perform, damaging the client relationship, while a candidate rated too low sits in the database unplaced for jobs they could excel at. Experienced recruiters with trade backgrounds make better assessments, but most recruiters have no welding, electrical, or machining experience themselves.

## Why It's Still Broken
Standardized trade skill assessments exist (NCCER, AWS qualification tests) but they are time-consuming (2-4 hours), expensive ($50-$200 per test), and overkill for a placement that might last 2 weeks. Staffing firms need a quick (15-20 minute) assessment that produces a consistent skill profile regardless of which recruiter administers it. Building this requires encoding the domain knowledge of experienced trade recruiters into a structured rubric — essentially capturing the tacit knowledge of "what questions to ask and how to interpret the answers" that senior recruiters have developed through years of placing hundreds of tradespeople.

## What a Fix Looks Like
A structured digital assessment tool administered during candidate intake, with trade-specific question paths: a welder is asked about specific processes, positions, materials, and codes they have worked with, then presented with 3-5 scenario-based questions ("the weld is porosity testing high — what do you check first?") designed by experienced trade professionals. The system produces a standardized skill profile with competency ratings by trade sub-specialty, verified against the candidate's certification documentation. The profile is consistent regardless of which recruiter administers it and directly maps to job order requirements for matching.

## Who Feels the Pain
Recruiters without trade backgrounds who are uncomfortable assessing candidates they cannot technically evaluate, and clients who receive workers whose skills do not match the staffing firm's representation.

## Impact If Fixed
Reduces skill-mismatch placements by 40-50% (each costing $1K-$3K in client trust and replacement costs), enables non-technical recruiters to accurately assess trade candidates, and standardizes the firm's quality guarantee to clients.
