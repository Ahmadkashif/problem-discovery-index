# ADA Grievance Tracking and Resolution Process

**Niche:** [[niches/municipal-services/ada-accessibility-services/profile|ADA Accessibility Services]]
**Industry:** [[industries/municipal-services|Municipal Services]]
**Type:** Fix (Pain Point)
**One-liner:** ADA grievances are filed on paper forms that disappear into HR filing cabinets — complainants never hear back, and the city has no record of resolution when DOJ investigators ask.
**Tags:** #workflow-orchestration #compliance #worker-facing #quick-win

## The Problem
Title II requires municipalities to establish a grievance procedure for ADA complaints and designate a responsible employee (the ADA coordinator). In practice, most municipalities have a PDF form on their website (or a paper form at city hall) that gets submitted to the city clerk, forwarded via email to someone in HR or public works, and then... nothing. There's no ticketing system, no resolution timeline, no tracking of whether the barrier was actually remedied. When a complainant follows up, nobody can find their original grievance. When DOJ conducts a compliance review, the city can't demonstrate that it has a functioning grievance process.

## Why It's Still Broken
ADA grievance volume is low in most municipalities (5–30 per year), which makes it seem unimportant. But each grievance represents a potential federal civil rights complaint, and the lack of documented response dramatically worsens the city's legal position. General-purpose ticketing systems (Zendesk, ServiceNow) don't include ADA-specific intake fields (barrier type, facility location, accommodation requested), resolution categories (barrier removed, accommodation provided, referred to transition plan), or the compliance reporting format that DOJ expects. The ADA coordinator — typically an HR generalist with 15 other responsibilities — doesn't have time to set up and maintain a custom workflow.

## What a Fix Looks Like
A pre-configured online grievance intake form with ADA-specific fields (barrier location, type of disability, accommodation needed, date of occurrence) that creates a tracked case visible to the ADA coordinator and the complainant. Automated acknowledgment within 24 hours. Resolution deadline tracking (15 business days for initial response). Resolution categories aligned with DOJ compliance expectations. An annual summary report showing total grievances, resolution rates, average response time, and most-common barrier types. Deployable in under an hour with no IT involvement — embed the intake form on the city website and start receiving structured complaints.

## Who Feels the Pain
ADA coordinators who know they're non-compliant but don't have time to build a process from scratch, and residents with disabilities whose complaints disappear into a void.

## Impact If Fixed
Reduces DOJ enforcement risk by documenting a functioning grievance process — the single most-cited deficiency in Title II compliance reviews. Improves complainant satisfaction by providing acknowledgment and tracking. Generates data on recurring barriers that informs capital planning, potentially directing $50K–$200K in accessibility improvements to the highest-impact locations.
