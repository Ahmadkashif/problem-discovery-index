# Nobody Monitors What the Counterparty Owes Us

**Niche:** [[niches/contract-lifecycle-platforms/obligation-performance-monitoring/profile|Obligation Performance Monitoring]]
**Industry:** [[industries/contract-lifecycle-platforms|Contract Lifecycle Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Obligation management is framed entirely around what the company must do, and the money is usually in what the counterparty committed to and has not delivered.
**Tags:** #descriptive-statistics #time-series-forecasting #hypothesis-testing #confidence-intervals #evaluation-metrics #revenue-impact #quick-win #data-integration
**Contested on:** Every serious competitor here is fighting to join contract terms to operational reality and say whether a commitment is actually being met — and whoever does that takes the commercial function, because knowing the obligation and knowing whether it is honoured are different products and only the first exists.

## The Problem
A supplier contract commits the vendor to a service level with credits for breach, quarterly business reviews, an annual security attestation, a price reduction at a volume threshold the company passed eight months ago, and a right to audit. None of it is monitored. The company has not claimed a credit in three years despite outages it can document, has not received the price reduction it is entitled to, and has never exercised the audit right. The vendor is not behaving badly; nobody on the customer's side is watching, and the vendor has no obligation to volunteer it.

## Why It's Still Broken
Obligation management arrived through legal and compliance, whose framing is what the company must do to avoid breach, so inbound obligations were never the design centre. The benefit is also diffuse across procurement, finance and the business unit, with no single owner, so nobody builds the process. And claiming against a supplier feels adversarial to the person who manages the relationship, which is a genuine consideration and is also how a great deal of money is left on the table.

## What a Fix Looks Like
Extract and monitor the counterparty's obligations with the same machinery as the company's own, and account for the money. Identify inbound commitments during extraction — service levels with credits, price and volume terms, reporting and review obligations, attestations, most-favoured-nation and benchmarking rights, audit rights — as a distinct category. Monitor the measurable ones against the systems that know: outages against monitoring, volumes against purchasing, prices against invoices, which is where the volume-threshold discounts turn up. Track the evidenced ones by whether the artefact arrived, since a missing quarterly report is trivially detectable and frequently goes unremarked for years. Quantify accrued entitlements in money — credits available, overpayments against contracted pricing, discounts not applied — which is what turns this from a compliance list into a recovery programme with a number attached. Alert before claim deadlines expire, since most credit regimes require a claim within a window and the entitlement is lost silently. And give the relationship owner the evidence and the choice, because whether to claim is a commercial judgement and the current position is not a judgement at all but an absence of information.

## Who Feels the Pain
Procurement and finance paying more than the contract requires; business units accepting service that breaches a level they are entitled to; and companies whose supplier contracts contain protections nobody has ever used.

## Impact If Fixed
Inbound obligations are extracted by the same process as outbound ones and simply ignored, which makes this a framing gap rather than a technical one. Quantifying accrued entitlements and alerting before claim windows close produce recoverable money rather than a compliance report.
