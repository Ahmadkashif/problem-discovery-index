# Practice Area Profitability Analyzer

**Niche:** [[niches/small-law-firms/general-practice-solo/profile|General Practice Solo Attorneys]]
**Industry:** [[industries/small-law-firms|Small Law Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Shows the solo attorney which practice areas actually make money per hour invested — including unbillable admin time — so they can stop taking unprofitable case types that feel busy but bleed revenue.
**Tags:** #gradient-boosting #time-series-forecasting #feature-engineering #evaluation-metrics #data-integration #revenue-impact #tacit-knowledge-ml

## The Problem
Solo general practitioners take whatever cases walk through the door because they fear turning away revenue. But not all practice areas are equally profitable when accounting for total time invested (billable hours + unbillable admin, court wait time, client hand-holding, research). A solo might bill $250/hour for a real estate closing that takes 3 hours of billable work and 1 hour of admin, netting $187.50/hour effective rate. That same attorney might bill $300/hour for a contested divorce that generates 20 billable hours but requires 15 hours of unbillable client communication, emotional management, and discovery coordination — netting $171/hour effective. Experienced solos develop tacit intuition about which case types are "worth it," but they cannot articulate the math because they don't track the unbillable components. This intuition takes 5-10 years to develop and cannot be transferred to a new solo.

## Why Nobody Has Built This
Practice management tools track billable time by matter and practice area, but they don't capture the unbillable overhead that varies dramatically by case type. A real estate closing has 30 minutes of unbillable admin; a custody battle has 10 hours of unbillable client crisis management. Without tracking the full time investment (billable + unbillable + opportunity cost of calendar blocking), profitability analysis is meaningless. Building this requires ambient time capture that can attribute administrative activities to specific matters and practice areas — a hard classification problem because a 20-minute phone call with an upset divorce client doesn't get logged as billable time and doesn't get attributed to any matter in current systems.

## What to Build
A profitability intelligence layer that combines three data streams: (1) billable time entries from the PMS, (2) ambient activity tracking (email threads tagged to matters, calendar events, phone call duration, document editing sessions), and (3) matter metadata (practice area, fee arrangement, client type). A gradient-boosted model trained on completed matters predicts total time investment and collection probability for new matters at intake, giving the solo a "profitability score" before accepting a case. The dashboard surfaces practice-area-level metrics: effective hourly rate (revenue collected / total hours invested), collection rate, average matter duration, and client acquisition cost per practice area. Time-series forecasting projects monthly revenue by practice area mix.

## Target Customer
Solo general practitioners handling 3+ practice areas, grossing $150K-500K annually, who suspect some case types are unprofitable but lack the data to make strategic decisions about practice area focus.

## Impact If Built
Enables solos to make data-driven decisions about which practice areas to grow, shrink, or eliminate. Early-adopter solos who rationalize their practice area mix report 20-30% effective hourly rate increases within 12 months by shifting volume from high-overhead case types to efficient ones. For the 360,000 solos losing 25-35% of revenue to invisible overhead, even a 10% improvement in practice area selection recovers $15K-50K per attorney annually.
