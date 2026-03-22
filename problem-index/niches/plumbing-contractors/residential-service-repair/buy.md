# ServiceTitan-Native Smart Dispatch with Skills and Parts Matching

**Niche:** [[niches/plumbing-contractors/residential-service-repair/profile|Residential Service & Repair]]
**Industry:** [[industries/plumbing-contractors|Plumbing Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** ServiceTitan's dispatch board shows technician availability and location but has no concept of technician skills, truck inventory, or job-type matching — a native plugin that adds these dimensions to dispatch decisions would eliminate the dispatcher's reliance on memory.
**Tags:** #data-integration #workflow-orchestration #automation #quick-win

## The Problem
ServiceTitan is the dominant FSM platform for residential plumbing with an estimated 30-40% market share among mid-size shops (5-20 trucks). Its dispatch board shows a map with technician locations, a calendar with availability blocks, and a call queue — but matching a call to a technician is entirely manual. The dispatcher drags a job to a tech's calendar based on proximity and availability. There is no structured data on which technicians are skilled at which job types (tankless installs, sewer line replacements, gas line work), what parts each truck currently carries, or which technician has the highest close rate for different price tiers. Every dispatch decision depends on the dispatcher's personal knowledge of the team.

## What Already Exists
ServiceTitan's dispatch board provides GPS-based technician location, schedule availability, and basic job categorization. Third-party route optimization tools (OptimoRoute, WorkWave) can optimize multi-stop routes but don't integrate with ServiceTitan's job-type and skills context. ServiceTitan's "Smart Dispatch" feature (released 2024) recommends technicians by proximity and availability but does not factor in skills, truck inventory, or historical performance.

## The Customization Gap
The gap is a skills-and-inventory layer on top of ServiceTitan's existing dispatch infrastructure. Needed: (1) a technician skills matrix — editable by the service manager — that tags each tech's proficiency level (apprentice/journeyman/expert) for job categories (water heater, drain, sewer, gas, fixture, repipe), (2) a truck inventory module that tracks high-value parts on each truck (water heaters by size/fuel/brand, common fittings, specialty tools) updated by the tech via mobile app at end of day, and (3) a dispatch recommendation engine that ranks available technicians for each incoming call by weighted score: proximity (30%), skill match (30%), truck inventory match (25%), historical close rate for job type (15%). Built as a ServiceTitan Certified App using their open API, sold at $49-99/month per dispatched tech, positioned as a "dispatch intelligence" upgrade for shops that have outgrown manual matching.

## Target Customer
Residential plumbing companies running 5-20 trucks on ServiceTitan, with a dedicated dispatcher who currently relies on memory and whiteboard notes to match technicians to calls, experiencing 2-4 mis-dispatches per day that result in supply house runs or return visits.

## Impact If Solved
Reduces mis-dispatches by 40-60%, eliminating 1-2 supply house trips per tech per day (saving $50-100 per trip in drive time and lost billable hours). Increases first-trip completion rate from an industry average of 65-70% to 80-85%, directly improving customer satisfaction and same-day revenue capture.
