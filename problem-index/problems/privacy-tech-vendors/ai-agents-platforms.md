# AI Agents & Platform Opportunities — Privacy Tech Vendors

**Industry:** [[privacy-tech-vendors|Privacy Tech Vendors]]

---

## 1. Consent Integrity Platform
#ai-platform #causal-inference #cnns #bayesian-inference #confidence-intervals #hypothesis-testing #compliance #evaluation-metrics

**Concept:** A platform that measures whether consent means anything. It runs a sampled post-hoc panel asking users what they believe they agreed to and compares that to what was recorded — producing the first empirical measure of consent validity anyone would have. It scores interface configurations automatically against the accumulated body of regulatory decisions: relative prominence, click-depth asymmetry, default states, bundling, pre-selection. And it tests designs against understanding rather than acceptance, which is a different optimisation and produces visibly different interfaces.

**Inputs:** Rendered consent interfaces and their layout properties; interaction telemetry including dwell and detail expansion; sampled survey responses; recorded consent; the corpus of published regulatory decisions and the designs they concerned.

**Outputs / Actions:** A comprehension estimate with its sampling error, reported alongside acceptance rate and a design risk score — three numbers where the industry currently manages one. Specific property-level findings a customer can act on. Design variants evaluated on whether users can subsequently state what they agreed to.

**Why now:** Enforcement has accumulated into a consistent body of decisions that the industry adapts to mechanically, round after round, without the substantive question ever being measured. The incentive conflict is explicit — vendors compete on acceptance rates and a vendor optimising for informed choice loses deals — which means this is a product for a new entrant, a regulator-facing service or a publisher who wants defensible consent, rather than for an incumbent.

**Market:** Publishers and platforms facing enforcement exposure, regulators and supervisory authorities who currently assess designs by inspection, and consumer organisations running the measurement studies that shape enforcement.

---

## 2. Observed Data Map Platform
#ai-platform #graph-neural-networks #bert #transformers #change-point-detection #confidence-intervals #data-integration #compliance

**Concept:** A platform that derives the data map instead of asking for it. It classifies personal data using context — surrounding schema, table relationships, sample values, downstream usage — rather than pattern matching, extending into the unstructured estate where the real exposure sits. It infers the flow graph from what systems actually do: query logs, pipeline definitions, integration configurations, egress, application code, and rendered browser behaviour on the organisation's own properties. And it reconciles the observed picture against the declared register, so the privacy team's work becomes the discrepancies rather than the whole compilation.

**Inputs:** Data stores across structured, semi-structured and unstructured estates; query, pipeline and integration configurations; network egress; application code; browser rendering with tag loading sequence relative to consent state; the declared register and vendor list.

**Outputs / Actions:** Classification with precision and recall reported per data category, since missing special-category data is a materially worse error than missing an email address. Coverage as a first-class number, because presenting a partial scan as an inventory is the failure that recurs across this whole cluster. A discrepancy queue — flows and destinations the register does not contain — which inverts the privacy officer's job from compilation to exception handling. And the consent-conditioned check that enforcement actually turns on: whether a tag fires before consent and whether rejecting stops it, which fails commonly and is almost never detected internally.

**Why now:** Browser-side observation requires no access and is immediately valuable; the server-side inference shares machinery with classification, which makes this one programme rather than two. Enforcement has focused specifically on undisclosed transfers and pre-consent collection, against organisations that did not know what their own systems were doing.

**Market:** Privacy platforms, enterprise privacy teams maintaining records they know are incomplete, and the regulators and researchers who currently produce this evidence from outside.

---

## 3. Fulfilment Engineering Agent
#ai-agent #graph-neural-networks #large-language-models #gradient-boosting #confidence-intervals #change-point-detection #worker-facing #compliance

**Concept:** An agent for the point where a privacy obligation meets infrastructure that was not designed for it. It derives the set of systems a subject's data actually reached from the flow graph rather than from memory, propagating identifiers through derived tables, views and exports. It verifies deletion where verification is possible — re-querying after the fact is checkable for many stores and is rarely done. And it reports coverage as a partition rather than a binary: reached, partially reached, excluded with the reason, so the organisation knows its real position instead of a confirmation.

**Inputs:** The inferred flow graph; identifier propagation paths; each system's deletion capability and retention configuration; backup and log architectures; third-party processor request mechanisms; historical fulfilment records and scripts; engineering time per request.

**Outputs / Actions:** A lineage-derived reach set, which is more complete and repeatable than what an engineer remembers. Verified removal where verification is possible. An explicit coverage partition, which is uncomfortable and true and is the precondition for prioritising the architectural fix. A stated policy position on training data and models, since removing an individual's influence from a fitted model is unsolved in the general case and should be handled as documented policy rather than improvised per request. And a recurring-cost measurement — engineering hours per request across a year — which is the business case for building deletion as a platform capability and is currently recorded nowhere.

**Why now:** Request volumes have grown steadily under successive privacy regimes, the manual work recurs because each request produces a script rather than a capability, and nobody has quantified the cost that would justify doing it properly.

**Market:** Privacy platforms whose workflow currently ends at routing, data platform teams carrying the manual load, and the privacy officers recording fulfilments whose real coverage they cannot state.
