# Maintenance Agreement Management

**Parent Industry:** [[industries/hvac-contractors|HVAC Contractors]]
**Category:** Highly Automatable

## Profile
**Market Size:** $5-8B (embedded in recurring revenue across residential and light commercial HVAC)
**Share of Parent Industry:** Embedded function — maintenance agreements generate 15-25% of revenue for well-run residential HVAC companies and represent the primary source of recurring, predictable revenue in an otherwise seasonal, demand-driven business.
**Digital Adoption:** Medium — ServiceTitan and FieldEdge both have membership agreement modules that track agreement customers, schedule seasonal visits, and automate renewal reminders. But these modules handle logistics (when to visit) without addressing economics (which agreements are profitable, which customers are at risk of non-renewal, when to upsell from basic to premium agreements).
**Target Buyer:** HVAC company owner or operations manager responsible for growing and retaining the maintenance agreement base
**Automation Potential:** Very High — agreement renewal, upsell timing, and profitability analysis are all pattern recognition tasks on structured data (agreement history, service history, equipment age, customer spend patterns) perfectly suited to ML models

## What Makes This a Distinct Niche
Maintenance agreements are the HVAC industry's recurring revenue anchor. A typical agreement costs the homeowner $150-350/year and includes 2 seasonal visits (AC tune-up in spring, heating tune-up in fall), priority scheduling, and a 10-15% discount on repairs. For the HVAC company, agreements provide: predictable revenue (billable before the work is performed), capacity utilization during shoulder seasons (spring and fall tune-ups fill the schedule between summer AC emergencies and winter heating emergencies), and a customer retention mechanism (agreement customers are 3-5x more likely to call the same company for repairs and 5-8x more likely to purchase system replacements from that company). The management challenge: most HVAC companies have 200-2,000 active agreements but treat them as a undifferentiated list. They don't know which agreements are profitable (a customer with a 25-year-old system who uses 4 repair visits per year at the 15% discount may cost more to service than the $299/year agreement generates), which customers are at risk of non-renewal (a customer who didn't use any agreement benefits last year is likely to cancel), or when to approach a customer about upgrading from a basic tune-up agreement to a premium agreement with parts coverage.

## Current Tools & Gaps
ServiceTitan's Membership module tracks agreement customers, schedules seasonal visits, sends renewal reminders, and reports agreement revenue. FieldEdge has similar functionality. Both handle the logistics of maintenance agreements but not the economics or growth optimization. Neither platform provides: per-agreement profitability analysis (agreement revenue minus cost-to-serve including tune-up labor, discounted repairs, and priority scheduling value), renewal risk prediction (which agreements will likely cancel at renewal based on usage patterns and customer behavior), or upsell timing optimization (when to approach agreement customers about upgrading or adding equipment).

## Problems
- [[niches/hvac-contractors/maintenance-agreement-management/build|🔨 Build: Maintenance Agreement Renewal Prediction and Upsell Engine]]
- [[niches/hvac-contractors/maintenance-agreement-management/buy|🛒 Buy: ServiceTitan Tracks Agreements but Can't Predict Renewal Risk or Optimize Upsell Timing]]
- [[niches/hvac-contractors/maintenance-agreement-management/fix|🔧 Fix: Agreement Profitability Visibility]]
