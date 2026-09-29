# Buy: Referral Management Products Adapted to a Platform Outside the Network

**Niche:** [[niches/telehealth-platforms/care-coordination/profile|Care Coordination & Referral Closure]]
**Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Referral management and care coordination software works inside a health system where both ends are on the same network; a telehealth platform is outside every network it refers into.
**Tags:** #workflow-orchestration #data-integration #compliance #evaluation-metrics #confidence-intervals #automation #descriptive-statistics #gradient-boosting
**Contested on:** Whether referral closure tooling that assumes a shared network can work when the referrer shares nothing with the recipient.

## The Problem

Referral management is a real product category. Health systems and ACOs buy software that routes referrals, tracks their status, manages authorisation and reports leakage, and the better products close the loop reliably within the system.

They work because both ends are inside one organisation or one contracted network, on connected systems, with a shared incentive to keep the patient. A telehealth platform refers to specialists it has no relationship with, whose systems it does not touch, in networks it is not part of, for patients it may never see again. Every mechanism the products rely on is absent.

## What Already Exists

Referral management and closed-loop referral products, care coordination platforms serving health systems and ACOs, prior authorisation automation vendors, e-prescribing with dispense reporting, lab ordering interfaces, and the interoperability frameworks. Patient engagement and messaging tools.

## The Customization Gap

**Closure has to be inferred rather than received.** In-network products get a status from the receiving system. Here closure comes from a patchwork — dispense notifications, returned results, payer portal statuses, exchange queries, and the patient's own report — each partial. Combining them into a confident closure determination, with an explicit unknown state, is the core adaptation.

**The patient is the primary closure channel and the products underuse them.** In-network tools treat patient outreach as a reminder mechanism. Here the patient is frequently the only party who knows whether they attended, which makes well-timed, one-tap confirmation a first-class data source rather than a nudge.

**There is no network to manage leakage against.** Leakage reporting assumes preferred providers and a financial interest in keeping referrals inside. A telehealth platform's interest is that the patient gets seen anywhere, which changes the metric from leakage to completion and removes the steering logic entirely.

**Prior authorisation has to work without an institutional payer relationship.** Authorisation automation vendors integrate on behalf of provider organisations with established payer connections. A platform operating across many states and payers with a contractor workforce has a much wider and thinner set of relationships, and the automation coverage is correspondingly patchier.

**Prioritisation matters more because the volume per coordinator is higher.** Health system coordinators work a panel. A platform coordinator faces open items across thousands of episodic patients, which makes predictive prioritisation the difference between a workable queue and an impossible one — and no referral product predicts failure.

## Target Customer

Platform operations teams evaluating care coordination software and finding it assumes a network. Also the referral management vendors, for whom out-of-network episodic referrers are an emerging segment with a genuinely different closure model.

## Impact If Solved

The workflow, task management and authorisation integrations get bought, and the inferred closure, patient-as-channel, completion-not-leakage framing, thin payer relationships and predictive prioritisation get built. Concretely: a platform that can say what share of its referrals were completed, which nobody in this industry currently can.
