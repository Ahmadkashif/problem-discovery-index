# Context With the Alert

**Niche:** [[niches/embedded-finance-platforms/the-compliance-analyst/profile|The Compliance Analyst]]
**Industry:** [[industries/embedded-finance-platforms|Embedded Finance Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The analyst is asked whether a transaction is suspicious for a product they have never used, built by a company they have never spoken to, for customers they know nothing about.
**Tags:** #gradient-boosting #k-nearest-neighbors #large-language-models #confidence-intervals #evaluation-metrics #worker-facing #compliance #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to give one analyst responsible for dozens of independently run products enough context to judge an alert without learning each product from scratch — and whoever supplies that context decides whether the oversight function is real or nominal.

## The Problem
The alert says a customer received eleven transfers in a day. Is that suspicious? For a gig payout product it is a busy Saturday. For a teen account it is alarming. For a marketplace seller it depends on the marketplace. The analyst cannot answer without knowing the product, and what they have is a transaction list and a rule name. So they either escalate everything, which buries the real cases, or they clear on instinct, which is the failure mode nobody sees until an examiner does.

## Why Nobody Has Built This
Monitoring tools were built for a bank reviewing its own customers, where product context is ambient and never needed to be delivered — the software could assume the analyst knew the product because they always had. Per-product baselines require the cross-programme data to be modelled, which nobody did. Programme teams have no obligation to explain their product to the platform's analysts. And analyst judgement quality is unmeasured, so the deficit is invisible.

## What to Build
Deliver the context with the alert. Attach a product profile to every alert — what this programme does, who its customers are, what normal transaction behaviour looks like for it — which is the core and is the difference between a judgement and a guess. Compute the per-programme behavioural baseline from the platform's own data, since the platform holds it and the analyst does not, and this is where the position's advantage is. Express the alert relative to that baseline rather than to a threshold, because eleven transfers means nothing and the ninety-ninth percentile for this product means something. Compare against similar programmes on the same rails, which supplies a reference the analyst could never build. Assemble the investigation evidence automatically from the systems that hold it, since gathering is most of the time spent. Suggest a disposition with its reasoning visible, so the analyst evaluates rather than starts cold. Record dispositions with reasons, which builds the corpus for calibration and for the evidence niche. Measure disposition quality by sampling and review, because an oversight function that has never checked its own judgements has no basis for claiming any. Route alerts to analysts by product familiarity where the coverage allows, since repeated exposure to a product is how context actually builds. Show the analyst which alerts they cleared that later proved to matter, as that is the only feedback the role ever gets. And track queue depth and time per alert honestly, since a function that cannot keep up is a finding.

## Target Customer
Platform compliance operations leadership, the analysts themselves, sponsor banks relying on their judgement, and transaction monitoring vendors whose products assume a single-institution context.

## Impact If Built
The tooling assumed the analyst knew the product because in a bank they always did. Per-programme baselines computed from data only the platform holds turn an unanswerable question into a comparative one.
