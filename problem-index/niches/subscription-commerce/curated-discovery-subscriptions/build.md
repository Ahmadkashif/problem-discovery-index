# Choosing for Somebody Who Did Not Choose

**Niche:** [[niches/subscription-commerce/curated-discovery-subscriptions/profile|Curated Discovery Subscriptions]]
**Industry:** [[industries/subscription-commerce|Subscription Commerce]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Recommendation engines are a solved commodity for browsing catalogues, and choosing what to put in a box a customer did not select is a different problem that the tooling does not address.
**Tags:** #k-nearest-neighbors #bayesian-inference #contrastive-learning #evaluation-metrics #confidence-intervals #gradient-boosting #revenue-impact #markov-decision-processes
**Contested on:** Every serious competitor in this sub-niche is fighting to choose contents a subscriber will be pleased to receive without them having asked for anything specific — and whoever does that keeps the subscriber, because the alternative is a customer who decides they would rather choose for themselves.

## The Problem
A recommender suggests ten items and the customer picks one; the nine misses cost nothing. A curated box contains five items the customer must receive; two misses out of five is a disappointing box and three is a cancellation. The recommendation machinery available was built for the first situation, optimises average relevance, and is indifferent to the distribution — which is exactly the wrong objective when every item is delivered and a single bad one colours the whole box. Operators therefore fall back on quizzes and rules, which are worse at the relevance part too.

## Why Nobody Has Built This
The recommendation literature and its tooling are built around ranking for selection, and the delivered-set problem is a different objective nobody has productised. Feedback per item is sparse because nobody collects it well. The cost of a miss is unquantified, so the objective cannot be stated. And the category is full of operators without the data capability to build something bespoke.

## What to Build
Optimise the set, not the average. Select contents to minimise the probability of a disappointing item rather than to maximise mean predicted appeal, since the customer's experience is dominated by the worst item in the box and the standard objective is indifferent to it — this reframing is the build. Collect per-item feedback in a form people will actually give: one tap per item, in the app or on a card in the box, which is the difference between a feedback rate of two percent and thirty. Read behaviour as feedback where explicit signals are absent — returns, unopened items where observable, what gets re-ordered from the shop, what gets given away in a swap. Manage exploration deliberately, since learning a subscriber's taste requires occasionally sending something outside the confident region and doing that by accident is how boxes go wrong — allocating a known share of the box to exploration makes it a decision rather than a mistake. Model the cost of a miss explicitly, since a mildly disliked item and an item that offends a stated exclusion are not the same error. Respect hard exclusions absolutely, because a single violation of a stated allergy, ethical or size constraint destroys trust permanently. Report predicted box satisfaction before dispatch, so a bad box can be caught while it is still changeable. And learn across subscribers, since a new subscriber's first box is the highest-stakes decision and cold-start is where the category loses people.

## Target Customer
Curated subscription operators, the merchandisers making the selections, and the platform vendors whose recommendation offering is a catalogue recommender.

## Impact If Built
The customer's experience is dominated by the worst item in a box and the standard objective optimises the mean. Allocating a known share of the box to exploration converts taste learning from an accident into a decision, and one-tap per-item feedback is the difference between a two percent response rate and a usable one.
