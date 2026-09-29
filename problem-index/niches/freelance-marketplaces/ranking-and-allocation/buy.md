# Buy: Learning-to-Rank Infrastructure Adapted to Two-Sided Outcomes

**Niche:** [[niches/freelance-marketplaces/ranking-and-allocation/profile|Ranking & Allocation]]
**Industry:** [[industries/freelance-marketplaces|Freelance Marketplaces]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Mature ranking and recommendation stacks assume a single-sided relevance objective; a labour marketplace needs two-sided outcomes and supply-side fairness constraints they do not express.
**Tags:** #loss-functions #matrix-decompositions #gradient-boosting #word-embeddings #evaluation-metrics #cross-validation #automation #revenue-impact
**Contested on:** Whether a general-purpose ranking stack can express the constraint that the ranked items are people whose income depends on their position.

## The Problem

Ranking infrastructure is one of the best-served areas in applied machine learning. Open-source learning-to-rank libraries, feature stores, embedding retrieval, online serving layers and experimentation platforms are all mature and well documented. A marketplace team can stand up a competent ranker in a quarter.

What that stack assumes is a single-sided problem: items have no interests, and relevance to the searcher is the whole objective. On a freelance marketplace the items are people, the objective is a joint outcome for two parties, and the distribution of exposure across the supply side is itself a product decision with income consequences. None of that is expressible in the interfaces the standard stack provides.

## What Already Exists

LightGBM and XGBoost with ranking objectives, TensorFlow Ranking, and a well-developed literature on pairwise and listwise losses. Vector retrieval through FAISS and the managed vector databases. Feature stores, online inference platforms and interleaving frameworks. Multi-armed bandit libraries for exploration. Every one of these is production-grade and none of them needs replacing.

## The Customization Gap

Four adaptations sit between the stack and the problem.

**The label is joint and delayed.** Standard ranking pipelines assume an immediate relevance judgement per query-item pair. Here the label is a contract outcome attached to neither the query nor the item alone, arriving weeks later, and absent entirely for the majority of sessions. The pipeline has to carry censored, delayed, session-detached labels through training and evaluation — which means the feature store must snapshot features as of impression time, not as of training time, or the model learns from the future.

**Exposure is a resource, not a by-product.** A ranker that is 2% better at relevance and concentrates 60% of impressions on 5% of freelancers may be worse for the marketplace, because the concentrated supply saturates and the long tail leaves. Expressing an exposure floor, or an amortised-fairness constraint across sessions, requires post-processing the ranked list against supply-side state that the ranking library has no concept of.

**Cold start is the normal case, not the edge case.** A large fraction of the supply side has no outcome history at all, and the ones who do are disproportionately those the previous ranker favoured. The retrieval and scoring layers need a principled prior for the unobserved — skills, portfolio content, verification status — rather than a default score that permanently buries new entrants.

**Adversarial features need separating from honest ones.** In a normal recommender, features are attributes. Here some features are under the ranked party's deliberate control, and the ones easiest to manipulate are often the most predictive in historical data. The feature pipeline needs an explicit manipulability classification and the training loop needs to weight accordingly — a distinction no ranking library models.

## Target Customer

Marketplace engineering teams that already run a ranking stack and are hitting its ceiling — typically the point at which supply-side complaints about distribution reach leadership, or the point at which relevance improvements stop moving completion rate. Also the platforms buying managed search infrastructure who need to layer marketplace semantics on top of it.

## Impact If Solved

The team keeps the well-understood infrastructure and adds the four things that make it a labour marketplace ranker rather than a product search ranker. Practically this means the exposure distribution becomes a dial leadership can set rather than an emergent property nobody chose, and new freelancers get a defensible path to their first contract instead of waiting for a signal that only hiring produces.
