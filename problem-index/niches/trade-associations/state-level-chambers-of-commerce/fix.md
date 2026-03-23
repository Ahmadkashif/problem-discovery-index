# Dues Renewal Churn

**Niche:** [[niches/trade-associations/state-level-chambers-of-commerce/profile|State-Level Chambers of Commerce]]
**Industry:** [[industries/trade-associations|Trade Associations]]
**Type:** Fix (Pain Point)
**One-liner:** Chambers lose 15-25% of members at renewal annually, but the membership director doesn't know a member is at risk until the renewal invoice goes unpaid — by which time re-engagement is nearly impossible.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #revenue-impact #automation

## The Problem
Chamber membership renewal typically happens annually. The current process: send an invoice 60 days before renewal, follow up at 30 days, call at 15 days, and mark as lapsed if unpaid by the date. This reactive approach treats all members the same — the engaged member who attends every event and the member who joined 11 months ago and never participated both get the same invoice. The membership director invests the same follow-up effort on a member who was always going to renew (the board chair's company) as on a member who silently disengaged 6 months ago. By the time non-renewal becomes apparent, the member has already made their decision.

## Why It's Still Broken
AMS platforms track transactions (dues paid, events attended) but don't model engagement health. A member who paid dues and attended 2 events appears "active" in the database, even though they stopped attending 8 months ago and never opened the last 5 newsletters. The data to predict churn exists — event attendance trend, email open rate, committee participation, referral activity — but no AMS synthesizes these signals into a churn risk score. Membership directors rely on intuition, which doesn't scale beyond 200 members.

## What a Fix Looks Like
A churn prediction model that scores every member's renewal likelihood based on engagement signals: event attendance trend (declining = risk), email open rate (dropping = risk), committee/volunteer participation (none = risk), referral/networking activity (low = risk), and years of membership (year 1 and year 3 are highest churn years). Members with low renewal probability are flagged 6 months before renewal for personalized re-engagement — a phone call from the CEO, an invitation to a high-value event, or a meeting to discuss what the chamber could do differently.

## Who Feels the Pain
Chamber CEOs and membership directors who set annual revenue budgets based on projected retention, then scramble in Q4 when renewal rates come in 5-10% below projections, forcing program cuts and sponsorship scrambles.

## Impact If Fixed
Increases renewal rate from 80% to 90% by enabling early intervention, recovers $100K-$400K in annual dues per mid-size chamber, and replaces the stressful "invoice and chase" renewal cycle with a proactive engagement strategy.
