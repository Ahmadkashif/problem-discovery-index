# Niche Analysis — Threat Intelligence Vendors

**Parent Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]

## Niche Selection

Threat intelligence is an assurance product whose success case is an attack that did not happen, so the category competes on collection breadth and analyst reputation. The eight niches below start from the two measurable proxies nobody publishes, then follow the products that generate the data, the relevance problem, the two people at either end, and the mechanical layers.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Indicator Feeds | 🔵 High Market Share | ~$1.30B | High — volume delivery is solved | Security operations leadership |
| 2 | Feed Quality Measurement | 🔵 High Market Share | ~$1.00B | Very low — unmeasured by anyone | Vendor leadership, security buyers |
| 3 | Finished Intelligence Reporting | 🟠 Low Digitized | ~$850M | Very low — a report to a portal | CISOs, intelligence consumers |
| 4 | Relevance & Customer Targeting | 🟠 Low Digitized | ~$600M | Very low — coarse sector tags | Vendor product, customer analysts |
| 5 | The Intelligence Analyst | 🟣 Underserved Audience | ~$400M | Low — no outcome ever returns | Vendor research leadership |
| 6 | The SOC Analyst Receiving the Alerts | 🟣 Underserved Audience | ~$350M | Low — a queue of stale matches | Security operations |
| 7 | Indicator Lifecycle & Decay | ⚡ Highly Automatable | ~$300M | Low — aging is barely modelled | Vendor platform engineering |
| 8 | Enrichment & Integration | ⚡ Highly Automatable | ~$200M | Moderate — largely solved | Platform and integration teams |

## Why These Niches

Indicator feeds are the volume product and quality measurement is the thing nobody sells because nobody measures it. Finished reporting is careful analytical work that disappears into a portal with no feedback. Relevance is where the filtering burden was pushed onto the customer. The two underserved people sit at opposite ends of the same pipeline — the analyst who never learns whether their assessment changed anything, and the security analyst investigating stale indicators matching ordinary traffic. Lifecycle and enrichment are mechanical.

## Niches

- [[niches/threat-intelligence-vendors/indicator-feeds/profile|🔵 Indicator Feeds]]
- [[niches/threat-intelligence-vendors/feed-quality/profile|🔵 Feed Quality Measurement]]
  - [[niches/threat-intelligence-vendors/match-rate-measurement/profile|🎯 Match Rate Measurement]]
  - [[niches/threat-intelligence-vendors/precision-verification/profile|🎯 Precision Verification]]
- [[niches/threat-intelligence-vendors/finished-reporting/profile|🟠 Finished Intelligence Reporting]]
- [[niches/threat-intelligence-vendors/relevance-targeting/profile|🟠 Relevance & Customer Targeting]]
- [[niches/threat-intelligence-vendors/the-intelligence-analyst/profile|🟣 The Intelligence Analyst]]
- [[niches/threat-intelligence-vendors/the-soc-analyst/profile|🟣 The SOC Analyst Receiving the Alerts]]
- [[niches/threat-intelligence-vendors/indicator-lifecycle/profile|⚡ Indicator Lifecycle & Decay]]
- [[niches/threat-intelligence-vendors/enrichment-and-integration/profile|⚡ Enrichment & Integration]]

## Filter Notes

Seven of the eight are terminal — each names one contest every serious competitor is fighting over, and decomposing further would produce features rather than markets.

**Feed quality measurement** is not, and the industry's own analysis names both halves: whether an indicator ever matched anything in a customer's telemetry, and whether what it matched turned out to be real. These are different measurements with different data, different timelines and different difficulty. Match rate is computable from telemetry alone — did this indicator ever fire, at how many organisations, against what volume of traffic — requires no adjudication, produces an answer within a collection window, and would immediately reveal what proportion of a feed of millions has never matched anything anywhere. Precision requires ground truth: when an indicator fired, was the activity genuinely malicious, which needs an investigation to have concluded, an analyst to have recorded a verdict, and someone to have joined that verdict back to the indicator. Adjudicated outcomes are scarce, slow, inconsistently recorded and contested in exactly the ambiguous cases that matter most. A vendor with endpoint telemetry can publish match rates next quarter and would still be years from publishing precision — which is why the first would be built and the second deferred, and why the second is where the defensible claim lives.

Two adjacent candidates were rejected as belonging elsewhere: **operating detection and response on the customer's behalf** is the subject of [[industries/cybersecurity-mssp|Cybersecurity MSSP]], and **domain abuse, impersonation and takedown** belongs to [[industries/brand-protection-firms|Brand Protection Firms]].
