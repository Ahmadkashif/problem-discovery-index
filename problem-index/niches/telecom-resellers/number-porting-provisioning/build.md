# A Rejection Map of Every Losing Carrier

**Niche:** [[niches/telecom-resellers/number-porting-provisioning/profile|Number Porting & Provisioning Desk]]
**Industry:** [[industries/telecom-resellers|Telecom Resellers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Each porting desk learns, one rejection at a time, what each losing carrier rejects and how long it takes, and that knowledge is never pooled, though wholesale platforms see the rejections of thousands of resellers.
**Tags:** #large-language-models #logistic-regression #survival-analysis #feature-engineering #automation #data-integration
**Contested on:** Every serious competitor in this niche (wholesale and CPaaS porting APIs, porting-automation tools and outsourced porting desks) is fighting to get a port order to a firm order commitment on its first submission, and whoever matches the losing carrier's records most reliably before sending takes the account.

## The Problem
Losing carriers differ. One wants the service address exactly as printed on the bill. Another rejects any order where a feature change is pending. A third returns the same generic code for five different problems. Rural carriers may refuse ports outside a rate centre. A specialist at a small reseller meets each carrier a few times a year and relearns its habits each time.

## Why Nobody Has Built This
The data sits with wholesale carriers and CPaaS networks that file ports on behalf of thousands of resellers. They treat it as operational exhaust, not a product, and the rejection remarks are free text in inconsistent formats.

## What to Build
A platform-level model of losing-carrier behaviour, trained on every port the wholesale or CPaaS provider submits. It normalises rejection codes and remarks into a common set of reasons, learns each losing carrier's matching rules and the time it takes to confirm or reject by number type, and exposes both to resellers as a pre-submission check ("this carrier will reject: suite missing") and an expected FOC date. Every new rejection updates the map.

## Target Customer
Wholesale voice and CPaaS providers that run porting for resellers, and white-label UCaaS hosts. Both can offer it as a differentiator to their reseller base.

## Impact If Built
Every reseller on the platform benefits from the experience of all of them. First-time acceptance rises, and the platform can quote customers realistic dates instead of hopeful ones.
