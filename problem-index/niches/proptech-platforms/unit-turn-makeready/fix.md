# Days Vacant With No Decomposition

**Niche:** [[niches/proptech-platforms/unit-turn-makeready/profile|Unit Turn & Make-Ready Sequencing]]
**Industry:** [[industries/proptech-platforms|Proptech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Every operator tracks days vacant and none of them can say how many of those days were waiting for a vendor, waiting for a decision, waiting for an inspection, or genuinely being worked on.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #survival-analysis #workflow-orchestration #quick-win #revenue-impact
**Contested on:** Every serious competitor in turn operations is fighting to get a vacant unit from move-out to rent-ready in the fewest days across five vendors who do not talk to each other — and whoever cuts days-vacant most takes the account.

## The Problem
A regional manager is told her average turn is 14.2 days against a target of 10. She responds by pushing site managers to move faster, which is the only lever the number gives her. Whether the four extra days are vendor scheduling latency, waiting for an owner's approval on a scope item, waiting for a material, or the work itself taking longer than it should is unknown — and each of those requires an entirely different response. The target is managed by exhortation because the metric has no parts.

## Why It's Still Broken
Turn tracking records a start and an end, and sometimes a checklist of completed items with completion dates. It does not record waiting, because waiting is the absence of an event and nothing logs an absence. Decomposing would require each step to have a requested date, a scheduled date, a start and a finish — four timestamps instead of one — which nobody has asked for because the aggregate number is what appears in the owner report.

## What a Fix Looks Like
Timestamp the transitions and report the decomposition. For every turn, record when each step was requested, when it was scheduled for, when it actually started and when it finished, which is four taps or four automatic events rather than a checkbox. From that, days vacant decomposes into vendor lead time, waiting on approval, waiting on materials, active work, and slack between steps — and the answer is usually surprising to the operator, since most turns spend the majority of their days waiting rather than working. Report by property, by vendor and by step so the intervention is specific: this painter's lead time is six days and the next one's is two, or scope approvals at this property take four days because one regional manager approves them all. None of this requires modelling; it requires four timestamps where there is currently one.

## Who Feels the Pain
Site managers pushed to improve a number whose composition they cannot show; regional managers with one lever for five different problems; and owners paying for vacancy that is mostly queueing.

## Impact If Fixed
Decomposing days vacant almost always reveals that the dominant component is waiting rather than working, which redirects the entire improvement effort from pressuring staff to fixing scheduling and approvals. It is the cheapest possible change — timestamps — and it is the prerequisite for knowing whether anything else in this sub-niche worked.
