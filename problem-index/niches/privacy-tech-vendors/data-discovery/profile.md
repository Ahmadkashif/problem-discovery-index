# Data Discovery & Mapping

**Parent Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Category:** High Market Share
**Contested on:** Whether the record of where personal data lives and flows is observed from the systems or compiled by asking people what they think is true.

## Profile

**Market Size:** ~$1.40B
**Share of Parent Industry:** ~20%
**Digital Adoption:** Low — interviews, spreadsheets, partial scanning
**Target Buyer:** Privacy engineering, privacy counsel, data governance
**Automation Potential:** High for flows, moderate for meaning

## What Makes This a Distinct Niche

Every privacy obligation rests on knowing where personal data is. Fulfilling a deletion request requires knowing every place the person's data sits. Assessing an international transfer requires knowing what crosses which border. Responding to an incident requires knowing what was in the affected system. Producing a record of processing requires all of it.

That record is built by interviewing teams. A privacy programme manager sends a questionnaire to system owners asking what personal data their system holds, where it came from and where it goes. The responses are assembled into a record of processing activities, data flow diagrams and a system inventory, signed off, and filed.

It is wrong before it is finished. Systems are created, connected and retired continuously. The person answering for a system may not know what a downstream integration does with the data. Shadow systems are absent by definition. And the whole exercise repeats annually, by which point the estate has changed substantially.

Every serious competitor is fighting over the same thing: whether the map can be derived rather than surveyed. A vendor whose map was observed would be selling evidence where the category currently sells an artefact.

### Contested sub-niches

- [[niches/privacy-tech-vendors/data-flow-observation/profile|🎯 Data Flow Observation]]
- [[niches/privacy-tech-vendors/personal-data-classification/profile|🎯 Personal Data Classification]]

## Current Tools & Gaps

Data discovery and classification products scanning databases, warehouses and file stores for personal data patterns. Records of processing built from questionnaires with workflow around them. Data flow diagrams drawn by hand. Some integration-based discovery of SaaS applications. Cloud data catalogues with varying privacy awareness.

The gaps are consistent. Scanning covers structured stores an agent was pointed at and misses everything else — logs, caches, message queues, object storage, third-party systems, anything not connected. Flows between systems are described rather than observed, so the map records intent rather than behaviour. Classification is pattern-matching, so it finds email addresses and misses the identifier column that is personal data by linkage. Nothing measures the map's own completeness, so no organisation knows what fraction of its estate the record covers. And the record is a point-in-time artefact in a continuously changing estate.

## Problems

- [[niches/privacy-tech-vendors/data-discovery/build|🔨 Build: A Map That Is Observed]]
- [[niches/privacy-tech-vendors/data-discovery/buy|🛒 Buy: Data Catalogues and Lineage, Privacy-Aware]]
- [[niches/privacy-tech-vendors/data-discovery/fix|🔧 Fix: The Record Is a Survey From Last Year]]
