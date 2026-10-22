# NOC Alarm Correlation & Outage Reporting

**Parent Industry:** [[industries/wireless-carriers|Wireless Carriers]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to turn a flood of network alarms into the handful of incidents that need action, with a cause attached, fast enough to restore service and file the FCC outage report on time, and whoever gives the shortest time from first alarm to correct incident takes the network-operations contract.

## Profile
**Market Size:** ~$2B a year in service assurance, alarm management, AIOps and NOC staffing tools across carriers (estimate)
**Share of Parent Industry:** under 1% of carrier revenue (estimate)
**Digital Adoption:** High — every alarm, counter and ticket is digital; correlation is still largely rules and experienced operators
**Target Buyer:** VP Network Operations / Head of NOC
**Automation Potential:** Very high for correlation and reporting; Medium for restoration decisions

## What Makes This a Distinct Niche
A carrier's NOC receives a continuous stream of alarms from radios, transport, power, core and vendor systems. One fibre cut or power failure can raise thousands of alarms across dozens of sites. Operators must find the root event, open one incident rather than hundreds of tickets, dispatch the right team and, if the outage crosses Part 4 thresholds, notify the FCC through NORS within hours (roughly 120 minutes for notification, then an initial report within ~72 hours and a final report within ~30 days, as recalled). This is the most mechanical, repeatable decision work in network operations, and it is labelled by what the incident turned out to be.

## Current Tools & Gaps
Vendor element managers, NetScout and other service assurance suites, ServiceNow IT operations management, AIOps tools such as BigPanda and Moogsoft, and in-house correlation rules. The gaps: rules break whenever topology changes; correlation stops at the domain boundary (radio, transport, power); and outage scope for NORS is estimated by hand.

## Problems
- [[niches/wireless-carriers/noc-alarm-outage-reporting/build|🔨 Build: Topology-Aware Alarm-to-Incident Correlation]]
- [[niches/wireless-carriers/noc-alarm-outage-reporting/buy|🛒 Buy: IT AIOps Taught Radio and Transport Topology]]
- [[niches/wireless-carriers/noc-alarm-outage-reporting/fix|🔧 Fix: Outage User-Minutes Estimated by Hand for NORS]]
