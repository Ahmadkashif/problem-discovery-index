# The Support Agent Who Cannot See the Reason

**Industry:** [[neobanks|Neobanks]]
**Type:** Worker Life Changing
**One-liner:** The person a frozen member reaches can see that the account is restricted and not why, and spends the call apologising for a decision they are not permitted to explain or reverse.
**Tags:** #large-language-models #bert #k-nearest-neighbors #evaluation-metrics #feature-engineering #worker-facing #workflow-orchestration #automation

## The Problem
A member calls or opens a chat because their card declined at a checkout. The agent opens the account and sees a status flag: restricted, under review, pending documentation. The reason codes that produced it live in the risk platform, which the agent does not have access to, partly by design and partly because nobody built the integration.

So the agent reads a script. The account is under review, we cannot discuss the specifics, please upload the requested documentation, the review takes up to X business days. The member, who has rent due on Friday, asks what documentation. The agent can see a generic request and not what the analyst actually needs. The member asks how long. The agent can see a service-level target and not the current queue depth. The member asks to speak to the person reviewing it. There is no such path.

The same conversation happens dozens of times a shift. The agent has no authority to resolve any of it and no information to offer.

Alongside the freeze calls run the ordinary ones — a pending deposit, a failed transfer, a disputed charge — where the agent hunts across the core provider's interface, the card platform, the dispute tool and a knowledge base to assemble an answer that exists in four systems.

## Why It Matters to the Worker
Being the face of a decision you did not make and cannot explain is a specific kind of work, and it is corrosive in a way that hard work is not. Agents absorb the anger of people in genuine financial distress, all day, while holding information they are not allowed to share and lacking information they would share if they had it.

Quality scoring makes it worse. Agents are measured on member satisfaction after calls where the member's problem was structurally unsolvable by the agent, which converts a systemic gap into an individual performance score.

The escalation path is the other grievance. An agent who can tell that a case is wrong — the member has been with the institution three years, has direct deposit from the same employer, and the freeze was triggered by a benefit payment — has no mechanism to say so beyond a free-text note that may or may not be read. Their judgement, which is often good, has no channel.

## What a Solution Looks Like
Reason codes translated and surfaced, not hidden. There is a real distinction between information the institution cannot legally disclose to a member and information it withholds from its own agent by accident of architecture. Most restriction reasons fall in the second category. An agent who can see that the trigger was a documentation requirement on a specific deposit can say something true and useful.

Documentation requests that are specific. What the analyst actually needs, in plain language, with the acceptable formats stated, generated from the case rather than from a template. A large fraction of review cycles are spent on members supplying the wrong document because nobody told them which one.

Honest timelines from the actual queue rather than the published target, which is the single most requested and least available piece of information on these calls.

A unified case view. One surface that assembles the ledger position, the card status, the restriction reason, the documents received and the dispute state, so the agent stops navigating four systems while a distressed person waits.

An escalation channel that carries the agent's own judgement as structured signal rather than a note, and that is measured — how often front-line escalations turn out to be right is a number the institution should want.

## Impact If Solved
Support attrition in consumer fintech is high and is driven less by volume than by powerlessness. Giving agents the reason, a specific request and a real timeline removes most of the repeat contact as a side effect, because the majority of follow-up calls exist only because the first call could not answer the question.
