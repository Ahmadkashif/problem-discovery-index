# 811 Locate Request Coordination

**Niche:** [[niches/utility-contractors/small-residential-utility/profile|Small Residential Utility]]
**Industry:** [[industries/utility-contractors|Utility Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** 811 utility locate requests — the mandatory step before any excavation to mark existing underground utilities — take 2-10 business days to process, and 20-30% of locates are incomplete or late, forcing contractors to either delay construction (losing money) or excavate without complete locates (risking utility strikes and OSHA violations).
**Tags:** #automation #workflow-orchestration #compliance #worker-facing

## The Problem
Federal law (Pipeline Safety Improvement Act) requires contractors to call 811 before any excavation to request marking of existing underground utilities. The 811 center dispatches locate requests to every utility with underground facilities in the area (gas, water, sewer, electric, telecom, cable). Each utility must mark their facilities within 2-10 business days (varies by state). The contractor cannot begin excavation until all utilities have responded. The problem: 20-30% of the time, one or more utilities fail to respond within the window — they don't mark their facilities on time, or they mark incomplete locates (marking the main but not the service line). The contractor scheduled a crew and equipment for the dig date, but the incomplete locate means they either: (1) delay construction (crew idle time costs $500-1,500 per day), (2) hand-dig around the un-located utility (slower and more expensive), or (3) excavate without the locate (illegal, risking a $10K+ utility strike and OSHA citation).

## Why It's Still Broken
The 811 system is fragmented: each state operates its own 811 center with different processes, timelines, and enforcement mechanisms. Utilities receive hundreds of locate requests daily and prioritize by volume, not by the contractor's schedule. There is no feedback loop: when a utility misses the locate deadline, the contractor calls 811 to report the late locate, 811 notifies the utility, and the utility adds it to the queue — adding days to the delay. No tool helps the contractor track which utilities have responded and which are outstanding, or escalate late locates proactively.

## What a Fix Looks Like
A locate tracking and escalation system that: (1) submits 811 locate requests through the state's online portal (most states support online submission) and captures the ticket number and utility notification list; (2) tracks responses from each notified utility — marked complete, marked as clear (no facilities in the area), or no response; (3) identifies late or missing responses 24 hours before the locate expires and auto-generates escalation notices to the 811 center and the non-responding utility; (4) alerts the contractor's scheduler when the locate is complete (all utilities responded) so the construction crew can be confirmed; and (5) maintains a locate compliance history by utility — documenting which utilities consistently miss deadlines, useful for regulatory complaints and industry advocacy.

## Who Feels the Pain
Small utility contractors who schedule crews based on the locate completion date and lose $500-1,500 per day when locates are late. Homeowners whose connection is delayed because a utility didn't mark their facilities on time. Excavation contractors who face the impossible choice between financial loss (waiting) and legal risk (digging without complete locates).

## Impact If Fixed
Reduces construction delays from incomplete locates by 40-60% through proactive tracking and escalation. Saves $200-500 per late-locate incident in avoided crew idle time. Creates data-driven evidence of locate performance by utility, supporting regulatory improvement efforts. Reduces utility strike risk by ensuring excavation only begins after all locates are confirmed complete.
