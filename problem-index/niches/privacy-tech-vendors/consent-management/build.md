# Build: Measuring Whether They Understood

**Niche:** Consent Management
**Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Comprehension measurement for consent interfaces — using the interaction telemetry these platforms already collect to establish whether people understood what they agreed to, and optimising toward that.
**Tags:** #evaluation-metrics #hypothesis-testing #confidence-intervals #logistic-regression #bayesian-inference #gradient-boosting #compliance #worker-facing
**Contested on:** Whether the consent record reflects an informed choice, or an interface optimised until enough people clicked accept.

## The Problem

Consent is legally meaningful only if it is informed. The entire apparatus — the banner, the record, the audit trail — exists to demonstrate that a person made an informed choice.

Nobody measures whether they did. The metric the industry runs on is acceptance rate, which is a measure of interface effectiveness at producing a click. A banner can drive acceptance to ninety-five per cent through design choices that have nothing to do with understanding, and the resulting consent records are indistinguishable from records of genuinely informed choices.

The telemetry to measure the real thing is already being collected. These platforms see how long someone looked at the banner before acting, whether they opened the detail panel, how far they scrolled, whether they toggled individual purposes, whether they hesitated, and what they did on subsequent visits. Every one of those is evidence about engagement with the choice, and all of it is currently used — where it is used at all — to improve acceptance.

Regulators have been converging on interface design for years precisely because they cannot measure comprehension either, so they regulate the patterns as a proxy. A measure of actual comprehension would be a better instrument than any list of prohibited designs.

## Why Nobody Has Built This

**The customer is optimising for the other thing.** Consent platforms are bought partly by marketing operations, whose interest is acceptance. A product measuring comprehension is measuring something its buyer is not asking for and may find inconvenient.

**A comprehension measure would expose the current position.** Establishing that most consents are given without engagement is a finding about every customer's banner and about the vendor's own optimisation features.

**Comprehension is hard to define operationally.** Understanding what you agreed to is a mental state. Proxies — engagement, recall, ability to state what was accepted — are measurable and contestable, and defining them invites argument.

**Measurement requires asking some users.** The strongest measure involves surveying people shortly after they consented about what they think they agreed to, which costs conversion and requires a customer willing to do it.

**No regulator requires it.** Compliance is assessed against interface patterns and record-keeping. A vendor that measures comprehension gains no compliance credit, so the investment has no regulatory return.

**Acceptance is the number in every sales conversation.** Vendors compete partly on the acceptance rates their banners achieve, which makes comprehension an awkward thing to start measuring.

## What to Build

**Derive an engagement measure from existing telemetry.** Time to decision, detail panel opening, scroll depth, per-purpose toggling, hesitation and revisit behaviour, combined into a measure of how much attention the choice received. This requires no new collection and produces the first quantitative account of how consent is actually given.

**Validate it against comprehension studies.** Periodically survey a sample of users shortly after consenting about what they believe they agreed to, and use the results to calibrate the telemetry-derived measure. This is the step that turns a proxy into something defensible, and it is standard practice in every field that measures understanding.

**Report the distribution, not just the rate.** Of consents obtained, what proportion were given with meaningful engagement. A customer with ninety per cent acceptance and three per cent engagement is in a very different legal position from one with sixty per cent acceptance and thirty per cent engagement, and today they look identical.

**Point the optimisation tooling at informed choice.** The same experimentation machinery that tests banner variants for acceptance can test them for comprehension. A vendor offering to optimise for informed consent rather than for acceptance would be selling something genuinely different and defensible.

**Verify the vendor list against reality.** Check that the third parties named in the banner match those actually receiving data, using the observation from [[niches/privacy-tech-vendors/data-flow-observation/profile|🎯 Data Flow Observation]]. A consent that names ten vendors while fourteen receive data is not consent to the four.

**Make withdrawal as easy as granting and measure the asymmetry.** The difficulty differential between accepting and withdrawing is measurable in clicks and time, is regulated in several jurisdictions, and is not reported by any platform.

**Publish aggregate research.** The vendors hold the largest consent interaction dataset in existence. Publishing aggregate findings about what designs produce genuine engagement would be a substantial contribution and a strong position to hold as regulation tightens.

## Target Customer

Privacy counsel rather than marketing operations — the buyer for whom a defensible consent position matters more than the acceptance rate, and who is increasingly the one answering for it.

Organisations under regulatory attention, where demonstrating informed consent rather than merely recording consent is worth real money.

Regulators and researchers as the audience for the aggregate work, which is where a vendor could establish the measure as the standard.

## Impact If Built

Consent acquires a quality measure. The industry currently has a quantity measure and treats it as though it answered the legal question, which it does not.

Optimising for comprehension rather than acceptance would change what these platforms are for, and would give the customers who want to do the right thing a way to demonstrate it.

And a validated comprehension measure would be a better regulatory instrument than pattern prohibition — regulators regulate interface designs because they cannot measure understanding, and a measure would let them regulate the outcome instead.
