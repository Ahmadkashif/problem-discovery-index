# Reg E Dispute Processing

**Industry:** [[neobanks|Neobanks]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Disputes arrive as a member's free-text description of what went wrong and must become a coded claim against a network deadline, and the clock does not adjust for volume.
**Tags:** #bert #large-language-models #gradient-boosting #k-nearest-neighbors #evaluation-metrics #feature-engineering #compliance #workflow-orchestration

## The Problem
A member reports a transaction they did not authorise, or a merchant that never delivered, or a subscription they cancelled and were billed for anyway. Regulation E gives the institution ten business days to investigate before provisional credit is owed, forty-five in total, ninety for new accounts and certain transaction types. The network chargeback rules run on their own timetable with their own reason codes and their own evidence requirements, and those two regimes do not line up.

The member's description arrives as a sentence in an app. Somebody must decide whether this is unauthorised use, a merchant dispute, a processing error or a member misunderstanding their own statement — categories that carry different obligations and different economics. Then the claim must be filed under the correct network reason code, with the evidence that code requires, within the network's window rather than Reg E's.

Volume is seasonal and spiky. A single merchant going out of business, a data breach, or a subscription service changing its billing descriptor produces hundreds of related claims in a week. The deadline is per-claim and absolute, and missing it means eating the loss.

A sizeable fraction of claims are first-party — the member did authorise it, or a family member did — and distinguishing those from genuine fraud, without accusing a customer, is the judgement the whole process turns on.

## What Already Exists
Quavo, Pega and Ethoca-adjacent tooling automate parts of the chargeback lifecycle. Networks provide dispute portals and Visa's VCR and Mastercard's Mastercom structure the filing. Provisional credit is usually automated at a threshold. Most institutions have written decision trees.

## The Customisation Gap
Classification from the member's own words is the first unautomated step and the one that determines everything after it. The same claim described three ways routes three ways. Institutions have tens of thousands of historical claims with their eventual disposition attached — recovered, written off, denied, represented successfully — which is a directly supervised classification problem nobody treats as one.

First-party misuse detection is the substantive gap. The signals are present in the institution's own data: device and location at the time of the transaction matched to the member's pattern, merchant relationship history, prior claim frequency, the specific phrasing used. Institutions handle this with a blunt count of prior claims, which punishes members with genuinely compromised cards and misses the pattern that actually distinguishes the cases.

Evidence assembly per reason code is mechanical and manual — pulling the authorisation record, the device fingerprint, the delivery confirmation, the cancellation email the member forwarded — and the representment success rate depends almost entirely on whether it was assembled well.

Nothing forecasts the queue. A merchant failure is visible in the institution's own transaction data days before the claims arrive, which is enough time to staff for it.

## Impact If Solved
Dispute operations scale linearly with cardholders and are staffed to peak, and the deadlines are regulatory rather than negotiable. Classifying claims from the member's description, assembling evidence per reason code and separating first-party misuse on behavioural evidence rather than claim count addresses the three places where the cost and the unfairness both sit.
