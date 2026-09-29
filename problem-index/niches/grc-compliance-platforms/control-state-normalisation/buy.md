# Buy: Maturity Modelling With Actual Inputs

**Niche:** Control State Normalisation
**Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Capability maturity models have graded implementation depth for decades using self-assessment and interviews, and the platforms could compute the same grades from configuration data and do not.
**Tags:** #gradient-boosting #evaluation-metrics #confidence-intervals #k-means-clustering #compliance #data-integration #automation
**Contested on:** Whether "this control is implemented" means anything comparable across two organisations, or describes configurations with nothing in common.

## The Problem

The idea that a capability exists in degrees rather than in a binary state is old and well developed. Capability maturity models grade practices across levels — ad hoc, repeatable, defined, managed, optimised — and are used across software engineering, security and operations. The security-specific versions are widely known and applied.

Their weakness has always been the input. Maturity assessment is performed by interview and self-assessment, by a consultant over several weeks, producing a rating that reflects what people said about their practices. It is expensive, infrequent, subjective, and optimistic in a predictable direction.

Compliance platforms have the opposite profile. They observe actual configuration continuously and automatically, across the whole estate, and then reduce it to a pass flag. They have the inputs maturity models always wanted and use them for the crudest possible output.

Nobody has joined the two. Maturity grading has the conceptual framework and bad data; the platforms have excellent data and no framework.

## What Already Exists

Maturity models: CMMI and its descendants, the Cybersecurity Capability Maturity Model, the NIST CSF implementation tiers, the CIS Controls implementation groups, and the various vendor-specific security maturity frameworks. All define graded levels; all are assessed by interview.

Assessment services: consultancies performing maturity assessments, and the tooling supporting them, which is largely questionnaire-based.

Configuration data sources: cloud security posture management from Wiz, Orca and Prisma; identity providers; endpoint managers; and the compliance platforms' own integration layer, all producing detailed, continuous configuration state.

Benchmarking: the CIS benchmarks, which specify configuration in precise technical detail — the closest existing thing to a graded technical rubric and used for hardening rather than for maturity grading.

## The Customization Gap

**Maturity levels are described in process language.** Levels are phrased in terms of documentation, repeatability and management, which do not map directly to observable configuration. Translating each level into configuration signatures is the adaptation, and it is where the intellectual work sits.

**CIS benchmarks are the missing bridge and are used for the wrong purpose.** They already express configuration requirements in precise technical terms at different rigour levels. Using benchmark conformance as the graded input to a maturity measure is close to obvious and nobody does it.

**Maturity is assessed per domain, control state is per control.** Aggregating control-level observations into a domain-level maturity grade requires a weighting scheme, which is where honest reporting of uncertainty matters — and where a vendor score would be tempted to overclaim.

**Process maturity is genuinely unobservable in part.** Whether an organisation reviews and improves its practices cannot be read from configuration. The honest adaptation covers the observable dimensions well and states plainly that it does not cover the rest, rather than inferring process maturity from technical state.

**Self-assessment optimism is the thing being replaced.** The value proposition is that this grade is derived from what is actually configured rather than from what someone reported, which is a strong claim and the main reason to build it.

**Continuous versus point-in-time changes the artefact.** Maturity assessments are annual snapshots. A continuously computed grade shows drift, regression and seasonal decay, which is new information the maturity tradition has never had.

## Target Customer

The compliance platforms, for whom this is a differentiated output computed from data they already hold and currently discard.

Cloud security posture vendors are the alternative adapters, sitting even closer to the configuration data, and maturity grading would extend them from finding misconfigurations into characterising overall implementation depth.

Buyers are enterprise security leadership, who commission expensive periodic maturity assessments and would prefer a continuous one derived from observation.

## Impact If Solved

Maturity assessment moves from interview to observation, which addresses the criticism the discipline has always carried and could not answer for want of data.

CIS benchmark conformance as a graded input is available immediately, is technically precise, and is already accepted by the security community — which means it would not require a new rubric to be trusted.

And a continuously computed grade would reveal drift and regression, which is a category of information the annual-assessment tradition structurally cannot produce and which is where most real degradation happens.
