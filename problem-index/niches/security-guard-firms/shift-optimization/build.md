# Constraint-Aware Guard Schedule Optimizer

**Niche:** [[niches/security-guard-firms/shift-optimization/profile|Guard Scheduling & Shift Optimization]]
**Industry:** [[industries/security-guard-firms|Security Guard Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No scheduling tool optimizes guard assignments considering qualifications, overtime thresholds, rest requirements, site preferences, and equitable distribution simultaneously.
**Tags:** #reinforcement-learning #automation #workflow-orchestration #revenue-impact

## The Problem
A security company with 80 guards covering 25 sites across three shifts must solve a multi-constraint optimization problem every week: each site requires specific qualifications (armed, CPR-certified, bilingual, site-trained), each guard has maximum hours before overtime kicks in, state laws mandate minimum rest periods between shifts (typically 8 hours), some clients demand specific guards (or refuse specific guards), and equitable shift distribution reduces turnover. Operations managers "solve" this by hand in spreadsheets, spending 15-25 hours per week building schedules that are feasible but never optimal. The result: 8-12% of labor hours are overtime that could have been avoided with better distribution.

## Why Nobody Has Built This
The constraint space is enormous — qualifications, overtime, rest periods, preferences, equity, site requirements, availability, and coverage minimums create a combinatorial problem that grows exponentially with guard and site count. Generic scheduling tools handle time-off requests and availability but don't model security-specific constraints. Building an optimizer requires both deep understanding of security labor rules and advanced constraint satisfaction or operations research techniques.

## What to Build
A schedule optimization engine that takes inputs (guard roster with qualifications, site requirements, labor rules, preferences, availability) and produces a weekly schedule that minimizes total labor cost (prioritizing straight-time over overtime), satisfies all hard constraints (qualifications, rest periods, coverage), and optimizes soft constraints (guard preferences, equitable distribution, client preferences). The engine should re-optimize in real time when constraints change (callout, new site, guard termination).

## Target Customer
Security companies with 50+ guards and 15+ sites spending 15-25 hours per week on manual scheduling and paying 10-15% of labor cost in avoidable overtime.

## Impact If Built
Reducing overtime from 12% to 5% of total hours on a $5M annual payroll saves $350,000/year. Reducing scheduling manager time from 20 hours/week to 3 hours/week recovers another $40,000/year in management capacity.
