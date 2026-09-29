# Machine Learning Opportunities — Data Marketplace Brokers

**Industry:** [[data-marketplace-brokers|Data Marketplace Brokers]]
**Derived from:** [[problems/data-marketplace-brokers/high-impact|High Impact]], [[problems/data-marketplace-brokers/low-impact-1|Low Impact 1]], [[problems/data-marketplace-brokers/low-impact-2|Low Impact 2]], [[problems/data-marketplace-brokers/worker-life-1|Worker Life 1]], [[problems/data-marketplace-brokers/worker-life-2|Worker Life 2]]

---

## 1. Pre-Purchase Coverage and Quality Measurement
#hypothesis-testing #confidence-intervals #descriptive-statistics #evaluation-metrics #bayesian-inference #k-nearest-neighbors #data-integration #revenue-impact

**Problem statement:** Datasets cannot be evaluated before purchase. Samples are curated, coverage statistics are self-reported against undefined universes, and overlap with a buyer's existing holdings is unknowable without a match. Buyers discover in week six that coverage of their segment is a third of the headline number because the headline counted a different population.

**ML task:** Privacy-preserving overlap estimation between a buyer's reference population and a seller's dataset, plus standardised quality characterisation computed by the marketplace
**Input data:** Seller dataset field statistics computed in place — population rates, distinct value distributions, record age, update recency; buyer reference list under private set intersection or clean room protocols; cross-provider records covering the same entities; historical buyer renewal and churn behaviour; field-level query telemetry showing which fields buyers actually use.
**Target:** Estimated coverage of the buyer's specific population with a confidence interval, and standardised per-field quality measures comparable across providers in a category.
**Evaluation metric:** Accuracy of the pre-purchase coverage estimate against measured coverage after purchase — directly checkable on historical transactions and the number that determines whether buyers trust the estimate at all. For quality measures, correlation with buyer renewal, which is the strongest available outcome signal.
**Scope:** Private set intersection and clean room architectures already exist and are deployed by these same platforms for advertising use cases; applying them to evaluation is a product decision rather than a technical advance. Cross-provider agreement is the accuracy proxy that works without external ground truth — where several providers cover the same entities, disagreement localises quality problems, and the marketplace is the only party who can compute it. Sample representativeness testing puts a number on the curation gap that analysts currently flag as an unquantifiable asterisk. 2-3 ML engineers plus a privacy engineer, 5-6 months.
**Data availability:** Field statistics are computable in place without exposing records. Renewal and churn behaviour is complete inside the marketplace. Query telemetry showing which fields matter exists in the sharing platforms and is not used for this.

---

## 2. Cross-Provider Entity Resolution as Marketplace Infrastructure
#bert #word-embeddings #k-nearest-neighbors #dbscan #graph-neural-networks #evaluation-metrics #data-integration #feature-engineering

**Problem statement:** Every buyer combining several providers writes the same crosswalks and the same entity resolution layer independently. The mapping between any two providers in a category is largely fixed, so the work done by one buyer would serve every subsequent one, and the marketplace is positioned to do it once and does not.

**ML task:** Entity resolution across provider datasets covering the same entity types, plus semantic field mapping between provider schemas
**Input data:** Provider datasets with their identifiers, names, addresses and attributes; standard identifiers where populated (DUNS, LEI, place identifiers); provider schema documentation; historical buyer-built crosswalks where obtainable; field value distributions for semantic matching.
**Target:** A canonical entity identity spanning providers, and a validated field-level mapping between any two provider schemas.
**Evaluation metric:** Pairwise precision and recall on a manually adjudicated sample, with false merges weighted heavily — combining two genuinely different companies corrupts every downstream analysis and is far worse than a missed link. For field mapping, buyer acceptance of proposed mappings without modification.
**Scope:** Commercial entity resolution is hard for well-understood reasons: legal versus trading names, address changes, subsidiaries and acquisitions, and standard identifiers populated exactly where they are least needed. Semantic field mapping must handle the case where two similarly named fields have genuinely different definitions — full-time employees versus total staff — which is documented in prose if at all and is the difference that silently corrupts merged data. Schema drift monitoring requires no learning and prevents the silent breakages that make buyers distrust purchased data. 3 ML engineers, 6 months.
**Data availability:** Provider data is accessible to the marketplace under existing arrangements in the cloud-native platforms. Buyer-built crosswalks are the ideal training signal and sit inside buyer environments, obtainable only by agreement.

---

## 3. Licence Term Extraction and Lineage-Based Enforcement
#large-language-models #bert #transformers #word-embeddings #transfer-learning #evaluation-metrics #compliance #data-integration

**Problem statement:** Permitted-use terms live in a signed agreement and the data lands in a warehouse, with no connection between them. Two years later an engineer joins a restricted table into a training pipeline. The analytics-versus-training distinction is now the most consequential term in many licences and the least likely to reach the person who needs it.

**ML task:** Extraction of permitted use, prohibited use, retention, territory and attribution terms from licence agreements into a machine-readable policy, plus checking downstream lineage against that policy
**Input data:** Data licence agreements and their amendments; marketplace standard licence templates; data catalogue metadata; warehouse lineage graphs; access control configurations; historical compliance reviews and their conclusions.
**Target:** A structured policy per dataset, and detected lineage paths that violate it.
**Evaluation metric:** Field-level extraction accuracy against attorney-reviewed agreements, weighted heavily toward the training-use and resale terms since those carry the largest exposure. For enforcement, recall on violating lineage paths in a seeded test — a missed violation is the failure that matters and a false positive costs an engineer a review.
**Scope:** Data licences are reasonably standardised in structure and highly variable in terms, which suits retrieval-augmented extraction with clause-level review. Most extracted terms map directly onto access controls and lineage checks the modern warehouse can already enforce, so the gap is translation rather than infrastructure. Retention and deletion obligations are the near-universal unmet term and are enforceable from an expiry date and a lineage graph with no modelling at all. 2 ML engineers plus data counsel, 4-5 months.
**Data availability:** Agreements sit in contract systems disconnected from the data platform, which is the integration obstacle. Lineage graphs are increasingly complete in modern warehouses and are the enabling asset.

---

## 4. Provenance Artefact Analysis and Chain Consistency Checking
#large-language-models #bert #hypothesis-testing #confidence-intervals #change-point-detection #evaluation-metrics #compliance #transfer-learning

**Problem statement:** Provenance review rests on a supplier's self-completed questionnaire, a privacy policy and contractual warranties, assessing a collection chain the reviewer cannot see past one link. Enforcement now reaches purchasers, litigation over training data has made the question acute, and approvals are point-in-time while the rules move constantly.

**ML task:** Extraction from provenance artefacts — privacy policies, terms of service, consent flow descriptions, supplier questionnaires — plus consistency checking across the declared chain and continuous monitoring of public signals
**Input data:** Supplier privacy policies and terms; consent flow documentation; completed provenance questionnaires; contractual warranties; named upstream sources and their own published policies; regulatory enforcement actions and litigation filings; historical reviews and their conclusions.
**Target:** Structured provenance attributes per supplier, and detected inconsistencies between a supplier's warranty and the disclosures of the sources it names.
**Evaluation metric:** Extraction accuracy on whether a policy discloses onward sale, covers the buyer's intended use, and names the relevant jurisdictions — the three determinations reviewers spend most of their time on. For consistency checking, precision on flagged inconsistencies as judged by counsel, since a false flag consumes expensive legal time.
**Scope:** This assists a legal judgement and must not appear to make one; the output is evidence assembly and contradiction surfacing, with the determination remaining with the reviewer. The chain consistency check is the genuinely novel piece — comparing what a supplier warrants against what its named sources publicly disclose is exactly what a reviewer tries to do by reading and rarely has time to complete. Continuous monitoring of enforcement actions and litigation against approved suppliers converts point-in-time approval into a standing position. 2 ML engineers plus privacy counsel, 5 months.
**Data availability:** Privacy policies and terms are public and machine readable in aggregate. Questionnaires and warranties are held by the marketplace or buyer. Consent flow evidence is the artefact that most often does not exist at all, which is itself the finding.
