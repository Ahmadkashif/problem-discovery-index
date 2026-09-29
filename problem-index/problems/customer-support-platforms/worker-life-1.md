# Agent Metrics and the Queue

**Industry:** [[customer-support-platforms|Customer Support Platforms]]
**Type:** Worker Life Changing
**One-liner:** Support agents stop being managed by handle time and a satisfaction score that is statistically meaningless at individual volume, and start being measured on whether the customer's problem was actually solved.
**Tags:** #bert #large-language-models #hypothesis-testing #confidence-intervals #descriptive-statistics #evaluation-metrics #worker-facing #automation

## The Problem
A support agent works a queue and is measured on average handle time, tickets per hour, first response time and customer satisfaction. Those numbers determine their performance review and frequently their pay.

Both headline metrics are broken in ways that are well understood and widely ignored. Handle time rewards closing quickly, which rewards not solving the problem — the customer returns tomorrow as a new ticket, attributed to somebody else. Satisfaction surveys have single-digit response rates, are answered disproportionately by the angry and the delighted, and are heavily influenced by whether the answer was yes rather than by whether the agent was any good. At the volume an individual agent handles, the score is dominated by noise, and everyone who has looked at the distribution knows it.

So agents optimise. Close fast. Avoid the hard tickets. Ask for a good rating. Route ambiguous cases elsewhere. None of this is dishonest; it is the rational response to the measurement.

Meanwhile generative deflection is removing the easy tickets, which raises the average difficulty of what remains while the handle time targets stay where they were.

## Why It Matters to the Worker
Support is a role where the measurement shapes the day more than in almost any other job. An agent watches a timer, works a queue that never empties, and is evaluated on numbers they know are partly luck.

The satisfaction score is the sharpest grievance. An agent who correctly enforces a policy the customer dislikes receives a bad rating for doing their job properly, and this happens constantly. Being penalised for accurate work is corrosive in a way that pay alone does not fix, and it is a consistent theme in why people leave support.

Deflection has added a new anxiety. Agents are aware that the easy volume is being automated, that their remaining work is harder, and that the same targets apply — and in many organisations nobody has said anything about what the role becomes.

## What a Solution Looks Like
Resolution as the primary metric, defined as the problem not recurring: no repeat contact on the same issue from the same customer within a window. It is directly observable, hard to game in the way handle time is gamed, and it is what the company actually wants.

Difficulty adjustment. Tickets vary enormously and are not assigned randomly, so raw handle time comparisons across agents are meaningless. Predicting expected effort from the ticket and comparing against it is straightforward and makes the comparison fair.

Satisfaction reported with honest uncertainty, or not reported at individual level at all. A score built on eleven responses should carry an interval that makes clear it distinguishes almost nothing.

Quality assurance from the full population rather than from a five-ticket monthly sample — automated review of every interaction against defined criteria, with human review focused where the automated score and the outcome disagree.

## Impact If Solved
Support turnover is famously high and the measurement system is a substantial and entirely self-inflicted part of it. Measuring resolution rather than speed aligns the agent's incentive with the customer's outcome, and difficulty adjustment removes the unfairness that agents correctly perceive.
