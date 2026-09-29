# Machine Learning Opportunities — AI Red Teaming Firms

**Industry:** [[ai-red-teaming-firms|AI Red Teaming Firms]]
**Derived from:** [[problems/ai-red-teaming-firms/high-impact|High Impact]], [[problems/ai-red-teaming-firms/low-impact-1|Low Impact 1]], [[problems/ai-red-teaming-firms/low-impact-2|Low Impact 2]], [[problems/ai-red-teaming-firms/worker-life-1|Worker Life 1]], [[problems/ai-red-teaming-firms/worker-life-2|Worker Life 2]]

---

## 1. Structured Coverage Measurement Over a Harm Taxonomy
#hypothesis-testing #confidence-intervals #evaluation-metrics #pac-learning-and-vc-dimension #bayesian-inference #dimensionality-reduction #compliance

**Problem statement:** A clean assessment report tells a client nothing without a denominator, and no method exists for stating coverage of a system with an unbounded natural-language input space. Firms are selected on reputation and price because thoroughness is invisible, and regulators are about to ask organisations to demonstrate that testing was adequate.

**ML task:** Coverage estimation over an explicit taxonomy and technique-family space, with statistical bounds on failure rates within probed categories and novelty measurement of the probes themselves
**Input data:** Probes from historical engagements with their harm category, technique family, target model, configuration and outcome; probe embeddings for novelty and diversity measurement; the firm's cumulative assessment corpus; taxonomy definitions.
**Target:** Coverage as a structured claim — categories probed, attempts per category, technique families used, categories not covered — and within-category failure rate bounds.
**Evaluation metric:** Whether coverage claims predict what is later found. If a category reported as well-covered subsequently yields a critical finding from another party or in production, the coverage claim was wrong, and tracking this across engagements is the only honest validation available. Report probe diversity within a category as a distinct measure, since a hundred near-identical attempts are not a hundred attempts.
**Scope:** The honest framing is coverage of a defined space rather than of all possible failures, and stating that limitation explicitly is what makes the claim defensible rather than misleading. Novelty measurement — embedding probes and comparing against the firm's historical corpus — distinguishes genuine research from a checklist run and is a metric a sophisticated client would immediately want. This is a measurement and reporting discipline more than a modelling problem, which is why it has not been built. 2 ML engineers plus a measurement statistician and senior researchers, 5-6 months.
**Data availability:** Firms hold thousands of assessments with probes and outcomes, generally as engagement artefacts rather than as a structured corpus. Assembling it is the prerequisite and is entirely internal.

---

## 2. Sector Incident Mining for Domain Harm Taxonomies
#large-language-models #bert #word-embeddings #k-means-clustering #evaluation-metrics #transfer-learning #compliance

**Problem statement:** Generic harm categories do not describe what goes wrong in a clinical triage assistant or a lending system, so every sector engagement begins with a domain expert building a taxonomy from scratch — rebuilt for the next client in the same sector because taxonomies are delivered as client artefacts rather than retained.

**ML task:** Extraction of failure modes from sector incident literature, mapped onto AI-relevant categories, plus severity anchoring on realised consequence
**Input data:** Published clinical incident reports and safety literature; regulatory enforcement actions; litigation filings and settlements; sector risk management frameworks; the firm's prior taxonomies across clients in the sector; historical findings with client-assigned severity and realised impact where known.
**Target:** A domain failure taxonomy with categories, probe strategies and severity anchored on documented consequence rather than researcher intuition.
**Evaluation metric:** Whether taxonomy-derived probes find issues that generic probes miss — a direct comparison runnable on any engagement and the only test of whether the domain work is adding anything. For severity, consistency across researchers on the same finding, which is currently poor and makes reports incomparable.
**Scope:** The domain knowledge lives in sector risk literature that has never been mapped onto AI failure modes, and that mapping is the contribution. Severity calibration is the more immediately valuable half: anchoring on what actually happens if the failure occurs in this deployment, drawn from documented incidents, replaces the intuition that currently makes the same finding critical to one researcher and moderate to another. 2 ML engineers plus domain experts per sector, 5 months for the first sector.
**Data availability:** Sector incident literature is public and substantial in healthcare and finance, thinner elsewhere. Prior taxonomies exist in delivered reports and are recoverable.

---

## 3. Finding Generalisation into Probe Families
#large-language-models #bert #word-embeddings #contrastive-learning #evaluation-metrics #transfer-learning #change-point-detection

**Problem statement:** A discovered vulnerability is captured as a single prompt string, and the client's next model update may resist that exact string while the underlying weakness persists. Regression suites therefore go stale immediately, and assurance cadence cannot match model update cadence.

**ML task:** Generating variation families around a confirmed finding that probe the same underlying weakness, plus change impact scoping when a client's configuration changes
**Input data:** Confirmed findings with their exact probes and the model responses; the researcher's stated hypothesis about the underlying weakness where recorded; historical probe families and their persistence across model versions; client configuration change history; which findings survived which updates.
**Target:** A family of probes that continue to detect the weakness after a model update resists the original, and per-finding change impact classification.
**Evaluation metric:** Family persistence — the proportion of findings whose probe family still detects the weakness after a model update that defeats the original single probe. This is directly measurable against historical version transitions and is the number that determines whether continuous assurance is possible at all.
**Scope:** Capturing the researcher's reasoning about why a probe worked is the prerequisite and is currently not recorded, which is the core reason findings do not generalise — the prompt is saved and the insight is not. Change impact scoping is separable and immediately useful: classifying which findings depend on model behaviour, retrieval configuration or guardrail settings lets a client scope a re-test rather than commissioning a full engagement. 2 ML engineers plus senior researchers, 5 months.
**Data availability:** Findings and probes are held. The reasoning behind them lives in researchers' heads and in engagement notes, and structuring its capture is a workflow change that should precede the modelling.

---

## 4. Automated Outcome Classification to Reduce Human Exposure
#large-language-models #bert #evaluation-metrics #hypothesis-testing #confidence-intervals #k-means-clustering #worker-facing #compliance

**Problem statement:** Red team researchers read the model's worst outputs for hours daily as a job requirement, and much of that reading is confirming that a probe failed. The industry has not built the exposure protections that content moderation adopted only after documented harm and litigation.

**ML task:** Classifying probe outcomes — refused, complied, partially complied, ambiguous — with severity estimation, so that humans review only what needs judgement
**Input data:** Probe and response pairs with researcher-assigned outcome and severity labels from historical engagements; harm category; model and configuration; refusal patterns; the firm's severity rubric.
**Target:** The outcome classification and severity a researcher would assign.
**Evaluation metric:** Agreement with researcher judgement, reported separately for clear refusals (where automation is safe and most of the exposure reduction lives) and for ambiguous or partial compliance (where it must escalate). The operational metric is the reduction in harmful content a researcher actually reads at constant coverage, which is the point of the exercise and is directly measurable.
**Scope:** The design objective is exposure reduction rather than throughput, and that changes the calibration: the classifier should escalate liberally on anything uncertain, accepting more human review than a throughput-optimised system would, because the harm being managed is to the reviewer. Presentation controls — summaries, redaction, text rather than imagery — are established in moderation tooling and are a product change rather than a modelling one. Exposure measurement per researcher, with enforced rotation, is the control that matters most and requires only logging. 2 ML engineers plus a clinical advisor, 4 months.
**Data availability:** Probe and response corpora are held with researcher labels. This data is itself harmful content and requires careful access control and handling in any training pipeline, including for the engineers building the classifier.
