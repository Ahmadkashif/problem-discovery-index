# Nobody Measures the Blocked Customer

**Niche:** [[niches/edge-cdn-providers/bot-and-abuse-management/profile|Bot & Abuse Management]]
**Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Type:** Fix (Pain Point)
**One-liner:** Bot management reports requests blocked, which is a success metric, and the legitimate users among them are counted by nobody.
**Tags:** #descriptive-statistics #logistic-regression #hypothesis-testing #confidence-intervals #evaluation-metrics #compliance #quick-win #worker-facing
**Contested on:** Every serious competitor in bot management is fighting to keep up with adversaries who adapt within days of a rule shipping — and whoever detects the adaptation as it happens across their whole customer base takes the market, because no single customer can see it.

## The Problem
The dashboard reports several million requests blocked this month, presented as the product working. Among them are customers on older devices whose fingerprints look unusual, users of assistive technology whose interaction patterns do not match the behavioural model, people on shared or corporate connections whose addresses carry a poor reputation, and privacy-conscious users whose browser configuration is atypical. None of them appears as a false positive, because a blocked user does not file a report — they leave, and in the case of assistive technology users they encounter a challenge they frequently cannot complete at all. The precision side of an explicitly two-sided trade-off is unmeasured.

## Why It's Still Broken
Blocked requests are counted by the system and false positives are not, because identifying a wrongly blocked legitimate user requires knowing they were legitimate, which the system by definition concluded otherwise. The asymmetry in measurability produces an asymmetry in attention, and the reported metric only ever looks good. Customers experience false positives as support complaints, which vastly undercount. And the populations most affected — older devices, assistive technology, unusual configurations — are exactly those least likely to complain through a channel anybody counts.

## What a Fix Looks Like
Measure the other side deliberately, since it will not measure itself. Sample blocked traffic and review it, which is the only direct method and is entirely practical at a small sampling rate — a few hundred reviewed sessions a month produces a usable estimate of a number that is currently unknown. Provide a challenge path that a legitimate user can complete and count its completions, since a completed challenge after a block is a confirmed false positive and is the cheapest available label. Correlate blocks with downstream conversion and support contacts, which estimates the business cost of the precision side. Report block rate by device age, browser, assistive technology signal and network type, because the disparity is the finding and it is not currently looked for. Measure challenge completion rates by the same segments, since a challenge that cannot be completed by users of assistive technology is an exclusion rather than a security measure. Let the customer set the trade-off explicitly with the estimated cost of each side shown, rather than choosing a sensitivity level with no information. And report the false positive estimate alongside the blocked count, so the headline metric describes both sides of the decision.

## Who Feels the Pain
Legitimate users blocked from services they pay for, particularly those on older devices and using assistive technology; customers losing sales they will never attribute; and security teams tuning a system on a one-sided metric.

## Impact If Fixed
Sampled review of blocked traffic is practical and produces the missing half of a two-sided trade-off that is currently tuned on one. The segment breakdown is the part most likely to be uncomfortable and most likely to identify a systematic exclusion nobody intended.
