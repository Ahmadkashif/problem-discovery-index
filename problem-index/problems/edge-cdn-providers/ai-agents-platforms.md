# AI Agents & Platform Opportunities — Edge & CDN Providers

**Industry:** [[edge-cdn-providers|Edge & CDN Providers]]

---

## 1. Cache Intelligence Platform
#ai-platform #gradient-boosting #time-series-forecasting #k-means-clustering #confidence-intervals #evaluation-metrics #compliance #automation

**Concept:** A platform that derives cache configuration from observed traffic rather than from a cautious engineer's rules. It measures whether a response actually varies by each header, cookie and query parameter, so a cache key including an attribute the response never varies on is identified as pure fragmentation with a computed cost. It estimates real content change intervals to set time-to-live from evidence rather than caution. Everything is gated by a deliberately conservative safety classifier that identifies responses which must never be cached — personalised, authenticated, or varying between clients for the same key — because that is the one error that is a security incident rather than a cost.

**Inputs:** Request and response streams with headers, cookies and parameters; response variance across clients for identical keys; content change timestamps; current configuration and realised hit ratios; authentication and session indicators.

**Outputs / Actions:** Cache key recommendations with the fragmentation cost of each removed attribute. Evidence-based time-to-live proposals per resource class. A must-not-cache classification that gates every recommendation. Dead rule identification. Hit ratio decomposition showing exactly what each configuration decision costs. It proposes and never applies a caching change automatically.

**Why now:** The traffic that answers these questions has flowed past for twenty years and the configuration has been set by caution because nothing established safety. The safety classifier is what makes acting on the optimisation defensible, and it is the piece nobody built.

**Market:** CDN providers as a differentiator in a market where delivery itself has commoditised, and large customers directly. Hit ratio determines both the customer's origin cost and their user experience, which makes it the number the relationship is judged on.

---

## 2. Campaign Defence Agent
#ai-agent #graph-neural-networks #dbscan #change-point-detection #gradient-boosting #confidence-intervals #evaluation-metrics #compliance

**Concept:** An agent that treats automated traffic as campaigns rather than requests. It clusters requests by shared infrastructure, fingerprint and behavioural characteristics into coordinated operations, propagates recognition across the provider's whole customer base within minutes rather than through an eventual rule update, and treats a shift in a campaign's characteristics as a detectable change point — so adaptation is observed as it happens rather than inferred from rising success. Critically, it estimates false positives from downstream behaviour, giving customers the number they have never had and which explains why they tune so conservatively.

**Inputs:** Request fingerprints, header consistency, timing and navigation sequences; IP and ASN reputation; challenge outcomes; verified crawler identities; cross-customer request populations; confirmed fraud outcomes where customers feed them back.

**Outputs / Actions:** Campaign-level classifications with confidence rather than per-request verdicts. Cross-customer propagation of newly identified operations. Adaptation alerts when a campaign's characteristics shift. Estimated false positive rate with the evidence. Error rate reporting across client populations, since blocking decisions affect real people and the fairness question deserves to be visible.

**Why now:** Per-request signatures have a short useful life against operators who test against the major providers before deploying. Campaign-level relational modelling survives the adaptation of any single signal, and cross-customer propagation is the provider's structural advantage that per-request rules never exploited.

**Market:** CDN and security providers, and their customers in commerce, ticketing, travel and financial services. The false positive number alone changes the conversation, because customers currently tune against an error they cannot see.

---

## 3. Configuration Experimentation Agent
#ai-agent #causal-inference #hypothesis-testing #confidence-intervals #time-series-forecasting #evaluation-metrics #automation #worker-facing

**Concept:** An agent that lets the person who owns the edge configuration actually measure it. Because the provider sits in the request path it can route deterministically, which makes genuine split testing a platform capability no customer could build: apply a change to a random subset of requests or clients, hold the rest as control, and measure real user latency, origin load, error rate and conversion with honest intervals. Every recommendation arrives as a hypothesis with a predicted effect and a one-click way to test it, and a change with no detectable effect is reported as such rather than as a small improvement.

**Inputs:** Configuration state and change history; request routing capability; real user monitoring; origin load and error telemetry; customer conversion signals where shared; rule match counts.

**Outputs / Actions:** Split-tested configuration changes with measured effects and intervals. A rule inventory showing match counts and the predicted impact of removing each. Recommendations framed as testable hypotheses. Automatic regression detection when a change degrades an outcome. A standing record of which changes actually helped, which is the artefact that makes future decisions cheaper.

**Why now:** Edge configuration is owned by people who cannot measure it, which is exactly why rule sets only grow and vendor recommendations go unadopted. Deterministic request routing makes the experiment trivial for the provider and impossible for anyone else.

**Market:** CDN providers as a retention and adoption feature, and enterprise customers with significant edge configuration. The unlock is that recommendations become verifiable, which is the reason they are currently ignored.
