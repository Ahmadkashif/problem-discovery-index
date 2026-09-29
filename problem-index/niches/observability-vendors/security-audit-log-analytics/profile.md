# Security & Audit Log Analytics

**Parent Industry:** [[industries/observability-vendors|Observability Vendors]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor here is fighting to make years of security-relevant logs affordable to keep and fast to investigate — and whoever does that takes the security operations account, because retention is mandated and the cost of it is the reason teams keep changing vendors.

## Profile
**Market Size:** ~$2.2B US security and audit log analytics
**Share of Parent Industry:** ~18% of category revenue
**Digital Adoption:** High — every regulated organisation runs something
**Target Buyer:** Security operations, compliance and audit functions
**Automation Potential:** High for detection engineering and investigation; retention economics are the binding constraint

## What Makes This a Distinct Niche
Security log analytics looks like observability and behaves like a different business. The retention horizon is years rather than weeks, driven by regulation and by the fact that intrusions are frequently discovered long after they occur. The query pattern is rare, deep and time-bounded — an analyst investigating a specific hypothesis across eighteen months — rather than frequent and interactive. The buyer is a security operations function with a compliance mandate, purchasing against a competitive set of security-specific vendors. And the content matters as much as the platform: detection rules, threat intelligence and investigation workflow are the product, in a way that has no analogue on the engineering side. The economics are the perennial fight: the volume is enormous, the retention is mandatory, and the price per gigabyte determines what the organisation can afford to keep, which determines what it can investigate.

## Current Tools & Gaps
Security information and event management platforms, log analytics products with security content, data lake approaches with security tooling on top, and detection engineering frameworks. The gaps: retention cost forces organisations to discard logs they are likely to need, which is the single largest constraint on investigation; detection rules are written and never evaluated, so nobody knows which fire usefully — the identical problem the alerting niche describes for engineering; investigation is a manual pivot across sources with the analyst holding the hypothesis in their head; and log source coverage is assumed rather than verified, so a source that silently stopped forwarding is discovered during an investigation.

## Problems
- [[niches/observability-vendors/security-audit-log-analytics/build|🔨 Build: Retention Priced So You Discard What You Will Need]]
- [[niches/observability-vendors/security-audit-log-analytics/buy|🛒 Buy: Detection Engineering as a Measured Discipline]]
- [[niches/observability-vendors/security-audit-log-analytics/fix|🔧 Fix: The Log Source That Stopped Forwarding]]
