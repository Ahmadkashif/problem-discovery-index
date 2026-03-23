# Patient Retention Prediction and Re-Engagement Engine

**Niche:** [[niches/chiropractic-practices/cash-pay-wellness/profile|Cash-Pay Wellness & Maintenance]]
**Industry:** [[industries/chiropractic-practices|Chiropractic Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product predicts which cash-pay chiropractic patients are about to stop coming and triggers personalized re-engagement at the optimal moment — before the patient has mentally decided to quit.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #revenue-impact

## The Problem
A cash-pay wellness practice with 300 active patients has an average monthly churn rate of 5-8%. The DC notices when a regular patient hasn't come in for 3 weeks and calls them — but by then, many have already decided to stop. The patterns that predict dropout are visible in the data weeks before the last visit: decreasing visit frequency, shorter appointment durations, fewer add-on services, cancellation/reschedule rate increasing. An experienced office manager "senses" when a patient is disengaging, but this intuition doesn't scale and isn't available when the office manager is new.

## Why Nobody Has Built This
Chiropractic practice management systems capture appointment data but don't analyze behavioral patterns. Generic customer retention tools (for SaaS, gyms, etc.) don't account for clinical factors — a patient who reduces visits because they're feeling better is different from one who's losing interest. Building a chiropractic-specific retention model requires training on data from thousands of patient journeys across many practices, which no single practice can provide.

## What to Build
A retention analytics platform that connects to the practice management system, tracks patient engagement signals (visit frequency, cancellations, membership status, payment patterns), and uses a predictive model to score each patient's dropout risk weekly. When risk crosses a threshold, triggers a personalized re-engagement workflow — text message from the DC, special offer, or staff phone call — tailored to the patient's engagement pattern and reason-for-visit history. Dashboard shows retention metrics, at-risk patients, and the financial impact of churn.

## Target Customer
Cash-pay chiropractic practices with 200+ active patients and $30K+ monthly recurring revenue from memberships and visit packages.

## Impact If Built
Reduces monthly churn rate from 6% to 3-4% by catching at-risk patients before dropout. For a practice with 300 patients at $150/month average revenue, reducing churn by 2 percentage points saves 6 patients per month — $10,800 per month or $130K per year in retained revenue.
