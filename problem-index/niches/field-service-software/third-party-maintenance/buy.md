# Parts Cross-Referencing From Automotive Aftermarket Practice

**Niche:** [[niches/field-service-software/third-party-maintenance/profile|Third-Party Maintenance — Parts Without the Manufacturer]]
**Industry:** [[industries/field-service-software|Field Service Software]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The automotive aftermarket solved part cross-referencing across manufacturers, aftermarket equivalents and superseded numbers decades ago with published standards and commercial catalogues, and third-party equipment maintainers do it from binders and memory.
**Tags:** #graph-theory #k-nearest-neighbors #bert #word-embeddings #evaluation-metrics #confidence-intervals #data-integration #automation
**Contested on:** Every serious competitor in third-party maintenance software is fighting to source, verify and certify a part for equipment its customer's manufacturer would rather it did not service — and whoever makes parts provenance reliable takes the account.

## The Problem
A technician needs a specific component. The OEM part number has been superseded twice. An aftermarket manufacturer makes an equivalent under a different number. A broker has one listed under the original number that may or may not be the right revision. Establishing which of these will actually work in this machine takes an experienced parts person forty minutes of phone calls and catalogue lookups, and the knowledge that makes it possible lives in a handful of people per organisation.

## What Already Exists
The automotive aftermarket has industry-standard catalogue formats, established interchange databases, and a mature ecosystem of commercial cross-reference products covering millions of parts across manufacturers and equivalents. The methodology — canonical part identity, interchange relationships, fitment against a vehicle configuration — is directly analogous and thoroughly proven. Equipment manufacturers publish parts catalogues, and in many categories right-to-repair developments have improved documentation access. Entity resolution tooling for matching part descriptions across sources is commodity.

## The Customization Gap
The adaptation is to equipment whose fitment model is more complex than a vehicle's and whose data is less openly published. It requires: (1) a fitment model that accounts for machine serial ranges, hardware revisions and software versions together, since compatibility in this equipment is frequently a three-way condition rather than a model-year lookup; (2) building the interchange graph from the maintainer's own successful and failed installations, because no published interchange database exists for most of this equipment and the organisation's own history is the only ground truth available; (3) confidence and provenance on every interchange assertion, so a technician knows whether an equivalence is documented, inferred, or tried once by a colleague; (4) pooling across maintainers where they are willing, since the same interchange knowledge is being rediscovered independently by every organisation in the segment; and (5) ingestion from broker and marketplace listings, which is where availability actually lives and which is unstructured text.

## Target Customer
Independent service organisations, parts brokers, and the inventory and field service vendors serving them.

## Impact If Solved
Cross-referencing consumes a large share of a parts person's day and is the main reason a part is not on the truck, which makes it a direct contributor to first-visit resolution in this segment. Building the interchange graph from installation history also converts the segment's most valuable tacit knowledge — which lives in a few long-tenured people — into an organisational asset.
