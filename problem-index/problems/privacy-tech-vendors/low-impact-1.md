# The Data Map Is a Survey

**Industry:** [[privacy-tech-vendors|Privacy Tech Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every downstream obligation rests on knowing where personal data is, and that record is compiled by interviewing teams and is wrong before it is finished.
**Tags:** #bert #transformers #gradient-boosting #graph-neural-networks #dbscan #confidence-intervals #evaluation-metrics #data-integration

## The Problem
Records of processing, data inventories and flow diagrams are the foundation of a privacy programme. Fulfilling a deletion request requires knowing which systems hold the person's data. Assessing an international transfer requires knowing what crosses a border. Responding to an incident requires knowing what was in the affected system.

That record is built by asking. A privacy team interviews each business function, records what they say they collect and where they say it goes, and assembles it into a register. The teams answer from memory and from what they know about systems they own, which excludes what other teams connected to them, what a vendor's integration pulls, and what an analytics pipeline copied three years ago.

It then decays immediately. Systems are created continuously, data is copied into warehouses and notebooks, a new vendor is connected by a team that did not tell anyone, and a schema gains a field that turns a non-personal table into a personal one.

Discovery tooling exists and covers part of the estate — structured databases well, object storage moderately, and the long tail of software-as-a-service systems, analytics platforms and internal tools poorly. Which means the map is a survey plus a partial scan, presented as an inventory.

## What Already Exists
BigID, Securiti and the discovery modules of the larger platforms scan data stores, classify personal data by pattern and context, and build inventories. Cloud providers offer native classification services. Data catalogues from the analytics world hold schema-level metadata. Records of processing templates and workflow are standard across the privacy platforms. Vendor and processor registers are maintained manually with questionnaire evidence.

## The Customisation Gap
Classification needs to work on context rather than on pattern. A column of nine-digit numbers may or may not be a national identifier; a free-text field may contain anything; a column named after a customer may hold a company or a person. Classification that uses surrounding schema, table relationships, sample values and how the field is used downstream is materially more accurate than pattern matching and is what the long tail requires.

Flow inference is the larger gap. A map is not an inventory of stores, it is a graph of movements, and the movements are observable — in query logs, pipeline definitions, integration configurations, network egress and application code — rather than needing to be described. Inferring the graph from what systems actually do, and reconciling it against what the register claims, is the capability that would convert a survey into a measurement.

Coverage must be reported. A scan that reached forty percent of the estate should say so, and the current presentation of an inventory as complete is the same failure that appears across every assurance product in this cluster.

And the unstructured and semi-structured estate is where the real exposure sits — document stores, ticketing systems, support transcripts, shared drives — and is the part least covered by tooling designed for databases.

## Impact If Solved
Every privacy obligation an organisation has rests on this record, and it is a survey with a partial scan attached. Context-based classification, flow inference from what systems actually do, honest coverage reporting and extension into the unstructured estate would turn the foundational artefact from something assembled for an auditor into something that supports the operations that depend on it.
