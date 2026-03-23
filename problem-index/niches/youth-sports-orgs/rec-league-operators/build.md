# Automated Balanced Draft with Multi-Constraint Optimization

**Niche:** [[niches/youth-sports-orgs/rec-league-operators/profile|Rec League Operators]]
**Industry:** [[industries/youth-sports-orgs|Youth Sports Organizations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool generates balanced team assignments that simultaneously satisfy skill ratings, age distribution, geographic clustering, sibling placement, coaching parent requests, and carpool friend requests — the most politically contentious process in rec sports.
**Tags:** #reinforcement-learning #automation #workflow-orchestration #quick-win

## The Problem
Rec league draft night is the most stressful event on the commissioner's calendar. They must assign 200-500 children to 20-40 teams while balancing: skill ratings (from evaluations or prior season performance), age distribution within the division, geographic clustering (kids from the same school together for carpooling), sibling placement (together or separate, per family preference), coaching parent assignment (the coach's child must be on their team), and friend requests (parents who want their kids together). This is a multi-constraint optimization problem that commissioners currently solve with Excel, poster boards, and magnets over 4-8 hours of manual sorting. The result is always imperfect, and every perceived imbalance generates parent complaints that last the entire season.

## Why Nobody Has Built This
LeagueApps and SportsEngine offer basic random or snake-draft team assignment, but these don't handle the 6+ simultaneous constraints that rec leagues actually care about. Building a true balanced draft optimizer requires formulating it as a constraint-satisfaction problem with weighted priorities (skill balance is more important than carpool convenience, but both matter). The logic is well-understood in operations research but hasn't been applied to youth sports because the market is volunteer-run and budget-constrained — commissioners won't pay much, but the pain is enormous.

## What to Build
A draft optimization engine that: (1) imports player data from registration (age, school, address, skill rating, sibling registrations), (2) accepts commissioner-defined constraints and priorities (skill balance weight, geographic clustering weight, sibling rules), (3) accepts coach-specific requests (I want my child, request player X), (4) generates optimized team assignments that maximize balance across all weighted constraints, (5) produces a draft report showing balance metrics per team (average skill, age distribution, geographic spread), and (6) allows the commissioner to manually override and see the impact on balance scores.

## Target Customer
Rec league commissioners managing draft night for 100-500+ players across 10-40 teams who currently spend 4-8 hours on manual team formation.

## Impact If Built
Reduces draft time from 4-8 hours to 30-60 minutes, produces measurably more balanced teams (reducing parent complaints by 50-70%), and eliminates the #1 reason rec league commissioners quit after a single season.
