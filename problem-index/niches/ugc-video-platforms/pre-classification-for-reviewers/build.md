# Deciding More So People See Less

**Niche:** [[niches/ugc-video-platforms/pre-classification-for-reviewers/profile|Pre-Classification for Reviewers]]
**Industry:** [[industries/ugc-video-platforms|UGC Video Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every case a classifier can decide is a case a person does not have to watch, and nobody is optimising for that.
**Tags:** #cnns #transformers #evaluation-metrics #confidence-intervals #semantic-segmentation #worker-facing #automation #compliance
**Contested on:** Every serious competitor in this niche is fighting to decide automatically everything that does not need a person, so the queue that reaches a human is as small and as bearable as it can be — and whoever does it reduces a documented harm with capability already in the building.

## The Problem
Classifiers are tuned to an enforcement objective: accuracy, precision, recall against policy. The amount of material they leave for humans is an output of that tuning rather than a target of it. Nobody sets a goal of minimising human exposure, nobody measures exposure as a system output, and nobody evaluates a model change on how many hours of distressing material it spared a person. The most capable content understanding systems in existence are optimising something adjacent to this and not this.

## Why Nobody Has Built This
Model teams are evaluated on enforcement quality, so exposure reduction is not in anyone's objective — an outcome that belongs to a different organisation's workforce is not a metric in the team that could change it. The workforce is at arm's length. Deciding more automatically raises accuracy and liability concerns. And nobody measures reviewer exposure in a form that could be optimised against.

## What to Build
Make exposure a system metric and optimise it. Measure human exposure by category as an output of the classification system, which is the core — an unmeasured quantity cannot be reduced and this one is not measured. Raise automated coverage where confidence supports it, since each percentage point of coverage is a direct reduction in what a person sees. Present the minimum sufficient evidence by default — a still, a transcript excerpt, a blurred segment, a summary — because a decision frequently does not require watching. Summarise where a summary supports the decision, which these models do well and which no review interface uses. Route by category so a reviewer is not moved unpredictably between kinds of harm. Tune thresholds against exposure as well as against accuracy, making the trade explicit rather than incidental. Evaluate model changes on exposure reduction alongside enforcement metrics, which is the change that would make this an engineering objective. Handle the highest-harm categories with the most aggressive automation, as that is where the reduction matters most. Report exposure hours saved as a product outcome. And give the objective an owner, because at present the people who could reduce this harm most are not accountable for it.

## Target Customer
Trust and safety engineering leadership, moderators and vendor operators, regulators and litigators, and content classification vendors.

## Impact If Built
An outcome that belongs to a different organisation's workforce is not a metric in the team that could change it. Measuring human exposure as a system output and evaluating model changes against it makes the most capable tool available point at the harm.
