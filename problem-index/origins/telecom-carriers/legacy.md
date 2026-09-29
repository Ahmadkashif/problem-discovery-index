# Legacy: What Telecom Carriers Bequeathed

**Origin:** [[origins/telecom-carriers/profile|Telecom Carriers]]

## The Direct Inheritance

Every business with a recurring subscriber relationship inherited the churn model, usually without knowing where the pattern came from.

| Child | What it inherited |
|---|---|
| [[industries/crm-platforms\|CRM Platforms]] | The propensity score as a native object. Every modern CRM's "health score" or "risk of churn" field is the Mozer model, packaged as a feature rather than a research result. |
| [[industries/customer-support-platforms\|Customer Support Platforms]] | The complaint record as a predictive signal, not just a ticket to close. Support history was one of the four inputs joined in the original 47,000-subscriber dataset, and it still is. |
| [[industries/subscription-commerce\|Subscription Commerce]] | The retention-offer logic wholesale: predict who is leaving, price an incentive against their remaining value, act before cancellation. |
| [[industries/streaming-video-platforms\|Streaming Video Platforms]] | The same recurring-revenue exposure telecom faced first — a subscriber who can cancel with one click instead of one phone call — and the same answer, watch-time and engagement in place of minutes and complaints. |
| [[industries/membership-community-platforms\|Membership & Community Platforms]] | Renewal as the default and cancellation as the event to predict, at a much smaller scale than a national carrier but the identical shape of problem. |

## The Deeper Inheritance: behaviour as a leading indicator

Before telecom, the record of what a customer had already done was mostly used to bill them, or to decide whether to extend them credit. The Mozer-era insight — that the same operational exhaust could be joined and read forward as a prediction of what the customer would do **next** — is now assumed by default in almost every subscription business in this vault. It was not obvious in 1999; it required someone to notice that four unrelated back-office systems, joined at the subscriber level, already contained the answer.

That is the origin of every "health score," "propensity to churn," and "customer lifetime value" model in the index — a lineage broader than the five children named above, running quietly through the vault's software-as-a-service, gym, and lending-relationship notes as well.

## The Second Inheritance: a market manufactured by regulation

Churn was not a discovery telecom made about human nature. It was a problem regulation created by removing a monopoly and replacing it with a market. [[origins/retail-banking/profile|Retail Banking]] bequeathed rails that outlived their constraint; telecom bequeathed a *competitive structure*, manufactured on a specific date, that made a previously irrelevant number — will this customer still be here next month — into the number that decided which companies survived.

## What an Episode Should Take From This

1. **The data existed before the question did.** Billing, usage, credit and complaints were all recorded for other reasons. The churn model is what happens when someone finally asks a new question of old records.
2. **A market has to be manufactured before a retention problem exists.** Monopolies do not need churn models. Telecom's is a case where regulation, not technology, created the business problem technology then solved.
3. **The dollar framing is the whole reason this survived.** A 2%→1% churn reduction stated as "$54M a year" is what got budget approved. A modelling exercise stated only in precision and recall would not have.

**Sources:** See [[origins/telecom-carriers/the-mechanism|The Mechanism]] and [[origins/telecom-carriers/the-fight|The Fight]] for full citations; Mozer et al., IEEE Trans. Neural Networks 11(3), 2000.
