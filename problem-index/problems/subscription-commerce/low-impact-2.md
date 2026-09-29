# Skip, Pause and Swap Flexibility

**Industry:** [[subscription-commerce|Subscription Commerce]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every subscription platform supports skip, pause and swap, and companies bury them because they appear to reduce revenue — which is how a customer who wanted to skip one delivery cancels instead.
**Tags:** #survival-analysis #gradient-boosting #causal-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #logistic-regression #revenue-impact

## The Problem
A customer has too much of the product, is going away, or wants something different this month. The options that would keep them subscribed — skip this delivery, pause for two months, swap an item — all exist in the platform.

They are frequently hard to find. The reasoning is straightforward and wrong: a skipped delivery is revenue not taken this month, so making skips easy looks like making revenue optional. Product teams optimise the account page toward retention of the next charge rather than toward retention of the customer.

The result is that a customer whose need was "not this month" arrives at the cancel button, because that was the option they could find. Cancellation is permanent and skipping is not, and the company has traded a deferred charge for a lost customer.

The same reasoning appears in the cancel flow, where a pause offer is presented as a retention save after the customer has decided rather than as a normal option before they had to.

Nobody in the category seems to have measured this properly. Whether easy skips increase or decrease lifetime value is a straightforward experiment, and the belief that they decrease it is held on intuition.

## What Already Exists
Skip, pause, swap, delay and cadence change are supported by Recharge, Ordergroove, Skio and every serious subscription platform. Customer portals expose them to varying degrees. Cancel flows with pause offers are a standard pattern. SMS and email management of upcoming deliveries is common. Some platforms report skip rates.

## The Customisation Gap
The capability exists and the policy question is unanswered. What surfacing flexibility does to lifetime value is testable and untested, so the design is set by a revenue instinct that may be exactly backwards.

Proactive offering is the larger unexploited move. A customer whose skip pattern indicates accumulation should be offered a cadence change before they cancel, not after. That prediction is available from their own behaviour and nothing acts on it.

Cadence optimisation as a product feature barely exists. Most subscriptions offer a small set of intervals chosen for operational convenience, and the right interval varies per customer and is inferable from their skip and swap behaviour.

Pause quality is the fourth gap. A paused customer is a retained one only if they return, and what happens during a pause — communication, timing of the return prompt, whether the return is easy — determines whether they do. Most companies treat a pause as an absence and do nothing.

## Impact If Solved
Flexibility is the mechanism that converts a temporary mismatch into a continued subscription, and it is deliberately obscured on a belief nobody has tested. Measuring the effect properly and offering the right flexibility proactively addresses a large share of cancellations that were never really about wanting to leave.
