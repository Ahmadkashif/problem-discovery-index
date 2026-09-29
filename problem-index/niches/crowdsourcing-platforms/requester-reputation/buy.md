# Buy: Two-Sided Reputation Systems Adapted to an Anonymous Buyer

**Niche:** [[niches/crowdsourcing-platforms/requester-reputation/profile|Requester Reputation & Trust]]
**Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Two-sided marketplaces have well-developed mutual rating systems; here only one side is rated and the other side's behaviour is already measured and simply withheld.
**Tags:** #bayesian-inference #descriptive-statistics #confidence-intervals #evaluation-metrics #hypothesis-testing #workflow-orchestration #worker-facing #automation
**Contested on:** Whether mutual-rating infrastructure is even needed when the behavioural facts are already recorded.

## The Problem

Two-sided reputation is a solved design problem in marketplaces. Mutual ratings, simultaneous release to prevent retaliation, review text, response mechanisms and aggregate scores are standard in ride-hailing, accommodation, freelance and delivery marketplaces, and the design literature on their failure modes is extensive.

Importing that here would be building the wrong thing. Ratings are subjective reports; what a worker needs about a requester is objective and already recorded — rejection rate, approval speed, payment reliability, realised pay. The gap is a publishing decision, not a missing system, and reaching for a mutual-rating product would introduce all of rating's problems while ignoring the data that is already there.

## What Already Exists

Mutual rating systems across the marketplace category. Review platforms with moderation and response. Simultaneous-release designs from the two-sided literature. Trust and safety scoring. Bayesian shrinkage approaches for small samples. Worker-built requester review sites, which are the existing reputation infrastructure in this market.

## The Customization Gap

**Behavioural facts beat ratings and should lead.** Rejection rate is a count. A rating is an opinion coloured by the rater's experience and by retaliation fear. Leading with counts and treating any ratings layer as supplementary is the right design and it is the opposite of what a mutual-rating product provides.

**Retaliation is asymmetric and severe.** A worker who rates a requester badly can be excluded from their future batches and, on platforms where a requester can reject, punished immediately. Any subjective layer needs anonymity and aggregation thresholds far stronger than the standard simultaneous-release design.

**Requesters are frequently one-off.** A researcher posting a single study has no reputation to build and no future to protect, which defeats the ordinary mechanism by which reputation disciplines behaviour. Institution-level aggregation — this university, this company — is a more useful unit than the individual account and is not how marketplace rating works.

**Normalisation by task type is essential.** Raw rejection rates across heterogeneous task types are misleading in both directions. Percentile against comparable tasks is the honest presentation and no rating product does this because ratings are assumed comparable.

**The existing community infrastructure should be incorporated, not competed with.** Workers already maintain review sites and blocklists. A platform that ingested and credited that work, rather than launching a rival system, would get better coverage and the community's trust — which a cold launch will not have.

## Target Customer

Platforms building requester transparency, who should be told the mutual-rating products are the wrong shape. Also the marketplace trust vendors, for whom count-based counterparty disclosure is a distinct pattern in labour markets where the platform already measures everything.

## Impact If Solved

The presentation, moderation and shrinkage machinery gets borrowed where useful, and the count-first design, retaliation-resistant subjective layer, institution-level aggregation, task-type normalisation and community integration get built. Concretely: a requester panel built from facts the platform already has rather than opinions it would have to collect.
