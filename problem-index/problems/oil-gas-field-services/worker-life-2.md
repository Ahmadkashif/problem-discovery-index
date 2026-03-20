# Crew Scheduling Across Scattered Wellsites

**Industry:** [[oil-gas-field-services|Oil & Gas Field Services]]
**Type:** Worker Life Changing
**One-liner:** Field techs get predictable, fair schedules instead of constant last-minute route changes that destroy their personal time and add hundreds of unnecessary driving miles per week.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #evaluation-metrics #cross-validation #optimization-fundamentals #bias-variance-tradeoff #worker-facing

## The Problem
A typical oilfield service company dispatches crews to wellsites scattered across a basin that can span 100+ miles in any direction. Scheduling is done by a dispatcher using a whiteboard or spreadsheet, assigning jobs based on who is available and roughly where they are. The result is chronic inefficiency: a tech drives 45 minutes past a wellsite that needs service to reach their assigned site, while another tech drives 45 minutes in the opposite direction to cover the skipped one. Schedules change constantly as emergency calls come in, and techs often learn about route changes mid-drive via radio or text. A field tech may drive 200-400 miles per day, with 30-40% of that mileage being avoidable. The unpredictability means techs cannot reliably tell their families when they will be home, and the excessive windshield time is physically exhausting and a leading cause of vehicle accidents.

## Why It Matters to the Worker
Field techs on 14/14 or 7/7 rotation schedules already sacrifice significant family time. When the days they are on-shift are further degraded by 2-3 extra hours of unnecessary driving and constant re-routing, it erodes morale and accelerates burnout. Younger workers especially cite unpredictable schedules as the primary reason they leave oilfield service for less lucrative but more predictable jobs. Excessive driving also increases fatigue-related accident risk — vehicle incidents are the #1 cause of oilfield fatalities.

## What a Solution Looks Like
An optimization engine that ingests the day's job queue (scheduled maintenance, emergency calls, inspection deadlines), tech locations and skill certifications, wellsite access constraints (daylight-only access, seasonal road closures), and estimated job durations to produce optimized daily routes. As emergency jobs come in, it dynamically re-optimizes and pushes updated routes to techs' mobile devices with clear ETAs. Techs see their full day's route by 5 AM, and changes are minimized to genuine emergencies. The system also balances workload across techs over the rotation cycle so that no one tech consistently gets the longest drives or worst sites.

## Impact If Solved
Reduces daily driving miles per tech by 25-35%, reclaiming 1-2 hours per day. Cuts fuel costs by $500-$1,000/month per truck. Reduces fatigue-related driving incidents. Gives field techs schedule predictability that materially improves their quality of life during on-rotation days.
