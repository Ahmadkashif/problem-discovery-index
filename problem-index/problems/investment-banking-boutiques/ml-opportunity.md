# Machine Learning Opportunities — Investment Banking Boutiques

**Industry:** [[investment-banking-boutiques|Investment Banking Boutiques]]
**Derived from:** [[problems/investment-banking-boutiques/high-impact|High Impact]], [[problems/investment-banking-boutiques/low-impact-1|Low Impact 1]], [[problems/investment-banking-boutiques/low-impact-2|Low Impact 2]], [[problems/investment-banking-boutiques/worker-life-1|Worker Life 1]], [[problems/investment-banking-boutiques/worker-life-2|Worker Life 2]]

---

## 1. Buyer Propensity Ranking From the Firm's Process History
#tacit-knowledge-ml #gradient-boosting #survival-analysis #graph-theory #k-nearest-neighbors #causal-inference #evaluation-metrics #revenue-impact

**Problem statement:** A senior banker looks at a three-hundred-name buyer screen and knows which fifteen will actually bid — from years of watching sponsors and strategics behave in processes. The firm holds the behavioural record that produced that judgment, across every process it has run, and never uses it. Learn, for a new mandate, each candidate buyer's probability of reaching each stage of the sale funnel.

**ML task:** Multi-stage propensity estimation (ordinal or sequential binary classification, NDA → IOI → management meeting → LOI → final bid) with a time-to-event component for how fast buyers move, ranked per mandate
**Input data:** Historical buyer trackers from every sell-side and capital-raising process (stage reached, dates, indication ranges, final bids); data room engagement logs per bidder (documents opened, time spent, Q&A volume); mandate descriptors (sector, size, margins, growth, geography, ownership, process type); buyer attributes from PitchBook or Capital IQ (fund size and vintage, dry powder, portfolio companies and their hold periods, recent acquisitions); the sponsor–fund–portfolio-company graph.
**Target:** For each (mandate, buyer) pair, probability of reaching each funnel stage and, conditional on bidding, the bid's position relative to the clearing price.
**Evaluation metric:** Ranking quality on held-out mandates — recall of eventual final-round bidders within the top-k of the ranked list, for k equal to the number of buyers the firm typically contacts. Recall dominates precision here: missing the winning bidder costs the client real value, while an extra name costs an email. Report separately for strategic and financial buyers and for sectors with thin history.
**Scope:** Hard, and the difficulty is mostly not the model. *Data collection:* the expert's knowledge is encoded only indirectly, in a decade of per-deal spreadsheets with inconsistent buyer names, missing late-stage outcomes and no shared schema; entity resolution across sponsors, funds, portfolio companies and individual partners is the first several months of work. *Labelling:* realised behaviour is the only usable label, because MD tiers are inconsistent with themselves over time and across colleagues — but realised behaviour is censored by the MD's own choices (an uncontacted buyer never bids), so the training set is selection-biased toward the expert's prior; inverse-propensity weighting on contact decisions and deliberately contacting a small number of model-suggested names outside the MD's list are both needed to learn anything the expert did not already know. *Deployment:* a buyer list is drafted in an afternoon; the ranking must arrive faster, explain every name with the firm's own past interactions, and accept MD overrides as new labels, or it will be ignored. 1 data engineer and 1 ML engineer for 6–9 months, most of it on the ledger.
**Data availability:** Entirely internal and owned by the bank as its own work product, which is the point — no vendor can reconstruct private buyer behaviour in private processes. Volume is the constraint: a mid-market boutique running 30–60 processes a year with 100–200 buyers each accumulates tens of thousands of labelled pairs per decade, sufficient for gradient-boosted models with strong buyer-level features but thin for rare sectors. Client-confidential mandate details must be abstracted to descriptors before reuse.

---

## 2. Private-Target Peer Selection and Undisclosed Multiple Estimation
#word-embeddings #k-nearest-neighbors #transformers #linear-regression #gradient-boosting #confidence-intervals #feature-engineering #data-integration

**Problem statement:** For a private mid-market target, choose the public companies and past transactions an informed buyer would actually benchmark against, and estimate the multiples of comparable private transactions whose terms were never disclosed.

**ML task:** Similarity retrieval over business descriptions and financial profiles, plus regression with prediction intervals for undisclosed transaction multiples
**Input data:** Business descriptions from filings, websites and CIMs; segment revenue and margin data; terminal spreads; disclosed precedent multiples; the firm's own closed-deal multiples; private-market aggregates (PitchBook, GF Data); deal date and rate environment.
**Target:** A ranked peer set with a similarity rationale; an estimated EV/EBITDA range with an interval for each undisclosed precedent.
**Evaluation metric:** For peer selection, agreement with senior-banker-curated peer sets on held-out pitches (nDCG), audited by whether the selected peers' multiples explain the eventual transaction price better than industry-code peers. For multiple estimation, interval coverage on disclosed deals held out — a stated 80% interval must contain 80% of actuals — since the estimates feed a football field a board will rely on.
**Scope:** Retrieval is a quick win with embeddings and a firm-tuned reranker. Multiple estimation is genuinely uncertain and must be shown as a range with provenance, never as a point that could be mistaken for a disclosed figure. 1–2 ML engineers, 4 months.
**Data availability:** Public and licensed data is abundant; the firm's own deal multiples are the differentiator and carry confidentiality restrictions that limit external display.

---

## 3. Diligence Question Clustering, Answer Retrieval and CIM Consistency
#bert #large-language-models #word-embeddings #k-means-clustering #evaluation-metrics #workflow-orchestration #automation

**Problem statement:** Hundreds of diligence questions per bidder arrive through the data room. Cluster near-duplicates across bidders, match each to existing answers and documents, and flag draft answers that contradict figures in the CIM or management presentation.

**ML task:** Semantic clustering and retrieval over short questions; numeric claim extraction and cross-document contradiction detection
**Input data:** Data room Q&A logs from current and past processes; the CIM, management presentation and model; the data room index; prior answer library.
**Target:** Question clusters; suggested answers with source citations; contradiction flags with the conflicting passages.
**Evaluation metric:** Cluster purity judged by deal teams; answer-suggestion acceptance rate; and for contradiction detection, recall on seeded inconsistencies — a missed contradiction is far more costly than a false alarm the associate dismisses.
**Scope:** Mature techniques; the work is integration with data room exports and building the contradiction checker. 1 ML engineer, 3 months.
**Data availability:** Q&A logs are exportable from all major data rooms. The content is client-confidential and must stay inside the process it came from; cross-process reuse is limited to question patterns, not answers.

---

## 4. Automated Tie-Out Across Deck, CIM and Model
#large-language-models #transformers #object-detection #evaluation-metrics #feature-engineering #compliance #quick-win

**Problem statement:** Every number in a board book, fairness presentation or CIM must match its source in the model and financials. Extract each figure, resolve what it represents, link it to a source cell, and flag mismatches and stale values.

**ML task:** Table and chart number extraction from slides and PDFs; semantic labelling of each figure (metric, period, adjustment basis); entity matching to model cells
**Input data:** PowerPoint and PDF drafts including charts and footnotes; Excel models; audited financials and quality-of-earnings schedules; prior versions.
**Target:** For each figure, its resolved meaning, its source, and a match/mismatch/unresolved status.
**Evaluation metric:** Recall of seeded and historical errors is the primary metric — a tie-out tool that misses errors is worse than none, because it is trusted. Secondary: proportion of figures auto-resolved, which determines how much manual checking remains.
**Scope:** Extraction from native PowerPoint is tractable; charts and pasted images are harder. Semantic labelling of "adjusted" versus "reported" figures is the subtle part. 2 engineers, 4–5 months.
**Data availability:** Every past board book and its model are retained; historical errors caught in review are rarely logged and would need reconstruction from version history.

---

## 5. Mandate Conversion and Pitch Effort Allocation
#gradient-boosting #logistic-regression #survival-analysis #evaluation-metrics #feature-engineering #revenue-impact

**Problem statement:** A boutique pitches far more often than it wins, and allocates analyst effort to pitches by MD instinct. Estimate the probability that a pitch converts to a mandate within a horizon, and the expected fee, to allocate production effort.

**ML task:** Binary classification with a time-to-mandate survival component
**Input data:** CRM pitch records (DealCloud or Salesforce); prior relationship touchpoints; company ownership and sponsor hold period; competing banks known to be pitching; sector cycle indicators; outcome — mandate won, lost to a named competitor, or no transaction.
**Target:** Probability of mandate within 12 and 24 months; expected fee.
**Evaluation metric:** Calibration and Brier score, because the output is used for resource allocation, not ranking alone; AUC as secondary.
**Scope:** Modest model; CRM hygiene is the limiting factor. 1 analyst-engineer, 3 months.
**Data availability:** Internal CRM; outcomes for lost pitches are often unrecorded and must be backfilled from public deal announcements.
