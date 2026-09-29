# Enrichment & Integration

**Parent Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Category:** Highly Automatable
**Contested on:** Whether context arrives attached to the indicator or is assembled by whoever needs it, every time, from the same public sources.

## Profile

**Market Size:** ~$200M
**Share of Parent Industry:** ~4%
**Digital Adoption:** Moderate — largely solved and unevenly applied
**Target Buyer:** Platform and integration teams, security operations
**Automation Potential:** Very high — it is lookups and plumbing

## What Makes This a Distinct Niche

Between the indicator and the person who acts on it sits a layer of context: what this address is, who owns it, what else resolves there, what malware family it is associated with, which campaign, which report. And between the vendor and the customer's tooling sits a layer of plumbing: formats, transport, deduplication, normalisation and routing into the platforms that will match against it.

Both are mechanical and largely solved. Standard formats exist and are broadly adopted. Enrichment sources have APIs. Every platform has connectors.

The contest is where the work happens. When enrichment is applied at the vendor, every customer gets it once. When it is left to the customer, every organisation performs the same lookups against the same public sources, separately, at their own cost, with their own inconsistencies. The industry has largely chosen the second, which means the same passive DNS query is run by thousands of organisations about the same address.

It is the smallest niche in the industry and the one where the remaining inefficiency is most obviously duplicated effort rather than a hard problem.

## Current Tools & Gaps

STIX and TAXII for structured exchange, with simpler formats widely used in practice. Threat intelligence platforms handling ingestion, deduplication and normalisation across feeds. Enrichment services with APIs — passive DNS, WHOIS, geolocation, ASN, reputation. Connectors into every major SIEM and endpoint platform.

The gaps are about where enrichment sits and what survives the pipeline. Context is frequently stripped in normalisation, so an indicator arrives at the matching engine without the report it came from or the campaign it belongs to. Feed provenance is lost in deduplication, which blocks every per-feed measurement. Relationships between indicators — this address served this domain which delivered this hash — are collapsed into a flat list. Enrichment is duplicated across every customer. And format richness is unused because most pipelines reduce everything to a value and a type.

## Problems

- [[niches/threat-intelligence-vendors/enrichment-and-integration/build|🔨 Build: Context That Survives the Pipeline]]
- [[niches/threat-intelligence-vendors/enrichment-and-integration/buy|🛒 Buy: Data Pipeline Practice for Intelligence Ingestion]]
- [[niches/threat-intelligence-vendors/enrichment-and-integration/fix|🔧 Fix: Everyone Runs the Same Lookup Separately]]
