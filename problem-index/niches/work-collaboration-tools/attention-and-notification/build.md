# The Aggregate Measured and Governed

**Niche:** [[niches/work-collaboration-tools/attention-and-notification/profile|Attention & Notification]]
**Industry:** [[industries/work-collaboration-tools|Work Collaboration Tools]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every tool defaults to notifying, none is accountable for the total, and no organisation has ever counted how many interruptions its people receive in a day.
**Tags:** #descriptive-statistics #gradient-boosting #evaluation-metrics #confidence-intervals #hypothesis-testing #optimization-fundamentals #worker-facing #workflow-orchestration
**Contested on:** Every serious competitor that takes this seriously is fighting to make the total interruption load a measured quantity with an owner — and whoever gives an organisation control over the aggregate takes the attention nobody is currently accountable for.

## The Problem
A knowledge worker receives messages from two chat platforms, notifications from four work management tools, comments from a document system, alerts from a code repository, meeting reminders, and email. Each individual notification was configured by a reasonable default. The aggregate is an interruption every few minutes through the working day, which makes sustained work effectively impossible and which the person experiences as a personal failure of discipline. Their employer has no measurement of it, no owner for it and no instrument to change it, and each vendor's product analytics report the resulting engagement as a success.

## Why Nobody Has Built This
The incentives are aligned against it at every level. Each vendor's engagement metrics improve with more notifications, so no vendor will reduce its own. The individual can only act on their own settings, tool by tool, and is penalised socially for being unreachable. And the organisation has no function whose objective is attention — IT owns the tools, HR owns wellbeing in the abstract, and nobody owns the number. The result is an unmanaged commons, which is the structure of problem that does not get solved by any participant acting alone.

## What to Build
Measure the aggregate and give the organisation a lever. The measurement first, because nothing else can happen without it: total notifications per person per day across all systems, their distribution through the day, how many arrived during focus periods, and how many were acted upon versus dismissed — which is computable from the systems' own delivery records and has apparently never been assembled anywhere. Report it at the team and organisation level, not the individual, since the purpose is to govern the system rather than to coach people about their settings. Then the control layer: a single cross-tool policy that batches non-urgent notifications into intervals, defers anything without a genuine time constraint, and routes by relevance rather than by membership. Relevance is the interesting modelling problem — whether a message actually concerns this person, estimated from their prior responses, their role and the content — and is what separates useful routing from a blunt delay. The organisation sets the default and individuals adjust within it, which is the inversion that matters: currently the default is maximal and the individual must opt out.

## Target Customer
Digital workplace and IT functions in large organisations, the small category of focus and workplace experience vendors, and any employer whose knowledge workers report that they cannot get anything done.

## Impact If Built
The attention cost of the current arrangement is large, well documented and entirely unmeasured, which means no organisation can act on it. Measuring the aggregate is the intervention — it creates an owner and a number, and the number will be startling enough to prompt action that no amount of advice about notification settings has achieved.
