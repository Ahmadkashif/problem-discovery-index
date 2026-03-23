# Recurring Booking Change Chaos

**Niche:** [[niches/pet-services/client-communication-booking/profile|Client Communication & Booking]]
**Industry:** [[industries/pet-services|Pet Services]]
**Type:** Fix (Pain Point)
**One-liner:** Pet service providers managing 20+ recurring clients spend 30-60 minutes daily processing schedule changes — "skip Tuesday," "add Friday this week," "we're on vacation next week" — across text messages with no system to track the changes.
**Tags:** #automation #workflow-orchestration #quick-win #worker-facing

## The Problem
A dog walker with 25 recurring clients has a base schedule (MWF for Bella, daily for Max, TTh for Luna), but every week brings 5-10 changes: a client working from home skips a day, another needs an extra walk on Saturday, one family goes on vacation for a week, another changes their regular days starting next month. These changes arrive as text messages throughout the day ("Hey can you skip Wednesday this week? Thanks!"), and the walker must update their mental model, calendar, and invoicing. One forgotten change means showing up at an empty house or missing a walk the client expected.

## Why It's Still Broken
The per-change overhead is small (read text, update calendar, acknowledge), but the volume creates a management burden that's invisible until it causes an error. Most walkers manage their schedule in Google Calendar, which has no concept of "recurring with exceptions" — each change requires manually editing individual calendar events. There's no tool that models recurring pet service schedules with easy exception handling and keeps the client, walker, and invoicing system in sync.

## What a Fix Looks Like
A recurring schedule manager where each client has a base schedule, and changes are applied as exceptions: "skip," "add," "move." The walker can view the current week's actual schedule (base minus skips plus adds), and the system auto-adjusts invoicing (skipped walks aren't billed, added walks are). Changes can be requested by the client through a simple interface (tap to skip, tap to add) rather than requiring a text conversation. The walker's daily route recalculates when the schedule changes.

## Who Feels the Pain
Solo walkers and sitters managing 20+ recurring clients who make 1-2 scheduling errors per week — each error either wasting a trip or missing a committed service — and spend 30-60 minutes daily processing text-based schedule changes.

## Impact If Fixed
Eliminates scheduling errors (saving 1-2 wasted trips per week worth $30-60), reduces daily schedule management time by 60-70%, and provides accurate invoicing that reflects actual services delivered rather than a base schedule with manual adjustments.
