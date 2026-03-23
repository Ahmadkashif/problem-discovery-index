# Day-Of No-Show and Replacement Scramble

**Niche:** [[niches/catering-companies/temp-crew-coordination/profile|Temp Crew Coordination & Day-Of Staffing]]
**Industry:** [[industries/catering-companies|Catering Companies]]
**Type:** Fix (Pain Point)
**One-liner:** 10-15% of confirmed temp crew no-show on event day — and the operations manager has 2-4 hours to find replacements by calling through their roster one by one.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #automation #worker-facing

## The Problem
A caterer confirms a 12-person crew for Saturday's wedding. Two do not show up. It is 1 PM and service starts at 5 PM. The operations manager begins calling through their backup list — 15-20 phone calls to find 2 available people willing to work in 4 hours. Half do not answer. Three are already booked. One agrees but needs a ride. The event starts with 11 people instead of 12, degrading service quality. This scenario happens on 15-20% of events.

## Why It's Still Broken
No-shows are predictable — workers who confirmed less than 24 hours before the event, who have no-showed before, or who are booked for a 5 AM call time on a Sunday have measurably higher no-show rates. But caterers do not track these patterns because their scheduling system is a WhatsApp thread. There is no early warning system and no automated backup activation.

## What a Fix Looks Like
A no-show prediction model that scores each confirmed worker's show-up probability based on historical reliability, confirmation timing, event characteristics (early morning, late night, holiday), and communication patterns (did they respond to the reminder?). For workers scored below 70% probability, the system pre-activates a backup: contacting the next-ranked available worker before the no-show happens, not after. Automated 48-hour, 24-hour, and 4-hour confirmation pings with escalation to manual outreach if no response.

## Who Feels the Pain
The operations manager who spends the 3 hours before every large event anxiously checking confirmations instead of managing logistics, and the service captain who starts events understaffed and must redistribute work across the remaining crew.

## Impact If Fixed
Reducing effective no-show impact from 10-15% to under 3% prevents the understaffing that causes service failures on $5K-$30K events. Eliminating the day-of scramble recovers 2-3 hours of operations manager time per event — 200+ hours annually.
