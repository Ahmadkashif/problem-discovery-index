# Build: Case Assembly and Graduated Response for Account Review

**Niche:** [[niches/freelance-marketplaces/the-trust-safety-agent/profile|The Trust & Safety Agent]]
**Industry:** [[industries/freelance-marketplaces|Freelance Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Assemble the account's full evidentiary picture before the agent opens it, and give them something between "nothing" and "ban".
**Tags:** #graph-neural-networks #large-language-models #graph-theory #evaluation-metrics #confidence-intervals #gradient-boosting #worker-facing #workflow-orchestration
**Contested on:** Whether the evidence an account decision requires can be gathered automatically without the gathering becoming the decision.

## The Problem

A flag arrives. The agent opens the account, reads the flag reason, checks the profile, scans the contract history, looks at the payment methods, searches for related accounts, reads some messages, forms a view, and acts. Fifteen minutes, most of it spent retrieving rather than reasoning.

The retrieval is the same retrieval every time, and it is incomplete under time pressure. The related-account check is a lookup on a couple of identifiers rather than a graph traversal. The client outcome history is a list of ratings rather than an analysis. The benign explanation — this freelancer works from a shared office, this agency legitimately operates multiple accounts, these two people are siblings who both freelance — requires evidence the agent does not have time to look for and therefore usually does not find.

## Why Nobody Has Built This

Trust and safety is a cost centre measured on handle time and backlog, and the investment goes into detection, which reduces the queue, rather than into adjudication, which does not. The engineering attention follows.

There is also a real caution about building anything that looks like an automated verdict on an account, and it is well-founded — an agent who receives a strong recommendation from a system under handle-time pressure will approve it, and the review becomes a rubber stamp with a human's name on it. That caution has, as in disputes, been allowed to block the evidence assembly as well, which is the part that is not a verdict at all.

And the graduated response gap is a policy vacuum. Platforms have suspend and not-suspend because nobody wrote the policy for anything in between, not because the intermediate actions are technically hard.

## What to Build

A case file that exists before the agent opens the ticket, and an action space wider than two options.

Assemble the evidence automatically. The account's full history as a timeline. Its position in the client-freelancer graph, with the relationship structure made visible: who they work with repeatedly, whether those clients have independent activity, whether the cluster is closed. Identifier overlaps — device, payment, address, network — with each one's base rate stated, because a shared IP in a country with heavy NAT means almost nothing and a shared payment instrument means a great deal, and an agent under time pressure treats them as equivalent. Client outcomes: completion rates, dispute history, repeat business, rating distribution against the category. The specific pattern that triggered the flag, with the threshold it crossed and how far.

Present benign explanations as first-class content, not as an afterthought. For each suspicious signal, what would make it innocent, and whether the record supports that. Registered agency with multiple freelancer accounts. Co-working space with many users. Family members in the same household. Shared device in a region where that is normal. The system should actively look for the exculpatory evidence, because the agent under queue pressure will not, and this is where wrongful suspensions come from.

Define the graduated action space and put it in the tool. Restrict withdrawals pending review while leaving work allowed. Remove from search ranking without suspending. Cap contract values. Require additional verification. Discount specific signals — these ratings do not count — without touching the account. Apply a review period with defined exit criteria. Each of these is a proportionate response to a moderate suspicion, and each is currently unavailable, which is why moderate suspicion resolves either to nothing or to a suspension.

Keep the determination human and keep the system out of the recommendation business, for the same reason as in disputes: a recommendation under handle-time pressure becomes the decision. The system's job is that the agent sees everything relevant in the first thirty seconds.

## Target Customer

Trust and safety operations leadership at platforms where the queue has outgrown the team, and where wrongful-suspension incidents have reached leadership or the press. The graduated action space is also what a regulator asks about when examining whether a platform's enforcement against workers is proportionate.

## Impact If Built

The agent spends their fifteen minutes deciding rather than retrieving, and the exculpatory evidence gets looked for by something that is not under time pressure. Moderate suspicion gets a proportionate response instead of an all-or-nothing one, which is where most of the harm in this function currently lives. And the decisions become reviewable, because the case file is a record of what was known at the time.
