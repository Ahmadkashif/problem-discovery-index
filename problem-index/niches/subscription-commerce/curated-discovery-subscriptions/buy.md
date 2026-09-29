# Recommendation and Preference Elicitation

**Niche:** [[niches/subscription-commerce/curated-discovery-subscriptions/profile|Curated Discovery Subscriptions]]
**Industry:** [[industries/subscription-commerce|Subscription Commerce]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Recommendation research covers cold start, exploration and preference elicitation thoroughly, and curated subscriptions use a sign-up quiz.
**Tags:** #k-nearest-neighbors #bayesian-inference #markov-decision-processes #contrastive-learning #evaluation-metrics #confidence-intervals #monte-carlo-methods #gradient-boosting
**Contested on:** Every serious competitor in this sub-niche is fighting to choose contents a subscriber will be pleased to receive without them having asked for anything specific — and whoever does that keeps the subscriber, because the alternative is a customer who decides they would rather choose for themselves.

## The Problem
Learning what somebody likes from sparse feedback, deciding when to explore rather than exploit, handling a new user with no history, and eliciting preferences with the fewest questions are all well-studied problems with implementations and published results. Conversational and critique-based recommendation exists specifically for the case where a system proposes and a user refines. Curated subscriptions ask eight multiple-choice questions at sign-up and assign from rules.

## What Already Exists
Collaborative and content-based recommendation with cold-start strategies; bandit and Bayesian methods for exploration under uncertainty; preference elicitation minimising questions asked; critique-based and conversational recommendation; diversity and coverage objectives for result sets; and matrix factorisation with side information.

## The Customization Gap
The adaptation is to a delivered set with expensive errors and slow feedback. It requires: (1) an objective over the set's worst item rather than its mean, which is the reframing above and which none of the standard formulations express; (2) exploration with a real cost, since a bandit's exploration arm here is a disappointing physical item rather than a wasted impression — the exploration budget has to be set against a churn cost and that is a materially different calculation; (3) feedback that arrives weeks later and sparsely, which makes the delayed-reward formulation the right one and rules out the fast-iteration assumptions of online recommendation; (4) hard constraints as absolute rather than as strong preferences, since dietary, allergy, ethical and size exclusions must never be violated and a probabilistic recommender will violate them occasionally by construction; and (5) inventory constraints in the selection, since the curated box is chosen from what was bought and the recommendation must respect a stock plan.

## Target Customer
Curated subscription operators, subscription platform vendors, and the recommendation community for whom the delivered-set problem is an under-studied variant.

## Impact If Solved
The literature covers cold start, exploration and elicitation and this category uses a quiz. An objective over the set's worst item, and exploration priced against a churn cost rather than a wasted impression, are the two adaptations the standard formulations do not express.
