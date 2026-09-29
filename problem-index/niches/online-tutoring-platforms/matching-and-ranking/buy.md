# Buy: Marketplace Ranking Stacks Adapted to a Relationship

**Niche:** [[niches/online-tutoring-platforms/matching-and-ranking/profile|Matching & Tutor Ranking]]
**Industry:** [[industries/online-tutoring-platforms|Online Tutoring Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Marketplace ranking infrastructure optimises a transaction; tutoring is a repeated relationship where the first booking is the least informative event in it.
**Tags:** #matrix-decompositions #gradient-boosting #loss-functions #evaluation-metrics #confidence-intervals #word-embeddings #automation #revenue-impact
**Contested on:** Whether conversion-optimised ranking infrastructure can be pointed at a relationship that unfolds over months.

## The Problem

Marketplace search and ranking is a well-served area. Learned ranking, embedding retrieval, feature stores, real-time serving and experimentation platforms are all mature, and a tutoring marketplace can run a competent conversion-optimised ranker without much difficulty.

Conversion is the wrong objective here and the infrastructure encodes it deeply. The value of a tutoring match is realised over weeks of repeated sessions, and the first booking tells you almost nothing about whether the match was good — a poor fit books as readily as a good one. The whole stack, from the label definition through to the experiment metrics, is oriented around an event that is nearly uninformative about the outcome it is supposed to produce.

## What Already Exists

Learning-to-rank libraries, collaborative filtering and matrix factorisation implementations, embedding retrieval, feature stores, real-time inference platforms, and experimentation frameworks with interleaving. All production-grade and none of it needs replacing.

## The Customization Gap

**The label arrives weeks later and is a trajectory.** Ranking pipelines want a per-impression relevance label available quickly. Here the useful label is whether the relationship sustained, which arrives after several sessions and is a sequence rather than a binary. Carrying delayed, trajectory-shaped labels through training and evaluation requires the feature store to snapshot at impression time and the pipeline to handle long censoring — a substantial plumbing change.

**Fit is an interaction and rankers model relevance.** Standard ranking scores an item against a query. Compatibility is a function of the specific pair, needing latent-factor structure over tutor-student pairs with side information for cold starts. Bolting this onto a pointwise ranker is not straightforward and is the core modelling difference.

**The query is a child, described by a parent, imperfectly.** Search queries are short and explicit. Here the input is a parent's description of their child's difficulty, which is often inaccurate — parents commonly report the symptom rather than the gap. The intake has to be designed to elicit better information and the model has to be robust to it being wrong, including revising the match after the first session.

**Exposure allocation has income consequences.** Ranked items are people whose earnings track their position. Exposure floors, new-tutor exploration and amortised fairness across sessions are constraints no ranking library expresses, and here they carry the additional weight that a tutor's ability to build a client base depends entirely on them.

**Rematching is a first-class flow and nobody has one.** When a match fails, the right product action is a supported rematch with what was learned from the failure carried forward. The ranking stack has no representation of a second attempt informed by a first, and the failed-match record is the most informative training data the platform generates.

## Target Customer

Tutoring marketplace engineering teams running a conversion-optimised ranker and looking at first-match churn they cannot move. Also the broader services-marketplace ranking vendors, for whom relationship-shaped matching is a recognisable gap across several verticals.

## Impact If Solved

The retrieval, serving and experimentation infrastructure gets kept, and the delayed trajectory label, the interaction model, the imperfect query, the exposure constraints and the rematch flow get built. Concretely: the ranker starts optimising whether the family is still there in six weeks, which is the outcome the business actually depends on.
