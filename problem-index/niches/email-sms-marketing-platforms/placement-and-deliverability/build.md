# Delivered Is Not Placed

**Niche:** [[niches/email-sms-marketing-platforms/placement-and-deliverability/profile|Placement & Deliverability]]
**Industry:** [[industries/email-sms-marketing-platforms|Email & SMS Marketing Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Inbox placement and carrier filtering decide whether the channel works, neither is observable, and the platform reports delivered for every outcome including the ones that reached nobody.
**Tags:** #bayesian-inference #gradient-boosting #confidence-intervals #evaluation-metrics #hypothesis-testing #revenue-impact #change-point-detection #descriptive-statistics
**Contested on:** This niche is not terminal — inferring where an email landed and decoding why a carrier dropped a text are different contests with different winners, and they are stated separately in the sub-niches.

## The Problem
A campaign reports ninety-nine percent delivered. Some of those messages are in an inbox, some are in a promotions tab, some are in spam, some were accepted and quietly discarded, and some texts were filtered by a carrier that returned a code meaning anything from unreachable handset to blocked content. The platform cannot distinguish any of these and reports them identically. The brand optimises subject lines and send times against a population that may substantially not have received the message, and the first signal that something is wrong is usually a revenue decline nobody can explain.

## Why Nobody Has Built This
The providers and carriers do not disclose placement and have no obligation to, which is a genuine external constraint rather than a product oversight. Inferring it requires a cross-brand corpus that only a large platform has and that no single sender could assemble. Reporting a lower, more honest placement figure looks worse than a competitor's delivery rate. And deliverability has historically been a specialist craft rather than a modelled system.

## What to Build
Infer placement instead of reporting acceptance. Model where messages landed from the signals that do exist — engagement distribution shape, timing patterns, authentication and complaint feedback, provider-specific behaviours — which is the core and is tractable for a platform precisely because it sees the same providers across thousands of senders. Use the cross-brand corpus as the reference, since a provider's behaviour change is visible across many senders at once and invisible within one, which is the structural advantage this niche rests on. Report placement as an estimate with uncertainty rather than delivery as a fact, and explain the difference, since the current number is not wrong so much as answering a different question. Decode carrier responses properly, which is the second sub-niche and is a distinct problem. Detect provider and carrier behaviour changes quickly, because these shift and a brand's sudden decline is usually a change at the other end. Diagnose causes — authentication, content, list quality, complaint rate, sending pattern — and give the specific remedy, which is what a deliverability specialist does manually and slowly. Warn before a reputation problem becomes a block, since recovery is far harder than prevention. Validate inference against seed panels and any provider feedback available, so the estimate is checked rather than asserted. Make placement the headline metric in reporting, which is the presentational change that makes the whole thing matter. And measure revenue against estimated placement, since that comparison shows a brand what the invisible loss is costing.

## Target Customer
Messaging platforms, deliverability teams and specialists, and the brands whose channel performance is governed by something they cannot see.

## Impact If Built
The platform reports delivered for outcomes ranging from inbox to silently discarded, and the brand optimises against a population that may not have received the message. A cross-brand corpus makes placement inference tractable for a platform and impossible for any single sender.
