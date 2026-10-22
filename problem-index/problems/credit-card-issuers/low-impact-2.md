# Dispute Intake to Network Reason Code

**Industry:** [[credit-card-issuers|Credit Card Issuers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Case-management software can log a dispute; it cannot turn a cardholder's account of what went wrong into the right network reason code, evidence request and Reg Z clock on the first call.
**Tags:** #large-language-models #bert #transformers #evaluation-metrics #compliance #workflow-orchestration #automation

## The Problem
Cardholders disputed $9.8B of card charges in 2024, producing $5.9B of chargebacks (CFPB). Each dispute starts as a story told to an agent or typed into an app: "I cancelled this subscription in March", "the hotel charged me twice", "I never got the sofa", "I don't recognise this". The agent has to decide what kind of dispute it is — fraud, authorisation, processing error or consumer dispute in Visa's grouping, with Mastercard's own reason codes — because the category decides what evidence the cardholder must supply, whether a provisional credit is due, which network window applies and what the merchant can rebut. Under Reg Z 1026.13 the issuer has to acknowledge a billing-error notice within 30 days and resolve it within two complete billing cycles, never more than 90 days, and cannot collect or adversely report the disputed amount meanwhile.

Misclassification at intake is the expensive error. A "not as described" claim coded as fraud gets a new card issued and loses the chargeback when the merchant shows the cardholder's own device and address; a recurring-billing dispute coded as a consumer dispute without the cancellation date can't be charged back at all. The case then ends as a write-off, or as a denial that becomes a complaint.

## What Already Exists
General case-management and CRM platforms (Salesforce Financial Services Cloud, Pega, ServiceNow), contact-centre platforms, the networks' dispute portals (Visa Resolve Online, Mastercom), and processor-embedded dispute modules. Specialist dispute software such as Quavo exists and is concentrated among banks and credit unions.

## The Customisation Gap
The card-specific layer is the translation: mapping a free-text or spoken narrative, together with the transaction record (card-present or not, recurring flag, merchant category, authorisation data), to the correct network reason code and condition; generating the right evidence questions for that code; deciding provisional-credit eligibility; setting both the Reg Z deadlines and the network's chargeback and pre-arbitration windows; and flagging the narratives that read like first-party misuse — a Quavo-sponsored survey in 2026 found nearly four in ten consumers admitting to a dispute they later realised may not have been valid — for a lighter-touch check before a fraud reissue. Network rules change twice a year, so the mapping has to be maintained, not configured once.

## Impact If Solved
Getting the reason code and evidence right on first contact raises chargeback recovery, cuts write-offs and repeat contacts, and gives the issuer a clean record of every Reg Z deadline it met — the record an examiner asks for when a dispute becomes a complaint.
