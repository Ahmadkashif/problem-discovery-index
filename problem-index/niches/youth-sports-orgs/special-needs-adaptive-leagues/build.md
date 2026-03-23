# Participant-Buddy Matching Engine

**Niche:** [[niches/youth-sports-orgs/special-needs-adaptive-leagues/profile|Special Needs Adaptive Leagues]]
**Industry:** [[industries/youth-sports-orgs|Youth Sports Organizations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool matches adaptive sports participants to support volunteers ("buddies") based on the participant's specific needs (physical support, behavioral guidance, communication assistance) and the volunteer's capabilities, experience, and training — a matching problem currently done by one overwhelmed coordinator on game day.
**Tags:** #recommendation #automation #workflow-orchestration #worker-facing

## The Problem
Adaptive sports programs pair each participant with a volunteer buddy who provides individualized support during activities. The matching is critical: a nonverbal child with autism needs a buddy experienced with AAC communication devices, a wheelchair user needs a buddy who can assist with transfers, and a child with behavioral triggers needs a buddy trained in de-escalation. Currently, the program coordinator makes these matches manually — reviewing participant profiles (which are often incomplete paper forms), assessing volunteer capabilities (which are self-reported and rarely verified), and trying to remember who worked well together last season. On game days with 30 participants and 30 buddies, the coordinator is physically running around the field making last-minute reassignments when matches don't work.

## Why Nobody Has Built This
Adaptive sports programs are small (50-200 participants per program), volunteer-run, and have zero technology budget. The matching problem is complex: it requires structured data about both participants (disability type, communication method, mobility level, behavioral considerations, sensory sensitivities) and volunteers (experience with specific disability types, physical capability, training completed, preferred age group). No mainstream sports platform collects this data. Building a matching engine for this market requires deep understanding of disability support needs that general sports tech companies don't have.

## What to Build
A matching platform that: (1) collects structured participant profiles from parents (disability type, mobility, communication method, sensory needs, behavioral considerations, support level required), (2) collects structured volunteer profiles (disability experience, training completed, physical capability, schedule, preferred age group), (3) generates optimal participant-buddy matches based on needs alignment and compatibility, (4) tracks match quality through session feedback from coordinators and families, (5) learns from match history (which pairings worked, which didn't) to improve future matches, and (6) handles game-day substitutions when a matched buddy is absent.

## Target Customer
Program directors of adaptive youth sports leagues managing 30-200 participants who need buddy matching every session or game day.

## Impact If Built
Reduces buddy-matching time from 2-4 hours per event to 15-30 minutes, dramatically improves match quality (reducing mid-session reassignments by 60-70%), and enables programs to scale participant enrollment by 30-50% because the matching bottleneck is the primary capacity constraint.
