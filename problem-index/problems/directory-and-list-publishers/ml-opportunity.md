# Machine Learning Opportunities — Directory & List Publishers

**Industry:** [[directory-and-list-publishers|Directory & List Publishers]]
**Derived from:** [[problems/directory-and-list-publishers/high-impact|High Impact]], [[problems/directory-and-list-publishers/low-impact-1|Low Impact 1]], [[problems/directory-and-list-publishers/low-impact-2|Low Impact 2]], [[problems/directory-and-list-publishers/worker-life-1|Worker Life 1]], [[problems/directory-and-list-publishers/worker-life-2|Worker Life 2]]

---

## 1. Learning the Researcher's Verdict on a Business Record
#tacit-knowledge-ml #gradient-boosting #survival-analysis #large-language-models #evaluation-metrics #feature-engineering #worker-facing #revenue-impact

**Problem statement:** Experienced tele-researchers and compilation analysts read conflicting signals — a ring-out at a retail number, an answering-service greeting, a re-registered LLC, a stale website — and "know" whether a business is open, moved, closed or a lead-generation front. The ML problem is to learn that verdict from their historical call outcomes and notes, joined to what later proved true, and use it to decide which records need a call and what an ambiguous call meant.

**ML task:** Per-field calibrated probability that each assertion (exists, at this address, this phone, this primary category) is true now; survival model of time to change by segment; and a value-of-call estimate — the probability that calling would change what is published
**Input data:** Source assertions per field with source and date (carrier listings, state filings and annual-report status, web crawl snapshots, review recency); call history with outcome codes, researcher, time of day and attempt count; short researcher notes and, where recorded, call audio transcribed; customer bounce reports, credit claims and undeliverable returns; later corrections from licensees.
**Target:** Field status at the next authoritative observation (verified call, registry change, licensee correction, confirmed bounce); time until the field changed; whether a call changed the published value.
**Evaluation metric:** Brier score and calibration by segment (industry, size band, region), measured out of time on records verified after the training cut-off. Operationally, call yield — the share of calls that change the published record — against the current prioritisation as baseline. Recall on closures and fronts matters more than precision: publishing a dead or fake business costs credits and trust, while an unnecessary call costs under a minute.
**Scope:** The data collection challenge comes first: the researcher's reasoning has to be captured inside a sub-minute, quota-measured call, so capture must cost seconds — a structured outcome drafted from live transcription and confirmed with one key, plus a free-text flag for patterns. The labelling challenge is that truth is itself a judgement: two researchers disagree on the same record, the same researcher drifts over time, and outcome labels arrive months later and are biased towards complaints, so a sample of records must be double-called to estimate inter- and intra-rater agreement, which sets the ceiling for the model. The deployment challenge is speed: scores must be in the queue before the dialer connects and explanations must be readable in two seconds, or callers ignore them. 2 ML engineers, 1 data engineer and a tele-research operations lead, 6–9 months, with value first appearing as call triage before any record is published without a call.
**Data availability:** Large compilers hold years of call outcomes and source histories; Data Axle alone reports ~25M calls a year. Reasons are thin (status codes), audio is often unrecorded, and outcome signals sit with customers and licensees, so building the joined ledger is most of the work.

---

## 2. Modelled Employee Size and Sales Volume for Private Businesses
#bayesian-inference #gradient-boosting #linear-regression #confidence-intervals #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** Most businesses in a compiled file are private and never report headcount or revenue, yet employee band and sales volume are among the most-used selects. Estimate both with honest intervals, so that the band a record is sold under is right more often and buyers can see how sure the compiler is.

**ML task:** Hierarchical regression with prediction intervals (quantile or Bayesian), producing a point estimate, an interval and a probability for each size band
**Input data:** Industry code, location type (storefront, office, residential), building and site attributes, years in business, number of locations, web and job-posting activity, review counts, phone-verified headcount where callers asked, public-company and government-contractor disclosures, and public ground-truth samples such as the jobs field in SBA's PPP loan files (recalled).
**Target:** Employee count and annual sales volume; band membership.
**Evaluation metric:** Band accuracy and interval coverage on held-out ground truth, reported by industry and size, because buyers select by band. Over-estimation is the costlier error: it moves sole proprietors into lists sold as ten-plus-employee firms and generates the most credit claims.
**Scope:** 2 data scientists, 4–5 months. Ground truth is scarce and biased towards larger and public firms, so calibration on small firms needs deliberate phone sampling.
**Data availability:** Features are in the compiled file; ground truth must be assembled from public samples and caller-collected headcounts.

---

## 3. Business Entity Resolution Across Sources
#k-nearest-neighbors #word-embeddings #logistic-regression #graph-theory #evaluation-metrics #data-integration

**Problem statement:** Thousands of sources describe the same business under different names, addresses and numbers. Decide which source records describe the same establishment, and keep distinct the location, the legal entity and the brand.

**ML task:** Candidate blocking with embedding nearest neighbours, pairwise match classification, and graph clustering into establishment and entity clusters with merge and split decisions over time
**Input data:** Source records with names, addresses, phones, websites, registry identifiers and dates; historical merge and split decisions by analysts; known corporate linkages.
**Target:** Match / non-match per pair; cluster membership; establishment-versus-entity link.
**Evaluation metric:** Pairwise precision and recall plus cluster-level B-cubed F1 on an analyst-labelled sample. Report false merges and false splits separately: a false merge deletes a real business from the count, a false split sells a duplicate.
**Scope:** 2 ML engineers, 4–6 months to replace rule-based matching in one segment. The hard tail is franchises, multi-tenant buildings and home-based businesses sharing residential addresses.
**Data availability:** Compilers hold years of analyst merge decisions, which are usable labels once extracted from change logs.

---

## 4. Proprietary Heading and Industry Classification
#bert #transformers #large-language-models #transfer-learning #evaluation-metrics #automation

**Problem statement:** Assign every record a stable primary code and secondary codes in the compiler's own SIC-extension and heading taxonomy, with exclusions buyers rely on and evidence attached.

**ML task:** Multi-label text classification with a designated primary label, fine-tuned from a pretrained language model on the compiler's labelled records, with a change gate that only reclassifies on new evidence
**Input data:** Business name, carrier advertising classification, website text, filings, review categories, prior codes and analyst corrections.
**Target:** Primary code; set of secondary codes; mapped NAICS.
**Evaluation metric:** Primary-code accuracy and multi-label F1 on an analyst-audited sample, with churn — codes changed without new evidence — as a hard constraint, and count deltas on the top repeat orders reviewed before each release.
**Scope:** 1 ML engineer and 1 taxonomy analyst, 3–4 months; a quick win because labels already exist in the file.
**Data availability:** Tens of millions of coded records exist, but historic codes contain the very errors being fixed, so a clean audited sample is needed for evaluation.

---

## 5. Detecting Lead-Generation Fronts and Fake Listings
#graph-neural-networks #dbscan #gradient-boosting #graph-theory #evaluation-metrics #compliance

**Problem statement:** In locksmith, towing, garage-door, moving and similar categories, networks of listings share call-forwarding numbers, virtual addresses and templated websites while posing as local businesses. Detect them before they are published and sold.

**ML task:** Graph construction over listings (shared phones, addresses, domains, registrants, text templates), density clustering to find suspicious groups, and node classification of listings as genuine, front or unknown
**Input data:** Phone carrier and line-type data, address type (virtual office, mailbox, residence), domain registration and hosting, website text similarity, review patterns, researcher flags and complaint history.
**Target:** Front / genuine label per listing; cluster-level network flag.
**Evaluation metric:** Precision at the volume analysts can review per week, and recall on a set of known networks; a false accusation of a genuine small business is the costlier error.
**Scope:** 1 ML engineer and 1 analyst, 3–4 months for the highest-risk categories.
**Data availability:** Researcher flags and complaints provide seed labels; graph features come from data the compiler already holds or can license.
