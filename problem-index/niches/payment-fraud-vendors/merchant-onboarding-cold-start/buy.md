# Cold Start From Recommendation Systems

**Niche:** [[niches/payment-fraud-vendors/merchant-onboarding-cold-start/profile|Merchant Onboarding & Cold Start]]
**Industry:** [[industries/payment-fraud-vendors|Payment Fraud Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Recommendation systems developed a whole literature on making good predictions for a new entity with no history, and fraud onboarding waits for data.
**Tags:** #transfer-learning #matrix-decompositions #k-nearest-neighbors #evaluation-metrics #confidence-intervals #gradient-boosting #bayesian-inference #k-means-clustering
**Contested on:** Every serious competitor in this niche is fighting to know a new merchant's definition of normal before it has any history — and whoever transfers that from merchants already on the network wins the first ninety days the customer judges them on.

## The Problem
Cold start is one of the most studied problems in applied machine learning. Recommendation systems face it constantly and answered it with content-based features, hierarchical priors, transfer from similar entities, and active elicitation of a few high-information signals. The methods are well understood and widely deployed. Fraud onboarding faces an identical structure and answers it by waiting for three months of data.

## What Already Exists
Content-based cold start methods; hierarchical and multi-task models with shared priors; similarity-based transfer; active preference elicitation; and exploration strategies for new entities.

## The Customization Gap
The adaptation is to a cold start with immediate financial consequence. It requires: (1) errors during the cold start that cost the merchant real revenue rather than a poor recommendation, so exploration must be conservative — this is the substantive difference; (2) an adversary who deliberately targets new merchants knowing their models are weak, which has no analogue in recommendation; (3) the entity being a merchant with its own data governance, so pooling requires a contractual basis; (4) the relevant similarity being behavioural rather than categorical, since vertical labels predict poorly; and (5) a customer actively judging performance during the cold start, which means expectation management is part of the solution.

## Target Customer
Data and onboarding leadership, new merchants, customer success teams, and machine learning platform vendors serving multi-tenant risk products.

## Impact If Solved
Cold start is thoroughly solved elsewhere and this category waits for data. The adaptations that matter are conservative exploration when errors cost revenue, and an adversary who targets new merchants precisely because the model is weak.
