# Build: A Graded Implementation Measure

**Niche:** Control State Normalisation
**Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A graded, comparable measure of how thoroughly each control is actually implemented, derived from the configuration detail integrations already collect and discard.
**Tags:** #gradient-boosting #k-means-clustering #evaluation-metrics #confidence-intervals #dimensionality-reduction #compliance #automation #data-integration
**Contested on:** Whether "this control is implemented" means anything comparable across two organisations, or describes configurations with nothing in common.

## The Problem

The platform's integrations return rich configuration data. Which accounts have multi-factor authentication and of what kind. Which repositories require review and how many approvals. Which buckets are public. Which endpoints report to the device manager and which have fallen out. Which log sources are flowing and at what retention.

All of that collapses into a flag. The control is passing.

The collapse destroys the information that matters most. Coverage — is this enforced on everything or on the subset the integration happened to check. Strength — hardware keys or SMS, two approvals or one, thirty days of logs or four hundred. Enforcement — technically prevented or merely required by a written policy. Exceptions — how many, for how long, on what.

Two organisations with identical dashboards can be in materially different security positions, and there is no artefact anywhere in this category that would reveal it. The enterprise buyer reading the certificate, the insurer pricing the risk, the platform benchmarking peers and any future efficacy study are all working with a variable that has been flattened to the point of meaninglessness.

The information was collected. It was thrown away at the last step.

## Why Nobody Has Built This

**Binary status is what the audit needs.** An auditor asks whether the control is implemented and the answer is yes or no. The product was built to produce audit artefacts and the flag is the artefact.

**Grading exposes customers.** A platform that reports implementation depth will show some customers as thinly compliant. Those customers passed their audit and will not welcome a score suggesting otherwise, and they are the ones paying.

**It complicates the sales promise.** The category's pitch is straightforward readiness — connect, remediate, certify. A graded measure introduces nuance into a product whose appeal is that it removes nuance.

**Comparability across integrations is real work.** Multi-factor authentication configuration looks different in each identity provider. Building a normalised representation across dozens of integrations is unglamorous engineering that no single customer asks for.

**Any score will be contested.** A proprietary depth score becomes a number customers optimise and competitors attack. Making it credible requires transparent methodology and probably external validation, which is more work than a flag.

**The framework did not ask for it.** Frameworks specify intent and auditors accept judgement. Nothing in the compliance apparatus requires depth to be measured, so nothing does.

## What to Build

**Retain the configuration detail.** Stop discarding what the integrations return. The corpus of actual configuration state across tens of thousands of organisations is the asset, and it is currently being reduced to a boolean and thrown away.

**Measure coverage explicitly.** For every control that applies to a population — accounts, repositories, endpoints, workloads — what fraction is actually covered. This is the single most valuable dimension and is directly computable. A control at sixty per cent coverage is not the same as one at a hundred, and today both are green.

**Grade strength against a published rubric.** Per control, the meaningful configuration distinctions, defined openly. Not a secret score — a stated rubric with the raw configuration behind it, so a customer or auditor can see exactly why a control graded where it did and disagree specifically.

**Separate enforced from asserted.** The largest and least examined distinction in the category: a control implemented as a technical configuration that cannot be bypassed, versus one implemented as a policy people are expected to follow. Both pass audits. They are not the same thing, and no platform reports which is which.

**Fold exceptions into the state.** Exception count, scope, age and renewal history as part of the control's measure rather than as free text alongside it. A control with a standing exception covering half the estate is not passing in any meaningful sense.

**Report what verification actually established.** For each control, what the platform's integration genuinely observed versus what the framework asked for. The gap is often substantial and is never disclosed — this is the honesty that would make the whole measure credible.

**Publish the rubric and invite attack.** The measure's value depends entirely on being trusted. Open methodology, external review and a willingness to revise are what separate this from another vendor score.

## Target Customer

Platform product leadership, where a defensible depth measure is a genuine differentiator in a category where the products have converged and compete on integration count.

Enterprise security buyers doing third-party assessment, who currently receive a certificate and would immediately use a coverage and enforcement breakdown.

Cyber insurers, who need exactly this as the independent variable for underwriting and currently work from questionnaire self-assertion.

## Impact If Built

The category acquires a variable that means something. Every downstream use — benchmarking, third-party assessment, underwriting, and any efficacy research — currently rests on a flag that conceals the differences that matter.

Coverage measurement alone would change customer behaviour immediately, because a control at sixty per cent coverage is visibly incomplete in a way a green tick is not.

And separating enforced controls from asserted ones would surface the most consequential distinction in compliance practice, which the entire apparatus currently treats as equivalent.
