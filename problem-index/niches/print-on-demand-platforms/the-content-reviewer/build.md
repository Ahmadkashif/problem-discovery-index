# Court-Level Questions at Hundreds a Day

**Niche:** [[niches/print-on-demand-platforms/the-content-reviewer/profile|The Content Reviewer]]
**Industry:** [[industries/print-on-demand-platforms|Print on Demand Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A reviewer decides whether an uploaded design infringes a trademark or is a legitimate parody, at a rate of hundreds a day, on questions that occupy courts.
**Tags:** #worker-facing #compliance #large-language-models #evaluation-metrics #confidence-intervals #descriptive-statistics #graph-theory #automation
**Contested on:** Every serious competitor in this niche is fighting to support a reviewer deciding genuinely contested legal questions at volume — and whoever does that manages the liability, because the platform carries it and the decision is made in seconds by somebody with no legal support.

## The Problem
A design uses a famous brand's name in a way that is either a parody, a descriptive reference or an infringement depending on how a court would read it. The reviewer has forty seconds, a policy document written by somebody who was not a lawyer, and no idea what the platform decided about the eleven similar designs it has seen this year. They remove it, because removal is the safe direction for their own accountability, and a creator with a legitimate parody loses a listing with no explanation. Next week a near-identical design is approved by a different reviewer. The platform has no consistent position on a question it answers hundreds of times a day.

## Why Nobody Has Built This
The function was staffed as content moderation, which assumes a policy can be applied, and these questions do not reduce to a policy. Legal cannot review at this volume and has no mechanism to encode guidance into the queue. Decisions are recorded as actions rather than as reasoning, so no precedent accumulates. And the asymmetry — removal is safe for the reviewer, wrong for the creator, and invisible to everybody — determines the outcome.

## What to Build
Give the reviewer precedent and a framework. Build a precedent library of the platform's own decisions with the reasoning and the features that mattered, surfaced automatically by similarity when a new case arrives, which is the largest single improvement available and turns an isolated judgement into an application of a position. Encode legal guidance into decision frameworks for the recurring patterns — parody, descriptive use, stylised reference, fan work — since a small number of shapes cover most of the volume and a lawyer can write the framework once rather than reviewing each case. Provide rights-holder context at the point of decision: which marks are registered for which classes, which holders enforce, which have standing programmes, since that information exists and materially changes the right answer. Support a graduated outcome rather than approve or remove — restrict to certain products, require a modification, refer to the rights holder — because the binary forces removals that are not warranted. Route the genuinely novel to a legal escalation with a response time that fits, and record the answer as precedent. Measure consistency by replicating cases across reviewers, since a question answered differently by two reviewers is a policy gap. Balance the accountability, because a reviewer punished only for approvals will remove. And report decision patterns to legal, since the aggregate is where the platform's actual position is visible and is currently visible to nobody.

## Target Customer
Trust and safety organisations, platform legal functions, the reviewers, and the creators on the wrong side of an inconsistent decision.

## Impact If Built
The platform answers a contested legal question hundreds of times a day and has no consistent position, because decisions are recorded as actions rather than as reasoning. A similarity-surfaced precedent library turns each isolated judgement into an application of a position the platform can actually hold.
