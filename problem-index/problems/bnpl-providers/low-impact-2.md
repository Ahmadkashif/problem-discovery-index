# Dispute and Refund Handling Under Reg Z

**Industry:** [[bnpl-providers|BNPL Providers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The provider sits between a merchant's return policy and a consumer's instalment schedule, and must reconcile two systems that were never designed to talk.
**Tags:** #bert #large-language-models #gradient-boosting #k-nearest-neighbors #evaluation-metrics #feature-engineering #compliance #workflow-orchestration

## The Problem
A consumer returns an item. The merchant processes the return on its own timetable — inspection, restocking, refund issuance — which may take three weeks. Meanwhile the instalment schedule continues, and payment two and three are debited from the consumer's account for a product sitting in a warehouse.

The provider is in the middle. It did not sell the item, it does not control the return, and under the CFPB's 2024 interpretive rule it carries Regulation Z obligations on disputes and refunds that resemble a credit card issuer's. The consumer contacts the provider because the provider is the one taking the money.

The mechanics are fiddly. A partial return changes the instalment amounts, which changes the schedule, which changes what has already been paid versus what is owed. A refund arriving after the plan is fully paid has to be returned to the consumer's card rather than applied to a balance. A refund arriving mid-plan can be applied to the remaining instalments or returned, and the two produce different consumer experiences and different complaint rates. Merchant refund files do not always identify which plan they correspond to.

The consumer, meanwhile, is being debited for something they returned, and their view of who is at fault is not subtle.

## What Already Exists
Providers operate dispute flows and pause mechanisms. Merchant integrations include refund APIs that, when used correctly, notify the provider. Card network dispute rights apply to the underlying funding instrument. Case management tooling is standard. The interpretive rule made the obligations explicit.

## The Customisation Gap
Refund-to-plan matching is the mechanical core and is frequently manual. A merchant's refund file gives an order reference, an amount and a date; joining that to the right plan, with partial amounts and multiple items, is entity matching that falls to an operations team when the reference does not match cleanly.

Nothing predicts the return. Return probability is estimable from merchant category, item type, basket composition and the consumer's own history, and a plan on a basket with an eighty percent return rate could be scheduled differently. Providers treat all plans identically.

Schedule adjustment logic is rule-based and produces the complaints. Whether to shorten the plan, reduce each instalment, or refund to the card is a consumer-experience decision with measurable downstream effects on complaints and retention, and it is set by a default nobody has tested.

Complaint classification from consumer narratives is unautomated, which matters because complaint themes are the earliest signal of a merchant whose return handling is failing — the provider sees that pattern across merchants before any individual merchant does.

## Impact If Solved
Refund and dispute handling generates a disproportionate share of complaints, regulatory attention and support cost relative to its transaction share, and most of it is mechanical reconciliation between two systems with different clocks. Automating refund-to-plan matching and choosing schedule adjustments on measured consumer outcomes removes the situation that produces the sector's most damaging consumer stories.
