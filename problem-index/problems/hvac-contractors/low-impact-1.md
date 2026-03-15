# Maintenance Agreement Renewal Risk Scoring and Outreach

**Industry:** [[hvac-contractors|HVAC Contractors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic CRM churn prediction tools exist but don't understand HVAC maintenance agreement dynamics — the service visit intervals, equipment age triggers, and customer behavior patterns that predict whether a maintenance customer will renew, cancel, or upgrade to a replacement equipment plan.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #revenue-impact #automation

## The Problem

Maintenance agreements (also called service plans or comfort clubs) are the recurring revenue foundation of well-run HVAC firms — customers pay $150-$300 annually for scheduled preventive maintenance visits and priority service response. Retention is the key metric: acquiring a new maintenance customer costs 5-8× more than renewing an existing one. Firms lose customers to cancellation without knowing they were at risk until the renewal date is missed.

HVAC-specific cancellation signals exist: customers who cancel appointment times twice or more are 3× more likely to cancel their agreement; customers whose equipment reaches 10+ years old and haven't been quoted a replacement are near-end-of-relationship; customers who haven't used their included repair discount in 3+ years show low engagement. These patterns exist in ServiceTitan data but aren't surfaced as actionable signals.

## What Already Exists

Generic CRM churn prediction tools (Salesforce Einstein, HubSpot predictive scoring) score accounts on general engagement signals. They don't know that a maintenance visit reschedule is a stronger churn signal than a missed email open, or that equipment age is the primary replacement upsell trigger in HVAC.

## The Customisation Gap

An HVAC maintenance retention model needs: (1) HVAC-specific features — equipment age, maintenance visit completion rate, appointment reschedule/cancel history, time since last repair call, discount utilization; (2) ServiceTitan integration to pull these features automatically; (3) a churn probability score per customer at 90-day renewal horizon; (4) automated outreach templates differentiated by churn reason (engagement lapse, equipment age trigger, price sensitivity signal). The feature set and interpretation are HVAC-specific and require domain understanding to define correctly.

## Impact If Solved

A 5% improvement in maintenance agreement retention on a 2,000-customer book of business recovers $15,000–$30,000 in annual recurring revenue. Proactive outreach to at-risk customers before their renewal date is the highest-ROI customer retention activity in HVAC service.
