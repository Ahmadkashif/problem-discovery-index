# List Growth Quality and Decay

**Industry:** [[newsletter-media|Newsletter Media]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Subscribers are bought from channels of wildly varying quality, and a cheap subscriber who never opens damages the sender reputation that governs delivery to everyone else.
**Tags:** #gradient-boosting #survival-analysis #k-means-clustering #logistic-regression #confidence-intervals #evaluation-metrics #feature-engineering #revenue-impact

## The Problem
Growth is bought. Paid social, recommendation networks, co-registration paths, cross-promotion swaps, giveaways and content upgrades each deliver subscribers at a cost per acquisition, and the quality varies by an order of magnitude.

The variation is not visible at signup. A subscriber acquired through a giveaway and one acquired from a cited article look identical in the list. Their behaviour diverges immediately and permanently: one opens for years, the other never opens and eventually marks a send as spam.

The damage is not confined to the bad subscriber. Complaint rates and engagement distribution feed the sender reputation that determines placement for the whole list. A publisher who adds twenty thousand low-quality subscribers has not merely wasted money; it has degraded delivery for the hundred thousand good ones, which is a far larger cost and is attributed to the acquisition channel by nobody.

Decay runs continuously. Subscribers lose interest, change jobs, abandon addresses. Continuing to mail the dormant depresses engagement rates and eventually triggers the provider's spam-trap and reputation mechanisms. Every publisher knows to suppress the dormant and few can say what the right threshold is for their list.

And cost per acquisition is the metric everyone optimises, which is exactly the wrong one, because it treats a subscriber who will generate years of advertising impressions and one who will generate a spam complaint as the same purchase.

## What Already Exists
ESPs report engagement by segment and support sunset policies. Recommendation networks like beehiiv Boosts and SparkLoop provide growth with partial quality signals. Double opt-in reduces low-intent signups at a conversion cost. List hygiene vendors verify addresses. Cohort reporting exists in the better platforms.

## The Customisation Gap
Lifetime value by acquisition source is rarely computed. The publisher has every subscriber's source, engagement history, tenure and eventual outcome, which supports a direct survival and value analysis by channel, and growth is nonetheless bought on cost per acquisition.

The reputation externality is entirely unmodelled. The cost of a low-quality cohort includes its effect on everyone else's delivery, which is the largest component and appears in no channel evaluation anywhere in this industry.

Sunset thresholds are rules of thumb. The right point to stop mailing a dormant subscriber is an empirical question — the probability of reactivation against the reputation cost of continued non-engagement — and it differs per publisher and per provider.

Early quality prediction is unattempted. A subscriber's first two weeks of behaviour predict their trajectory well, and a publisher who could grade a cohort at day fourteen rather than at month six would stop buying badly far sooner.

## Impact If Solved
Growth spend is the largest discretionary cost in a newsletter business and is allocated on a metric that ignores both subscriber value and the reputation damage bad cohorts cause. Value-based channel evaluation, an explicit reputation externality and empirically derived sunset thresholds redirect the budget and protect the delivery the whole business depends on.
