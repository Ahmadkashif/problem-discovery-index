# Relevance Ranking and Batching From Consumer Products

**Niche:** [[niches/work-collaboration-tools/attention-and-notification/profile|Attention & Notification]]
**Industry:** [[industries/work-collaboration-tools|Work Collaboration Tools]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Consumer platforms spent a decade learning how to decide which notifications are worth sending and when, and enterprise tools notify on every event because a rule said the person was subscribed.
**Tags:** #gradient-boosting #logistic-regression #optimization-fundamentals #evaluation-metrics #confidence-intervals #hypothesis-testing #worker-facing #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to make the total interruption load a measured quantity with an owner — and whoever gives an organisation control over the aggregate takes the attention nobody is currently accountable for.

## The Problem
A person is notified of every message in a channel they joined for one project, every comment on a document they once edited, and every status change on a task they are watching. None of the notifications is wrong by the rule that generated it and almost none of them requires action. Consumer platforms solved this class of problem with relevance models, frequency capping and timing optimisation — and while the objectives those models were tuned for are not ones an enterprise should copy, the machinery for deciding what is worth an interruption is entirely transferable.

## What Already Exists
Notification relevance ranking, frequency capping, digest batching and send-time optimisation are mature capabilities with extensive published practice and open implementations. Multi-armed bandit and ranking infrastructure is commodity. The engineering patterns for cross-channel notification orchestration exist in the marketing automation stack. Everything required is available and well understood.

## The Customization Gap
The adaptation is to an objective that is the opposite of the consumer one. It requires: (1) optimising for acted-upon rather than opened, since the consumer objective is engagement and the enterprise objective is that an interruption was worth taking — which inverts the training signal and is the whole point; (2) the cost of a missed notification modelled explicitly, because the enterprise failure mode is asymmetric in the other direction from consumer, and suppressing a genuinely urgent message is far worse than sending an unnecessary one; (3) relevance learned per person from their own response behaviour rather than from a global model, since what matters to an individual is idiosyncratic and the data per person is adequate; (4) batching windows that respect meeting calendars and stated focus periods, which is information the organisation has and no notification system uses; and (5) an explicit override for genuine urgency that has a cost to the sender, as the fix note describes, since any suppression system without one will be defeated by people marking everything important.

## Target Customer
Collaboration platform vendors, digital workplace functions, and the operating system and device vendors whose focus features currently operate without any signal about what matters.

## Impact If Solved
Relevance ranking with an acted-upon objective would remove a large share of interruptions with very little risk, and the machinery is bought rather than built. Modelling the cost of suppression is the specific adaptation that makes it safe in a work context, where a missed message can have consequences that a missed consumer notification does not.
