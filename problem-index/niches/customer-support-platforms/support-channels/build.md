# One Conversation Across Every Door

**Niche:** [[niches/customer-support-platforms/support-channels/profile|Support Channels]]
**Industry:** [[industries/customer-support-platforms|Customer Support Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A customer who tries the chat, gives up, and telephones starts over with an agent who cannot see what they already explained, because the channels share a database and not a conversation.
**Tags:** #graph-theory #large-language-models #bert #evaluation-metrics #confidence-intervals #data-integration #workflow-orchestration #worker-facing
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
A customer opens a chat, explains a problem over six messages, gets an unhelpful automated response, and calls the support line. The agent who answers asks for their account details and what the problem is. The customer explains again, with less patience. The chat transcript exists and is either not surfaced, surfaced as a raw transcript the agent has no time to read, or attached to a different record because the phone number and the chat identity were never linked. The organisation records two contacts, one of them abandoned, and a satisfaction score that reflects the second conversation.

## Why Nobody Has Built This
The channels grew up as separate products with separate identity models — a chat session identified by a cookie or an account login, a call identified by a phone number — and linking them is an identity resolution problem nobody owns. Even where the link is made, the prior conversation is delivered as a transcript, which an agent with a customer waiting cannot read. And the metrics reinforce the separation: each channel is measured on its own contact volume and handle time, so a chat that ends in a call improves the chat team's numbers.

## What to Build
Continuity as a first-class property. Identity resolution across channel-specific identifiers so that a chat session, an email thread and a phone call from the same person are recognised as one conversation — which requires the account, the device, the phone number and the email to be resolved into a customer, with confidence, and is the foundational piece. The prior context is delivered to the agent as a summary rather than as a transcript: what the customer has tried, what they were told, what remains unresolved, in three lines, which is what an agent can absorb while a customer is on the line. Escalation from an automated channel carries everything forward, so the customer never re-explains. And the measurement changes with it: an issue rather than a contact is the unit, so a chat that became a call is one issue with a channel switch, which is both the truth and a measure the organisation can improve.

## Target Customer
Support platform vendors spanning channels, contact centre technology owners, and the support organisations whose customers routinely start over.

## Impact If Built
Re-explaining is the single most common customer complaint about support and is entirely avoidable. Resolving identity across channels and delivering context as a summary rather than a transcript are both tractable, and changing the unit of measurement from contact to issue is what stops the organisation from rewarding the behaviour that causes it.
