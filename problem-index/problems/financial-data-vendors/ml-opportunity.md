# Machine Learning Opportunities — Financial Data Vendors

**Industry:** [[financial-data-vendors|Financial Data Vendors]]
**Derived from:** [[problems/financial-data-vendors/high-impact|High Impact]], [[problems/financial-data-vendors/low-impact-1|Low Impact 1]], [[problems/financial-data-vendors/low-impact-2|Low Impact 2]], [[problems/financial-data-vendors/worker-life-1|Worker Life 1]], [[problems/financial-data-vendors/worker-life-2|Worker Life 2]]

---

## 1. Line-Item Standardisation From Expert Collector Decisions
#tacit-knowledge-ml #transformers #large-language-models #gradient-boosting #k-nearest-neighbors #evaluation-metrics #confidence-intervals #revenue-impact

**Problem statement:** Learn how a vendor's best collection analysts map an issuer's as-reported line items, footnote disclosures and XBRL tags onto the standardised template, so that a new filing is pre-mapped the way a senior analyst would map it, with calibrated confidence and the precedent shown.

**ML task:** Multiclass classification of template position (including an explicit "ambiguous — escalate" class) conditioned on retrieved precedent, plus a binary "override the XBRL tag" classifier
**Input data:** As-reported line label and amount; the issuer-provided XBRL tag and its extension status; the surrounding statement structure; linked footnote text; the issuer's own mapping history across prior quarters; mappings of semantically similar items at peer issuers; house policy version in force.
**Target:** Standardised template field (and sign/scale normalisation) per line item; probability that the XBRL tag should be overridden; abstention when confidence is below a policy-set threshold.
**Evaluation metric:** Accuracy at the auto-accept confidence threshold — what fraction of fields can be skipped by the analyst with an error rate no worse than current sample QA — is the headline. Report separately on items that seniors historically disagreed on, where the target is high abstention rather than accuracy. Asymmetric cost: an auto-accepted wrong mapping propagates to every client's screen and costs far more than an unnecessary escalation, so precision on auto-accept dominates recall.
**Scope:** The hard part is the tacit-knowledge capture, not the model. Data collection: the keying tool must log the override path, the passage being read and the alternative considered, which means changing a production tool during earnings season; budget a quarter of instrumentation before any training. Labelling: experts disagree with each other and with their own past decisions, and policy changes mid-history, so historical mappings must be policy-version stamped and a sample double-annotated and adjudicated to measure the ceiling before claiming a model beats it. Deployment: it must be faster than the expert — if the analyst has to re-verify a proposal from scratch it will be turned off in week two — so every proposal ships with its evidence and the routine majority must be skippable. 3 ML engineers, 1 data engineer and part-time senior analysts as adjudicators, 9–12 months.
**Data availability:** Exceptionally rich and entirely internal: decades of final mappings for tens of thousands of issuers, plus resolved client error tickets as adjudicated corrections. What does not exist is the decision path, which instrumentation starts producing immediately.

---

## 2. Consensus Hygiene: Stale and Basis-Mismatched Estimate Detection
#gradient-boosting #change-point-detection #bayesian-inference #evaluation-metrics #feature-engineering #descriptive-statistics #revenue-impact

**Problem statement:** A consensus estimate is a mean or median over contributed broker estimates, some of which are stale (not updated after guidance changed) or on a different basis (GAAP versus adjusted, including or excluding an acquisition). Estimates specialists exclude them by judgement; the model should flag them before the consensus is published.

**ML task:** Binary classification of each contributed estimate as stale or basis-inconsistent, with change-point detection on the company's guidance and peer-estimate trajectory to define "stale"
**Input data:** Contributed estimate history per broker, field and period; revision timestamps; company guidance events and earnings dates; other contributors' revisions; broker basis declarations where present; historical specialist exclusion decisions and reasons; actual reported values.
**Target:** Exclude/include recommendation with reason code (stale, basis, outlier, likely keying error).
**Evaluation metric:** Agreement with specialist exclusions on held-out periods, and — more objectively — improvement in consensus error against the eventually reported actual on the reported basis. A wrongly excluded valid outlier hides genuine dispersion, so report the dispersion impact alongside accuracy.
**Scope:** Directly supervised from years of specialist exclusion decisions; the "actual on the same basis" target requires careful alignment but exists in the vendor's own database. 2 ML engineers, 5 months.
**Data availability:** Internal and excellent. Exclusion reasons are sometimes recorded as codes without narrative, which caps the reason-classification part.

---

## 3. Finance-Domain Speech Recognition With Speaker Resolution
#transformers #seq2seq #transfer-learning #large-language-models #bert #evaluation-metrics #automation

**Problem statement:** Adapt speech recognition and diarisation to earnings and investor calls so the live draft needs minimal editing, every speaker resolves to a named person and firm, and guidance statements are tagged.

**ML task:** Domain-adapted sequence-to-sequence speech recognition with contextual biasing; speaker resolution as entity linking against a participant directory; sentence classification for guidance and KPI statements
**Input data:** Call audio; years of machine-draft/edited-final transcript pairs; issuer filings and prior transcripts for vocabulary; operator introductions; the vendor's directory of covering analysts and corporate officers.
**Target:** Corrected transcript text; speaker identity per turn; spans labelled as forward guidance, KPI disclosure or Q&A.
**Evaluation metric:** Entity and number error rate rather than overall word error rate, since a wrong ticker or figure matters and a dropped filler word does not; speaker attribution accuracy; editor minutes per call hour.
**Scope:** Fine-tuning an open recogniser on the edited archive is a known path; contextual biasing from issuer vocabulary is the high-value step. 2 ML engineers, 4–6 months.
**Data availability:** The edited-transcript archive is a large parallel corpus that every transcript vendor already owns.

---

## 4. Client Discrepancy Triage and Data Error Detection
#bert #large-language-models #autoencoders #k-nearest-neighbors #evaluation-metrics #data-integration #worker-facing

**Problem statement:** Classify incoming client discrepancy tickets by cause (methodology difference, restatement, genuine collection error, client misunderstanding) and, upstream, detect the values likely to generate such tickets before clients find them.

**ML task:** Text classification of tickets with retrieval of resolved precedents; unsupervised anomaly scoring of newly collected values against the issuer's own history and peers
**Input data:** Ticket text and the field and issuer referenced; resolved ticket history with root-cause codes; value lineage; issuer time series; peer distributions; competitor values where the client supplied them.
**Target:** Root-cause class with retrieved precedent; per-value anomaly score routed to collection QA.
**Evaluation metric:** For triage, root-cause accuracy and reduction in specialist time-to-answer. For detection, the fraction of later client-reported errors that were flagged at collection time, at a review volume QA can absorb — recall at fixed alert budget.
**Scope:** Triage is quick to build on resolved tickets. Upstream detection is the larger prize, because every error caught before release is a ticket that never happens and a client that never discovers it. 2 ML engineers, 5 months.
**Data availability:** Resolved tickets with root causes exist at every vendor; their quality varies, and many lack the structured cause.

---

## 5. Private-Markets Document Extraction and Entity Resolution
#large-language-models #transformers #graph-neural-networks #graph-theory #evaluation-metrics #data-integration #automation

**Problem statement:** Private-markets data arrives as unstructured documents — public pension board packets and FOIA responses with fund cash flows, press releases announcing rounds, Form D filings, GP quarterly letters — and must be extracted into structured records and resolved onto the right fund, firm and company entities.

**ML task:** Table and field extraction from heterogeneous PDFs; entity resolution over a firm–fund–company–investor graph
**Input data:** Pension fund reports and FOIA responses; Form D filings; press releases and news; GP-submitted surveys; the vendor's existing entity graph with aliases and history.
**Target:** Structured commitment, contribution, distribution and NAV records; deal records (date, amount, investors, valuation where disclosed); resolved entity IDs with merge/split recommendations.
**Evaluation metric:** Field-level precision at the auto-accept threshold, since a wrong cash flow corrupts a fund's IRR and every benchmark it feeds; entity-resolution pairwise F1 with particular attention to false merges, which are harder to unwind than false splits.
**Scope:** Extraction is commodity with current models once tables are reliably parsed; entity resolution across fund vehicles, feeder funds and renamed GPs is the domain work and depends on the vendor's graph. 2–3 ML engineers, 6 months.
**Data availability:** Researchers' manual extraction history provides labels; the documents are public or contributed.
