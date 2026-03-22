# Remote Monitoring with Limited Connectivity

**Niche:** [[niches/solar-installers/rural-off-grid/profile|Rural & Off-Grid Solar]]
**Industry:** [[industries/solar-installers|Solar Installers]]
**Type:** Fix (Pain Point)
**One-liner:** Off-grid solar systems in remote locations lack the reliable internet connectivity that standard monitoring platforms require — leaving systems unmonitored, with equipment failures going undetected for days or weeks until the customer calls to report they're out of power.
**Tags:** #time-series-forecasting #automation #worker-facing #change-point-detection #gradient-boosting

## The Problem
Grid-tied solar monitoring (Enphase Enlighten, SolarEdge monitoring) requires a continuous internet connection via WiFi or Ethernet. Off-grid installations are by definition in locations without reliable internet — rural cabins, agricultural properties, remote telecom towers, and wilderness homes. Without monitoring, the installer has no visibility into system performance: a failed charge controller, a degraded battery, or a ground fault can go undetected until the customer's power fails. For agricultural solar (well pumps, livestock water systems), an undetected failure means livestock without water — a life-threatening situation. For residential off-grid, a winter equipment failure means a family without heat and power in a location potentially hours from the nearest service. The installer only learns about problems when the customer calls in crisis, leading to expensive emergency service calls to remote locations.

## Why It's Still Broken
Standard monitoring platforms require always-on broadband. Cellular connectivity (LTE) is available in many rural areas but is inconsistent — signal strength varies, and data transmission fails during weather events that also stress the solar system. Satellite connectivity (Starlink, cellular-satellite hybrids) is becoming available but adds $50-120/month in service costs to systems where the customer is already budget-constrained. No monitoring platform is designed for intermittent connectivity — they expect continuous data streams and alert when data stops, creating constant false alarms in areas with spotty cellular service.

## What a Fix Looks Like
A monitoring system designed for intermittent connectivity that: (1) runs edge processing on a local device at the off-grid site — collecting data continuously from the charge controller, inverter, and battery monitor, performing anomaly detection locally, and storing data for batch upload; (2) transmits data via cellular when available, using compressed data packets that can transmit a day's monitoring data in a single brief connection rather than requiring continuous streaming; (3) triggers immediate satellite alerts (via Iridium or similar low-bandwidth satellite) only for critical failures (battery critically low, charge controller failure, ground fault detected) that warrant emergency notification regardless of cellular availability; and (4) provides the installer with a dashboard showing all monitored off-grid systems with traffic-light status — systems that haven't reported in 48+ hours are flagged for proactive outreach before a customer-reported emergency.

## Who Feels the Pain
Off-grid system owners who discover equipment failures only when they lose power — potentially days or weeks after the failure occurred. Installers who receive emergency service calls to remote sites, losing a full day of travel plus emergency rates for visits that could have been prevented with monitoring. Agricultural customers whose livestock are at risk when solar-powered water systems fail silently.

## Impact If Fixed
Detects 80-90% of equipment failures within hours rather than days or weeks, enabling proactive service before the customer experiences an outage. Reduces emergency service calls to remote sites by 50-70%, saving $500-2,000 per avoided emergency trip. Gives off-grid customers the monitoring visibility that grid-tied customers take for granted. Could be priced at $10-20/month per monitored site including cellular data.
