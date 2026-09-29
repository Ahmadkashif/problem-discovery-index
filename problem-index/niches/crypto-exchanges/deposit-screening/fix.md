# Frozen With No Explanation

**Niche:** [[niches/crypto-exchanges/deposit-screening/profile|Deposit Screening]]
**Industry:** [[industries/crypto-exchanges|Crypto Exchanges]]
**Type:** Fix (Pain Point)
**One-liner:** The customer's deposit is held, the reason is a risk score they cannot see, and the support reply says the review is ongoing.
**Tags:** #worker-facing #compliance #quick-win #automation #evaluation-metrics #workflow-orchestration #descriptive-statistics #large-language-models
**Contested on:** Every serious competitor in this niche is fighting to decide correctly whether arriving funds are criminal proceeds — and the contest splits cleanly enough that it is not terminal.

## The Problem
A customer received coins from a gaming platform, a friend, or a service several hops removed from anything illicit. The deposit is held. They are told a review is in progress and cannot be told why, because the reason is a vendor characterisation the exchange treats as confidential and would not fully understand if disclosed. They wait weeks. Support cannot see the case status, the analyst queue has no visible priority, and the customer's only escalation is a public complaint.

## Why It's Still Broken
Explanation was treated as a disclosure risk, so the default became silence — and silence is cheap for the institution and expensive only for the customer. The reason lives in a vendor's interface rather than in a form anyone can communicate. Support and compliance are separate functions with no shared case view. And nobody measures how long holds last or how many resolve in the customer's favour.

## What a Fix Looks Like
Tell the customer what can be told, and measure the queue. Publish what triggers a hold in general terms, which is the fix and costs nothing that is not already inferable from the public ledger. Tell the customer what would resolve it — the provenance that would satisfy an analyst — since most legitimate customers can supply it and currently do not know to try. Give support a case status view, because the customer is asking a question support cannot see the answer to. Set and publish a resolution timeframe, as an open-ended hold on someone's money is the core grievance. Age and escalate cases explicitly, since the queue's tail is where the damage concentrates. Report hold duration and outcome rates internally, which is a straightforward query and is the first honest picture the exchange would have of its own control. Prioritise by amount and by customer history, because a small deposit from a long-standing account and a large one from a new account are not the same case. Structure the provenance submission rather than accepting free-form email, so analysts are not reading attachments. Record the resolution reason in a fixed vocabulary, which builds the label set the evaluation problem needs. And route repeat holds on the same customer for review, since a customer held three times is either a real case or a threshold error.

## Who Feels the Pain
Customers separated from their funds with no stated reason or timeline; support agents with no visibility into the case; analysts working an unprioritised queue; and exchanges whose complaint volume is their only feedback signal.

## Impact If Fixed
Silence became the default because explanation looked like disclosure risk and the cost fell entirely on the customer. Stating the trigger, the remedy and a timeframe resolves most legitimate cases and generates the resolution labels the control has never had.
