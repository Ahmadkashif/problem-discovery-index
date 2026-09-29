# Build: Award Probability Before the Proposal Is Written

**Niche:** [[niches/freelance-marketplaces/proposal-and-bidding/profile|Proposal & Bidding]]
**Industry:** [[industries/freelance-marketplaces|Freelance Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Predict whether a posted job will be awarded to anyone, and to this freelancer in particular, and show both numbers before they spend an evening and a credit balance.
**Tags:** #gradient-boosting #logistic-regression #survival-analysis #confidence-intervals #evaluation-metrics #feature-engineering #worker-facing #quick-win
**Contested on:** Whether an award probability can be calibrated well enough that a freelancer will trust it with their evening.

## The Problem

A freelancer's scarcest resource is the hour they spend reading a brief and writing a tailored response to it. They spend that hour against a job post with no information about whether the post will result in a hire at all. A substantial share of posts on every major marketplace never produce a contract — the client was price-checking, or had already chosen someone, or never had budget.

The information that would separate these posts exists. Every platform holds millions of historical posts with their outcomes and the client behaviour that preceded them. The freelancer is denied access to the only dataset that could tell them where to spend their effort, and the platform sells them the right to guess.

## Why Nobody Has Built This

The revenue conflict is direct and is the whole answer for the credit-based platforms. Bids are monetised. A model that says "this post has a 15% chance of being awarded" reduces bid volume on exactly the posts where volume is highest, because low-intent posts attract bids indiscriminately. The monetisation team's forecast and the freelancer's interests point in opposite directions, and there is no version of this that does not show up as a revenue line.

There is a second obstacle that is real but smaller: the demand side would object to being scored. A client whose post is labelled unlikely-to-be-awarded receives fewer and worse proposals, which makes the prediction self-fulfilling and makes the client unhappy. Handling that requires the score to be about the post rather than the person, to be visible in aggregate rather than as a public label, or to be surfaced to the client as an improvement prompt before it is surfaced to freelancers as a warning.

## What to Build

Two models, both of which train on labels the platform already has in abundance.

The first predicts **award probability for the post**: will this job result in a contract with anyone, within a horizon. Features are entirely available at post time — client tenure, prior posts and their outcomes, prior spend, payment verification, budget stated relative to the scope described, brief length and specificity, category, whether the post reuses text from a prior post, time of day, whether the client responded to messages on previous posts. Framing it as survival rather than binary classification is worth the effort, because "awarded within four days" and "awarded within six weeks" are completely different propositions for a freelancer deciding where to spend tonight.

The second predicts **conditional win probability for this freelancer**: given the job is awarded, what is the chance it goes to them. This depends on their fit, their rate against the stated budget, the competing proposal count and composition, their history in the category and their response latency. Multiplied together, the two give the number that actually matters: the expected value of writing this proposal.

Calibration is the entire product. A freelancer will use this exactly as long as the stated 20% is 20% in practice, and will abandon it permanently after one bad week if it is not. Report reliability diagrams, not AUC. Show the number with an interval. Under-promise on new clients, where the model genuinely does not know.

Close the loop by making the recommendation actionable rather than merely informative: given a freelancer's available hours this week and the current post feed, which subset of posts maximises expected contracts. That is a small optimisation over the two models and it is what turns a score into a tool.

And build the demand-side half deliberately, because it is what makes the whole thing politically survivable: tell clients, at post time, what about their post predicts a poor response — an unrealistic budget, a vague scope, unverified payment — and let them fix it. The same model serves both sides, and framing it as post quality improvement for clients is the version that ships.

## Target Customer

Platforms not monetised on bid volume have the cleanest path, and should treat this as a competitive weapon against those that are. For credit-based platforms the buyer is whoever owns supply-side retention rather than bid revenue, and the argument is churn: the freelancers who leave are disproportionately those who spent weeks bidding into nothing. There is also an independent third-party product here, built on public job feeds and observable outcomes, which needs no platform cooperation and has been partially attempted by scraping tools that lack the outcome labels.

## Impact If Built

The supply side's unpaid labour stops being spent on posts that were never going to hire. Freelancers write fewer, better proposals against jobs that exist, which raises the quality clients see. And the marketplace stops quietly taxing the least-informed participants for the privilege of guessing.
