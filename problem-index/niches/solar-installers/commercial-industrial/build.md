# Commercial Solar ROI Calculator with Demand Charge Analysis

**Niche:** [[niches/solar-installers/commercial-industrial/profile|Commercial & Industrial Solar]]
**Industry:** [[industries/solar-installers|Solar Installers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A C&I solar financial modeling platform that takes the customer's utility bill, interval meter data, and system design as inputs and produces an hour-by-hour savings analysis accounting for demand charges, TOU rates, demand ratchets, and tax benefits — replacing the 4-8 hour custom Excel model that C&I solar developers currently build for every project.
**Tags:** #time-series-forecasting #gradient-boosting #revenue-impact #data-integration #automation

## The Problem
Commercial electricity rates are 5-10x more complex than residential rates. A manufacturing facility might pay: energy charges that vary by TOU period (on-peak $0.12/kWh, off-peak $0.06/kWh), demand charges based on peak 15-minute power draw ($15-25/kW/month), a demand ratchet that sets minimum billing demand at 80% of the highest peak from the prior 12 months, power factor penalties if reactive power exceeds thresholds, and facilities charges based on meter capacity. Solar interacts differently with each component — it directly reduces energy charges during production hours but only reduces demand charges if it happens to produce during the facility's peak demand window (which is often in the evening when solar production is declining). A C&I solar proposal that ignores demand charge interaction will overstate savings by 20-40% for demand-charge-heavy customers. Building the correct financial model requires 15-minute interval analysis across 8,760 hours, matched against the specific utility's rate schedule.

## Why Nobody Has Built This
Three barriers. First, rate complexity: there are 3,000+ C&I rate schedules in the US, each with unique demand charge calculations, TOU period definitions, and ratchet provisions. Building a comprehensive rate database is a massive ongoing data maintenance effort. Second, interval data access: accurate demand charge modeling requires the customer's actual 15-minute interval load data (or a synthetic load profile calibrated to their consumption pattern), which is obtained from the utility or smart meter — not a standardized data format. Third, tax benefit modeling: C&I solar economics depend heavily on the Investment Tax Credit (ITC), Modified Accelerated Cost Recovery System (MACRS) depreciation, and potentially tax equity structures — financial calculations that change with annual tax law updates.

## What to Build
A C&I solar financial platform with three modules. First, rate analysis: import the customer's utility bill (OCR scan or manual entry), identify the rate schedule, and auto-populate the full rate structure from a maintained database of C&I tariffs for the top 200 utilities. Second, load-solar matching: import 15-minute interval data (from the utility's Green Button portal) or generate a synthetic load profile from the customer's industry type and monthly consumption, then overlay the proposed solar production curve (from Aurora/Helioscope) to calculate hour-by-hour energy savings, demand charge impact, and ratchet effects. Third, financial analysis: model the complete project economics including ITC, MACRS depreciation, loan/lease/PPA structures, and maintenance costs over a 25-year horizon, producing an IRR, NPV, payback period, and LCOE that the C&I buyer and their CFO can evaluate. Output is an investor-grade financial memo, not a consumer-facing proposal.

## Target Customer
C&I solar developers and energy consultants doing 10-50 commercial solar proposals per year, currently spending 4-8 hours per project on custom financial modeling. Solar companies expanding from residential into C&I who lack the financial modeling expertise.

## Impact If Built
Reduces C&I proposal financial modeling from 4-8 hours to 30-60 minutes through automated rate analysis and interval matching. Increases proposal accuracy by correctly modeling demand charge interaction, which most simplified tools get wrong. Enables smaller solar companies to enter the C&I market without hiring dedicated financial analysts. Worth $200-500/month per user, targeting 2,000-5,000 C&I solar developers.
