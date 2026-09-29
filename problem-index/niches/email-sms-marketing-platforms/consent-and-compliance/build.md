# Consent You Cannot Prove

**Niche:** [[niches/email-sms-marketing-platforms/consent-and-compliance/profile|Consent & Regulatory Compliance]]
**Industry:** [[industries/email-sms-marketing-platforms|Email & SMS Marketing Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Consent provenance is frequently a timestamp and a source label, and the standard a court or a carrier asks for is what the subscriber actually saw and agreed to.
**Tags:** #compliance #workflow-orchestration #automation #evaluation-metrics #data-integration #descriptive-statistics #confidence-intervals #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to make consent provable and bulk sender requirements automatic rather than advisory — and whoever does that removes a litigation exposure and a delivery gate in the same product.

## The Problem
A brand is challenged over a text message. The platform's record says: number, timestamp, source equals website form. That is not proof of anything. It does not show what the form said, whether the consent checkbox was pre-ticked, what disclosures appeared, whether the number was typed by the person who owns it, or whether the consent covered marketing of this kind. In litigation, and increasingly in a carrier's assessment of a sender, the question is what the subscriber actually saw and agreed to, and almost no platform can answer it. The exposure is real, quantified in settlements, and the record was designed as an operational field rather than as evidence.

## Why Nobody Has Built This
Consent was modelled as an operational flag to decide whether to send, not as evidence to defend a claim — a design choice made before the enforcement environment existed and never revisited. Capturing form state and disclosure text requires instrumenting the brand's own site, which the platform does not own. Brands resist friction in the sign-up flow. And the cost arrives as a rare large event rather than as a continuous problem.

## What to Build
Capture consent as evidence. Record what the subscriber saw — the form, the disclosure text, the checkbox state, the page — at the moment of consent, which is the fix and is the difference between a record and proof. Store it immutably with a verifiable timestamp, since the defence rests on the record not having been altered. Capture the scope of consent, because consent for order notifications and consent for marketing are different and conflating them is a common and expensive error. Verify the subscriber controls the number or address through a confirmation step, which is both stronger evidence and better list quality. Track consent through its life, including changes of preference and withdrawal, so the current state is always defensible. Assemble an evidence package on demand, which is what a legal team actually needs and currently builds by hand under pressure. Enforce the bulk sender requirements as conditions rather than settings — authentication, one-click unsubscribe, complaint thresholds — since they now gate delivery and a platform that lets a sender violate them is failing them. Warn before a threshold is breached, which is the difference between an adjustment and a block. Audit existing lists for weak provenance, which most brands have never done and where the exposure is concentrated. And report a provable-consent rate, because a brand that cannot state what share of its list it could defend does not know its own exposure.

## Target Customer
Brand legal and compliance functions, messaging platforms carrying the reputational risk, and the lifecycle teams whose list quality determines delivery.

## Impact If Built
Consent was modelled as an operational flag before the enforcement environment existed and is asked to serve as evidence. Capturing what the subscriber actually saw, immutably, is the difference between a record and proof, and the same capture improves list quality.
