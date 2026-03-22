# Automated Permit Application and Interconnection Filing by Jurisdiction

**Niche:** [[niches/solar-installers/permitting-interconnection/profile|Permitting & Interconnection]]
**Industry:** [[industries/solar-installers|Solar Installers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A platform that takes the solar system design and automatically generates jurisdiction-specific permit plan sets, fills out permit application forms, submits interconnection applications to the utility, and tracks both processes through approval — replacing the 2-5 hours of manual preparation and submission that a permitting coordinator currently spends per project.
**Tags:** #bert #automation #workflow-orchestration #compliance #large-language-models

## The Problem
A solar installer operating in a metro area may submit permits to 15-30 different jurisdictions, each with unique requirements: different plan set formats (some require a separate structural letter, some don't), different application forms (some online, some PDF, some in-person only), different code editions (2018 IRC vs. 2021 IRC vs. state amendments), different fees ($200-1,500), and different review timelines (3 days to 8 weeks). A dedicated permitting coordinator spends 2-5 hours per project preparing plan sets, completing application forms, and submitting to the specific jurisdiction. For an installer doing 30-50 installations per month, this requires 1-3 full-time permitting coordinators at $45K-65K each. Interconnection applications add another layer: each utility has its own application form, documentation requirements, and submission portal. The permitting coordinator must know the requirements for every jurisdiction and utility in their territory — institutional knowledge that walks out the door when the coordinator quits.

## Why Nobody Has Built This
The long tail of jurisdictions is the core challenge. There are 20,000+ building permit jurisdictions in the US, and only 300+ have standardized through SolarAPP+. Building a comprehensive database of requirements for even the top 1,000 jurisdictions requires researching each jurisdiction's permit application process, form format, required documents, fee schedule, and submission method — and maintaining this database as jurisdictions update their requirements. Many jurisdictions publish requirements as unstructured text on municipal websites or don't publish them online at all. Similarly, the 3,000+ utilities each have unique interconnection application processes. The total data maintenance burden has deterred startups from tackling this at scale.

## What to Build
A permit automation platform with three layers. First, a jurisdiction requirements database: for each jurisdiction in the installer's territory, maintain structured records of required documents, application forms (auto-fillable), fee schedules, submission methods, and review timelines — initially built through manual research, then maintained through automated monitoring of municipal website changes and installer feedback. Second, a plan set generator: take the system design from Aurora (equipment specifications, site plan, electrical diagram) and automatically generate the plan set in the format required by the specific jurisdiction — including jurisdiction-specific notes, code references, and structural details. Third, an application submitter and tracker: auto-fill application forms with project data, submit electronically where possible (online portals), generate print-ready packages where not, and track application status through approval, inspection scheduling, and PTO.

## Target Customer
Solar installers doing 20+ installations per month across multiple jurisdictions, currently employing 1-3 dedicated permitting coordinators. National solar companies operating in 10+ states where jurisdiction variability is extreme.

## Impact If Built
Reduces per-project permitting labor from 2-5 hours to 15-30 minutes through automated plan set generation and application preparation. Eliminates the institutional knowledge risk when permitting coordinators leave. Reduces permit rejection rates by ensuring jurisdiction-specific requirements are met on first submission. Worth $50-100 per project in labor savings, generating $5M-10M in addressable market across the US solar industry.
