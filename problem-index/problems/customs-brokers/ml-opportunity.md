# Machine Learning Opportunities — Customs Brokers

**Industry:** [[customs-brokers|Customs Brokers]]
**Derived from:** [[problems/customs-brokers/high-impact|High Impact]], [[problems/customs-brokers/low-impact-1|Low Impact 1]], [[problems/customs-brokers/low-impact-2|Low Impact 2]], [[problems/customs-brokers/worker-life-1|Worker Life 1]], [[problems/customs-brokers/worker-life-2|Worker Life 2]]

---

## 1. HTS Code Classification from Product Descriptions
#transformers #bert #transfer-learning #attention-mechanisms #word-embeddings #loss-functions #backpropagation #evaluation-metrics #compliance #revenue-impact

**Problem statement:** Predict the most likely HTS classification codes for imported goods from product descriptions, reducing classification research time and misclassification risk.

**ML task:** Hierarchical text classification — HTS chapter → heading → subheading → 10-digit code from product description text
**Input data:** CBP CROSS database (60,000+ binding rulings with product descriptions and assigned HTS codes); broker's historical entry data with product descriptions and filed HTS codes; HTS schedule section/chapter notes as background context
**Target:** Top-3 HTS candidates with confidence scores; GRI analysis rationale for top candidate; relevant prior binding rulings; applicable duty rates and tariff programs per candidate
**Evaluation metric:** Top-1 accuracy on held-out CROSS rulings; agreement rate with broker's expert classification on novel products; misclassification rate reduction vs. broker-only classification
**Scope:** CBP's CROSS database is the primary training corpus — publicly available with 60,000+ labeled product-to-HTS examples. Fine-tuning a BERT or LegalBERT model on CROSS ruling text: 8-12 week project. The hierarchical classification structure (chapter → heading → subheading) benefits from a cascaded classification approach that narrows the candidate set at each level.
**Data availability:** CROSS database is publicly available from CBP. The broker's own historical entry data provides additional training signal aligned with their client portfolio. HTS schedule text is public domain.

---

## 2. Commercial Invoice Data Extraction
#large-language-models #attention-mechanisms #transformers #transfer-learning #word-embeddings #feature-engineering #evaluation-metrics #quick-win

**Problem statement:** Extract customs-required data fields from commercial invoice documents in multiple formats and languages for entry preparation data population.

**ML task:** Named entity recognition and structured extraction — customs-specific fields (shipper, consignee, country of origin, HTS/tariff code suggestion, description, quantity, unit, invoice value, currency) from unstructured invoice text
**Input data:** Commercial invoice documents (PDF, Excel, image scan) with manually extracted field values as training labels. Multi-language examples (Chinese, Spanish, German, Japanese supplier invoices are common).
**Target:** Structured extraction of all customs-required entry fields with confidence score per field; flagged low-confidence fields for human review; multi-document reconciliation output
**Evaluation metric:** Extraction accuracy per field on held-out invoice set; coverage (% of required fields extractable with > 90% confidence); review time reduction vs. manual data entry
**Scope:** Quick win — LLM-based document extraction with customs-specific prompting achieves strong baseline performance on standard commercial invoices. Fine-tuning on a labeled invoice corpus improves accuracy for non-standard formats. 4-6 week project.
**Data availability:** The broker's historical entry files contain the commercial invoices and the manually-entered field values that provide training labels. Any broker with 2+ years of digital entry records has a sufficient training set.

---

## 3. Section 301 / 232 Exclusion Matching
#transformers #word-embeddings #attention-mechanisms #transfer-learning #norms-and-inner-products #evaluation-metrics #compliance #revenue-impact

**Problem statement:** Match newly-published tariff exclusions against a broker's client import portfolio by semantic similarity between exclusion descriptions and client product descriptions.

**ML task:** Semantic similarity — score each new exclusion's product description against client import records to identify matches; threshold matching at exclusion applicability level
**Input data:** USTR exclusion product descriptions; client import records with product descriptions and HTS codes; historical exclusion-to-product matches confirmed by brokers (positive labels); confirmed non-matches (negative labels)
**Target:** Match score per exclusion-client product pair; duty savings estimate for matched pairs; draft exclusion application for high-confidence matches
**Evaluation metric:** Recall on exclusions confirmed applicable to client products; precision at 0.7 match threshold (reducing false positive applications); duty savings identified per client per year
**Scope:** Semantic similarity between regulatory language and commercial product descriptions is a good fit for transformer-based embedding models. USTR exclusion descriptions are public; client product descriptions are from entry records. 4-6 week project. The duty savings calculation layer is straightforward once matches are identified.
**Data availability:** USTR exclusion database is public. Client import records are in the entry management system. Confirmed applicability examples from prior exclusion applications provide training labels.

---

## 4. Entry Risk Scoring for CBP Examination Probability
#gradient-boosting #logistic-regression #feature-engineering #cross-validation #evaluation-metrics #conditional-probability-and-bayes-theorem #compliance

**Problem statement:** Score each import entry for CBP examination probability before filing, enabling the broker to advise clients on examination risk for time-sensitive shipments.

**ML task:** Binary classification (CBP exam requested: yes/no) from entry features
**Input data:** Historical entry records with examination outcomes (exam requested vs. released). Features: commodity chapter, country of origin, importer of record (new vs. established), value, ADD/CVD subject status, prior examination history for this importer, ports known for higher examination rates.
**Target:** Examination probability per entry; risk factors driving the score; estimated delay impact if examined
**Evaluation metric:** AUC on examination prediction; broker-reported usefulness for client timeline communication; precision at 0.7 probability threshold
**Scope:** Any broker with 2+ years of entry examination records has training data. Gradient boosting on 8-10 entry features: 3-4 week project. Entry exam records are in ACE (if the broker pulls them consistently) or in their entry management system if flagged.
**Data availability:** ACE examination status is visible in the broker's portal. The broker's entry management system logs examination requests. Country-commodity risk profiles are implicit in the historical data.

---

## 5. Trade Program Eligibility Analysis
#large-language-models #attention-mechanisms #transformers #feature-engineering #descriptive-statistics #revenue-impact #quick-win

**Problem statement:** Identify which of a client's current imports qualify for preferential duty programs (USMCA, CAFTA, GSP, etc.) that the client is not currently claiming, to surface duty reduction opportunities.

**ML task:** Rule-based classification enriched with LLM reasoning — trade program eligibility determination from HTS code + country of origin + country-of-origin rule
**Input data:** Client entry records (HTS code, country of origin per entry); USMCA/CAFTA tariff schedules and ROO (rules of origin) requirements; GSP beneficiary country and product lists; Section 301 tariff applicability by HTS/country combination
**Target:** Eligibility flag per entry line per trade program; estimated duty savings per eligible unclaimed program; summary of documents required to claim the program (certificate of origin, etc.)
**Evaluation metric:** Coverage of trade program eligibility rules in the model; accuracy of eligibility flags vs. CBP binding rulings; duty savings identified per client per year
**Scope:** Quick win for the rules-based eligibility determination — trade program rules are structured enough for rule-based classification augmented by LLM for ambiguous ROO analysis. 3-4 week project. The output feeds the quarterly client report.
**Data availability:** USMCA/CAFTA/GSP eligibility rules are public. Client entry data is in the entry management system. The analysis joins public trade data to the client's entry records.
