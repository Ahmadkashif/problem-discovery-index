# Machine Learning Opportunities — CRM Platforms

**Industry:** [[crm-platforms|CRM Platforms]]
**Derived from:** [[problems/crm-platforms/high-impact|High Impact]], [[problems/crm-platforms/low-impact-1|Low Impact 1]], [[problems/crm-platforms/low-impact-2|Low Impact 2]], [[problems/crm-platforms/worker-life-1|Worker Life 1]], [[problems/crm-platforms/worker-life-2|Worker Life 2]]

---

## 1. Behavioural Deal Outcome and Timing Forecasting
#gradient-boosting #survival-analysis #logistic-regression #time-series-forecasting #feature-engineering #cross-validation #confidence-intervals #evaluation-metrics #revenue-impact

**Problem statement:** CRM forecasts are computed from stage and close date, two fields the representative controls and is incentivised to distort. The platform simultaneously carries unfalsifiable behavioural signal — buying-committee breadth, response latency, meeting cadence, champion engagement — through its own email and calendar integrations, and does not use it.

**ML task:** Joint classification of win or loss and survival modelling of time to close, with self-reported stage treated as a weak feature rather than as the specification
**Input data:** Email and calendar activity per opportunity (unique contacts engaged and its trajectory, response latency, meeting frequency and postponements, seniority of engaged contacts); call transcripts and their topics; document sends and opens; opportunity attributes (segment, product, source, amount); representative and team; historical won and lost outcomes with full activity history.
**Target:** Closed-won or closed-lost, and the actual close date.
**Evaluation metric:** Quarter-level aggregate calibration is what determines adoption — a leader cares whether the team's quarter number is right, not whether individual deals were ranked well. Report interval coverage at team-quarter granularity, and separately measure slip detection, since slipping deals rather than lost deals are what break a forecast. Compare against the manager call-down as the baseline, which is the honest comparison and one nobody makes.
**Scope:** Small samples at the level of interest are the core difficulty: a team-quarter may contain two hundred deals, and aggregate accuracy across a large customer base is easy and irrelevant. Hierarchical pooling across the vendor's customer base with per-customer calibration is the workable structure. Activity capture consent and the surveillance question must be settled explicitly with customers before any of this ships. 3-4 ML engineers plus a revenue operations lead, 6-9 months.
**Data availability:** Outcomes are complete and clean. Activity capture is the constraint — email and calendar integration adoption is inconsistent, and coverage is worst at exactly the enterprises where the forecast matters most.

---

## 2. Continuous Account Entity Resolution with Asymmetric Merge Cost
#bert #word-embeddings #graph-neural-networks #dbscan #k-nearest-neighbors #feature-engineering #evaluation-metrics #data-integration

**Problem statement:** The same customer exists in the CRM four times under different spellings, subsidiaries are entered as independent accounts, and acquisitions are never reflected. Enrichment appends firmographics without fixing relationships, and deduplication runs as a periodic clean-up with thresholds set as though the two error types cost the same.

**ML task:** Entity resolution over account and contact records with an explicit asymmetric loss, plus graph inference of the commercial hierarchy from transaction and engagement patterns
**Input data:** Account and contact records with names, domains, addresses and identifiers; opportunity and transaction history; email domains observed in engagement; external hierarchy data from enrichment providers; historical confirmed merges and merge reversals.
**Target:** Canonical account identity per record, and the commercial parent-child relationships that reflect how the customer actually buys.
**Evaluation metric:** Precision on merges weighted far above recall, since a false merge destroys history and is very hard to undo while a missed duplicate is untidy. Report the merge reversal rate as the primary operational metric — it is directly observable and is what customers actually complain about. For hierarchy, agreement with the customer's own revenue reporting.
**Scope:** The commercial hierarchy is a different object from the legal hierarchy that enrichment providers sell, and inferring it from who signs, who pays and who engages is the genuinely proprietary piece. Contact departure prediction — from tenure, role, engagement trend and account hiring activity — is a small, separable model with immediate value. 2-3 ML engineers, 5 months.
**Data availability:** Records are abundant and messy, which is the ideal shape. Confirmed merges exist in platform audit logs and are rarely retained as a labelled set.

---

## 3. Activity-to-Record Generation
#large-language-models #transformers #bert #word-embeddings #evaluation-metrics #transfer-learning #automation #worker-facing

**Problem statement:** Representatives spend several hours a week transcribing into the CRM events that were already captured elsewhere — calls on recorded lines, emails in the mail system, meetings on the calendar. The record is written late, from memory, immediately before a pipeline review, which is exactly why it is unreliable.

**ML task:** Summarisation and structured extraction from call transcripts and email threads into CRM objects — activity logs, contacts, next steps, and proposed stage movement with supporting evidence
**Input data:** Call recordings and transcripts; email threads with participants; calendar events and attendees; document send and open events; the CRM schema and required fields; historical representative-authored records as style and content references.
**Target:** The record the representative ultimately confirms, with their edits as the correction signal.
**Evaluation metric:** Proportion of generated fields accepted unedited, by field type. For stage movement, agreement with the representative's confirmed stage and — more informatively — whether model-proposed stages predict outcomes better than representative-asserted ones, which is directly testable and is the real argument for the feature.
**Scope:** The design constraint is that this must return something to the representative or it becomes another surveillance layer they route around. Pairing generation with retrieval — what changed at this account, who has gone quiet, what comparable deals needed next — is what makes it adopted rather than resented. Recording consent varies by jurisdiction and must be handled per-region. 2-3 ML engineers, 5-6 months.
**Data availability:** Transcripts, email and calendar data are abundant where integrations are enabled. Historical records paired to the conversations that produced them exist only where activity capture was already on, so the training set skews toward more instrumented customers.

---

## 4. Assignment Policy Evaluation and Territory Opportunity Estimation
#gradient-boosting #logistic-regression #causal-inference #optimization-fundamentals #k-means-clustering #confidence-intervals #evaluation-metrics

**Problem statement:** Routing trees accumulate hundreds of branches encoding compensation politics, and nobody measures whether the assignment policy produces better outcomes than an alternative. Territory design is an annual argument settled with a spreadsheet, with no estimate of where the revenue actually is.

**ML task:** Conversion prediction conditional on assignment, used both for routing and for opportunity estimation; plus a constrained optimisation for territory balance
**Input data:** Historical leads and accounts with assigned representative, lead attributes, firmographics, source and outcome; representative attributes and historical conversion by segment; territory definitions over time; quota attainment history; account-level revenue potential proxies.
**Target:** Conversion and realised revenue per assignment; and for territories, expected opportunity per account.
**Evaluation metric:** For routing, a policy comparison against the current rules using the natural variation that exists — assignment is not random, so causal care is required and any claimed lift should be validated by a live randomised holdout before it is believed. For territories, quota attainment dispersion across representatives, which is the fairness metric the annual argument is really about.
**Scope:** The politics are the deployment risk, not the modelling. Framing must be characteristic-to-outcome matching rather than representative ranking, or the sales organisation rejects it regardless of accuracy. A small randomised routing holdout is cheap, is the only way to measure the policy honestly, and no company runs one. 2 ML engineers plus revenue operations, 4-5 months.
**Data availability:** Complete within the platform. The missing ingredient is variation — routing rules are deterministic, so counterfactual assignment is unobserved and must be created deliberately.
