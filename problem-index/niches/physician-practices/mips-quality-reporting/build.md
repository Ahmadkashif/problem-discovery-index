# An In-Year MIPS Score Forecast by Clinician

**Niche:** [[niches/physician-practices/mips-quality-reporting/profile|MIPS & Quality Measure Reporting]]
**Industry:** [[industries/physician-practices|Physician Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Practices learn their MIPS score after the year closes, when nothing can change it; a forecast by clinician and measure in June would show where effort still moves the score above 75.
**Tags:** #bayesian-inference #monte-carlo-methods #gradient-boosting #evaluation-metrics #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to land each clinician's MIPS score above the 75-point threshold from data the practice already holds, and whoever clears the threshold for the most clinicians without adding manual chart abstraction takes the account.

## The Problem
MIPS scores combine quality, cost, improvement activities and Promoting Interoperability, and quality measures are scored against benchmark deciles published by CMS. A practice's dashboards show measure rates but not where the clinician will land, or which measure swap would gain the most points.

## Why Nobody Has Built This
Scoring rules change every year, and cost measures are computed by CMS from claims the practice cannot see until feedback arrives. Registries submit after the year ends. Few practices have analysts to model it.

## What to Build
A forecasting model that projects each measure's year-end rate from year-to-date data and seasonality, maps it to benchmark deciles, and simulates the composite score with uncertainty, including estimated cost-measure performance from prior feedback. It recommends the measure set and the gap closures that move the most clinicians above 75 using data already in the chart, so no new abstraction is needed.

## Target Customer
Quality managers at specialty groups of 10–300 clinicians reporting traditional MIPS or MVPs.

## Impact If Built
Moving a clinician from just under to just over the threshold turns a negative adjustment into a neutral or positive one. For a specialist billing ~$400,000 a year to Medicare Part B (estimate), a swing of a few percent is ~$10,000–$30,000.
