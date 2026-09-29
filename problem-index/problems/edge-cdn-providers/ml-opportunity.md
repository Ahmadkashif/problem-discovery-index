# Machine Learning Opportunities — Edge & CDN Providers

**Industry:** [[edge-cdn-providers|Edge & CDN Providers]]
**Derived from:** [[problems/edge-cdn-providers/high-impact|High Impact]], [[problems/edge-cdn-providers/low-impact-1|Low Impact 1]], [[problems/edge-cdn-providers/low-impact-2|Low Impact 2]], [[problems/edge-cdn-providers/worker-life-1|Worker Life 1]], [[problems/edge-cdn-providers/worker-life-2|Worker Life 2]]

---

## 1. Cacheability and Time-to-Live Inference from Observed Traffic
#gradient-boosting #time-series-forecasting #k-means-clustering #hypothesis-testing #confidence-intervals #feature-engineering #evaluation-metrics #compliance

**Problem statement:** Cache rules are written once by a cautious engineer and accumulate for years, so content that is static is cached for an hour, keys include attributes the response never varies on, and Vary headers are set broadly. Every one of those decisions is measurable from traffic the provider already carries.

**ML task:** Inference of true response variance by request attribute, estimation of content change frequency, and classification of responses that must never be cached
**Input data:** Request and response pairs at scale with headers, cookies, query parameters and response bodies or hashes; observed response variation across clients for identical keys; content change timestamps; existing cache configuration and realised hit ratios; authentication and session indicators.
**Target:** Whether a response actually varies by a given attribute; the empirical change interval for a resource; and whether a response is personalised or sensitive.
**Evaluation metric:** For the safety classifier, false negatives are the severe class — caching a personalised or authenticated response is a security incident — so recall on must-not-cache must be extremely high and should be reported as the headline. For cacheability, the business metric is realised hit ratio improvement against the counterfactual, measured through a split rather than before-and-after.
**Scope:** The asymmetry drives the design: the safety classifier gates everything and must be conservative, while the optimisation operates only on what it clears. Response body inspection raises real privacy and retention questions and can often be avoided by working from hashes and variance rather than content. Dead rule detection — which rules have matched traffic in ninety days — needs no modelling and should ship first. 3 ML engineers plus a delivery architect, 6 months.
**Data availability:** Complete and enormous. Retention of response detail is the constraint and is deliberately short at most providers, so much of this must be computed in stream rather than retrospectively.

---

## 2. Campaign-Level Bot Detection with Cross-Customer Propagation
#graph-neural-networks #gradient-boosting #dbscan #change-point-detection #confidence-intervals #feature-engineering #evaluation-metrics #compliance

**Problem statement:** Bot management runs on per-request signals that adversaries adapt within days of a rule shipping, tuned conservatively because false positives are invisible — blocked legitimate users leave rather than complain. The phenomenon is a coordinated campaign and it is modelled as individual requests.

**ML task:** Graph-based clustering of requests into campaigns by shared infrastructure, fingerprint and behavioural characteristics; change point detection on campaign evolution; and false positive estimation from downstream behaviour
**Input data:** Request features including TLS and browser fingerprints, header ordering and consistency, timing, IP and ASN, request sequences and navigation patterns; challenge outcomes; known-good verified crawler identities; confirmed fraud and credential stuffing outcomes where customers share them; cross-customer request populations.
**Target:** Campaign membership, and separately confirmed malicious outcomes where available.
**Evaluation metric:** False positive rate on legitimate users is the metric that is currently unmeasured and matters most, estimated from downstream behaviour — challenged sessions abandoned, blocked clients with long legitimate histories. Report it alongside detection rate, because the conservative tuning customers apply is a direct consequence of never seeing this number.
**Scope:** Cross-customer propagation is the structural advantage and the reason this belongs at a provider rather than at a customer — an operation seen against one customer is relevant to the next within minutes. Adaptation detection treats a shift in campaign characteristics as a change point in a monitored population, which is far more useful than discovering it through rising successful attempts. Privacy and fairness both matter here: fingerprinting is intrusive and blocking decisions affect real people, so error rates across client populations should be examined explicitly. 3-4 ML engineers plus security researchers, 8 months.
**Data availability:** Request data is vast. Confirmed malicious labels are scarce and depend on customer feedback loops that mostly do not exist.

---

## 3. Edge Placement Analysis
#gradient-boosting #causal-inference #time-series-forecasting #optimization-fundamentals #confidence-intervals #evaluation-metrics #revenue-impact

**Problem statement:** Edge compute is sold on a latency claim that is true for logic with no origin dependency and false for logic that must reach back to a regional database. Customers decide by intuition, rarely measure afterwards, and discover the cost model on the invoice.

**ML task:** Prediction of real user latency under edge versus origin placement given data dependencies and traffic geography, plus cost modelling across the two billing structures
**Input data:** Function code and its observed call patterns to origin services; traffic geographic distribution; network latency between edge locations and origin regions; existing real user monitoring; edge execution time and request volumes; origin compute cost structure and utilisation.
**Target:** Realised real user latency and total cost following a placement decision, measured against the counterfactual through a split deployment.
**Evaluation metric:** Accuracy of the predicted latency difference, with sign correctness weighted most heavily — telling a customer the edge will help when it will hurt is the failure that ends trust in the advice. Cost prediction should be evaluated at realistic volumes rather than at the margin, since the two billing models cross over.
**Scope:** Data dependency detection is the crux and separates the workloads that benefit from those that do not; it is derivable from static analysis of the function plus observed call patterns. Counterfactual measurement through split deployment is uniquely available to a provider sitting in the request path and is what makes the advice verifiable rather than assertive. 2 ML engineers, 4-5 months.
**Data availability:** Traffic geography, network latency and edge execution telemetry are all held by the provider. Origin cost structure requires customer input and is the missing half of the comparison.

---

## 4. Configuration Diagnosis and Hit Ratio Decomposition
#gradient-boosting #bert #k-means-clustering #change-point-detection #hypothesis-testing #evaluation-metrics #automation #worker-facing

**Problem statement:** CDN support is dominated by mechanically detectable problems in customers' own applications — a cache-defeating header, an analytics query parameter creating a unique key per visitor, an over-broad Vary — delivered as unwelcome findings by engineers many times a day.

**ML task:** Automated diagnosis of hit ratio loss with attribution to specific causes, plus clustering of support tickets into product findings
**Input data:** Request and response headers, cookies and query parameters; realised cache outcomes per request; customer configuration; purge events and their scope; origin error rates and their sources; historical support tickets with resolved causes.
**Target:** The cause of cache misses, attributed by proportion, and the ticket cause as ultimately resolved.
**Evaluation metric:** Decomposition accuracy — do the attributed proportions sum correctly and match what an expert engineer would conclude on a sample. Operationally, the metric is ticket deflection: the proportion of the recurring causes that customers resolve from the dashboard without opening a ticket.
**Scope:** Almost all of this is deterministic analysis rather than learning, and its absence is a product choice. The valuable framing is delivering it proactively rather than on request, which removes both the volume and the blame dynamic. Ticket clustering turns the ten recurring causes into product findings — a default to change, a validation to add — which is the durable improvement. 2 ML engineers, 3-4 months.
**Data availability:** Complete in the request path. Ticket histories provide labels of moderate quality.
