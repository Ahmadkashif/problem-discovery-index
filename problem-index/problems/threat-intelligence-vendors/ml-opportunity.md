# Machine Learning Opportunities — Threat Intelligence Vendors

**Industry:** [[threat-intelligence-vendors|Threat Intelligence Vendors]]
**Derived from:** [[problems/threat-intelligence-vendors/high-impact|High Impact]], [[problems/threat-intelligence-vendors/low-impact-1|Low Impact 1]], [[problems/threat-intelligence-vendors/low-impact-2|Low Impact 2]], [[problems/threat-intelligence-vendors/worker-life-1|Worker Life 1]], [[problems/threat-intelligence-vendors/worker-life-2|Worker Life 2]]

---

## 1. Feed Match Rate, Precision and Timeliness
#bayesian-inference #confidence-intervals #hypothesis-testing #gradient-boosting #survival-analysis #evaluation-metrics #causal-inference #probability-distributions

**Problem statement:** The success case is an attack that did not happen, which has been accepted as a reason to measure nothing. Two proxies are directly observable and unused: whether a feed's indicators ever match anything in a customer's telemetry, and whether the matches turn out to be real.

**ML task:** Measure per-feed match rate, true positive rate and timeliness relative to the customer's own detection, across an installed base and reported by customer segment
**Input data:** Indicator feeds with provenance and timestamps; customer telemetry matches; investigation dispositions establishing true and false positives; the customer's own detection events and their timing; customer segment covariates — sector, size, technology estate.
**Target:** Whether an indicator matched, whether the match was a genuine detection, and whether the intelligence preceded the customer's own detection.
**Evaluation metric:** These are measurements rather than predictions, and the discipline required is reporting them by segment rather than in aggregate — a feed that performs well for large financial institutions and poorly for mid-market manufacturers is two different products sold as one. Timeliness against the customer's own detection is the clearest evidence of value: intelligence arriving after the customer's tools flagged the activity added nothing, and intelligence arriving first added lead time, which is directly computable.
**Scope:** Telemetry access is the practical barrier for standalone vendors and is free for the endpoint-bundled competitors, who could publish these numbers tomorrow from data they already hold. Publishing enables comparison and would move the market from breadth toward accuracy, which advantages some vendors and disadvantages others — which is why nobody has gone first. 2 ML engineers, 4-6 months where telemetry is available.
**Data availability:** Complete for vendors with telemetry; unavailable to those without, which is itself a structural fact about who can build this.

---

## 2. Exposure-Chain Relevance Scoring
#graph-neural-networks #gradient-boosting #bert #k-nearest-neighbors #confidence-intervals #dimensionality-reduction #evaluation-metrics #data-integration

**Problem statement:** Feeds are delivered broadly with sector tags because the vendor does not know the customer's environment, so the filtering falls to the scarcest people in the organisation — which turns intelligence into a source of work rather than leverage.

**ML task:** Score relevance by reasoning over the exposure chain — technology present, in an affected version, in a reachable position, without a mitigating control — and estimate targeting fit from historical victim patterns
**Input data:** The customer's asset inventory, software bill of materials, external attack surface and control configuration; threat and vulnerability intelligence with affected components and versions; the vendor's historical victim data by sector, size, geography and function; exploitation evidence.
**Target:** Whether an item requires action in this environment, validated against what the customer's team actually actioned.
**Evaluation metric:** The operative measure is reduction in items requiring human triage at a fixed recall on things that genuinely needed action — a relevance model that filters aggressively and misses a real exposure is worse than no filter, so recall on actioned items is the binding constraint and precision is the benefit. Report targeting fit separately with intervals; adversary targeting is patterned but noisy, and a confident statement that a campaign will not target this organisation is a claim the data rarely supports.
**Scope:** The intelligence and the environment sit in different systems at different companies, and joining them is the whole opportunity. Delivery should be a short ranked list with reasoning rather than a filtered feed — a team can act on five items with explanations and cannot act on eight hundred filtered ones. 2-3 ML engineers, 6-9 months.
**Data availability:** Environment data sits with the customer and requires an integration they would grant; historical victim data sits with incident-response-connected vendors and is their unique asset.

---

## 3. Indicator Decay and Reassignment Detection
#survival-analysis #change-point-detection #bayesian-inference #gradient-boosting #time-series-forecasting #confidence-intervals #probability-distributions #evaluation-metrics

**Problem statement:** Indicators are observations about a moment. Infrastructure is reassigned, domains re-registered, addresses reallocated — and a stale indicator produces false positives or blocks a business service, which is why security teams confine feeds to detection rather than prevention.

**ML task:** Model per-type, per-context indicator survival, and detect the transition from malicious to legitimate use promptly
**Input data:** Indicators with type, first and last observation, and context of observation; passive DNS, certificate and hosting change data; aggregate match behaviour across an installed base including the character of matching traffic; investigation dispositions over time; sinkhole data.
**Target:** Whether an indicator remains predictive of malicious activity, and the point at which it stops.
**Evaluation metric:** Detection latency on reassignment is the metric that matters operationally, because the cost being avoided is a block that takes down a business service. Report survival curves by indicator type and context separately — a file hash for a specific sample stays valid indefinitely, a commodity botnet address may be meaningless in days, and treating them alike is the source of most of the practical problem. Per-customer calibration matters too: the same indicator produces different false positive rates in environments with different traffic profiles.
**Scope:** The aggregate view across an installed base is what makes decay observable — an indicator that stops matching malicious activity and starts matching benign traffic is detectable in aggregate and invisible to any single customer. 2 ML engineers, 4-6 months.
**Data availability:** Passive DNS and infrastructure data are commercially available; aggregate match behaviour requires installed-base telemetry.

---

## 4. Alert Attribution and Investigation Assembly
#gradient-boosting #graph-neural-networks #large-language-models #confidence-intervals #k-nearest-neighbors #change-point-detection #evaluation-metrics #worker-facing

**Problem statement:** A large share of a security operations queue is generated by intelligence feeds and a large share of that is false positives, investigated identically each time by analysts whose attrition is the sector's chronic problem — and nobody attributes the cost back to the feed that produced it.

**ML task:** Attribute alert volume and investigation hours per feed, suppress known-stale and previously-dismissed matches before they become alerts, and pre-assemble the investigation context
**Input data:** Alerts with their generating feed and indicator; investigation duration and disposition; asset context and exposure position; traffic detail and corroborating activity; prior dispositions on the same indicator and asset; indicator decay state.
**Target:** True positive rate and analyst hours consumed per feed, and whether a pre-assembled investigation reaches the same disposition as a manual one.
**Evaluation metric:** For suppression, the safety-critical measure is whether any suppressed match would have been a true positive — measured on historical data before deployment, with a conservative threshold, because the cost of suppressing the one that mattered is not commensurable with the cost of an extra investigation. For assembly, disposition agreement with manual investigation plus the time saved. For attribution, the number that matters is hours per feed per year, which makes a purchasing decision accountable and is computed nowhere.
**Scope:** Ranking on the full exposure chain rather than on indicator severity puts attention where it belongs — a match on an internet-facing asset with corroborating behaviour is a different event from a match on a laptop browsing shared hosting. 2 ML engineers, 4-6 months.
**Data availability:** Complete within any security operations platform.
