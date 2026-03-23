# MOS-to-IT-Role Granular Translation Engine

**Niche:** [[niches/it-staffing-firms/veteran-it-placement/profile|Veteran IT Career Placement]]
**Industry:** [[industries/it-staffing-firms|IT Staffing Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product translates military IT experience at the task level — mapping specific duties, systems, and clearances from military service records to precise civilian IT role requirements and salary bands.
**Tags:** #bert #text-classification #nlp #tacit-knowledge-ml #worker-facing

## The Problem
A veteran separating from the Army with MOS 17C (Cyber Operations Specialist), 6 years of service, experience with "Kali Linux, Wireshark, ACAS vulnerability scanning, and incident response on classified networks" needs to know: which civilian roles match (SOC Analyst? Penetration Tester? Security Engineer?), at what level (junior, mid, senior?), at what salary range, and which certifications they should pursue to fill gaps. Current translation tools map at the MOS level, which is too coarse — two 17C soldiers with the same rank but different duty assignments may qualify for entirely different civilian roles.

## Why Nobody Has Built This
The granular data does not exist in structured form. Military service records (DD-214, ERB/ORB) describe assignments and schools attended but not daily tasks. The mapping requires understanding both military and civilian IT domains deeply — a rare combination. DoD has not released structured task-level data for most MOSs. Building the mapping requires interviewing hundreds of veterans across specialties to capture the actual work performed at each duty station and rank level.

## What to Build
A translation engine that ingests a veteran's DD-214, military resume, and self-reported duty descriptions, then produces: (1) a ranked list of matching civilian IT roles with confidence scores, (2) certification gap analysis (what they need to get vs. what their military training already covers), (3) salary range expectations by geography, and (4) a "civilianized" resume that preserves accuracy while using terminology ATS systems can parse. The engine improves through feedback from successful placements.

## Target Customer
Veteran-focused IT staffing firms, Transition Assistance Program (TAP) providers, and military-friendly employers with dedicated veteran hiring programs.

## Impact If Built
Reduces average time-to-placement for veteran IT candidates from 4-6 months to 6-8 weeks. Increases salary attainment by 15-25% by placing veterans in roles that accurately reflect their experience level rather than defaulting to entry-level positions.
