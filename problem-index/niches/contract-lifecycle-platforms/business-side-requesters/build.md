# Legal Is a Black Box With No Estimate

**Niche:** [[niches/contract-lifecycle-platforms/business-side-requesters/profile|Business-Side Requesters]]
**Industry:** [[industries/contract-lifecycle-platforms|Contract Lifecycle Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The person who needs a contract submits a form and receives silence, so they route around the system, and every governance failure in the category starts there.
**Tags:** #large-language-models #survival-analysis #gradient-boosting #bert #evaluation-metrics #confidence-intervals #worker-facing #workflow-orchestration
**Contested on:** Every serious competitor that takes this seriously is fighting to let the person who needs a contract get one — or know exactly when they will — without asking a lawyer, and whoever does that takes the deployment, because the requester decides whether a CLM system is used or routed around.

## The Problem
A salesperson needs an order form for a deal closing at the end of the month. They submit a request with eleven fields, three of which they guess. Nothing happens visibly for four days. They ask in a chat channel; somebody says it is in the queue. On the seventh day a document arrives with tracked changes, and they cannot tell whether the changes matter to their customer. On the next deal they take the previous contract from a shared drive, change the name and the numbers, and send it directly — which is faster, works, and is exactly the behaviour the CLM system was bought to prevent.

## Why Nobody Has Built This
The buyer is legal operations and the user is the business, which is a classic misalignment: the product is specified by people who do not experience it. Status is modelled as a workflow state for internal purposes rather than as something to communicate outward. Estimating completion requires predicting cycle time, which nobody does even though the historical data supports it well. And bypass is invisible — a contract that never entered the system leaves no trace in it — so the failure is unmeasured and the product appears to be working.

## What to Build
Design for the requester. Determine self-service eligibility from the request itself rather than from the requester's choice of form: a standard agreement type, within policy thresholds, with a known counterparty is generated and sent without legal involvement, and the requester never sees a queue. For everything else, give an estimated completion date with a confidence range, predicted from historical cycle times for comparable requests — which is straightforward modelling and is the single thing requesters most want. Show real status in plain terms: with legal, with the counterparty, awaiting your approval. Explain returned redlines commercially — what changed, what it means for the deal, what needs a decision from the requester and what does not — since the tracked-changes document is unreadable to its recipient. Make the intake form derive most of its fields from the opportunity or purchase record rather than asking, since the requester's guesses are a major source of downstream error. And close the loop by telling them when it is signed, with the executed copy, which is a surprisingly common gap.

## Target Customer
Legal operations, whose adoption depends on it; and the revenue and procurement functions who generate the volume and currently route around the system.

## Impact If Built
Bypass is the source of nearly every governance failure in the category, and it is a rational response to an experience nobody designed. A completion estimate and genuine self-service eligibility are the two changes that make the sanctioned path faster than the workaround.
