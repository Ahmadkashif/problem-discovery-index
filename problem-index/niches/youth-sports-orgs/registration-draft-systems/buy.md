# Skill Evaluation Data Collection for Draft Prep

**Niche:** [[niches/youth-sports-orgs/registration-draft-systems/profile|Registration & Draft Systems]]
**Industry:** [[industries/youth-sports-orgs|Youth Sports Organizations]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Google Forms and paper rating sheets collect evaluator scores during player evaluations, but the data must be manually aggregated, normalized across evaluators, and formatted for the draft — a 5-8 hour process that determines team balance for the entire season.
**Tags:** #data-integration #automation #tabular-ml #quick-win

## The Problem
Before the draft, rec leagues hold player evaluations where coaches rate each player on 3-5 skills (throwing, hitting, fielding, speed for baseball; dribbling, passing, shooting for soccer). Evaluators score on 1-5 or 1-10 scales, but different evaluators have different baselines: Coach A scores generously (average: 7/10), Coach B scores strictly (average: 4/10). The raw scores must be normalized across evaluators to produce fair composite ratings for the draft. Currently, the commissioner exports scores from Google Forms or collects paper sheets, enters data into a spreadsheet, manually normalizes evaluator differences, calculates composite ratings, and ranks players for draft preparation. This 5-8 hour process is error-prone, and any scoring bias that isn't caught results in unbalanced teams.

## What Already Exists
Google Forms collects structured data. SportsEngine includes basic evaluation features. LeagueApps offers team formation tools. Purpose-built evaluation apps (iScore, GameChanger) focus on game statistics, not pre-draft skill evaluations. No tool handles the complete evaluation-to-draft pipeline: structured skill scoring by multiple evaluators, automatic cross-evaluator normalization, composite rating calculation with configurable skill weights, and export in draft-ready format showing ranked players by division.

## The Customization Gap
The needed adaptation is an evaluation-to-draft data pipeline: (1) mobile-friendly scoring interface for evaluators at the field (score Player #47 on throwing: 1-5), (2) real-time data aggregation across multiple evaluators scoring simultaneously, (3) automatic score normalization by evaluator (adjusting for generous/strict tendencies using z-score normalization), (4) configurable composite rating calculation (skill weights vary by sport and age group), (5) draft board export showing ranked players with composite scores, individual skill breakdowns, and evaluator notes, and (6) prior-season performance import for returning players.

## Target Customer
League commissioners managing player evaluations for 100-500+ players assessed by 5-15 evaluators who currently aggregate scores manually in spreadsheets.

## Impact If Solved
Reduces evaluation data processing from 5-8 hours to 30 minutes, eliminates evaluator bias that causes 15-20% of players to be misranked, and produces more balanced teams — directly reducing the parent complaints that are the #1 source of commissioner burnout.
