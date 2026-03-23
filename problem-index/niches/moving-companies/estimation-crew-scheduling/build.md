# Estimate-to-Actual Feedback Learning System

**Niche:** [[niches/moving-companies/estimation-crew-scheduling/profile|Move Estimation & Crew Scheduling Optimization]]
**Industry:** [[industries/moving-companies|Moving Companies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No estimation tool learns from the gap between what was quoted and what actually happened on move day, so estimators repeat the same systematic errors for years.
**Tags:** #gradient-boosting #regression #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
An estimator walks a home, estimates 1,200 cubic feet, quotes 3 movers and 6 hours, and moves on. The move actually takes 1,450 cubic feet, 4 movers, and 8.5 hours. This gap — the estimation error — is never systematically captured, analyzed, or fed back to the estimator. The same estimator will underestimate the same type of move (split-level house, heavy garage, narrow staircase) repeatedly because they never see structured data on where their estimates diverge from reality. Moving companies track revenue and costs at the job level but don't decompose estimate-vs-actual into the specific factors (item count, access difficulty, drive time, crew experience) that explain the variance.

## Why Nobody Has Built This
Building this requires structured data on both sides of the equation: the estimate inputs (item inventory, access conditions, customer profile) and the actual outcomes (hours worked, cubic feet loaded, items requiring special handling). Most movers capture estimates in one system (or on paper) and actuals in another (timesheets, truck manifests). Joining these datasets requires integration work that small movers can't do and software vendors haven't prioritized. The deeper problem is that the estimation model itself — what experienced estimators look for and how they weight factors — is tacit knowledge that hasn't been formalized into features a model can learn from.

## What to Build
A system that captures structured estimate inputs (room-by-room inventory, access conditions, special handling items, customer move history) alongside structured move-day actuals (actual hours per phase, actual cubic footage, items that required extra time, complications encountered). A gradient-boosted regression model trains on the estimate-actual pairs to identify systematic biases: which estimators consistently underestimate staircases, which property types always run long, which item categories are mispriced. The system surfaces corrections to estimators before they finalize quotes — "homes with 3+ flights historically take 25% longer than your estimates."

## Target Customer
Moving company owners and lead estimators at companies doing 100+ moves/month who know their estimates are inconsistent but have no data to diagnose why.

## Impact If Built
Reduces estimation error from the industry average of +/-15-20% to +/-5-8% within 6 months of deployment. On a company doing 200 moves/month at $2,000 average revenue, a 10% improvement in estimation accuracy recovers $30,000-50,000/year in margin lost to underpriced binding quotes.
