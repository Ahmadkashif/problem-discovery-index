# Cost and Latency Visible Only in the Bill

**Niche:** [[niches/llm-application-tooling/application-frameworks-and-tracing/profile|Application Frameworks & Tracing]]
**Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Type:** Fix (Pain Point)
**One-liner:** Teams learn what their application costs from a monthly invoice with one line on it, having no view of which feature, which prompt version or which customer consumed it.
**Tags:** #revenue-impact #descriptive-statistics #data-integration #evaluation-metrics #confidence-intervals #automation #quick-win #time-series-forecasting
**Contested on:** Not terminal — the contest differs by whether the buyer is starting the application or operating it, and the decomposition is recorded in the profile.

## The Problem
A monthly model bill arrives, larger than expected. The team cannot attribute it: not to a feature, not to a prompt version, not to a customer segment, not to retries, not to the evaluation runs they kicked off, not to the one code path that accidentally includes a large document in every request. They know the total and nothing else. They respond by shortening prompts across the board, which degrades quality in places, and the actual driver — a retry loop that triples cost on a small share of requests — is still there next month.

## Why It's Still Broken
Cost attribution requires tagging every request with the dimensions that matter, which nobody sets up at the start and which is awkward to retrofit. Providers bill by account or key, not by feature. Tracing products record latency and tokens per span and mostly do not roll them into a cost view. And the bill is a finance artefact while the drivers are engineering facts, with nothing joining them.

## What a Fix Looks Like
Attribute the spend to the thing that caused it. Tag every model call with feature, prompt version, customer or tenant, and environment, which is a handful of attributes set once and is the precondition for every other view here. Report cost by each of those dimensions continuously rather than monthly, so a change's cost is visible the day it ships alongside its quality effect. Separate retries, evaluation runs and background jobs from user-facing traffic, since they are frequently a large share and are invisible in a single total. Report cost per unit of value — per resolved conversation, per document processed — rather than per token, which is the number that tells a team whether the application is economic. Alert on cost anomalies by dimension, so a runaway path is caught in hours. Report the cost of a prompt change alongside its quality change, since longer prompts are the usual remedy for quality problems and their cost is never weighed. Show the token composition of a typical request, which routinely reveals that most of the context is a document nobody needed. And feed the attribution into routing decisions, which the routing niche develops.

## Who Feels the Pain
Engineering teams cutting prompts blindly to control a bill they cannot decompose; finance functions with one line to plan against; and the users whose experience degrades because the response to cost pressure was untargeted.

## Impact If Fixed
A handful of attributes on every model call is the precondition for every cost view, and almost nobody sets them. Reporting cost per resolved conversation rather than per token is what tells a team whether the application is economic at all.
