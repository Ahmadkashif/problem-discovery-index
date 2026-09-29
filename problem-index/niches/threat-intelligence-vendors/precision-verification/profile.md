# Precision Verification

**Parent Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Category:** Contested Sub-Niche
**Contested on:** Whether, when an indicator fires, anyone can establish that the activity it flagged was genuinely malicious.

## Profile

**Market Size:** ~$400M
**Share of Parent Industry:** ~8%
**Digital Adoption:** Very low — verdicts are recorded and never joined back
**Target Buyer:** Vendor leadership, security operations, independent evaluators
**Automation Potential:** Moderate — the join automates, the ground truth does not

## What Makes This a Distinct Niche

This is the half that needs ground truth. An indicator matched. Was the traffic it flagged actually malicious, or was it a supplier's newly-allocated address, a shared hosting provider, a sinkholed domain, or ordinary activity that happened to touch infrastructure someone once saw in a report?

Establishing that requires an investigation to have concluded and an analyst to have recorded a verdict. Those verdicts exist — every SOC records disposition on every alert — and they are inconsistent, compressed under time pressure, and contested in exactly the ambiguous cases that determine precision.

That dependency is what separates it from [[niches/threat-intelligence-vendors/match-rate-measurement/profile|🎯 Match Rate Measurement]], which needs only telemetry and produces an answer this quarter. Precision needs adjudicated outcomes, joined back to the indicator that produced them, at enough volume to be meaningful — which is a multi-year data collection problem with a governance layer, and it is why a vendor would build match rate first and defer this indefinitely.

It is also where the defensible claim lives. A match rate says a feed fires. Precision says it fires on the right things, which is the claim the category makes implicitly and has never substantiated.

## Current Tools & Gaps

Alert disposition recorded in case management systems — true positive, false positive, benign, duplicate — with wide variation in how consistently the categories are applied. Some indicator confidence scoring by vendors, based on collection method rather than on observed outcome. Community reputation services and allowlists for known-benign infrastructure. Post-incident reports linking activity to indicators, written for a few incidents rather than for all alerts.

The gaps are structural. Disposition is recorded and almost never joined back to the indicator that produced the alert, so the feedback exists and does not return. Disposition taxonomies vary between organisations, so the data is not comparable. The ambiguous cases — an indicator matching something suspicious that was never resolved — are recorded as whatever closes the ticket. Vendor confidence scores are not calibrated against observed precision. And no mechanism exists for organisations to contribute disposition data back, which is the only route to a population-scale measurement.

## Problems

- [[niches/threat-intelligence-vendors/precision-verification/build|🔨 Build: Verdicts Joined Back to Indicators]]
- [[niches/threat-intelligence-vendors/precision-verification/buy|🛒 Buy: Adjudication Practice From Clinical Trials]]
- [[niches/threat-intelligence-vendors/precision-verification/fix|🔧 Fix: The Disposition Is Whatever Closed the Ticket]]
