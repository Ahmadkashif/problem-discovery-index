# Machine Learning Opportunities — Open Source Commercial Vendors

**Industry:** [[open-source-commercial-vendors|Open Source Commercial Vendors]]
**Derived from:** [[problems/open-source-commercial-vendors/high-impact|High Impact]], [[problems/open-source-commercial-vendors/low-impact-1|Low Impact 1]], [[problems/open-source-commercial-vendors/low-impact-2|Low Impact 2]], [[problems/open-source-commercial-vendors/worker-life-1|Worker Life 1]], [[problems/open-source-commercial-vendors/worker-life-2|Worker Life 2]]

---

## 1. Adoption Reconstruction from Public Signal
#bert #word-embeddings #graph-neural-networks #gradient-boosting #k-means-clustering #confidence-intervals #feature-engineering #evaluation-metrics

**Problem statement:** Open-source vendors cannot enumerate their users, and the largest are frequently the quietest. Downloads conflate build caches with production clusters, telemetry is contentious and disabled by exactly the enterprises that matter, and every commercial decision runs on inference from bad numbers.

**ML task:** Entity resolution and classification across heterogeneous public sources to identify organisational adopters and estimate deployment scale
**Input data:** Public repository configuration files and manifests; container image layers and public registries; job postings naming the technology and the seniority of the roles; conference talks and public engineering blogs; issue and discussion participants with corporate email domains or affiliations; public infrastructure records; package dependency graphs.
**Target:** Confirmed adoption and approximate deployment scale, validated against the vendor's known customers and against publicly confirmed users.
**Evaluation metric:** Precision on identified adopters, since a sales organisation acting on a false positive wastes effort and looks foolish. Scale estimation should be evaluated in bands rather than as a number — the commercially relevant distinction is between experimentation, meaningful use and operating at a size where support is worth buying.
**Scope:** No single source is reliable and the joint signal is strong, which makes this fundamentally an entity resolution and evidence-combination problem rather than a classification one. Job postings are unusually informative about both adoption and scale. The cultural tension inside these companies is real — maintainers dislike community analysis for sales purposes — and the output framing matters as much as the accuracy. 2-3 ML engineers, 5-6 months.
**Data availability:** Public sources are abundant, free and messy. Validation labels come from known customers, which is a biased sample of the population being inferred.

---

## 2. Issue Triage, Duplicate Detection and Contribution Risk
#bert #word-embeddings #dbscan #gradient-boosting #large-language-models #evaluation-metrics #automation #worker-facing

**Problem statement:** A handful of maintainers face a queue from a community thousands of times larger, and the standard tooling — templates, labels, stale bots — does not change the arithmetic because a maintainer must still read everything to know what it is.

**ML task:** Multiclass classification of issues, semantic duplicate detection, reproduction assessment, and risk scoring of pull requests
**Input data:** Issue and discussion text with titles, bodies and comment threads; historical labels and resolutions; confirmed duplicate links; pull request diffs, test coverage and CI outcomes; contributor history; the project's own documentation and prior answers.
**Target:** The eventual label and disposition of each issue; confirmed duplicates; and for pull requests, whether the change was merged with minor review or required substantial architectural discussion.
**Evaluation metric:** For classification, accuracy on held-out issues by class, with support-question detection weighted heavily since routing those away from the defect queue is the single largest volume reduction. For duplicates, precision, because incorrectly merging two distinct reports hides one. For pull requests, the metric is maintainer time saved on the trivial without any high-risk change being fast-tracked.
**Scope:** Public issue corpora are large, labelled by history and freely available, which makes this one of the best-posed problems available to open-source tooling. Duplicate detection alone would materially change several major projects' queues. Pull request risk assessment must be conservative in one direction — fast-tracking a risky change is a far worse error than slow-reviewing a trivial one. 2 ML engineers, 4 months.
**Data availability:** Excellent and public. Cross-project training is straightforward and generalisation to a new project is the interesting evaluation.

---

## 3. Feature-to-Purchase Attribution for the Open-Core Boundary
#causal-inference #logistic-regression #gradient-boosting #hypothesis-testing #confidence-intervals #evaluation-metrics #revenue-impact

**Problem statement:** Where the line between free and paid sits determines the economics of an open-core company, is set by folklore about enterprise features, and is redrawn under pressure when growth disappoints or a hyperscaler competes. The evidence about which features actually drive purchase is not assembled.

**ML task:** Attribution of conversion and expansion to feature adoption, using trial behaviour and post-purchase usage, with causal care around confounding
**Input data:** Trial and evaluation session behaviour with feature usage sequences; conversion outcomes; post-purchase feature adoption and its timing; expansion and renewal events; churn with stated reasons; competitive context; historical boundary changes with their observable effects.
**Target:** Conversion, expansion and retention, modelled against feature adoption.
**Evaluation metric:** Predictive lift is secondary; the deliverable is an interpretable attribution with intervals, since the output is an argument in a strategy discussion rather than a scoring system. Confounding is severe — larger organisations both adopt more features and convert more — and any claimed effect should be checked against that first.
**Scope:** Trial behaviour is the cleanest available signal and is held by most of these companies and analysed impressionistically. The counterfactual for a boundary change is measurable only if instrumentation is in place beforehand, which it never is because the changes are made under duress — establishing that measurement in advance of the next change is itself the recommendation. Community sentiment measurement belongs alongside it, since a boundary change's cost is partly reputational and is currently assessed by reading social media. 2 ML engineers plus a product strategist, 4-5 months.
**Data availability:** Commercial-side data is complete. Free-tier usage is the missing half and is unmeasured for the same reasons adoption is invisible, which limits what can be concluded.

---

## 4. Cross-Channel Answer Unification
#bert #word-embeddings #k-means-clustering #large-language-models #gradient-boosting #evaluation-metrics #automation #worker-facing

**Problem statement:** The same technical question is answered in a paying customer's ticket and in a public issue, in systems that do not learn from each other, so both are re-derived and neither reaches the documentation.

**ML task:** Semantic matching across support tickets, public issues, forum posts and documentation, with promotion of well-answered questions into documentation
**Input data:** Support ticket text and resolutions; public issue and forum threads with accepted answers; existing documentation; version and configuration context; question frequency across both channels.
**Target:** Matching question clusters across channels, and whether a public answer was subsequently formalised into documentation.
**Evaluation metric:** Cross-channel duplicate recall — how often an engineer answering a ticket is correctly shown the equivalent public thread — and documentation coverage improvement measured by the decline in repeat questions on a topic after promotion. Deflection rate through community self-service is the operational outcome.
**Scope:** The technical problem is ordinary semantic matching and the value comes from spanning a boundary that exists for commercial rather than technical reasons. Promotion of good public answers into documentation is currently manual and therefore does not happen, and automating the identification of promotion candidates is most of the benefit. The commercial policy question — what the community gets — is organisational and must be settled separately. 2 ML engineers, 3-4 months.
**Data availability:** Both corpora exist and are sizeable. Public content is freely usable; ticket content is customer data and requires care when used to generate public documentation.
