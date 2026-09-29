# The RFI That Sat for Nineteen Days

**Niche:** [[niches/construction-tech-platforms/submittal-rfi-routing/profile|Submittal & RFI Routing Content]]
**Industry:** [[industries/construction-tech-platforms|Construction Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Project engineers spend their careers sending follow-up emails about unanswered RFIs, and no platform reports reviewer turnaround against the contractual window or escalates on the clock, so chasing is a personality trait rather than a process.
**Tags:** #survival-analysis #time-series-forecasting #descriptive-statistics #evaluation-metrics #confidence-intervals #workflow-orchestration #automation #worker-facing
**Contested on:** Every serious competitor in document workflow is fighting to read the specification and decide who a submittal or RFI should go to, in what sequence, and by when — and whoever routes most accurately against the spec takes the account.

## The Problem
An RFI goes to the architect with a fourteen-day contractual response window. On day nineteen it is still open. The project engineer has sent three emails, each individually polite, each requiring her to notice, decide to chase, compose and send. She chases the loud ones and the ones she remembers. The quiet RFI on a detail that blocks an activity six weeks out gets chased on day thirty, by which point the activity is already at risk. Everyone in the industry knows RFI latency drives schedule impact, and no platform treats a passed response window as an event.

## Why It's Still Broken
The workflow engines send reminders, which everyone ignores, and stop there. Automatic escalation to a named person on a schedule is a small feature and a politically loaded one — the reviewer being escalated about is the architect, who is the owner's consultant, and a general contractor's platform automatically emailing an owner about its architect's tardiness is a conversation vendors have not wanted to start. So the escalation is left to a project engineer to perform manually, which converts a systematic problem into an interpersonal one and places it on the most junior person in the chain.

## What a Fix Looks Like
Escalate on the contractual clock, automatically, with the contract cited and the schedule consequence attached. Compute and publish reviewer turnaround: by reviewer, by discipline, by RFI type, against the contractual window, with the distribution rather than the average — the tail is what hurts. Prioritise chasing by downstream impact rather than by age, so the RFI blocking an activity three weeks out outranks an older one blocking nothing, which requires linking RFIs to the activities they affect and is the single most valuable connection missing from these systems. Give the architect the same turnaround view, since most reviewers are not deliberately slow and a distribution of their own performance is the most effective thing anyone can show them. Route the escalation through the contract rather than through a project engineer's persistence.

## Who Feels the Pain
Project engineers whose careers consist of follow-up emails; superintendents whose activities are blocked by answers nobody chased; and reviewers who are chased inconsistently and have no view of their own performance.

## Impact If Fixed
Turnaround measurement and automatic escalation on the contractual window are both trivial to build and are absent everywhere, which makes this the highest ratio of value to effort in the niche. Prioritising by downstream schedule impact is the part that changes outcomes rather than just tidying a queue, and it is also the link that feeds the slip forecasting in the general contractor niche.
