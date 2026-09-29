# Context Assembly and Drafting Infrastructure

**Niche:** [[niches/customer-support-platforms/support-agent-tools/profile|Support Agent Tools]]
**Industry:** [[industries/customer-support-platforms|Customer Support Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Retrieval, summarisation and drafting are commodity capabilities, and a support agent still opens five tabs to understand who they are talking to and types the summary afterwards.
**Tags:** #large-language-models #bert #transformers #evaluation-metrics #confidence-intervals #data-integration #automation #worker-facing
**Contested on:** Every serious competitor building for support agents is fighting to measure and support whether the customer's problem was actually solved rather than how long it took — and whoever the agents experience as help rather than surveillance takes the deployment.

## The Problem
A conversation arrives. The agent opens the customer record, the order system, the billing system, the prior ticket history and the knowledge base, reads enough to form an understanding, and replies. Afterwards they write a summary and select a category from a list of ninety. The reading is retrieval and the writing is summarisation, and both are commodity operations performed by a person under a handle time target.

## What Already Exists
Retrieval over structured and unstructured sources, summarisation, and grounded drafting are all commodity and are increasingly shipped by the support platforms themselves. Categorisation from text is elementary. Integration frameworks for pulling customer state from adjacent systems are standard. Nothing in the required stack is unavailable; the variation is entirely in how well it is adapted.

## The Customization Gap
The adaptation is to an agent working under time pressure with a person waiting. It requires: (1) context delivered as an assembled brief rather than as retrieved documents — who this is, what they have bought, what has gone wrong before, what is open, what they are probably contacting about — since an agent cannot read five sources and needs five lines; (2) drafting grounded in the customer's own state rather than in the knowledge base alone, because a generic article restated is exactly the reply the customer already found and rejected; (3) categorisation derived from the conversation rather than selected from a list, which removes the most-disliked piece of after-work and also produces better data than an agent picking the third option under time pressure; (4) suggestions that are dismissible without friction and never auto-send, since the agent is accountable for what goes out and a system that sends on their behalf will be resisted correctly; and (5) an explicit position that the assistance is not a monitoring channel, because the same infrastructure could be used that way and agents will assume it is unless the product and the organisation are clear.

## Target Customer
Support platform vendors, support operations leaders, and the agents whose handle time is dominated by reading and typing.

## Impact If Solved
Context assembly and after-work generation together account for a substantial share of handle time and are pure overhead. Derived categorisation is the quiet win, since it removes a resented step and simultaneously produces far better categorical data than the current selection under time pressure — which is what every downstream analysis in this industry depends on.
