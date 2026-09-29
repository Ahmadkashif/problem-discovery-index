# Screening Outcomes Are the Only Accuracy Signal and Nobody Collects Them

**Niche:** [[niches/customs-brokers/sanctions-screening-data-providers/profile|Sanctions & Restricted Party Screening Data]]
**Industry:** [[industries/customs-brokers|Customs Brokers]]
**Type:** Fix (Pain Point)
**One-liner:** Customers clear millions of screening alerts a year as false positives, each disposition is a labelled judgment about the vendor's data, and none of it comes back.
**Tags:** #evaluation-metrics #cross-validation #confidence-intervals #logistic-regression #gradient-boosting #hypothesis-testing #probability-distributions #compliance #data-integration #revenue-impact

## The Problem
Every alert a screening system raises is dispositioned by a human at the customer — cleared as a false positive, escalated, blocked. Across a large customer base that is millions of expert judgments a year about whether the vendor's match was right, and the vendor sees almost none of them. So precision is unmeasured. The vendor cannot say which profile types, name populations, or list sources generate the most false positives, cannot demonstrate that a matching improvement actually improved anything, and cannot tell a prospective customer what alert volume to expect except by reference to another customer's anecdote. Meanwhile alert volume is the single largest cost the customer bears from the product, and reducing it is the thing they most want.

## Why It's Still Broken
Dispositions live in customer compliance systems and touch decisions the customer may regard as sensitive. Nothing in the integration asks for them, and there is no obvious incentive for a customer to send them back. The vendor also has a defensive instinct that runs deep in this segment: measured precision is a number a competitor can attack, and in a compliance product the safer posture has been to compete on list coverage, which is easier to assert and impossible to falsify.

## What a Fix Looks Like
Structured disposition return, designed so the customer gets more than they give. Dispositions are contributed in a standard taxonomy — false positive with the reason, true match, escalated for review — with no case detail leaving the customer, and in exchange the customer receives their own alert profile benchmarked against comparable organizations, which is genuinely useful for defending their programme to a regulator and which nobody currently offers. On the vendor side, precision becomes measurable by profile type, name population, list source, and match band, which turns matching improvement from an assertion into a demonstrated result and directs research at the profiles that generate the most wasted work. The most valuable single output is a calibrated expected alert volume for a prospective customer's counterparty profile, which changes a procurement conversation from list-count comparison to operational cost.

## Who Feels the Pain
Compliance teams clearing alert volume nobody can justify; the vendor's research organization improving matching with no measurement; sales teams competing on coverage counts because precision cannot be claimed; and the customer who eventually misses a real match inside a stream they had learned to clear quickly.

## Impact If Fixed
Converts the product's real cost driver into a managed quantity, and gives the vendor the only defensible accuracy claim available in a market where the underlying lists are public and identical for everyone. The disposition corpus is also strictly non-replicable — it can only be assembled by a provider with a large installed base willing to contribute — which makes it the right place for durable differentiation.
