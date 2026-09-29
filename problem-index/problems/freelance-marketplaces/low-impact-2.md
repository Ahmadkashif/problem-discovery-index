# Dispute Resolution and Escrow Adjudication

**Industry:** [[freelance-marketplaces|Freelance Marketplaces]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** When a client and a freelancer disagree about whether work was delivered, a support agent reads a message thread and decides who gets the money.
**Tags:** #bert #large-language-models #gradient-boosting #evaluation-metrics #confidence-intervals #compliance #worker-facing #k-nearest-neighbors

## The Problem
Escrow protects both sides until it has to be adjudicated. A client says the work was not what was agreed; a freelancer says it was and the client changed their mind. The evidence is a scope description written informally at the outset, a message thread, and the delivered files.

The adjudication is manual and fast. An agent reads the thread, applies policy, and releases or refunds. The decision is consequential — for a freelancer it may be a month's income, and an adverse outcome frequently also damages their metrics — and the agent has minutes.

Consistency is the recurring complaint from both sides. Similar cases resolve differently depending on the agent, the day and how the arguments were presented. There is usually no accessible precedent, no visible reasoning, and limited appeal.

The root cause is upstream: the scope was never specified tightly enough to adjudicate. Informal scoping is what makes marketplace transactions fast and it is also what makes disputes unresolvable, and the platform's interface encourages the informality.

## What Already Exists
All major platforms operate escrow with milestone release, a dispute process and an arbitration step, sometimes with a third-party arbitrator for large amounts. Policies are published. Some platforms provide structured contract templates and milestone definitions that reduce ambiguity where used. Message archives provide the evidence record. Fraud detection identifies collusive transactions and payment abuse.

## The Customisation Gap
Precedent is the missing infrastructure. Every platform has adjudicated thousands of disputes and none maintains a retrievable body of comparable cases with their reasoning, so each agent decides from policy and instinct. Surfacing similar past cases and how they were resolved would make outcomes consistent and is straightforward retrieval over the platform's own records.

Evidence structuring is the second gap. Reconstructing what was agreed from a long informal thread is the bulk of the adjudication time, and extracting the commitments — scope statements, revision agreements, deadline changes — into a timeline with citations would let an agent see the case rather than read it.

Prediction is the third, and it belongs upstream. Disputes are foreseeable from observable signals — vague scope, scope growth during the engagement, payment terms that are unusual for the category, communication patterns that have deteriorated — and flagging a live engagement as at risk while it can still be clarified is worth more than adjudicating it well afterwards.

And the reasoning should be given. A decision delivered with the specific evidence it rested on, and a real appeal route, is the minimum for a process that determines whether someone is paid for work they may well have done.

## Impact If Solved
Disputes are the point at which marketplace trust is tested for both sides, and they are resolved inconsistently by agents under time pressure with no precedent. Case retrieval and structured evidence make adjudication consistent and fast, upstream risk detection prevents a share of disputes from forming, and stated reasoning with an appeal path is what makes the outcome defensible to the person whose month of income it decides.
