# Subscriber Churn and Credit Allocation Tracking

**Niche:** [[niches/solar-installers/community-solar-programs/profile|Community Solar Programs]]
**Industry:** [[industries/solar-installers|Solar Installers]]
**Type:** Fix (Pain Point)
**One-liner:** Community solar projects lose 5-15% of revenue annually to subscriber churn because cancelled subscriptions take 30-90 days to reallocate — during which the developer generates electricity but receives no revenue for the unsubscribed capacity — and credit allocation errors compound the problem by over- or under-crediting subscribers.
**Tags:** #gradient-boosting #revenue-impact #automation #data-integration #logistic-regression

## The Problem
Subscriber churn is the community solar developer's most expensive operational problem. When a subscriber moves, cancels their utility account, or simply stops paying, their subscription share becomes unsubscribed capacity — the solar array continues producing energy for that share, but no subscriber receives the credits and the developer receives no subscription revenue. State regulations typically require projects to maintain 90-100% subscription levels; unsubscribed capacity below the threshold can trigger regulatory penalties. The reallocation process is manual: the developer identifies the cancellation (often weeks after the subscriber stopped paying), removes them from the utility's credit allocation roster, processes a waitlisted subscriber's enrollment, and coordinates with the utility to redirect credits — a process that takes 30-90 days. At $100-200/month per subscription, each month of unsubscribed capacity costs the developer $100-200 per vacant share. A 300-subscriber project with 10% annual churn loses $36K-72K per year in reallocation delays alone.

## Why It's Still Broken
Churn detection is delayed because developers learn about cancellations from utility credit allocation reports (which arrive monthly) rather than from real-time subscriber monitoring. By the time the developer sees that a subscriber's credits were returned as unallocated, the subscriber may have cancelled 4-6 weeks prior. Waitlist processing is manual — the developer contacts waitlisted prospects sequentially, processes enrollment paperwork, and coordinates utility account setup. The credit allocation reconciliation is a monthly Excel exercise comparing the developer's internal allocation calculations against the utility's credit report, with discrepancies requiring investigation.

## What a Fix Looks Like
A churn prediction and rapid reallocation system that: (1) predicts churn risk using subscriber signals — payment delays, utility account changes, lease expiration dates, property sale indicators (public records), and engagement metrics (do they open the monthly credit statement email?) — flagging at-risk subscribers 30-60 days before cancellation; (2) pre-qualifies waitlisted subscribers so that when a cancellation occurs, the replacement subscriber is already enrolled, credit-checked, and ready for utility activation within 3-5 business days rather than 30-90 days; (3) automates credit allocation reconciliation by parsing utility credit reports (PDF or data file), comparing against internal allocation calculations, and flagging discrepancies with root cause analysis (subscriber account change, utility processing error, or allocation calculation error).

## Who Feels the Pain
Community solar developers losing $30K-100K annually per project to churn-related unsubscribed capacity. Operations staff spending 10-20 hours per month on manual credit allocation reconciliation. Waitlisted subscribers who wait months for a subscription that should be available within days of a cancellation.

## Impact If Fixed
Reduces unsubscribed capacity duration from 30-90 days to 3-7 days, recovering $25K-60K per project per year in revenue. Predicts 60-70% of churn events 30+ days in advance, enabling proactive outreach and retention. Automates credit allocation reconciliation, saving 10-20 hours per month of analyst time per project.
