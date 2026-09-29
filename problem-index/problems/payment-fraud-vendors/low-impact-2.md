# Chargeback Representment Evidence

**Industry:** [[payment-fraud-vendors|Payment Fraud Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Disputing a chargeback means assembling the evidence the network's reason code requires within its deadline, and most of it is assembled by hand for a case that is frequently unwinnable.
**Tags:** #bert #large-language-models #gradient-boosting #k-nearest-neighbors #evaluation-metrics #feature-engineering #compliance #workflow-orchestration

## The Problem
A chargeback arrives with a network reason code. The merchant may contest it by submitting evidence, and what constitutes evidence depends entirely on the code: proof of delivery for a non-receipt claim, authentication records for an unauthorised claim, cancellation policy and acknowledgement for a subscription dispute, product description and communications for a not-as-described claim.

The evidence lives in several systems — order management, shipping carrier, authentication logs, customer support, email — and is assembled into a document within a deadline measured in days.

Win rates are modest and highly variable by reason code and by issuer. Some categories are close to unwinnable, and merchants spend effort contesting them anyway because the decision of what to contest is made by a rule about amount rather than by an estimate of probability.

First-party misuse is the frustrating majority in many merchant categories. The cardholder did make the purchase and has disputed it, and the evidence that would prove this — device, location, account history, prior orders, delivery confirmation to a known address — is available and frequently not compelling to an issuer working through volume.

Deadlines are absolute, volume is spiky, and the same evidence is assembled the same way every time.

## What Already Exists
Chargeback management platforms (Chargebacks911, Midigator, Justt, Kount's dispute tooling) automate parts of assembly and submission. Network portals structure filing. Visa's Order Insight and Mastercard's Ethoca provide pre-dispute deflection by giving issuers order detail at the moment of enquiry. Guarantee providers handle representment on the merchant's behalf.

## The Customisation Gap
Win probability is not predicted. Every representment is a decision to spend effort, the merchant has a history of outcomes by reason code, issuer, amount band and evidence type, and the choice of what to contest is made by an amount rule. Predicting the win probability before assembling is straightforward and would redirect effort from unwinnable cases to marginal ones.

Evidence selection is templated rather than optimised. Which specific items persuade for a given reason code and issuer is learnable from outcomes, and merchants submit the same bundle regardless.

Narrative quality is unmeasured and matters. The cover argument is read by a human under time pressure, and generating a clear, specific, evidence-anchored narrative is a natural language task with a measurable outcome attached.

Deflection is underused. Pre-dispute resolution through Order Insight and Ethoca is far cheaper than representment and depends on having order detail available at the enquiry moment, which is a data plumbing problem more than anything else.

And nothing feeds back. Chargeback outcomes are evidence about the original approval decision, about the merchant's descriptor and policies, and about which customers dispute — and they are handled as a recovery workflow rather than as signal.

## Impact If Solved
Representment is a deadline-driven assembly process with a modest and variable success rate, staffed to peak and spent substantially on cases that cannot be won. Predicting win probability, learning which evidence actually persuades and investing in pre-dispute deflection converts effort into recovery and turns the outcomes into signal the fraud model never receives.
