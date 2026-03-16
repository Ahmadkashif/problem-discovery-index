# Multi-Site Route and Schedule Optimization

**Industry:** [[cleaning-companies|Cleaning Companies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Routing tools can optimize delivery routes, but they can't handle the cleaning-specific constraint of variable-duration stops across different cleaning schedules at sites that need different team sizes.
**Tags:** #reinforcement-learning #regression #tabular-ml #workflow-orchestration

## The Problem
A commercial cleaning company serves 30-200 client sites with varying schedules: some daily, some 3x/week, some weekly, some monthly for deep cleans. Each site requires a specific team size (1-4 cleaners) for a specific duration (1-6 hours). Routing these teams across sites while minimizing drive time, respecting cleaning windows (many offices must be cleaned between 6pm-6am), and balancing workloads across crews is a complex optimization problem. Most companies solve it by hand, resulting in 15-25% excess drive time and uneven crew workloads.

## What Already Exists
Google Maps and Routific optimize delivery routes for single-stop, short-duration visits. Jobber and Housecall Pro provide basic scheduling but without true route optimization. These tools don't handle variable-duration stops, multi-day schedule patterns, or team-based assignment.

## The Customisation Gap
Cleaning-specific route optimization needs: (1) variable stop durations based on site contract, (2) multi-day schedule pattern optimization (which sites on which days to minimize weekly drive time), (3) team-based routing (crews of 2-4 traveling together), (4) cleaning window constraints (time-of-day restrictions per site), (5) dynamic rerouting when a cleaner calls out or a client requests an extra service.

## Impact If Solved
Reduces drive time 15-25% across the operation, saving 2-4 hours per crew per week. Enables companies to service 10-15% more sites with the same crew count. Improves schedule reliability, reducing the late arrivals that frustrate clients.
