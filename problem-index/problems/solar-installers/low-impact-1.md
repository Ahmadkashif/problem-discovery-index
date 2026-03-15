# Lead Qualification Scoring for Long Solar Sales Cycles

**Industry:** [[solar-installers|Solar Installers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic CRM lead scoring tools exist but don't model the solar-specific signals that predict whether a lead will close — homeownership, roof age, south-facing roof area, current electricity bill, shade conditions, local utility rate trajectory, and the customer's decision timeline for a $20,000 purchase.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #revenue-impact

## The Problem

Solar leads from digital marketing, referrals, and door-to-door canvasing vary enormously in close probability. A homeowner with a south-facing roof, high electricity bills, and good credit in a state with strong net metering policy is 5-10× more likely to sign than a homeowner with a heavily shaded roof, low electricity use, and a landlord situation. Sales reps who don't know which leads are qualified waste significant time on low-probability leads while high-probability leads sit uncontacted.

Generic lead scoring tools (Salesforce Einstein, HubSpot score) evaluate engagement signals (email opens, website visits) but not the property- and utility-specific signals that determine solar economics for a specific customer.

## What Already Exists

Zillow and county assessor data provide property characteristics. Utility rate databases are available. SunroofGuru and Google Project Sunroof provide solar potential estimates by address. No tool combines property data, utility economics, and engagement signals into a single solar-specific lead score.

## The Customisation Gap

A solar lead scoring tool needs: (1) property data (roof area, south-facing fraction, tree cover/shade estimate from Google Maps or aerial imagery); (2) utility economics (current electricity rate, net metering policy in the utility territory); (3) financial qualification signals (homeownership verified, estimated income tier from zip code); (4) behavioral signals (number of quotes requested, response time to outreach). The solar-specific weighting of these features — roof orientation matters more than email engagement for solar conversion — requires domain expertise to specify correctly.

## Impact If Solved

Enables sales team to prioritize the top 20% of leads who represent 60-70% of closed deals. Reduces time wasted on structurally unqualified leads. A 10% improvement in sales team allocation efficiency on a 40-person sales team adds $1-2M in annual revenue.
