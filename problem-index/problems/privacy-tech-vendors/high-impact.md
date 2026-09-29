# Consent Measured on Acceptance, Never on Understanding

**Industry:** [[privacy-tech-vendors|Privacy Tech Vendors]]
**Type:** High Impact
**One-liner:** The consent record satisfies an audit, the banner was optimised for acceptance, and whether the person understood what they agreed to is measured by nobody.
**Tags:** #causal-inference #hypothesis-testing #bayesian-inference #confidence-intervals #gradient-boosting #cnns #evaluation-metrics #compliance

## The Problem
Consent management platforms present an interface, record a choice, and produce a log that demonstrates consent was obtained. The customer configures the interface, and the configuration is chosen to maximise acceptance because acceptance determines how much data the business can use.

Regulators across several jurisdictions have addressed the resulting designs repeatedly and consistently: interfaces where rejecting takes more steps than accepting, where the reject option is visually de-emphasised, where choices are pre-ticked or bundled, where continuing to browse is treated as agreement. The findings have accumulated into a body of decisions that the industry tracks and adapts to, in a cycle where each round of enforcement produces a new design that complies with the letter of the finding.

The substantive question is not addressed by any of this. Valid consent is meant to be informed, specific and freely given, and nobody measures whether the person who clicked accept knew what they were agreeing to. Acceptance rate is measured to two decimal places; comprehension is not measured at all.

The vendor's position distributes the responsibility neatly. The platform supplies a configurable banner and the customer chooses the configuration, so a design that a regulator later finds non-compliant is the customer's choice made with the vendor's tool. That is contractually sound and leaves the industry's central question unowned.

The consequence is a large apparatus producing records whose legal sufficiency is contested and whose substantive meaning is unexamined — while users experience a daily interruption that most have learned to dismiss without reading, which is the clearest possible evidence about the consent being obtained.

## Why It's Unsolved
Measuring comprehension is genuinely harder than measuring clicks, and it requires asking users something rather than observing them. Survey-based comprehension measurement is possible, has been done in academic work, and is not something a vendor has commercial reason to build — because the finding would be that comprehension is low and that the product producing the consent record is producing records of something other than informed agreement.

The commercial gradient is explicit here rather than implicit. Vendors compete partly on acceptance rates achieved, customers buy on that basis, and a vendor that optimised for informed choice would report lower acceptance and lose deals. This is the clearest incentive conflict in the category and everyone in it knows.

The regulatory approach has also focused on interface mechanics rather than outcomes, which is understandable — mechanics are observable and auditable — and has produced an adaptation cycle rather than a change in substance.

And the alternative designs are not obvious. An interface that genuinely conveys what data is collected, by whom and for what, to a person who wants to read an article, is a real design problem with no established good answer, and the industry has had little reason to work on it.

## What a Solution Looks Like
Measure comprehension directly, with a sampled panel. Asking a small random sample of users, after the fact, what they believe they agreed to — and comparing that to what was actually recorded — produces the first empirical measure of consent validity that anyone would have. It is cheap, it is achievable, and the finding would be uncomfortable, which is why it would have to be built by someone whose product is not acceptance rate.

Test designs against understanding, not acceptance. Interface variants can be evaluated on whether users can subsequently state what they agreed to, which is a different optimisation from the one being run and would produce visibly different interfaces.

Measure the dark pattern properties the regulators actually rule on, automatically. Relative prominence, click-depth asymmetry between accept and reject, default states, bundling and pre-selection are all computable from the rendered interface, and a vendor could score its own customers' configurations against the accumulated body of decisions and tell them where they sit. That is a product feature that would sell on risk reduction rather than on acceptance.

Report both numbers. A platform that reported acceptance rate alongside a comprehension estimate and a design risk score would change what customers can buy on — and would be the only party in the chain with an interest in the second number.

## Impact If Solved
Consent is the legal foundation for a substantial share of the data economy, it is obtained through interfaces optimised against the standard they are meant to satisfy, and its substantive validity has never been measured. A sampled comprehension measure and an automated design risk score against the regulatory record would give customers something to manage other than acceptance — and would give the first vendor to publish it a genuinely defensible position as enforcement continues to tighten.
