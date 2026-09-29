# Explaining a Decision Nobody Can See

**Niche:** [[niches/online-marketplaces/the-seller-appeals-agent/profile|The Seller Appeals Agent]]
**Industry:** [[industries/online-marketplaces|Online Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A support agent handles an appeal from a seller whose income has stopped, cannot see why the account was suspended, and cannot explain a decision made by a system they have no visibility into.
**Tags:** #worker-facing #evaluation-metrics #compliance #descriptive-statistics #confidence-intervals #automation #data-integration #logistic-regression
**Contested on:** Every serious competitor in this niche is fighting to give the person handling an appeal the reason for the suspension and the authority to act on it — and whoever does that takes the account, because this conversation is where a marketplace's relationship with its sellers is decided.

## The Problem
A seller whose shop is their household income receives a suspension notice citing a policy section. They appeal. The agent who receives it sees the same policy code, a flag, and nothing else — not which listing triggered it, not which signal, not how close the score was to the threshold, not whether the seller has a clean five-year history. They write a templated response asking the seller to review the policy. The seller, who has reviewed the policy and cannot see what they did wrong, replies increasingly desperately. The agent escalates. Four days pass. The information that would have resolved this in one exchange sits in a detection system the support tool does not connect to.

## Why Nobody Has Built This
The detection systems were built by risk teams and the support tools by support teams, and nobody owns the join. There is a genuine concern that explaining detection signals helps bad actors evade them, which is real for some signals and is applied indiscriminately to all of them. Appeals are a cost centre measured on handling time. And the sellers who leave rather than appeal are not counted anywhere.

## What to Build
Connect the decision to the conversation. Surface the triggering evidence to the agent — which listing, which signal, which threshold, how marginal, what the seller's history is — with the genuinely sensitive detection detail withheld and the actionable part shown, since the distinction between what helps a seller fix a problem and what helps a bad actor evade is one somebody can draw and nobody has. Generate a specific, actionable explanation for the seller, because a seller told which listing and what to change complies, and a seller told to review the policy escalates. Show the agent the decision's confidence, so a marginal case and an overwhelming one are handled differently. Give the agent authority to reinstate within defined bounds, since a clear false positive should be resolved in the conversation rather than in a four-day queue. Prioritise by consequence, because a seller whose income has stopped is a different case from a dormant account and the queue currently treats them identically. Report the seller's own history in the view, since a five-year clean record is relevant and is currently invisible. Let the agent's assessment feed back into detection, which the fix note develops. And measure resolution quality and seller retention after an appeal rather than handling time, because the fast unhelpful response is the one the current metric rewards.

## Target Customer
Seller support organisations, the agents handling appeals, the sellers whose livelihoods are involved, and the operators losing supply through this channel.

## Impact If Built
The information that would resolve the appeal in one exchange sits in a system the support tool does not connect to. Drawing the line between what helps a seller comply and what helps a bad actor evade is a distinction somebody can make and nobody has.
