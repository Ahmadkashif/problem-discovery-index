# Search Outcomes as Ground Truth on Linkage Quality

**Niche:** [[niches/collections-agencies/identity-skip-trace-data-providers/profile|Identity Resolution & Skip Trace Data Providers]]
**Industry:** [[industries/collections-agencies|Collections Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Billions of searches return an address or a phone number, the customer then discovers whether it was right, and none of that verdict returns to the linkage that produced it.
**Tags:** #graph-neural-networks #contrastive-learning #random-forests #gradient-boosting #evaluation-metrics #cross-validation #confidence-intervals #probability-distributions #data-integration #revenue-impact

## The Problem
The identity graph is built by inference — records are linked because names, addresses, dates, and identifiers agree closely enough under rules and models developed over decades. Whether a given link is correct is knowable only from the outside, and the outside is exactly where the customers are. An agency dials the returned number and reaches the right person, reaches a stranger, or reaches a disconnected line; mails the returned address and gets a response or a return to sender. Every one of those is a verdict on a specific link, generated at enormous volume, and none of it comes back. So the graph is maintained on internal consistency and source quality heuristics, and its accuracy in the field is estimated rather than measured — in a product whose entire value is that the link is right.

## Why Nobody Has Built This
Outcomes belong to customers, arrive as operational exhaust rather than as structured feedback, and returning them requires an integration nobody has had a reason to build. There is a legitimate concern about the incentive too: a feedback loop that optimizes toward links customers act on could reinforce whatever is easiest to contact rather than what is correct, which in an identity product is a serious failure mode. And permissible-purpose regimes govern what customer activity data can be used for, so the compliance path has to be designed rather than assumed — which has been enough friction to stop the idea before it started.

## What to Build
A structured outcome return channel with the incentives and the compliance path designed in. Customers report contact outcomes at the link level — right party reached, wrong party, disconnected, mail returned — in exchange for something they want: link-level confidence on future searches and a measure of their own contact performance against comparable users. Outcomes are aggregated and de-identified before entering the graph's evaluation layer, so no customer's activity is reconstructable and permissible-purpose boundaries hold. The evaluation layer then supplies what the business has never had: measured precision by link type, source combination, record age, and population segment, which turns source quality from a procurement assumption into a measurable contribution. It supports honest confidence on every returned result rather than an ordering. And it identifies the specific linkage patterns that fail in the field, which is where the modelling effort should go and currently cannot be directed because nobody knows where the errors are.

## Target Customer
Chief data officers and heads of identity science at data providers running 300-1,500 staff, and the operations leaders at collection agencies and other high-volume users who currently discover linkage errors one wasted call at a time.

## Impact If Built
Converts the product's central claim from an internal quality process into a measured one. In a market where several providers assemble broadly similar source sets, demonstrated field accuracy by segment is the only durable differentiator, and it can only be built by the provider that closes the loop with its own customers. It also directs source acquisition spend — the industry's largest recurring investment — at measured contribution rather than at coverage counts.
