# Control State Normalisation

**Parent Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Category:** Contested Sub-Niche
**Contested on:** Whether "this control is implemented" means anything comparable across two organisations, or describes configurations with nothing in common.

## Profile

**Market Size:** ~$990M
**Share of Parent Industry:** ~11%
**Digital Adoption:** Very low — a pass flag
**Target Buyer:** Platform product leadership, enterprise security buyers, auditors
**Automation Potential:** Very high — the raw configuration data is already collected

## What Makes This a Distinct Niche

This is the independent variable. Before anyone can ask whether controls work, control implementation has to be a comparable quantity, and it is not.

A framework specifies intent — access is restricted to authorised personnel, changes are reviewed before deployment, systems are monitored for anomalous activity. A platform verifies whatever its integrations can observe and marks the control passing. Two organisations passing the same control may have enforced multi-factor authentication on every account with hardware keys and conditional access, or enabled it on the administrator group with SMS fallback and a standing exception list. Both are green. Both count identically in a readiness percentage and in any analysis built on it.

This is separable from its sibling in every operational respect. [[niches/grc-compliance-platforms/outcome-linkage/profile|🎯 Outcome Linkage]] needs data the platform does not hold, from parties who will not give it, over years, and produces a commercially awkward answer. Normalisation is entirely internal to the platform's own corpus, produces a better product immediately in the form of a defensible maturity measure, and can be validated against expert review this quarter.

The contest is over whether a graded measure of implementation can be derived from integration data without becoming a proprietary score nobody trusts. Whoever produces one that auditors and buyers accept defines how this market describes itself.

## Current Tools & Gaps

Binary or near-binary control status — passing, failing, in remediation, with an exception. Some platforms distinguish partial implementation coarsely. Exceptions and compensating controls are recorded as free text and are not comparable at all. Benchmarking against peers compares pass rates, which compares the flags rather than what they represent.

The gaps are large and unusually tractable, because the underlying data is already collected. Configuration detail flows through the integrations and is discarded once the control is marked. Coverage is not measured, so a control enforced on ten per cent of the estate and on a hundred per cent look the same. Exception volume and duration are not aggregated into the control's state. Nothing distinguishes a control implemented by enforced technical configuration from one implemented by a written policy, which is the largest and least examined difference in this whole category. And no platform reports what its own verification actually establishes versus what the framework asked for.

## Problems

- [[niches/grc-compliance-platforms/control-state-normalisation/build|🔨 Build: A Graded Implementation Measure]]
- [[niches/grc-compliance-platforms/control-state-normalisation/buy|🛒 Buy: Maturity Modelling With Actual Inputs]]
- [[niches/grc-compliance-platforms/control-state-normalisation/fix|🔧 Fix: Green Means Whatever the Integration Could See]]
