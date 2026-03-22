# Tenant Retention Predictor

**Niche:** [[niches/property-management/multifamily-apartment/profile|Multifamily Apartment]]
**Industry:** [[industries/property-management|Property Management]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A predictive model that identifies tenants at risk of non-renewal 60-90 days before their lease expires — using payment patterns, maintenance request frequency, communication sentiment, lease term, rent-to-market-ratio, and demographic signals — enabling proactive retention outreach that converts 20-30% of predicted departures into renewals.
**Tags:** #gradient-boosting #time-series-forecasting #revenue-impact #data-integration #tacit-knowledge-ml #logistic-regression

## The Problem
Tenant turnover is the most expensive event in apartment management: each turnover costs $3,000-8,000 in lost rent (average 30-45 day vacancy), turn costs (painting, cleaning, carpet, repairs), marketing (listing fees, advertising), and leasing (agent commission, screening costs). A 300-unit community with 40% annual turnover loses $360K-960K per year in turnover costs. Most PMs don't engage tenants about renewal until 60-90 days before lease expiration — by which point the tenant who has been unhappy for months has already signed a lease elsewhere. Experienced property managers develop intuition about which tenants will leave: the tenant who submitted 5 maintenance requests in 2 months is frustrated; the tenant who stopped saying hello in the hallway is disengaging; the tenant whose rent-to-income ratio increased after a market rent adjustment is financially stressed. This intuition is pure tacit knowledge — experienced managers retain 10-15% more tenants than inexperienced managers through early intervention.

## Why Nobody Has Built This
The training data exists within PM platforms (Yardi, AppFolio, RealPage) — years of tenant records with lease outcomes (renewed/vacated), payment history, maintenance request history, and communication logs. But PM platforms treat this data as historical records, not as training data for predictive models. Building the model requires joining tenant demographic data, payment patterns (late payments, partial payments), maintenance frequency and sentiment, lease terms, rent-to-market ratio, and community-level factors (competing supply, local employment trends). The target variable (renewed/vacated) is noisy — some tenants leave for reasons unrelated to satisfaction (job relocation, life changes) that can't be predicted from property management data.

## What to Build
A tenant retention intelligence platform that: (1) ingests tenant data from Yardi/AppFolio via API — payment history, maintenance requests, communication logs, lease terms, rental rate vs. market rate; (2) enriches with external data — competing apartment listings and pricing from Apartments.com/Zillow, local employment trends from BLS, and neighborhood livability scores; (3) trains a gradient-boosted classifier predicting renewal probability per tenant, updated monthly as new data arrives; (4) flags high-risk tenants (predicted non-renewal probability >60%) 90-120 days before lease expiration with the top contributing factors ("5 maintenance requests in 2 months, rent 8% above market, late payment in month 10 — retention risk: High"); (5) recommends retention actions — "Offer $50/month concession (costs $600/year vs. $5,000 turnover cost)" or "Resolve the open maintenance issue within 48 hours and schedule a retention call."

## Target Customer
Multifamily PM companies managing 1,000+ units across multiple communities, with enough historical data to train meaningful retention models. Institutional apartment owners (REITs, pension funds) focused on reducing turnover-driven NOI erosion.

## Impact If Built
Converts 20-30% of predicted non-renewals into renewals through proactive intervention, saving $600-2,400 per retained tenant vs. turnover cost. For a 1,000-unit portfolio with 40% turnover, retaining even 10% of departing tenants saves $120K-480K annually. Provides property managers with data-driven retention guidance rather than relying on intuition that varies dramatically by manager experience.
