# Carrier Identity as a Network Problem

**Niche:** [[niches/freight-tech-platforms/carrier-identity-vetting/profile|Carrier Identity & Vetting]]
**Industry:** [[industries/freight-tech-platforms|Freight Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Freight fraud is invisible in any single carrier's documents and obvious in the relationships between carriers, phone numbers, email domains, bank accounts and addresses — and vetting is performed one carrier at a time against a document checklist.
**Tags:** #graph-neural-networks #graph-theory #gradient-boosting #spectral-graph-theory #confidence-intervals #evaluation-metrics #compliance #revenue-impact
**Contested on:** Every serious competitor in carrier vetting is fighting to establish who is actually going to haul a load before it moves — and whoever detects the fraudulent and re-brokering carriers earliest takes the account.

## The Problem
A carrier presents an active authority, a current certificate of insurance and a clean safety record, all verifiable against public sources. The load is tendered and disappears. Afterwards it emerges that the authority was dormant for two years before being reactivated last month, the contact phone number has been used by four other authorities, the email domain was registered six weeks ago, the remittance bank account is shared with an entity that defaulted on three brokers last quarter, and the physical address is a mailbox service. Every one of those facts was available before the load moved, and none of them is visible in a per-carrier document check.

## Why Nobody Has Built This
The signal lives across brokers and brokers do not share. A single brokerage sees its own experience, which is too sparse to reveal a pattern, and is structurally reluctant to tell a competitor that a carrier defrauded it — partly from competitive instinct and partly from a well-founded fear of defamation exposure if it labels a carrier fraudulent and is wrong. The vetting vendors that have grown fastest are the ones that began assembling cross-broker signal, which confirms the thesis and also shows how early the work is. The technical challenge is real too: the graph is built from noisy, self-reported attributes and the adversary adapts to whatever features are used, which makes this a live adversarial problem rather than a static classification one.

## What to Build
A relationship graph across carriers, brokers and loads, with entity attributes — phone numbers, email domains, addresses, bank accounts, registered agents, insurance producers, equipment identifiers, driver identities — as nodes and edges rather than as fields on a record. Fraud patterns are structural: rapid authority reactivation combined with shared contact infrastructure, a cluster of authorities sharing a remittance account, an entity whose loads consistently deliver under a different carrier's name. Scoring is relational and adversarial-aware, with feature sets that can be rotated as patterns shift. Output is a risk assessment with the specific structural evidence named, because a broker declining a carrier needs a reason that is defensible and specific rather than a score. The hardest part is not the model but the consortium: the data has to be contributed by competing brokers, which requires a governance and liability structure that makes contribution safe.

## Target Customer
Freight brokerages of all sizes, cargo insurers whose losses fund this problem, shippers with theft exposure, and the vetting platforms already assembling cross-broker signal.

## Impact If Built
Detection before the load moves is the only detection that matters, since recovery after cargo theft is rare and double brokering is discovered when the actual hauler demands payment. Cross-broker relational signal is the only evidence that exists at that point in time, which makes this the defining technical problem of the category and the one whose solution determines who owns the vetting layer.
