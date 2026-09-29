# The Question Nobody Answered

**Niche:** [[niches/developer-relations-agencies/community-health/profile|Community Health]]
**Industry:** [[industries/developer-relations-agencies|Developer Relations Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** A developer asked a clear question in the community three weeks ago and it is still sitting there.
**Tags:** #quick-win #descriptive-statistics #evaluation-metrics #workflow-orchestration #automation #data-integration #worker-facing #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to measure whether a developer community is working, when member count and message volume rise as it fills with unanswered questions — and whoever measures it properly takes the account.

## The Problem
Unanswered questions accumulate in every developer community. Each one is a person who came for help and did not get it, and each one is read by newcomers deciding whether this is a place worth participating in. Nobody tracks them, because the platform reports messages rather than questions and nobody has defined what an answer is. The community's most visible signal to a prospective member is a list of questions with no replies.

## Why It's Still Broken
Nothing distinguishes a question from a message — a platform that counts activity cannot tell that a message was a request for help that went unmet, so the backlog is invisible in every metric. Nobody owns unanswered questions. Volume looks like health. And the people who left do not say why.

## What a Fix Looks Like
Identify the unanswered questions and give them an owner. Detect questions and whether they received a response, which is the fix and is straightforwardly automatable in any community platform. Maintain an unanswered queue with an owner and a target response time, which converts an ambient failure into a managed one. Report answer rate and time to first response as the community's headline metrics. Prioritise newcomers' first questions, since those determine whether a person stays and are disproportionately abandoned. Route questions to the people who can answer rather than hoping, which is the single largest improvement available. Recognise the community members who answer, because a small number carry the load and they leave when unacknowledged. Close the loop on questions that were answered elsewhere, so the visible backlog reflects reality. Escalate genuinely unanswerable questions to support or engineering rather than leaving them. Show the answer rate publicly, which changes behaviour on both sides. And treat an unanswered question as a defect rather than as a message.

## Who Feels the Pain
Developers who asked for help and were ignored; newcomers deciding not to participate; the few members who answer everything; and the company, whose community is its most visible support signal.

## Impact If Fixed
A platform that counts activity cannot tell that a message was a request for help that went unmet, so the backlog is invisible in every metric. Detecting questions and tracking answer rate makes the failure manageable.
