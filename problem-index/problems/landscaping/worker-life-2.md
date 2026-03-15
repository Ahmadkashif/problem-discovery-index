# Customer Renewal and Upsell Timing Based on Service History

**Industry:** [[landscaping|Landscaping]]
**Type:** Worker Life Changing
**One-liner:** Account managers at landscaping firms who manually review their customer list each spring to identify renewal candidates and upsell opportunities — a review that's usually done by memory rather than data — get an automatically-generated priority list showing which customers are renewal risks and which are ready for a service upgrade.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #revenue-impact #worker-facing

## The Problem

Landscaping customer retention requires proactive outreach before the season begins — customers who aren't contacted in late winter often don't renew; they wait until grass-cutting season begins and call whoever puts a flyer on their door. Account managers who should be making proactive retention calls instead spend their time on inbound requests and reactive scheduling, and by the time they get around to renewal outreach it's April and the lost customers have already signed with competitors.

The data needed to prioritize outreach exists in every field service management platform: last service date, service frequency, complaint history, total annual revenue per customer, years of tenure. But no tool surfaces this data as a ranked priority list with recommended actions — account managers query it manually or not at all.

## Why It Matters to the Worker

Account managers are measured on customer retention and upsell revenue. Their biggest constraint is time: they have 200+ accounts and can't actively manage all of them. A priority list that tells them "these 20 customers are at risk of not renewing; contact them this week" versus "these 15 customers with 3+ years of service who've never had irrigation service are upgrade candidates" would significantly change what they work on each week.

## What a Solution Looks Like

A weekly auto-generated priority list in Jobber or LMN showing: (1) renewal risk segment — customers with service in the prior year who haven't been contacted about the upcoming season and whose last service was > 60 days ago; (2) upsell opportunity segment — multi-year customers whose service profile is missing a standard add-on (lawn care only → add fertilization, fertilization only → add irrigation, irrigation only → add landscape maintenance); (3) account health flag — customers who had complaints or service issues in the prior season who need a proactive check-in. The account manager works through the list in order of priority score rather than whatever is top of mind.

## Impact If Solved

Proactive renewal outreach converts at 60-80% vs. 20-30% for customers contacted only after they cancel. For a firm with 300 recurring customers at $800 average annual contract value, recovering 10% of at-risk customers through proactive outreach is $24,000 in retained revenue per year.
