# Project Scoping & Budget Estimation for Video Production

**Industry:** [[video-production-smb|SMB Video Production]]
**Type:** High Impact
**One-liner:** Producers stop losing 15-30% of project margin to scope creep because every engagement starts with a data-driven budget that accounts for real revision patterns, shoot complexity, and client behavior.
**Tags:** #gradient-boosting #regression #tabular-ml #revenue-impact

## The Problem
SMB video production companies price projects using gut feel and rough comparables. A producer estimates a corporate brand video at $12K based on "a similar one we did last year," but doesn't account for the fact that this client's legal team will require 4 additional review rounds, the location has poor acoustics requiring ADR, or the requested 3 deliverable formats will triple the export/QC time. Scope creep is the single largest margin killer — shops routinely absorb 20-40 hours of unbilled post-production work per project because the original estimate didn't model the real cost drivers.

## Why It's Unsolved
Historical project data is scattered across invoices, email threads, project management tools, and editors' memories. There's no standardized way to tag a completed project with its actual cost drivers (number of revision rounds, shoot-day overruns, additional deliverables requested, client responsiveness delays). The few tools that exist for production budgeting (like StudioBinder or ProductionBeast) focus on film/TV-scale line items, not the SMB reality where a 3-person crew handles a $8K-$50K corporate video. The variance between projects is high — a "corporate video" could mean a 30-second social cut or a 10-minute training series — making simple averaging useless.

## What a Solution Looks Like
A system ingests historical project data (proposals, invoices, revision logs, client communication volume, deliverable specs) and builds a per-shop regression model that predicts total cost given project parameters. The producer enters project type, client industry, deliverable count, estimated shoot days, and client profile; the model returns a budget range with confidence intervals and flags the top 3 cost-risk factors (e.g., "clients in healthcare average 2.3 more revision rounds"). Over time, active projects feed back actual hours and costs, tightening predictions.

## Impact If Solved
A 10-person production shop doing $1.5M/year in revenue could recover $150K-$300K in currently-absorbed scope creep costs. Producers spend 60-70% less time on estimates and enter client conversations with defensible numbers instead of guesses.
