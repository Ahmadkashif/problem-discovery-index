# Low-Cost IoT Well Monitoring for Marginal Wells

**Niche:** [[niches/oil-gas-field-services/stripper-well-operators/profile|Stripper Well Operators]]
**Industry:** [[industries/oil-gas-field-services|Oil & Gas Field Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** IoT well monitoring exists but costs $5K-$15K per well to install — 10-30x more than a stripper well's monthly profit margin can justify.
**Tags:** #anomaly-detection #time-series-forecasting #tabular-ml #revenue-impact

## The Problem
A stripper well producing 5 barrels/day at $70/bbl generates $350/day in revenue. After royalties, taxes, and operating costs, the monthly profit margin is $1,000-$3,000. A SCADA installation costing $10K with $200/month monitoring fees requires 6-12 months of margin to pay back — too long for a well that might need to be plugged in 2 years. Without monitoring, the operator does not know if a well has stopped producing until their next physical visit (every 1-3 days for nearby wells, weekly for distant ones). A well that stops pumping on Tuesday and is not visited until Friday has lost $1,050 in production. Over a year, undetected downtime from delayed well checks costs a 50-well stripper operator $15K-$40K.

## What Already Exists
Industrial IoT platforms (Ambyint, Flowmore, ESP Analytics) offer well monitoring with production optimization, but their hardware, connectivity, and software costs target wells producing 50+ bbl/day where the ROI is clear. Low-cost IoT sensors (cellular-connected vibration sensors, tank level monitors) exist at $100-$500 hardware cost, but no oilfield-specific platform aggregates their data into a stripper-well-appropriate monitoring dashboard. Consumer IoT platforms (Particle, Blues Wireless) provide connectivity hardware but require custom application development.

## The Customization Gap
Stripper well operators need an IoT monitoring kit priced at $200-$500 per well with $20-$50/month connectivity: a vibration sensor on the pump motor (confirms the well is running or not), a tank level sensor (tracks production without manual gauging), and optionally a casing pressure sensor. The data feeds a mobile dashboard that sends a simple text alert when a well stops producing or when tank level changes anomalously (possible leak or theft). No detailed SCADA analytics — just "is it running?" and "is it producing?" The economics must work for a 5 bbl/day well: the monitoring cost must be recovered in less than 1 month of prevented downtime.

## Target Customer
Stripper well operators managing 10-100 wells who currently visit each well every 1-3 days to check pump status and gauge tanks — a process that could be reduced by 50% with basic remote monitoring.

## Impact If Solved
Reduces undetected downtime by 70-80% (preventing $10K-$30K annually in lost production per 50-well operator), cuts physical well visits by 40-50% (saving $15K-$25K annually in fuel and labor), and provides the first digital production data for wells that have never been monitored — enabling trend analysis that reveals gradual decline versus equipment issues.
