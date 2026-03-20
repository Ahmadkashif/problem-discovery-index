# Guard Scheduling and Post Coverage Optimization

**Industry:** [[security-guard-firms|Security Guard Firms]]
**Type:** High Impact
**One-liner:** Every shift is filled with the right guard before the client notices a gap — because the system predicted the no-show, arranged the backup, and confirmed coverage before the shift started.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #optimization-fundamentals #bias-variance-tradeoff #workflow-orchestration #revenue-impact

## The Problem
A security guard firm with 200 guards and 50 client sites must fill 300-500 shifts per week. Each shift has requirements: armed/unarmed, specific certifications, client preferences (some clients ban specific guards), geographic proximity, and overtime limits. No-show rates run 10-20% — every day, 5-15 guards don't show up, triggering a cascade of emergency calls to find replacements before the client discovers an uncovered post. An uncovered post is a contract-threatening event: clients pay for presence, and gaps expose them to liability. Operations managers spend 3-5 hours daily on schedule adjustments, phone calls, and emergency dispatching.

## Why It's Unsolved
The problem combines predictive (who will no-show?) with prescriptive (who should we call first for coverage?) with constraint satisfaction (who is qualified, available, and not in overtime?). Current scheduling tools fill slots but don't predict gaps or pre-position backups. The no-show prediction challenge is particularly hard because the same guard might be 98% reliable for daytime shifts but 60% reliable for overnight shifts — the context matters as much as the individual.

## What a Solution Looks Like
A scheduling system that optimizes initial shift assignment for coverage reliability (placing more reliable guards on harder-to-fill shifts), predicts no-show risk for each filled shift, pre-contacts backup guards for high-risk shifts, and auto-dispatches replacements when gaps occur. The system learns guard reliability patterns by shift type, site, day of week, and weather. Output: every shift filled with a primary guard and a ranked backup list, with automated confirmation workflows that detect gaps 2-4 hours before shift start rather than at shift start.

## Impact If Solved
Reduces uncovered post incidents from 10-15% to under 3% of shifts. Cuts operations manager scheduling time from 3-5 hours to under 1 hour daily. Decreases overtime costs by 20-30% through better initial assignment. Improves client retention by eliminating the #1 source of complaints (coverage gaps).
