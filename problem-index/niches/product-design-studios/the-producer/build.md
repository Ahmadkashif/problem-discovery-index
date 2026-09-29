# Seeing the Creep Before the Conversation

**Niche:** [[niches/product-design-studios/the-producer/profile|The Producer Holding the Budget]]
**Industry:** [[industries/product-design-studios|Product Design Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The producer knows three weeks early and has nothing to show for it.
**Tags:** #worker-facing #time-series-forecasting #evaluation-metrics #confidence-intervals #workflow-orchestration #descriptive-statistics #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to let the person who sees scope creep three weeks before anyone else raise it with evidence rather than as an accusation — and whoever supplies that takes the account.

## The Problem
Scope creep in a design engagement arrives as a series of small requests, each reasonable. The producer sees the burn rate diverging from the plan before anyone else, and has only a spreadsheet and their own judgement to bring to the conversation. Raising it means telling a client that their reasonable requests have added up, with no evidence beyond an assertion, and telling their own team that the work has to stop. So it is raised late, when it is expensive and unarguable.

## Why Nobody Has Built This
Project tooling tracks time rather than forecasting a position. Scope changes are not recorded as changes. The client has no visibility of the burn. And the producer's early knowledge is treated as intuition rather than as data.

## What to Build
Turn the producer's intuition into a forecast the client can see. Forecast the completion position from actual burn continuously rather than reporting hours spent, which is the core and converts a suspicion into a number weeks early. Detect scope drift by comparing what is being worked on against what was scoped, which surfaces the accumulation nobody is tracking. Record every incoming request as a change with an estimated impact at the moment it arrives, which is the practice that makes the conversation routine rather than confrontational. Give the client visibility of the same forecast, since a client who can see the position raises it themselves surprisingly often. Alert at a threshold rather than leaving the producer to judge when to speak. Separate scope change from estimating error, as they need different conversations and are always conflated. Show the impact of each request in days rather than in tone, which is what makes a refusal defensible. Track revision rounds against the contracted number, which is the commonest specific overrun. Support the producer across concurrent projects rather than one at a time. And make the conversation a scheduled review rather than an intervention, which is the change that takes the personal cost out of it.

## Target Customer
Design studios and consultancy design arms, producers and delivery leads, clients commissioning design, and professional services automation vendors.

## Impact If Built
The producer knows three weeks early and has only an assertion to bring, so the conversation happens late and expensively. A continuous forecast with change impacts recorded as they arrive makes it routine.
