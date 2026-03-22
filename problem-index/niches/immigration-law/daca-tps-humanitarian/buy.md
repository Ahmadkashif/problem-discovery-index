# Humanitarian Case Evidence Tracker

**Niche:** [[niches/immigration-law/daca-tps-humanitarian/profile|DACA/TPS & Humanitarian Relief]]
**Industry:** [[industries/immigration-law|Immigration Law]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** U-visa, T-visa, and VAWA cases require specific evidence packages (law enforcement certifications, medical records, personal declarations, country conditions evidence) that are tracked in spreadsheets — no case management system structures evidence collection around the requirements of each humanitarian form.
**Tags:** #workflow-orchestration #data-integration #compliance #worker-facing #quick-win

## The Problem
Humanitarian immigration cases (U-visa for crime victims, T-visa for trafficking victims, VAWA self-petitions for domestic violence victims) require assembling a specific evidence package that is unique to each visa type. A U-visa requires: a personal declaration describing the crime, a law enforcement certification (Form I-918 Supplement B) signed by the investigating agency, police reports, medical records, evidence of substantial harm, and evidence of helpfulness to law enforcement. Each piece of evidence must be obtained from a different source (the client, law enforcement, hospitals, therapists) with different timelines and different levels of cooperation. The law enforcement certification alone requires identifying the correct certifying agency, sending the request, following up (agencies have no deadline to respond and often take 3-12 months), and tracking which certifications have been received. For a legal aid organization handling 30-50 active U-visa cases, tracking evidence status across all cases is a spreadsheet nightmare: which clients have their police reports, which law enforcement certifications are outstanding, which personal declarations need revision, which medical records have been requested but not received.

## What Already Exists
Docketwise and INSZoom provide document storage and task management. LegalServer (used by many legal aid organizations) tracks case milestones. But none of these systems have evidence collection workflows structured around the specific requirements of I-918 (U-visa), I-914 (T-visa), or I-360 (VAWA). They treat all immigration cases the same — generic document upload and generic task lists. The evidence requirements for a U-visa are fundamentally different from a family-based petition, but the case management system treats them identically.

## The Customization Gap
The missing layer is form-specific evidence collection workflows: (1) for each humanitarian case type, a structured checklist of required evidence with source identification (who has it), status tracking (requested, received, reviewed, approved), and deadline management (statute of limitations for law enforcement certification requests), (2) law enforcement certification tracking — a dashboard showing all outstanding I-918B requests by agency, with automated follow-up letter generation at 30/60/90 days, (3) personal declaration workflow — a guided interview template (in the client's language) that walks through the required elements of a declaration for each visa type, generating a draft that the attorney reviews, and (4) evidence package completeness scoring — a visual indicator showing what percentage of required evidence has been collected, what is outstanding, and what is blocking filing. This is a customization of existing case management: the document storage and task management exist, but the humanitarian case-specific evidence structure does not.

## Target Customer
Legal aid organizations and immigration attorneys handling 15+ active U-visa, T-visa, or VAWA cases, currently tracking evidence collection in spreadsheets with manual follow-up for law enforcement certifications.

## Impact If Solved
Reduces evidence tracking overhead from 2-3 hours per case per month to 30 minutes of dashboard review. Prevents cases from stalling because a law enforcement certification request was sent but never followed up on (the most common bottleneck in U-visa cases). For an organization with 40 active humanitarian cases, this recovers 60-100 hours per month of paralegal time and accelerates case resolution for trauma survivors.
