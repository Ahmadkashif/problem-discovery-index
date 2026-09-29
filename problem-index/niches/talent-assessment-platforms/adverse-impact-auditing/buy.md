# Buy: Fairness Libraries Adapted to a Statutory Standard

**Niche:** [[niches/talent-assessment-platforms/adverse-impact-auditing/profile|Adverse Impact Auditing]]
**Industry:** [[industries/talent-assessment-platforms|Talent Assessment Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** ML fairness libraries implement a dozen group metrics; employment law asks about one, in a specific form, with specific categories and a specific reporting obligation.
**Tags:** #hypothesis-testing #confidence-intervals #evaluation-metrics #descriptive-statistics #compliance #bayesian-inference #automation #workflow-orchestration
**Contested on:** Whether general fairness tooling can produce an artefact that satisfies a statutory audit.

## The Problem

Algorithmic fairness has good open tooling. Fairlearn, AIF360 and their peers implement demographic parity, equalised odds, predictive parity and the rest, with visualisation, mitigation methods and a well-developed literature including the impossibility results that show the metrics cannot all be satisfied at once.

An employment bias audit is not an exercise in choosing a fairness metric. It is a compliance artefact computed in a prescribed way, on prescribed categories, with a prescribed publication obligation, by an independent auditor, under a statute. A team reaching for a fairness library will compute several metrics, none of which is the one the regulation asks about, and produce something that does not satisfy the requirement.

## What Already Exists

The fairness libraries and their metric implementations. Visualisation and reporting tooling. Bias mitigation algorithms. The psychometrics tradition's own impact analysis conventions, which predate the ML fairness literature by decades. Bias audit service providers who understand the statutory requirements. Documentation and audit trail tooling.

## The Customization Gap

**The metric is prescribed, not selected.** The applicable conventions in employment selection are specific and long-established, and a regulation that requires an audit specifies what it wants computed. Implementing that precisely, on the specified categories, is the requirement — and it is narrower than a fairness library's menu and not always present in it.

**Independence is part of the standard.** The regime requires an independent auditor. A vendor's self-computed fairness dashboard, however sophisticated, is not an audit, and the tooling has to support an external party's workflow — data access, verification, reproducibility and their own documentation.

**Publication is an obligation with a defined form.** The audit summary must be published in a specified way. That is a reporting artefact with a template, not a notebook output, and generating it reliably across many tools and many clients is where the operational work sits.

**The categories are legally defined and the data is self-reported and incomplete.** Fairness libraries assume clean group labels. Here they come from voluntary candidate self-identification with substantial non-response, and the handling of missing data materially affects the result — which needs a stated, defensible convention rather than a library default.

**Sample sizes are small and the libraries do not report inference.** Most fairness implementations return point estimates. At requisition scale the intervals are wide and reporting a ratio without one is misleading in both directions.

## Target Customer

Bias audit providers building repeatable audit pipelines across many clients and tools. Also employers and vendors preparing for audit who will find a fairness library does not produce the artefact, and regulators or standards bodies who would benefit from a reference implementation.

## Impact If Solved

The metric implementations, visualisation and mitigation machinery get reused where they fit, and the prescribed-metric computation, independent-auditor workflow, publication artefact, missing-data convention and small-sample inference get built. Concretely: an audit that satisfies the statute and is capable of finding something, rather than a fairness dashboard.
