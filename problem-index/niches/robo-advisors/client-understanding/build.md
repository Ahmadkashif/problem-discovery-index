# The Dataset They Publish and Do Not Use

**Niche:** [[niches/robo-advisors/client-understanding/profile|Client Understanding]]
**Industry:** [[industries/robo-advisors|Robo-Advisors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Millions of stated risk tolerances recorded before any market event, followed by what each client actually did in every drawdown since, and the allocation still comes from the form.
**Tags:** #gradient-boosting #causal-inference #survival-analysis #evaluation-metrics #confidence-intervals #logistic-regression #hypothesis-testing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to know the client well enough to keep them invested — and the contest splits cleanly enough that it is not terminal.

## The Problem
The questions behavioural finance has argued about for forty years are directly answerable here: does questionnaire risk tolerance predict behaviour at all, what does a panic sale cost in basis points, which clients are at risk and when, and what if anything prevents it. The platform has the stated tolerance, the complete behavioural record, the market conditions and the realised outcomes for millions of people. It produces occasional white papers and manages every client from the form.

## Why Nobody Has Built This
The questionnaire is a regulatory artefact — suitability documentation — so it was treated as the record rather than as a measurement, and nobody asked whether it was accurate because accuracy was never its purpose. Acting on inferred tolerance rather than a stated one raises a supervision question nobody wanted to answer first. Research sits in marketing rather than in product. And the platform's economics reward asset gathering, where retention is a lagging concern.

## What to Build
Turn the record into management. Test whether stated tolerance predicts drawdown behaviour, which is the core and is a straightforward analysis on data already held — the answer, whichever way it goes, changes the product. Quantify the realised cost of behaviour per client in basis points, since that number makes the whole problem legible to everyone from the board to the client. Infer tolerance from behaviour and reconcile it with the self-report, as the divergence is the signal and is currently unexamined. Predict who is at risk of selling before they do, because an intervention after the sale is a condolence. Run interventions as experiments rather than as campaigns, which is the only way to learn what works and is the decomposition below. Resolve the supervision question deliberately — inferred tolerance can inform advice, prompts and monitoring long before it moves an allocation. Update understanding continuously rather than at review, since the behavioural evidence arrives daily. Segment by the behaviour that matters rather than by age and balance, which is how the product currently thinks about people. Publish the findings, because the credibility from settling these questions is worth more than the secrecy. And measure retention and realised outcome as the function's metrics, since those are what the understanding is for.

## Target Customer
Product and investment leadership, chief investment officers defending advice quality, clients whose allocation rests on a stale form, and the behavioural finance research community.

## Impact If Built
The questionnaire was suitability documentation and was never meant to be accurate, so nobody checked. Testing it against the behavioural record is an afternoon's analysis on data already held, and it settles the question the whole product rests on.
