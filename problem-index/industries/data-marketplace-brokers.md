# Data Marketplace Brokers

## Profile
**Category:** Data & AI Economy
**Market Size:** ~$5B US commercial data exchange, alternative data and dataset brokerage
**Tech Maturity:** Excellent distribution, absent evaluation — Snowflake Marketplace, AWS Data Exchange, Databricks Delta Sharing and specialist brokers like Datarade, Demyst and Nomad Data have solved delivery. A buyer still cannot determine whether a dataset is any good, or whether it was lawfully collected, without buying it first.
**Workforce:** Data sourcing analysts, provenance and compliance reviewers, solutions engineers, partner managers, catalogue operations staff, legal counsel

## Key Pain Themes
The market's defining friction is that datasets cannot be evaluated before purchase. Sample files are curated, statistics are self-reported, and the properties a buyer actually needs — coverage of their population, freshness, accuracy against a known reference, and whether the fields they care about are populated — are discoverable only after money has changed hands and an integration has been built. Alongside it sits a provenance problem that has grown from a compliance footnote into a central risk: buyers increasingly need to know how data was collected, under what consent, and whether it may lawfully be used for model training, and the answer arrives as a warranty in a contract rather than as evidence. Two operational burdens follow: schema harmonisation, where every provider models the same entities differently; and licence term enforcement, where permitted use is written in prose and enforced by nothing. Sourcing analysts spend their time running evaluations they should not have to run, and provenance reviewers make judgement calls on suppliers they cannot audit.

## Current Tech Landscape
Cloud-native marketplaces have made delivery frictionless within their ecosystems, with Snowflake and Databricks sharing data without physically moving it. Discovery catalogues aggregate offerings across providers with self-reported metadata. Data quality tooling exists and runs after acquisition. Privacy regulation has made provenance a live commercial question, with several state privacy laws and the EU regime imposing obligations that flow through to buyers. Clean rooms have emerged for cases where the data cannot be shared directly. The alternative data segment serving investment firms operates with its own compliance conventions around material non-public information and consent.

## Problems
- [[problems/data-marketplace-brokers/high-impact|🔴 High Impact: Evaluating a Dataset Before Buying It]]
- [[problems/data-marketplace-brokers/low-impact-1|🟡 Low Impact: Cross-Provider Schema Harmonisation]]
- [[problems/data-marketplace-brokers/low-impact-2|🟡 Low Impact: Licence Term Expression and Enforcement]]
- [[problems/data-marketplace-brokers/worker-life-1|🟢 Worker Life: Sourcing Analyst Running Evaluations]]
- [[problems/data-marketplace-brokers/worker-life-2|🟢 Worker Life: Provenance Reviewer Signing Off a Supplier]]
- [[problems/data-marketplace-brokers/ml-opportunity|🧠 ML Opportunities]]
- [[problems/data-marketplace-brokers/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
A marketplace intermediating datasets sees something neither buyers nor sellers see: which datasets were evaluated and rejected, which were bought and churned, which fields buyers actually use, and how providers covering the same domain compare on the dimensions that matter. That is the basis for the quality signal the market conspicuously lacks. The reason it does not exist is that the marketplace's revenue comes from transactions rather than from outcomes, and publishing comparative quality would make some of its own suppliers unsaleable.
