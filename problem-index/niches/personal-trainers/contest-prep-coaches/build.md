# Contest Prep Data Dashboard with Adjustment Intelligence

**Niche:** [[niches/personal-trainers/contest-prep-coaches/profile|Contest Prep Coaches]]
**Industry:** [[industries/personal-trainers|Personal Trainers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No platform aggregates daily prep data (weight, macros, training volume, biofeedback, progress photos) into trend analysis that helps a contest prep coach decide whether to cut calories, add cardio, or hold steady — the most consequential decision made 12-20 times per prep cycle.
**Tags:** #gradient-boosting #time-series-forecasting #tabular-ml #tacit-knowledge-ml #ai-platform

## The Problem
Experienced contest prep coaches develop sophisticated pattern recognition for interpreting prep data: they know that a 2-pound overnight weight spike after a refeed day is water retention (hold steady), while the same spike after a normal day suggests dietary non-compliance (investigate). They know that declining biofeedback scores (mood, energy, libido) combined with stalled weight loss means metabolic adaptation (add a refeed), not insufficient deficit (don't cut calories further). This tacit knowledge about data interpretation drives the weekly adjustment decisions that make the difference between a competitor coming in on time and coming in flat, watery, or depleted. But this expertise lives entirely in the coach's head and is applied through manual spreadsheet analysis.

## Why Nobody Has Built This
Contest prep coaching is a small, niche market ($600M) with coaches who are resistant to algorithmic recommendations because the stakes are visible (the client literally stands on stage in a bikini). The data patterns are complex: weight responds to macros, water, sodium, sleep, menstrual cycle, stress, and training volume simultaneously — isolating which variable is driving the change requires multivariate analysis that coaches do intuitively but struggle to articulate. Building intelligent adjustment recommendations requires training on thousands of prep cycles with outcome labels (did the competitor come in well?) — data that exists but isn't digitized or aggregated.

## What to Build
A prep management dashboard that: (1) collects daily client data (weight, macros consumed, water intake, training log, biofeedback ratings, progress photos), (2) visualizes trends with rolling averages and rate-of-change analysis, (3) identifies data patterns that suggest specific interventions (metabolic adaptation, water retention, compliance issues), (4) presents adjustment recommendations (increase/decrease macros by X, add/remove Y minutes of cardio, schedule a refeed) based on similar patterns from historical preps, and (5) documents every adjustment with the data that drove it for future prep reference.

## Target Customer
Contest prep coaches managing 10-40 active competitors who currently analyze prep data in Google Sheets and make adjustment decisions from memory.

## Impact If Built
Reduces weekly per-client analysis time from 30-45 minutes to 10-15 minutes, enables coaches to scale from 20 clients to 40+ without quality degradation, and improves competitive outcomes by 15-25% through more consistent data-driven adjustments — the difference between a coach's top 5 clients getting great attention and the rest getting formulaic treatment.
