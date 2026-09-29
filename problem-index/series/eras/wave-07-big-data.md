# Wave 7 — Big Data (2006–2015)

**Trigger:** Google's GFS paper (SOSP, Oct 2003) and MapReduce paper (OSDI, Dec 2004); Hadoop split from Apache Nutch Jan 28 2006, v0.1 April 2006; Yahoo's TeraSort record May 2008
**What went to ~zero:** the cost of **keeping everything**
**Failure class produced:** the declined join, now with an alibi — "the data is in the lake"

## What Was True The Day Before

Storage was expensive enough that you decided in advance what was worth keeping, and the deciding was done by designing a schema. A schema is a claim about which questions will be asked. Everything outside it was discarded at the point of collection — not archived, *discarded* — so the questions nobody anticipated became permanently unanswerable.

Analytics meant an MPP warehouse, Teradata-class, expensive, and structured-only.

## The Trigger

Google published how it stored and processed the web on commodity machines. Doug Cutting and Mike Cafarella built the same architecture for Nutch from the papers — **architectural inspiration, not code reuse; Google never released Hadoop or collaborated on it.** Yahoo hired Cutting in 2006 and funded it into production.

The proof point was public and specific: **May 2008, a 910-node Yahoo cluster sorted 1TB in 209 seconds**, beating the prior 297-second record and marking the first time an open-source Java system took it.

## What Became Possible

Horizontal scale-out over unstructured and semi-structured data on commodity hardware, without committing to a schema first. You could keep everything now and decide what it meant later. **Schema-on-read** was the slogan and the whole proposition.

## The Competitive Fight

Three vendors fought to own the distribution: **Cloudera** (2008), **MapR** (2009), **Hortonworks** (June 2011, spun out of Yahoo with $23M, IPO 2014 as the first Hadoop pure-play).

All three lost, and the way they lost is the lesson. **Cloudera and Hortonworks merged — announced Oct 3 2018, completed Jan 3 2019, roughly $1.2B.** MapR sold its assets to HPE in 2019 after running low on cash.

They lost to the cloud data warehouse. **Snowflake, founded July 23 2012**, separated storage from compute so each scaled and billed independently — an answer to Hadoop's fixed-cluster contention that only became possible once cheap cloud object storage matured. BigQuery launched publicly Nov 2011; Redshift was announced at re:Invent 2012 and reached GA Feb 2013.

The on-prem distributions were selling operational complexity as a product at the exact moment managed services were removing it. **Hadoop's difficulty was its business model, and the difficulty was the thing that got commoditised.**

## What It Broke

**The data lake became the data swamp.** James Dixon coined "data lake" in a blog post on Oct 14 2010, contrasting it with curated data marts. By 2014 Gartner was flagging the failure mode explicitly: ingest without metadata or governance and schema-on-read defers validation to read time, so provenance, quality and semantics of dumped raw data go undocumented. The lake becomes unsearchable and untrustworthy.

The deeper damage is rhetorical, and it is why this wave matters to the series. "Keep everything, decide later" gave every organisation a **permanent excuse not to decide.** The data being *somewhere* became a substitute for the measurement being *made*. When the vault records an industry that holds complete data and never computes the number that matters, this is frequently the alibi in play.

*(Myth: the widely-repeated "85% of big data projects fail" has no traceable primary study. It is an analyst soundbite — Gartner's Nick Heudecker characterising an earlier, also-uncited 60% figure as conservative. Cite as a widely repeated industry claim or not at all.)*

## Children in This Vault

**Primary:**
- [[industries/customer-data-platforms|Customer Data Platforms]]
- [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
- [[industries/mlops-platforms|MLOps Platforms]]
- [[industries/data-platform-integrators|Data Platform Integrators]]
- [[industries/payment-fraud-vendors|Payment Fraud Vendors]]
- [[industries/game-analytics-vendors|Game Analytics Vendors]]
- [[industries/player-research-firms|Player Research Firms]]
- [[industries/behavioral-health-clinics|Behavioral Health Clinics]]
- [[industries/home-health-agencies|Home Health Agencies]]
- [[industries/urgent-care|Urgent Care Centers]]
- [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
- [[industries/data-analytics-consultants|Data Analytics Consultants]]
- [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
- [[industries/healthcare-practice-software|Healthcare Practice Software]]

**Secondary:**
- [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]]
- [[industries/crop-farming|Crop Farming]]
- [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
- [[industries/ai-red-teaming-firms|AI Red Teaming Firms]]
- [[industries/data-labeling-services|Data Labeling Services]]
- [[industries/synthetic-data-providers|Synthetic Data Providers]]
- [[industries/vector-search-vendors|Vector Search Vendors]]
- [[industries/ci-cd-platforms|CI/CD Platforms]]
- [[industries/cloud-cost-management|Cloud Cost Management]]
- [[industries/internal-developer-platforms|Internal Developer Platforms]]
- [[industries/observability-vendors|Observability Vendors]]
- [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
- [[industries/oil-gas-field-services|Oil & Gas Field Services]]
- [[industries/collections-agencies|Collections Agencies]]
- [[industries/identity-verification-vendors|Identity Verification Vendors]]
- [[industries/lending-marketplaces|Lending Marketplaces]]
- [[industries/robo-advisors|Robo-Advisors]]
- [[industries/game-liveops-services|Game LiveOps Services]]
- [[industries/dental-practices|Dental Practices]]
- [[industries/medical-billing|Medical Billing]]
- [[industries/pharmacy-independents|Independent Pharmacies]]
- [[industries/physical-therapy|Physical Therapy]]
- [[industries/public-adjusters|Public Adjusters]]
- [[industries/public-defenders|Public Defenders]]
- [[industries/talent-assessment-platforms|Talent Assessment Platforms]]
- [[industries/environmental-consultants|Environmental Consultants]]
- [[industries/commercial-real-estate|Commercial Real Estate]]
- [[industries/real-estate-appraisers|Real Estate Appraisers]]
- [[industries/cloud-infrastructure-consultants|Cloud Infrastructure Consultants]]
- [[industries/cybersecurity-mssp|Cybersecurity MSSPs]]
- [[industries/non-emergency-medical-transport|Non-Emergency Medical Transport]]
- [[industries/digital-forensics-firms|Digital Forensics Firms]]
- [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
- [[industries/insurtech-platforms|Insurtech Platforms]]

**Origins:** [[origins/hospital-systems/profile|Hospital Systems]] *(statutory trigger — HITECH, Feb 2009)*

**Sources:** Ghemawat, Gobioff & Leung, *The Google File System*, SOSP '03; Dean & Ghemawat, *MapReduce*, OSDI '04; hadoop.apache.org and sortbenchmark.org (Yahoo TeraSort, May 2008); Cloudera press release and CNBC/TechCrunch coverage (Hortonworks merger); jamesdixon.wordpress.com (data lake, Oct 14 2010); Gartner (data swamp critique, 2014); Snowflake corporate history.
