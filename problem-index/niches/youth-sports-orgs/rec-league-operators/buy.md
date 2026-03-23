# Referee Assignment Engine for Volunteer-Run Leagues

**Niche:** [[niches/youth-sports-orgs/rec-league-operators/profile|Rec League Operators]]
**Industry:** [[industries/youth-sports-orgs|Youth Sports Organizations]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** When I Work and Deputy handle shift scheduling for employees, but rec league referee assignment requires matching certified refs to games based on availability, certification level, conflict-of-interest rules, and geographic preference — constraints these platforms don't understand.
**Tags:** #automation #workflow-orchestration #quick-win

## The Problem
A rec league with 30 teams playing 10 games per Saturday needs 10-20 referees assigned to those games every week. The referee coordinator (a volunteer) must match referees to games based on: certification level (some games require higher-level refs), availability (referees submit weekly availability), conflict of interest (a ref can't officiate their own child's game), geographic preference (refs prefer fields closer to home), consecutive game limits (no ref should work 5 games straight), and equitable distribution (refs get paid per game and want fair allocation). This is a weekly constraint-satisfaction problem that the volunteer coordinator solves manually in 2-4 hours every Thursday night.

## What Already Exists
When I Work, Deputy, and Homebase handle employee shift scheduling with availability and preference matching. Arbiter (ArbiterSports) and Horizon WebRef handle referee assignment for high school and collegiate sports with full officiating management. But Arbiter costs $500+/year and is designed for school athletic departments, not volunteer rec leagues paying $20-40 per game. The affordable scheduling tools don't understand the specific constraints of referee assignment (conflict of interest, certification matching, consecutive-game limits).

## The Customization Gap
The needed adaptation is a referee-specific assignment engine for rec leagues: (1) referee profiles with certification level, child's team (for conflict detection), and weekly availability, (2) game schedule import with certification requirements per game, (3) auto-assignment that respects conflicts, certifications, availability, and equitable distribution, (4) referee notification with one-tap accept/decline, (5) auto-reassignment when a ref declines, and (6) season-end reporting showing per-ref game counts and payments. This is a vertical scheduling template with sport-specific constraint rules.

## Target Customer
Volunteer referee coordinators at rec leagues who spend 2-4 hours weekly on manual referee assignment and frequently can't fill all games.

## Impact If Solved
Reduces weekly referee assignment from 2-4 hours to 15-30 minutes, reduces unfilled games from 10-15% to under 3% through automated backup assignment, and eliminates the conflict-of-interest assignments that generate parent complaints and league credibility issues.
