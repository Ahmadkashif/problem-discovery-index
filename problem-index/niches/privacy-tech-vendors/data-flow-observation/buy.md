# Buy: Network and Cloud Telemetry, Read for Privacy

**Niche:** Data Flow Observation
**Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Security and cloud teams already collect complete egress and flow telemetry and read it for threats and spend, and nobody reads the same data for where personal information is going.
**Tags:** #graph-theory #gradient-boosting #evaluation-metrics #change-point-detection #data-integration #compliance #automation
**Contested on:** Whether where data actually goes can be derived from the systems that already record it.

## The Problem

The telemetry exists and is already being collected, at cost, by teams who read it for something else.

Security teams collect egress traffic, DNS queries, cloud flow logs and API access records to detect exfiltration, command-and-control traffic and anomalous access. Cloud teams collect the same data to attribute spend and diagnose performance. Both retain it, index it and query it routinely.

The privacy question — which of these flows carries personal data, to which third parties, across which borders — is answerable from the same records and is asked by nobody, because the privacy team does not know the data exists, does not have access to it, and would not know how to query it if they did.

So an organisation simultaneously operates a comprehensive record of where its data goes and a record of processing built by asking people what they think happens.

## What Already Exists

Security telemetry: SIEM platforms holding egress logs, DNS records, proxy logs and cloud audit trails; network detection and response tools; cloud-native flow logging across the major providers.

Data loss prevention: a category built specifically to detect sensitive data leaving the organisation, with content inspection and policy enforcement — the closest existing capability and aimed at preventing exfiltration rather than at documenting legitimate flows.

Cloud security posture and DSPM: Wiz, Orca, Cyera, Sentra and Dig, with cloud asset and data discovery and increasingly data movement visibility.

SaaS security posture: Obsidian, AppOmni and Valence, enumerating SaaS integrations, OAuth grants and their scopes — the clearest view of third-party data access in a modern estate.

Cost and observability: cloud cost tools attributing egress spend by destination, which is an underused proxy for data flow volume.

## The Customization Gap

**DLP looks for the wrong thing.** Data loss prevention detects unauthorised movement of sensitive data and is tuned to block exfiltration. Privacy needs an inventory of authorised flows — the routine, approved, contractual movement of personal data to processors — which DLP treats as noise to be allowlisted.

**Nothing attributes destinations to organisations.** Security tooling resolves destinations well enough to assess threat. Privacy needs the recipient's corporate identity, jurisdiction and contractual status, which is a different registry and a different lookup.

**Retention is wrong for the purpose.** Security telemetry is retained for weeks. A record of processing describes a year. Building a privacy flow map means either longer retention or continuous summarisation into a durable structure.

**The output format is an alert, not a register.** Security tooling produces detections. Privacy needs a stable, reviewable inventory of relationships with volumes, purposes and legal bases attached.

**SaaS posture tooling is the closest fit and serves security.** OAuth grant enumeration is precisely the third-party access inventory a processor register should be built from, and it is sold to security teams who use it to find risky integrations rather than to privacy teams who need to register them.

**No privacy vendor has the access.** The integration required is heavy and the privacy buyer cannot authorise it, which is why this has to be sold jointly or built by a vendor already inside the security stack.

## Target Customer

DSPM and cloud data security vendors — Cyera, Sentra, Dig — are the most plausible adapters: they already discover and classify data across cloud estates, already sell to a buyer who can grant access, and a privacy register is an adjacent output from the same telemetry.

SaaS security posture vendors are the sharpest fit for the third-party half, since their OAuth inventory is the processor register the privacy team is currently compiling from memory.

The privacy platforms as consumers rather than builders, integrating with the security stack instead of attempting their own network observation.

## Impact If Solved

An organisation stops paying to collect the same telemetry twice and stops maintaining two contradictory accounts of where its data goes.

SaaS OAuth inventories would replace the processor register's weakest input — who somebody remembered to register — with an enumeration of who actually has access.

And reading existing security telemetry for privacy purposes requires no new collection, which makes this one of the cheapest large improvements available in the category.
