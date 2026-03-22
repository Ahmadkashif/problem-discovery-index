# IAQ Monitors Without Solution Recommendations

**Niche:** [[niches/hvac-contractors/indoor-air-quality/profile|Indoor Air Quality]]
**Industry:** [[industries/hvac-contractors|HVAC Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Consumer and commercial IAQ monitors (Awair, AirThings, PurpleAir) tell you the air quality is bad but not what to do about it — IAQ professionals need monitoring tools that connect readings to specific, actionable remediation recommendations for the HVAC systems they work with.
**Tags:** #gradient-boosting #automation #data-integration

## The Problem
IAQ monitoring hardware has exploded post-COVID. Consumer devices (Awair Element, AirThings Wave Plus) and professional sensors (TSI BlueSky, Kanomax IAQ monitors) measure PM2.5, CO2, VOCs, temperature, and humidity in real time. These devices generate data and display it on dashboards — green/yellow/red indicators for each parameter. But the dashboard stops at "your CO2 is high" or "your PM2.5 is elevated." The device doesn't know the building, the HVAC system, or the available remediation options. An IAQ professional using a $500 AirThings sensor gets the same output as a homeowner — they have to apply their expertise to translate readings into recommendations. The monitoring hardware and the recommendation intelligence are completely disconnected.

## What Already Exists
AirThings Business provides multi-sensor deployments with cloud dashboards for commercial buildings. Awair Score gives a composite IAQ score with general advice ("open a window," "reduce chemical cleaning products"). PurpleAir provides hyperlocal outdoor PM2.5 data. IQAir provides air quality data with general health recommendations. None of these platforms know what HVAC system is installed, what filtration is in place, whether the building has mechanical ventilation, or what remediation options are feasible given the existing infrastructure. Their recommendations are generic consumer advice, not professional HVAC remediation guidance.

## The Customization Gap
The missing layer is building-context-aware remediation intelligence. When an IAQ monitor deployed by an HVAC professional shows CO2 at 1,500 ppm in a commercial office, the platform should know: (1) the building has a VAV air handling system with an outdoor air economizer; (2) the current outdoor air damper minimum is set at 15%; (3) increasing to 25% would bring CO2 below 800 ppm based on the space occupancy and volume; (4) the estimated energy cost increase is $X/month. This requires coupling monitoring data with a building profile (HVAC system type, filtration, ventilation method, duct configuration) that only an HVAC professional can provide. The recommendation engine then becomes a decision support tool: "Given your readings, your system, and your budget, here are the 3 best interventions ranked by cost-effectiveness." This transforms IAQ monitoring from a data display into a professional service tool.

## Target Customer
IAQ service companies and HVAC contractors offering IAQ services who want to deploy monitoring in client facilities and use the data to drive service recommendations, not just generate reports.

## Impact If Solved
Transforms IAQ monitoring from a one-time test into a recurring service relationship — deploy monitors, provide ongoing recommendations, bill monthly for monitoring + analysis. Creates $50-200/month per location in recurring revenue for IAQ companies. Improves remediation accuracy by basing recommendations on continuous data rather than single-point-in-time testing.
