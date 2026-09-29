# Reviewing Behaviour by Guessing What to Ask

**Niche:** [[niches/llm-application-tooling/the-prompt-author/profile|The Prompt Author]]
**Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Type:** Fix (Pain Point)
**One-liner:** The specialist responsible for what an application says can only find out what it says by using it and thinking of questions, which means they discover problems the way customers do.
**Tags:** #worker-facing #k-means-clustering #evaluation-metrics #descriptive-statistics #large-language-models #automation #quick-win #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to let the person who knows what the application should say change what it says, safely, without an engineer — and whoever does that takes the account, because that person is the bottleneck on every content change.

## The Problem
A compliance officer is accountable for what a financial assistant tells customers. To review it, they open the application and type questions they think of. They cannot see the range of questions customers actually ask, cannot see how the assistant answers the ones they would never think to ask, and cannot systematically check a policy area. They find problems at the same rate as a moderately curious customer, which is to say slowly and by luck. They are accountable for a surface they have no way to survey.

## Why It's Still Broken
Production traffic sits in engineering tools with no access path for a business reviewer. Nobody framed the specialist's task as reviewing a surface rather than testing a feature. Presenting real customer conversations raises a privacy question nobody wanted to handle. And the specialist, being accountable rather than technical, asks for a report and receives a demo.

## What a Fix Looks Like
Give them the surface, organised. Cluster production questions by topic and show the specialist what is actually being asked in their domain, with representative answers, which replaces guessing with a survey and is the fix. Highlight the answers most likely to be wrong — low confidence, poor user reaction, unusual for their cluster — so attention goes where it is needed rather than uniformly. Let them review by policy area rather than by conversation, since their accountability is organised around policies and the data is organised around sessions. Support a structured review pass with a record of what was checked and when, which is what accountability actually requires and currently does not exist. Redact or synthesise customer content so the privacy question is settled rather than avoided, since that objection is the reason access is not granted. Let them flag an answer as wrong and have it become a regression test case, which turns a review into a durable improvement and connects their judgement to the evaluation set. Report coverage — which policy areas have been reviewed and how recently — so the review is a managed process rather than an occasional impulse. And alert them when the application starts answering a new kind of question in their domain, which is when their input is most valuable and is currently invisible to them.

## Who Feels the Pain
Specialists accountable for a surface they cannot see; customers receiving answers no qualified person has ever reviewed; and the organisations whose compliance sign-off rests on someone typing questions they thought of.

## Impact If Fixed
Clustering production questions and presenting them by policy area replaces guessing with a survey. Letting a flagged answer become a regression test case turns the specialist's judgement into a durable improvement rather than a ticket.
