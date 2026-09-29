# Everything Is Marked Urgent

**Niche:** [[niches/contract-lifecycle-platforms/legal-ops-triage/profile|Legal Operations Triage]]
**Industry:** [[industries/contract-lifecycle-platforms|Contract Lifecycle Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The intake form has an urgency field, every requester selects the highest value, and the field therefore carries no information at all.
**Tags:** #descriptive-statistics #logistic-regression #survival-analysis #hypothesis-testing #confidence-intervals #evaluation-metrics #quick-win #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to tell a routine agreement from a genuinely dangerous one at the moment it arrives — and whoever does that takes legal operations, because everything downstream depends on the first thirty seconds being right.

## The Problem
The intake form asks how urgent the request is, with four options. The overwhelming majority of requests arrive marked most urgent, because requesters have learned that anything else is deprioritised and because their own deadline genuinely does feel pressing. The field is therefore useless and is ignored, which means the requests with a real deadline — a deal closing Friday, a regulatory filing — are indistinguishable from the rest, and legal operations reverts to prioritising by who asked.

## Why It's Still Broken
Self-declared priority is the easiest thing to collect and it degrades predictably wherever it is used, which is well known and has not changed the design here. There is no verification, so declaring urgency is free. Legal operations is reluctant to challenge a requester's stated deadline because the requester is usually more senior. And nobody measures the field's informativeness, so it survives on the assumption that it is doing something.

## What a Fix Looks Like
Replace the declaration with something checkable. Ask for the actual date and the reason — the deal closes on the twelfth, the filing is due on the ninth — which is specific, verifiable and far harder to inflate than a dropdown, and which is the single change that restores meaning to the field. Derive urgency from context where it exists: a linked opportunity's close date, a renewal deadline in the repository, a regulatory calendar. Compare declared urgency against what happened, since an agreement marked most urgent that then sat unsigned for three weeks is evidence about that requester's declarations, and reporting that pattern gently to the team changes behaviour without anyone having to challenge anybody. Publish realistic turnaround times by request type, because much of the inflation is requesters hedging against an unknown wait. Make the trade-off visible, so a requester marking something urgent sees what it displaces, which is how every functioning prioritisation scheme works. And measure whether the field predicts anything at all, which is a quick analysis that would establish the problem in an afternoon.

## Who Feels the Pain
Legal operations prioritising by seniority because the urgency field is noise; requesters with genuine deadlines who cannot signal them; and counsel working on the wrong thing first.

## Impact If Fixed
Asking for a date and a reason instead of a priority level costs nothing and restores the signal immediately. Publishing realistic turnaround times removes most of the hedging that causes the inflation in the first place.
