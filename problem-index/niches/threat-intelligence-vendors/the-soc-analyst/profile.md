# The SOC Analyst Receiving the Alerts

**Parent Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Category:** Underserved Audience
**Contested on:** Whether the alerts an intelligence subscription generates are worth the analyst's attention, and whether anyone has checked.

## Profile

**Market Size:** ~$350M
**Share of Parent Industry:** ~7%
**Digital Adoption:** Low — a queue and a clock
**Target Buyer:** Security operations leadership
**Automation Potential:** High for enrichment and suppression, low for the judgement

## What Makes This a Distinct Niche

The subscription generates alerts. The analyst works them. Most are stale indicators matching ordinary traffic — an address that hosted malicious infrastructure last quarter and now hosts a supplier, a domain that was sinkholed, a hash that matches a file with a legitimate use, a certificate on shared hosting.

Each takes minutes to dismiss and the minutes accumulate. The analyst learns which feeds produce noise and begins discounting their alerts, which is a rational adaptation and is also how a real detection gets missed.

The structural cause is arithmetic rather than vendor failure. The base rate of genuinely malicious traffic in an enterprise network is extremely low, so even a reasonably specific indicator produces mostly false positives. This is the standard screening result and it is essentially never explained to the people experiencing it, who conclude the problem is bad feeds or bad tooling.

This is an underserved audience because every party upstream optimises something else. The vendor optimises collection breadth. Procurement optimises indicator volume. The platform optimises matching throughput. Nobody optimises the analyst's queue, and the analyst is the constraint on the entire operation.

## Current Tools & Gaps

SIEM and case management with alert queues and disposition fields. Some enrichment at alert time — reputation lookups, passive DNS, historical context. Suppression rules and allowlists, maintained manually. Tuning based on analyst complaint. Playbooks for common alert types.

The gaps concentrate on what the analyst needs at the moment of triage. Enrichment is inconsistent, so an analyst frequently starts by looking up what the indicator is and why it fired. Nothing shows the indicator's age or the infrastructure type, which are the two facts that most often resolve an alert immediately. Suppression is manual and reactive, so the same benign match recurs until somebody writes a rule. Historical context is absent, so an analyst cannot see that this same alert was investigated and dismissed three times last month. And nothing feeds the dismissals back to anyone who could stop them.

## Problems

- [[niches/threat-intelligence-vendors/the-soc-analyst/build|🔨 Build: The Alert That Arrives Resolved]]
- [[niches/threat-intelligence-vendors/the-soc-analyst/buy|🛒 Buy: Enrichment and Suppression From Security Operations]]
- [[niches/threat-intelligence-vendors/the-soc-analyst/fix|🔧 Fix: The Same Benign Match, Every Week]]
