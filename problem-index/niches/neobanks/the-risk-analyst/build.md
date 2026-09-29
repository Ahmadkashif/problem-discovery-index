# A Screenshot and a Throughput Target

**Niche:** [[niches/neobanks/the-risk-analyst/profile|The Risk Analyst]]
**Industry:** [[industries/neobanks|Neobanks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Risk analysts spend their shift deciding, from a screenshot and a bank statement, whether a stranger deserves access to their own wages, and are measured on how many cases they close.
**Tags:** #worker-facing #large-language-models #evaluation-metrics #confidence-intervals #workflow-orchestration #compliance #transformers #automation
**Contested on:** Every serious competitor in this niche is fighting to give the analyst the evidence and the time to decide correctly rather than a screenshot and a throughput target — and whoever does that changes who gets access to their own wages.

## The Problem
The case arrives in the queue. The account is restricted. The member has uploaded a photograph of a pay stub and a screenshot of an employer's portal. The analyst has a few minutes, the risk system's flag with a code but no explanation, no visibility of what similar cases produced, and a daily target. They decide whether to restore access to someone's wages. They do this dozens of times a day, for years, and nobody has ever told them how often they were right.

## Why Nobody Has Built This
The analyst was added to catch what the model could not, so the role was designed as overflow capacity rather than as a decision function — capacity gets a queue and a target, and a decision function would have got evidence and a quality measure. Case evidence arrives as whatever the member could photograph. The risk system's reason codes are not exposed to the reviewing team. And outcomes are not joined back to who decided.

## What to Build
Give the analyst a case rather than a queue item. Assemble the evidence automatically — account history, deposit pattern, device consistency, prior interactions, the specific signal that fired — so the analyst starts with the institution's own knowledge rather than with a photograph. Explain why the case was flagged, in terms the analyst can evaluate, since re-deriving the suspicion from nothing is most of the work and is entirely avoidable. Extract the content of uploaded documents automatically, which is reliable now and removes the reading. Show comparable past cases and their outcomes, which is how consistency is achieved in practice and is the fix the reviewer most needs. Recommend an outcome with confidence and reasoning, leaving the decision human, because these decisions are consequential and an automated verdict on a person's wages would be both wrong and indefensible. Ask the member for the specific missing evidence automatically, rather than leaving the analyst to guess what would resolve it. Measure decision quality against outcomes rather than throughput, which is the fix note's subject. Route by complexity, so simple cases clear quickly and the difficult ones get the time they need. Record the reasoning in a structured form, which supports appeal, consistency analysis and model feedback at once. And give the analyst their own accuracy over time, because a person making consequential decisions all day deserves to know whether they are good at it.

## Target Customer
Risk operations leadership at digital banks, the analysts themselves, and the vendors supplying case management to this function.

## Impact If Built
The role was designed as overflow capacity for what the model could not catch, so it got a queue and a target rather than evidence and a quality measure. Assembling the institution's own knowledge into the case, and explaining why it fired, removes the work of re-deriving a suspicion from a photograph.
