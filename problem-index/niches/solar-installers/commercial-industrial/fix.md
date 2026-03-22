# Demand Charge Interaction Modeling

**Niche:** [[niches/solar-installers/commercial-industrial/profile|Commercial & Industrial Solar]]
**Industry:** [[industries/solar-installers|Solar Installers]]
**Type:** Fix (Pain Point)
**One-liner:** C&I solar customers with high demand charges discover post-installation that solar alone doesn't reduce their demand charges — because peak demand occurs in late afternoon or evening when solar production is declining — leading to savings shortfalls of 20-40% versus the installer's proposal.
**Tags:** #time-series-forecasting #revenue-impact #data-integration #gradient-boosting

## The Problem
Demand charges account for 30-60% of a commercial electricity bill. A manufacturing facility paying $20/kW/month with a 500 kW peak demand pays $10,000/month in demand charges alone — $120K/year. If their peak demand occurs at 5 PM (end of production shift, HVAC at maximum, solar declining), a 300 kW solar system reduces their demand by only 50-100 kW during that peak window, saving $1,000-2,000/month in demand charges instead of the $6,000/month the simplified model projected. The customer expected $72K/year in demand charge savings and gets $12-24K. This savings shortfall is the #1 cause of C&I solar customer dissatisfaction and the primary driver of legal disputes between C&I customers and solar developers.

## Why It's Still Broken
Accurate demand charge modeling requires the customer's 15-minute interval load data, which most C&I customers don't have readily available. Getting interval data from the utility requires customer authorization and often a 2-4 week processing time — longer than most sales cycles allow. Without interval data, developers estimate demand charge savings from monthly utility bills, which show peak demand but not when it occurs. The workaround — building a synthetic load profile from the customer's industry type — introduces 15-30% error in demand timing. Most C&I solar proposals either omit demand charge analysis entirely (stating "energy savings only") or use simplified estimates that overstate demand charge reduction.

## What a Fix Looks Like
A demand charge analysis tool that: (1) pulls interval data from the utility's Green Button Connect platform (or the customer's smart meter portal) with customer authorization — reducing the data access time from 2-4 weeks to minutes; (2) analyzes the load profile to identify when peak demand occurs relative to solar production, quantifying the overlap (or lack thereof); (3) models solar-only demand charge reduction showing the realistic savings — and identifies whether battery storage would be needed to meaningfully reduce demand charges (by discharging during peak demand periods); (4) produces a clear visualization for the customer: "Your peak demand occurs at 5:30 PM when your solar system produces only 30% of rated capacity. Solar alone reduces your demand charges by 15%. Adding a 100 kWh battery increases demand charge reduction to 65%." This honest analysis prevents post-installation disappointment and positions battery storage as a value-add rather than a surprise upsell.

## Who Feels the Pain
C&I solar customers who were promised significant demand charge savings that didn't materialize. Solar developers facing breach-of-contract claims from customers whose actual savings fall far short of projections. Sales reps who lose credibility when their financial models prove inaccurate.

## Impact If Fixed
Eliminates demand charge savings overstatement that causes 30-40% of C&I solar disputes. Increases battery storage attach rate by clearly demonstrating the demand charge value proposition. Builds installer credibility through honest, data-driven financial analysis. Reduces legal exposure from inaccurate savings projections, worth $20K-100K per avoided dispute.
