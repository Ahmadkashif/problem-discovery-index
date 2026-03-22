# Landlord Approval Bottleneck Tracker

**Niche:** [[niches/general-contractors/commercial-tenant-improvement/profile|Commercial Tenant Improvement Contractors]]
**Industry:** [[industries/general-contractors|General Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** TI contractors stop losing days on the schedule because a landlord approval request is sitting in a property manager's inbox with no visibility, no escalation, and no one tracking it.
**Tags:** #decision-trees #automation #workflow-orchestration #worker-facing

## The Problem
Commercial tenant improvement work requires landlord or property manager approval at multiple stages: design review, MEP (mechanical/electrical/plumbing) plan approval, construction start authorization, inspection access coordination, and substantial completion sign-off. Each approval can take 2-10 business days depending on the property management company. TI contractors submit approvals via email and then wait — with no tracking system, no escalation path, and no visibility into whether the property manager has even opened the submission. A single stalled approval can idle a crew for days on a 6-week project where every day matters. Contractors report that 20-30% of TI schedule delays are caused by landlord/PM approval bottlenecks.

## Why It's Still Broken
No construction PM tool models the landlord approval chain. Procore's RFI and submittal workflows are designed for architect/engineer review, not for property manager approvals which have different stakeholders, different SLAs, and different escalation paths. Property managers use their own systems (Yardi, AppFolio, MRI) which have no integration with construction PM tools. The TI contractor is stuck between two disconnected systems — their project management tool and the property manager's property management tool — with email as the only bridge.

## What a Fix Looks Like
A lightweight approval tracking layer specifically for landlord/property manager approvals in TI projects. The contractor submits an approval request through the system (attaching plans, photos, or documents) which generates a tracked email to the property manager with a unique link. The system logs when the email is opened, when the linked documents are viewed, and provides a simple approve/request-changes/deny response interface. If no response in the configured SLA (e.g., 3 business days), automatic escalation reminders go to the property manager and CC the building owner or asset manager. The contractor's dashboard shows all pending approvals across their project portfolio, sorted by days waiting and schedule impact.

## Who Feels the Pain
Project managers and superintendents who spend 3-5 hours per week following up on landlord approvals via phone and email. They carry the mental burden of tracking which approvals are pending for which projects and when to escalate — while simultaneously managing active construction on other jobsites.

## Impact If Fixed
Reduces landlord-approval-related schedule delays by 40-60%, recovering 1-3 days per TI project. Eliminates 3-5 hours per week of manual follow-up per active project portfolio. Creates an audit trail that protects the contractor when delay claims arise — documented proof that the approval was submitted on date X and not responded to until date Y.
