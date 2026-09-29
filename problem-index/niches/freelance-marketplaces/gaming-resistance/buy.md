# Buy: Fraud and Graph Analytics Adapted to Reputation Manipulation

**Niche:** [[niches/freelance-marketplaces/gaming-resistance/profile|Gaming Resistance]]
**Industry:** [[industries/freelance-marketplaces|Freelance Marketplaces]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Fraud platforms are built to catch a fraudulent transaction; reputation manipulation is a sequence of entirely legitimate transactions whose only defect is that they were arranged.
**Tags:** #graph-neural-networks #graph-theory #k-means-clustering #gradient-boosting #evaluation-metrics #dbscan #compliance #automation
**Contested on:** Whether transaction-fraud machinery can recognise abuse in which every individual transaction is real, paid and consensual.

## The Problem

Marketplaces buy fraud infrastructure, and it is good. Device fingerprinting, velocity rules, identity graphs, network-level risk scoring and managed review queues are all available off the shelf and catch payment fraud, account takeover and stolen-instrument abuse well.

Reputation manipulation slips through all of it, because it is not fraud in the sense any of these systems model. A freelancer and a cooperating client sign a real contract, real money moves through escrow, real platform fees are paid, and a real five-star rating is left. Nothing about the transaction is fraudulent. What is wrong is the relationship between the parties and the purpose of the transaction, and that is a property of the graph over months, not of the payment.

## What Already Exists

Sift, Sardine, Unit21 and the established fraud platforms, with rules engines, case management and device intelligence. Graph databases and graph ML libraries — PyTorch Geometric, DGL — that handle bipartite relational data at marketplace scale. Community detection algorithms, from Louvain through to learned approaches. Identity verification vendors. Every component is production-ready.

## The Customization Gap

**The label is different in kind.** Fraud platforms are trained on chargebacks and confirmed fraud, which arrive as ground truth from an external system. Reputation manipulation has no external oracle — nobody disputes a rating ring, because everyone involved is happy. Labels come only from manual integrity investigations, which are few, biased toward what was already detectable, and expensive. The adaptation is a pipeline that can learn from a handful of confirmed rings plus large-scale weak signals, rather than one that assumes a labelled stream.

**The unit of analysis is a subgraph over months.** Fraud scoring is per-transaction, sub-second, on features available at authorisation time. Manipulation detection is a batch problem over a client-freelancer bipartite graph with a year of history, looking for structure — reciprocity, closure, clients with no independent activity, contract values implausibly uniform. None of the real-time infrastructure applies; the platform's feature store, retention and compute assumptions all have to change.

**Benign structure looks exactly like malicious structure.** A freelancer with ten contracts from three long-standing clients is either a rating ring or a healthy retained-client relationship, which is what the marketplace wants most. Distinguishing them needs domain features the fraud stack has no concept of: whether the work product was delivered through platform tooling, whether contract values track scope, whether the client has spending elsewhere, whether communication volume matches the work claimed. Getting this wrong destroys the accounts of the platform's best freelancers.

**The action space is not "block".** Fraud systems decline or allow. Here the right response is usually to discount a signal rather than punish an account — this rating carries less weight, these completions do not count toward tier — because the confidence is lower and the cost of a false positive is someone's livelihood. That graduated response has no representation in a rules engine built to approve or decline.

**The adversary adapts and the vendor's model is shared.** A bought fraud model's decision boundary is learned across the vendor's customers and is not specific to this marketplace's mechanics. Manipulation techniques here are highly specific to how this platform computes tiers, and the arms race is per-platform. The bought layer handles the generic, and the platform-specific layer has to be owned.

## Target Customer

Trust and safety organisations at marketplaces that have already deployed a fraud platform and keep finding manipulation it does not see — usually discovered through client complaints about top-ranked freelancers rather than through any detection system.

## Impact If Solved

The generic infrastructure keeps doing what it does well and the marketplace-specific layer catches the abuse that is invisible to it. The practical result is that organised rating and completion manipulation gets discounted at the signal level rather than fought account by account after the ranking benefit has already been banked.
