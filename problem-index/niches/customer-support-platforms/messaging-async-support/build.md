# The Complete First Reply

**Niche:** [[niches/customer-support-platforms/messaging-async-support/profile|Messaging & Asynchronous Support]]
**Industry:** [[industries/customer-support-platforms|Customer Support Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Asynchronous support's one advantage over voice is time to gather what is needed before replying, and the most common first reply in the industry is a request for information the organisation already has.
**Tags:** #large-language-models #bert #gradient-boosting #evaluation-metrics #confidence-intervals #workflow-orchestration #automation #worker-facing
**Contested on:** Every serious competitor in asynchronous support is fighting to close an issue without the customer having to come back — and whoever raises first-contact resolution in a channel with no contact takes the account.

## The Problem
A customer writes that their order has not arrived. The reply asks for the order number, the delivery address and when they placed it. The customer is identified, has one recent order, and its tracking status shows a failed delivery attempt at an address that does not match their account — all of which the organisation knows. Two days and three exchanges later the issue is resolved. The single reply that would have resolved it on the first attempt was composable at the moment the message arrived, and the agent did not compose it because assembling the context takes longer than asking.

## Why Nobody Has Built This
The metric is first response time, which a request for information satisfies as well as a resolution does and considerably faster — so the incentive points exactly the wrong way and agents respond to it rationally. Assembling the context means querying several systems, which a macro cannot do and which most agent interfaces do not present. And round trips are not measured, so the cost of the incomplete reply is invisible while the benefit to the response time metric is immediate and reported.

## What to Build
Context assembled before the reply is drafted. When a message arrives, the system resolves the customer, retrieves their relevant state — recent orders, account status, open issues, prior conversations, entitlements, whatever the domain requires — and identifies which of the plausible causes the data already rules in or out. The draft reply addresses the likely case with the specifics filled in, and where information genuinely is needed, it asks only for what could not be determined and asks for all of it at once, which is the second most common failure. Predicted round trips is surfaced to the agent before sending, since a reply flagged as likely to require a follow-up is one worth thirty more seconds. And the measured objective is round trips per resolved issue, reported to the vendor and the customer, because it is the property the customer experiences and the one no current metric captures.

## Target Customer
Support platform vendors, support organisations in commerce, financial services and subscription businesses where the answer depends on account state, and the operations leaders whose response time looks excellent and whose resolution time does not.

## Impact If Built
Round trips determine elapsed resolution time in an asynchronous channel, and a single avoidable exchange costs a day of the customer's experience. Assembling context before drafting is achievable from systems the organisation already runs, and measuring round trips is what removes the perverse incentive that currently rewards the incomplete reply.
