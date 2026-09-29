# One Number for Six Different Populations

**Niche:** [[niches/email-sms-marketing-platforms/list-health-and-reactivation/profile|List Health & Reactivation]]
**Industry:** [[industries/email-sms-marketing-platforms|Email & SMS Marketing Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A list is six different populations needing six different actions, reported as one number and managed with one rule.
**Tags:** #survival-analysis #gradient-boosting #confidence-intervals #evaluation-metrics #k-means-clustering #revenue-impact #bayesian-inference #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to tell a brand which of its subscribers are still reachable and worth reaching — and whoever does that stops a list from being both a liability and an unworked asset at the same time.

## The Problem
The list has four hundred thousand subscribers. Some fraction are people who buy regularly. Some are abandoned addresses. Some are real people whose mail is going to spam, which looks identical to disengagement and needs the opposite response. Some are people who would buy again if contacted differently, and some would never. Some want less frequent mail and are silently being over-messaged toward an unsubscribe. The brand sees four hundred thousand, celebrates growth, and applies one rule. The distinctions are all predictable from data the platform holds, and separating them would simultaneously reduce a deliverability liability and surface revenue nobody is working.

## Why Nobody Has Built This
List size is a growth metric that everyone reports and nobody wants to reduce, so the incentive is to keep the number rather than to understand it — the metric shapes the behaviour directly. Reachability and interest are conflated because opens conflated them and the replacement has not been built. Win-back is treated as a campaign rather than as a segmentation problem. And a platform paid by contacts or volume has no reason to encourage pruning.

## What to Build
Segment the list by what should be done with each person. Predict reachability separately from interest, since a filtered subscriber and a disinterested one look identical and need opposite responses — this separation is the core and is possible using provider-level placement inference alongside individual behaviour. Estimate the probability each subscriber returns, with an expected value, which turns win-back from a blanket campaign into a targeted one and is the fix note's subject. Identify address decay directly, since abandoned addresses accumulate silently and are a pure deliverability liability with no upside. Detect over-messaging at the individual level, connecting to the fatigue work, because a subscriber sliding toward unsubscribe is recoverable with less mail rather than more. Recommend an action per person — maintain, reduce frequency, attempt reactivation, suppress, remove — which is the deliverable and replaces a single rule with a policy. Report list health as composition rather than as size, which is the presentational change that makes any of this matter. Value the list honestly, since an inflated count is a liability presented as an asset and brands make acquisition decisions on it. Feed the segmentation into deliverability management, as list composition is one of the strongest determinants of placement. Test the recommendations, because the whole thing should be validated rather than asserted. And measure revenue per reachable subscriber, since that is the honest unit and list size is not.

## Target Customer
Lifecycle and deliverability teams, messaging platforms whose customers manage lists by a single rule, and the brands whose list size is an unexamined number.

## Impact If Built
List size is a growth metric nobody wants to reduce, which shapes the behaviour directly. Separating reachability from interest is the core and is possible today, and it converts a single sunset rule into a per-person policy that reduces liability and surfaces revenue at once.
