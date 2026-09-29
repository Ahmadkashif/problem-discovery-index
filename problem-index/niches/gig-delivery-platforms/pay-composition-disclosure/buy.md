# Buy: Regulatory Reporting Tooling Adapted to Per-Offer Disclosure

**Niche:** [[niches/gig-delivery-platforms/pay-composition-disclosure/profile|Pay Composition Disclosure]]
**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Compliance and payroll reporting products disclose after the period closes; this disclosure has to happen in the offer payload, in under a second, before any work exists.
**Tags:** #compliance #workflow-orchestration #data-integration #descriptive-statistics #evaluation-metrics #automation #worker-facing #confidence-intervals
**Contested on:** Whether period-based compliance reporting infrastructure can serve a per-transaction, pre-decision disclosure obligation.

## The Problem

There is a mature market in compliance reporting: payroll systems that produce itemised statements, regulatory reporting platforms that file to jurisdictional requirements, and policy engines that apply differing rules by geography. A platform facing pay disclosure obligations will look here first, reasonably.

Every one of these products operates on a closed period. Work happened, amounts are known, a statement is produced and filed. The obligation in this industry is the opposite shape: the disclosure has to appear inside the offer, before the courier decides, at the latency of the offer path, for work that has not occurred and whose components include estimates that may change.

## What Already Exists

Payroll and contractor payment platforms with itemised statement generation and 1099 handling. Regulatory reporting products for jurisdictional filings. Rules and policy engines — both general-purpose and compliance-specific — capable of evaluating geographic rule sets. Audit logging and evidence retention products. Consent and disclosure management tooling from the privacy domain, which is the closest analogue in shape.

## The Customization Gap

**Pre-decision, not post-period.** The disclosure's entire purpose is to inform a choice that happens before the work. That places it in the offer construction path with a latency budget in the tens of milliseconds, which is not where any compliance product lives. The policy evaluation has to be inlined and cached rather than run as a batch job.

**The disclosed quantities include an estimate that can change.** A payroll statement discloses facts. An offer discloses a tip component that the customer may adjust afterwards. Representing a disclosed-but-conditional amount — and reconciling the disclosure against the realised value after delivery — has no analogue in payroll, and it is precisely the component with the contested history.

**Jurisdiction resolves per offer, not per employee.** A courier may cross a municipal boundary mid-shift, and the applicable minimum earnings standard or disclosure requirement can differ on either side of it. Payroll assigns a work location per employee per period. The offer path has to resolve jurisdiction geographically at construction time, which is a different data model.

**Minimum earnings standards are a constraint on the offer, not a check on the statement.** Where a jurisdiction sets a floor on earnings per engaged hour, the correct implementation adjusts or blocks offers that would breach it and reconciles at period end. Compliance products verify after the fact; this has to bind before.

**The audit unit is an offer, and the volume is enormous.** Millions of offers a day, each needing its components, the policy applied and the rendering retained for a statutory period. Compliance evidence stores are sized for periodic filings, not for per-transaction records at that cardinality, and the retention economics have to be designed rather than bought.

## Target Customer

Platform compliance engineering teams building to newly arrived jurisdictional requirements and discovering that the payroll or reporting vendor they engaged cannot operate inside the offer path. Also the compliance vendors themselves, for whom pre-decision per-transaction disclosure is a genuine product gap as platform-work regulation spreads.

## Impact If Solved

The bought layer handles jurisdictional rule management, audit retention and period reconciliation, and the platform owns the inline policy evaluation in the offer path. The practical outcome is that a platform can enter a newly regulating jurisdiction with a configuration change instead of an engineering fork — which is the difference between compliance being a cost of expansion and a barrier to it.
