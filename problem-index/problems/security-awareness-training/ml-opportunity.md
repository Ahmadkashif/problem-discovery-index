# Machine Learning Opportunities — Security Awareness Training

**Industry:** [[security-awareness-training|Security Awareness Training]]
**Derived from:** [[problems/security-awareness-training/high-impact|High Impact]], [[problems/security-awareness-training/low-impact-1|Low Impact 1]], [[problems/security-awareness-training/low-impact-2|Low Impact 2]], [[problems/security-awareness-training/worker-life-1|Worker Life 1]], [[problems/security-awareness-training/worker-life-2|Worker Life 2]]

---

## 1. Difficulty Calibration and Real-Outcome Linkage
#causal-inference #bayesian-inference #confidence-intervals #hypothesis-testing #survival-analysis #gradient-boosting #evaluation-metrics #compliance

**Problem statement:** Click rate improves reliably because the vendor and customer set the difficulty, and nobody has related simulated performance to whether anyone resists a real attack — despite every customer running a gateway that records real phishing, an incident record, and an employee reporting stream.

**ML task:** Rate simulation templates on a calibrated difficulty scale from measurable properties, and estimate the relationship between difficulty-adjusted simulated performance and real-world susceptibility
**Input data:** Simulation templates with contextual plausibility, personalisation, urgency framing, sender legitimacy and presence of the cues training teaches; per-employee simulation outcomes; gateway-recorded real phishing attempts per individual; employee reports of real messages; confirmed compromises; role, tenure and communication volume.
**Target:** Real-world susceptibility — reporting real phishing, falling for real phishing where observable, and involvement in confirmed incidents.
**Evaluation metric:** Report click rate at fixed difficulty, which is the minimum standard for the number to mean anything and is the change that removes the incentive to make simulations easier. For outcome linkage, the honest result may be a null, and a null would be the most important finding this category could produce — so the analysis must be powered enough to distinguish a weak relationship from none, which at any single organisation it is not, making cross-customer pooling necessary.
**Scope:** Real compromise is rare and attribution is genuinely hard — a compromise may reflect a gateway failure or a targeted attack that would have caught anyone. Reporting behaviour is the more tractable and arguably more important outcome, since a clicked-and-reported message is far less damaging than one that is neither clicked nor reported. 2 ML engineers plus a causal specialist, 9-12 months.
**Data availability:** Simulation data is complete at the vendor; gateway, incident and reporting data sit with the customer and require an integration nobody has asked for in these terms.

---

## 2. Reporting Behaviour as the Primary Objective
#survival-analysis #gradient-boosting #causal-inference #confidence-intervals #bayesian-inference #hypothesis-testing #evaluation-metrics #worker-facing

**Problem statement:** The behaviour that limits real harm is reporting, not click avoidance, and programmes optimise the latter — including through punitive designs that lower click rates by teaching people to say nothing.

**ML task:** Model reporting rate, speed and accuracy as the programme's primary outcome, and estimate how programme design features affect them
**Input data:** Reporting events with timing and accuracy; simulation and training exposure; programme design features including punitive policy, manager notification, template emotional content and recognition practices; organisational and team covariates; light survey instruments on trust in the security function and willingness to report mistakes.
**Target:** Reporting rate and speed, particularly reporting after a click, which is the behaviour a punitive programme most suppresses.
**Evaluation metric:** The decisive comparison is reporting rate under punitive versus non-punitive programme designs, pooled across customers — demonstrating that punishment reduces reporting is the evidence that would change policy where a values argument does not. Measure the trust cost alongside, with light survey instruments, so a customer can distinguish designs that build resistance from designs that build silence. Report exposure-adjusted rates: someone in a high-volume communication role receives more simulations and has more opportunity to fail, and a raw count mischaracterises them.
**Scope:** This reframes what the product optimises, which is a commercial decision before it is a technical one — but it is the frame under which the category's known harms become measurable trade-offs rather than anecdotes. 2 ML engineers plus a survey methodologist, 6-9 months.
**Data availability:** Reporting and programme configuration data sit with the vendor. Trust and willingness measures must be collected and are cheap.

---

## 3. Exposure-Driven Targeting and Contextual Delivery
#gradient-boosting #bert #transformers #k-nearest-neighbors #confidence-intervals #transfer-learning #evaluation-metrics #automation

**Problem statement:** Training is assigned uniformly, or by job title at best, to a population whose actual exposure differs enormously — while who receives what kind of phishing, who holds which access, and who has been impersonated externally are all observable.

**ML task:** Target training against measured individual exposure and assessed prior knowledge, and trigger contextual delivery at moments of relevance
**Input data:** Gateway records of phishing attempts by recipient and type; identity and access data showing who can approve payments, reach customer data or touch production; brand monitoring for external impersonation of specific individuals; adaptive assessment results; behavioural triggers — a genuinely suspicious message received, a payment change request, an unusual access grant.
**Target:** Retained behaviour change measured weeks later against real behaviour, not module completion.
**Evaluation metric:** Retention is the metric that matters and completion is the one collected, because completion is the compliance artefact. Evaluate content on durable behaviour change at 4 and 12 weeks, which will very likely show that some widely-used modules do nothing. Measure contextual delivery against scheduled delivery directly, since the hypothesis is that attention at the moment of relevance beats a module watched in March.
**Scope:** Assessed rather than assumed prior knowledge is standard practice in education and rare here, for the same reason: the artefact being sold is completion. Assigning introductory content to a security-aware engineer is the signal that makes people click through everything. 2 ML engineers, 6-9 months.
**Data availability:** Gateway, identity and brand monitoring data sit with the customer; retention measurement requires deliberate follow-up that nobody currently performs.

---

## 4. Report Triage, Campaign Clustering and Recipient Remediation
#bert #transformers #dbscan #gradient-boosting #k-nearest-neighbors #confidence-intervals #evaluation-metrics #automation

**Problem statement:** The programme's most valuable output — employee reports of real suspicious messages — arrives as an unmanageable queue at a security team at capacity, where the overwhelming majority are legitimate mail and the response is slow enough to kill the behaviour.

**ML task:** Cluster reports into campaigns, classify against organisation-specific normal traffic, and identify every other recipient of a confirmed malicious message
**Input data:** Reported messages with headers, links, attachments and body; the organisation's normal mail traffic for baselining; vendor and internal sender conventions; the programme's own simulation sends for auto-resolution; mail system records for recipient enumeration; triage dispositions as labels.
**Target:** Campaign membership, maliciousness, and the full recipient set of a confirmed campaign.
**Evaluation metric:** Clustering quality measured by how many individual triage tasks collapse into campaign decisions — the operational value is turning hundreds of tasks into a handful, and surfacing the live attack currently buried in volume. Classification must be calibrated per organisation, since what counts as unusual mail depends on that organisation's vendors, conventions and languages, and a generic classifier will flag ordinary correspondence in some and miss targeted lures in others. Measure time-to-reporter-feedback, because that is what sustains the reporting behaviour the whole programme depends on.
**Scope:** Auto-resolving reports of the programme's own simulations is trivial and removes a meaningful share of the queue. Recipient enumeration and remediation before others act is the response that actually prevents harm and requires the clustering and mail integration together. 2 ML engineers, 4-6 months.
**Data availability:** Complete within the customer's mail environment.
