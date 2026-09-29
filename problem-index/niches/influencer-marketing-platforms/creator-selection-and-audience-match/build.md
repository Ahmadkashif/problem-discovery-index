# Choosing on Follower Count

**Niche:** [[niches/influencer-marketing-platforms/creator-selection-and-audience-match/profile|Creator Selection & Audience Match]]
**Industry:** [[industries/influencer-marketing-platforms|Influencer Marketing Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The decision that determines whether a campaign works is made on follower count and engagement rate, when the question is whether this creator's audience contains buyers the brand does not already have.
**Tags:** #gradient-boosting #matrix-decompositions #evaluation-metrics #confidence-intervals #revenue-impact #causal-inference #k-nearest-neighbors #transformers
**Contested on:** Every serious competitor in this niche is fighting to predict whether a creator's audience contains buyers this brand does not already have — and whoever answers that replaces follower count as the currency of the category.

## The Problem
A brand selects forty creators for a campaign. The selection is made by filtering a database on follower range, engagement rate, category and location, then browsing profiles and forming an impression. Nothing in that process addresses whether these creators' audiences contain people who would buy this product, whether those people are already customers, or whether any similar creator has ever produced sales for a comparable brand. The platform knows the answer to the third question from its own history across thousands of campaigns, and offers a filter.

## Why Nobody Has Built This
The outcome is held by the brand and never returned in a usable form, so the corpus has inputs and no labels — this is the binding constraint and it is the same one running through the whole cluster. Audience composition is estimated from sparse public data rather than known. Follower count is available for every creator and a match score is not, which makes the poor metric the only universal one. And the platforms sell workflow, where selection quality is not the purchase decision.

## What to Build
Predict the match rather than describe the creator. Build a return path for outcome data — even coarse, even aggregate, even for a subset of brands willing — which is the prerequisite and the thing that converts a database into a learning system; a modest amount of returned outcome data would go a very long way here because the number of decisions is small. Model the audience rather than the creator: composition, purchase propensity for the category, and overlap with the brand's existing customers, which is the actual question and is what nothing currently answers. Predict incremental customers rather than reach, since a creator whose audience is already the brand's customer base produces sales that would have happened. Use the partnership corpus, since which creators produced results for which brands is the strongest available signal and sits unused in the platform's own history. Handle the small-numbers regime properly, as a brand runs tens of partnerships rather than millions of impressions and the estimates must carry honest uncertainty rather than false precision. Detect audience quality directly — purchased followers, engagement pods, bot activity — rather than through a single opaque authenticity score. Make tiers comparable, which is the fix note's subject and blocks the most valuable comparisons. Recommend portfolios rather than individuals, because a campaign is a set and audience overlap between chosen creators is a cost nobody currently measures. Explain the recommendation, since a manager must defend the selection internally and an unexplained score will not survive that. And evaluate against the follower-count baseline on realised sales, because that comparison is the whole argument.

## Target Customer
Brand partnership and performance teams, influencer platforms whose differentiation is a database, and the agencies selecting creators at volume.

## Impact If Built
The corpus has inputs and no labels because the outcome is held by the brand, and the decision count is small enough that a little returned data goes a long way. Modelling audience overlap with existing customers turns reach into incremental customers, which is the question nothing currently answers.
