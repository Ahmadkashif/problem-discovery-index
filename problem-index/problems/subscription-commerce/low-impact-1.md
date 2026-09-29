# Curation and Personalisation

**Industry:** [[subscription-commerce|Subscription Commerce]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Recommendation engines are a solved commodity for browsing catalogues, and choosing what to put in a box a customer did not select is a different problem that the tooling does not address.
**Tags:** #gradient-boosting #k-nearest-neighbors #contrastive-learning #bayesian-inference #evaluation-metrics #confidence-intervals #optimization-fundamentals #revenue-impact

## The Problem
A curated subscription selects on the customer's behalf. That is the product — the customer is paying not to choose — and it means every box is a prediction with a delivery cost attached.

The prediction is hard in ways ordinary recommendation is not. Feedback is sparse: one box a month, and the signal is often only whether they stayed. Repetition is penalised heavily, since sending something similar to last month's is a visible failure in a way that a repeated recommendation on a website is not. Novelty is the point, so an accurate prediction of something the customer already likes may be exactly wrong. And inventory constrains everything — the recommendation must be satisfiable from what is in the warehouse this month, across every subscriber simultaneously.

Most companies handle this with rules derived from a sign-up quiz. The quiz answers age immediately, are answered aspirationally, and describe a customer who has not yet received anything.

## What Already Exists
Recommendation systems are mature and available as managed services. Collaborative filtering, content-based approaches and hybrid systems are well understood. Preference quizzes are a standard onboarding pattern. Product attribute taxonomies exist in most categories. A few larger subscription businesses have built genuine recommendation capability and it is a visible differentiator.

## The Customisation Gap
Standard recommenders optimise the probability that a customer engages with an item they are shown. Here the objective is different and multi-term: satisfaction with a bundle, novelty, non-repetition, and satisfiability against constrained inventory across the whole subscriber base at once. That is an assignment problem with a preference model inside it, not a ranking problem.

Feedback is the binding constraint and it is improvable. Most subscription companies collect almost nothing per item — no rating, no easy way to say this was wrong — so the model learns from cancellation, which is the latest and least informative signal available. Lightweight per-item feedback would transform the data situation and is a product decision.

Bundle-level effects are unmodelled. A box is judged as a whole, and a good box is not simply five individually good items — variety, coherence and a standout item matter, and no recommendation framework represents this.

Inventory-aware allocation is the fourth gap: giving every subscriber the item the model likes best is impossible, and the fair and optimal allocation across a constrained catalogue is a real optimisation nobody solves.

## Impact If Solved
Box contents are the product in curated subscription and are selected by rules from an ageing quiz. Turning curation into an inventory-constrained assignment against a preference model — with real per-item feedback to learn from — improves the thing customers are actually paying for, and it is the strongest available lever on early-cycle satisfaction.
