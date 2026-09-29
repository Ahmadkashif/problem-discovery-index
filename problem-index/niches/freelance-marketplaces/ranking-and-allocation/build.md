# Build: Outcome-Targeted Ranking from the Engagement Record

**Niche:** [[niches/freelance-marketplaces/ranking-and-allocation/profile|Ranking & Allocation]]
**Industry:** [[industries/freelance-marketplaces|Freelance Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Rank freelancers by the probability that the engagement completes well and the client returns, not by the probability that someone clicks.
**Tags:** #loss-functions #gradient-boosting #survival-analysis #causal-inference #evaluation-metrics #confidence-intervals #revenue-impact #matrix-decompositions
**Contested on:** Whether a ranker can be trained against an outcome that arrives eight weeks after the session that produced it.

## The Problem

A freelance marketplace's ranker is trained on what it can observe immediately: was the profile clicked, was a message sent, was an invitation issued. The thing the marketplace actually wants is an engagement that completes, gets paid, is rated well and brings the client back for a second project. That signal arrives weeks or months later, is attached to a contract rather than a search session, and for most search sessions never arrives at all because nothing was ever hired.

So the ranking optimises a proxy. Freelancers who present well and respond fast rise; freelancers who deliver well but photograph badly do not. Clients hire from the top of a page ordered by clickability and experience an outcome ordered by something else, and the gap between the two is the platform's single largest unmeasured quality loss.

## Why Nobody Has Built This

The attribution is genuinely hard. A search session in March produces an invitation in March, a contract in April and a completion in June, and the chain between them is broken at every step by off-platform messaging, multi-candidate shortlists and contracts that quietly expire rather than ending. Most platforms have the pieces in separate systems and have never joined them into a single trainable record.

There is also a selection problem that a naive join makes worse. Outcomes are only observed for people who were ranked highly enough to be hired, which is exactly the population the current ranker favours, so training on completions alone reinforces whatever the current ranker already believes. Correcting for that requires either logged propensities from the existing ranker or deliberate exploration in the ranking itself, and deliberate exploration means showing some clients a worse page on purpose — a cost the product organisation has to agree to bear.

## What to Build

A ranking system trained on engagement outcomes rather than session engagement, with the attribution chain rebuilt as a first-class dataset.

Start by constructing the joined record: search session → impression → click → message → invitation → contract → milestone payments → completion or termination → rating → client return. Every stage is in the platform's own logs. The output is a per-impression label for the outcome that eventually followed, with the censoring made explicit — many impressions have no outcome because nothing was hired in that session, and that is informative rather than missing.

Model the outcome as a survival problem rather than a binary one, because the useful quantity is not "did this complete" but "did this complete, how long did it take, and did the client come back". Contracts that drag for four months and end in a partial refund are failures the binary label records as successes.

Handle the selection bias explicitly. Log the ranker's own scores as propensities and train with inverse propensity weighting; run a small, bounded exploration slot in each results page so that freelancers outside the current top ranks accumulate observable outcomes. Report the exploration cost honestly as a line item, because it is real and it is the price of a ranker that can improve.

Finally, evaluate on outcomes with confidence intervals wide enough to be believed. The metric that matters is completion-weighted placement quality and client repeat rate, measured against the incumbent ranker in an interleaved comparison, not offline NDCG against click labels.

## Target Customer

Platform product leadership at freelance marketplaces above roughly $100M in gross services volume, where a percentage point of completion rate is worth more than the engineering cost. The buyer is whoever owns marketplace quality rather than search relevance — the distinction matters, because the search team's metrics are the ones this displaces.

## Impact If Built

The platform's own record becomes the thing it ranks on. Clients hire people who finish well, freelancers rise on delivery rather than presentation, and the marketplace's take rate compounds against repeat engagements rather than first contracts. It also produces, as a by-product, the calibrated outcome model that every other problem in this industry needs — bid-award prediction, reputation calibration and dispute triage all draw on the same joined record.
