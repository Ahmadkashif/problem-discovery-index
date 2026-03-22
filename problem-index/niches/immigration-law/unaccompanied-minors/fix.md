# Guardian Ad Litem & Stakeholder Coordination

**Niche:** [[niches/immigration-law/unaccompanied-minors/profile|Unaccompanied Minors]]
**Industry:** [[industries/immigration-law|Immigration Law]]
**Type:** Fix (Pain Point)
**One-liner:** Unaccompanied minor cases involve 5-8 stakeholders (attorney, GAL, ORR case manager, sponsor, social worker, pro bono mentor, interpreter) coordinated through email and phone calls with no shared visibility into case progress or upcoming deadlines.
**Tags:** #workflow-orchestration #automation #data-integration #worker-facing

## The Problem
A single unaccompanied minor case involves coordination among multiple stakeholders who operate in different organizations with no shared information system. The immigration attorney handles the legal case. The guardian ad litem (GAL) advocates for the child's best interests and submits reports to the court. The ORR (Office of Refugee Resettlement) case manager oversees the child's placement (shelter, foster care, or sponsor). The sponsor (usually a family member in the U.S.) has custody of the child. A social worker may provide therapeutic services. A pro bono attorney from a large firm may handle the state court component. An interpreter is needed for almost every interaction. Each of these stakeholders needs to know: what hearings are upcoming, what documents are needed, what the child's current placement status is, and what actions are pending. Currently, the lead attorney coordinates all of this through individual phone calls and email chains. There is no shared calendar, no shared document repository, no shared task list. When the GAL needs to file a report before a hearing, the attorney reminds them by email. When the ORR case manager changes the child's placement, the attorney may not learn about it until the next check-in call. Critical information falls through the cracks because no one has a complete picture.

## Why It's Still Broken
Each stakeholder operates within their own organization's systems — the legal aid organization uses LegalServer, the ORR case manager uses a federal case management system, the GAL may use nothing beyond email, the pro bono attorney uses their firm's document management system. These systems don't communicate. Building a cross-organizational coordination tool requires all parties to adopt a common platform, which faces institutional resistance (ORR won't use a tool not approved by HHS, law firms won't store client data on external platforms). Privacy concerns are heightened because the client is a minor — sharing information across organizations requires specific consent and compliance with child welfare confidentiality rules.

## What a Fix Looks Like
A lightweight coordination portal (not a full case management system) that provides a shared view of case milestones and responsibilities without requiring stakeholders to migrate from their existing systems. Each stakeholder gets a login with role-appropriate visibility: (1) shared calendar showing all court dates (immigration and state), filing deadlines, GAL report due dates, and ORR review dates, (2) task board showing pending actions by stakeholder ("GAL: submit best-interest report by March 15," "Sponsor: bring child to medical exam by March 10"), (3) secure messaging channel replacing email chains, (4) document sharing for court orders, GAL reports, and ORR placement notices, and (5) automated reminders sent to each stakeholder for their pending tasks. The portal is read-only for case details (the attorney enters updates from their case management system) and write-only for task completion and messaging — minimizing the data entry burden on already-overextended stakeholders.

## Who Feels the Pain
Lead attorneys who spend 3-5 hours per week per case on stakeholder coordination phone calls and email chains, and children whose cases are delayed because a GAL report wasn't filed on time or a state court hearing was missed because the pro bono attorney wasn't notified.

## Impact If Fixed
Reduces attorney coordination overhead by 50-70% (from 3-5 hours to 1-2 hours per case per week). Prevents missed deadlines caused by communication failures between stakeholders. For a legal aid organization with 25 active unaccompanied minor cases, this recovers 50-75 hours per week of attorney time — equivalent to more than one full-time attorney position.
