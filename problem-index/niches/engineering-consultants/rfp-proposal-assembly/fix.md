# Resume and Project Sheet Inconsistency Across Proposals

**Niche:** [[niches/engineering-consultants/rfp-proposal-assembly/profile|RFP/Proposal Assembly Workflows]]
**Industry:** [[industries/engineering-consultants|Engineering Consultants]]
**Type:** Fix (Pain Point)
**One-liner:** The same engineer's resume and the same project description appear with different details in different proposals — conflicting experience dates, inconsistent project values, missing recent projects — because each proposal is assembled from a different historical copy with no single source of truth.
**Tags:** #data-integration #automation #compliance #worker-facing

## The Problem
When a principal or marketing coordinator assembles a proposal, they pull staff resumes and project descriptions from the most convenient past proposal — which may be 6 months or 3 years old. The result is that the same engineer's resume contains different project lists, different years of experience, and different credential descriptions across concurrent proposals. If a selection committee reviews two proposals from the same firm and notices discrepancies, it damages credibility. Worse, on federal proposals (SF330), discrepancies in project values, roles, or dates can trigger audit flags or disqualification. The root cause is that there is no single-source resume or project database — every proposal contains a snapshot that diverges immediately after submission.

## Why It's Still Broken
Maintaining a "master resume" and "master project sheet" requires discipline that firms consistently fail at: someone must update the master after every project milestone, every new certification, every conference presentation. In practice, the master resumes live in a shared drive folder that is updated once a year (if ever), and the proposal writer uses whatever version is fastest to find. The problem compounds as firms grow — a 30-person firm with 200 completed projects has 30 resumes and 200 project sheets to maintain, a data management burden that no one is assigned.

## What a Fix Looks Like
A lightweight database (not a full CRM) that serves as the single source of truth for staff profiles and project records. Staff profiles auto-update when projects are marked complete — the project's details (name, client, value, role, completion date) are added to every team member's resume. When a proposal is assembled, resumes and project sheets are generated from the database, ensuring consistency. A version control system tracks what was submitted in each proposal, so if a selection committee asks about a discrepancy, the firm can trace the difference. Annual review prompts ensure certifications, registrations, and continuing education are updated.

## Who Feels the Pain
Marketing coordinators who discover resume discrepancies during proposal QA review (often the night before submission), and principals whose credibility is damaged when a client notices inconsistencies.

## Impact If Fixed
Eliminates resume/project sheet discrepancies that currently affect 15-25% of proposals. Reduces QA review time from 2-3 hours to 30 minutes per proposal. Prevents the occasional proposal disqualification due to SF330 data inconsistencies — each disqualification represents $15,000-50,000 in wasted pursuit effort.
