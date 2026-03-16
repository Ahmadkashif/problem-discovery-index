# Route Optimization for Recurring Service

**Industry:** [[pest-control|Pest Control]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic routing tools optimize one day at a time, but pest control needs to optimize recurring service patterns across monthly and quarterly schedules with variable stop durations and time-window constraints.
**Tags:** #reinforcement-learning #regression #tabular-ml #workflow-orchestration

## The Problem
A pest control technician serves 8-15 stops per day across a territory. Each customer has a service frequency (monthly, bi-monthly, quarterly), a preferred time window, and a variable service duration (10 minutes for a basic exterior spray to 90 minutes for a full interior treatment). Scheduling these recurring visits across 300-1,000 customers in a territory while minimizing drive time, respecting time windows, and maintaining consistent scheduling (customers expect the same day/time each month) is an optimization problem that operations managers solve manually — typically freezing routes that become progressively less efficient as customers churn and new ones are added.

## What Already Exists
PestPac and FieldRoutes offer basic route optimization that resequences stops within a day but doesn't optimize the assignment of recurring customers to days or territories. Google Maps and Circuit optimize single-day routes. None handle the multi-day, recurring-schedule, variable-duration complexity of pest control routing.

## The Customisation Gap
Pest-control-specific routing needs: (1) multi-day schedule optimization (which customers on which days across monthly/quarterly cycles), (2) territory rebalancing as customer counts change, (3) variable stop duration based on service type and property characteristics, (4) time-window constraints from customer preferences, (5) drive-time seasonal adjustment (winter vs. summer activity levels change service density), and (6) new customer insertion without disrupting existing schedules.

## Impact If Solved
Reduces daily drive time 20-30%, adding 2-3 additional service stops per technician per day. Increases revenue per route by 15-20% through density optimization. Reduces customer complaints about inconsistent scheduling.
