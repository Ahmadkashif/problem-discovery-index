# Lock-Change Pricing From Modelled Fallout

**Niche:** [[niches/mortgage-lenders/secondary-marketing-pipeline-risk/profile|Secondary Marketing & Pipeline Risk]]
**Industry:** [[industries/mortgage-lenders|Mortgage Lenders]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every extension and renegotiation request is a bet on whether the borrower will leave, and lenders decide them by policy and persuasion instead of by a forecast of fallout.
**Tags:** #survival-analysis #gradient-boosting #logistic-regression #evaluation-metrics #feature-engineering #revenue-impact #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to forecast which locked loans will fund and to sell each one at its best execution, and whoever earns the most margin per locked loan net of hedge cost and lock concessions takes the account.

## The Problem
When rates fall after a borrower locks, the loan officer asks the lock desk to renegotiate the price or lose the deal. When an appraisal runs late, they ask for a free extension. The lock desk decides from a written policy (one renegotiation per loan, a fixed concession cap, an extension fee schedule) and from its read of the loan officer and borrower. Nobody knows, at the moment of decision, the probability that this borrower will actually walk at the current market, or what the concession costs once the hedge position is taken into account. Concessions granted to borrowers who would have closed anyway are pure margin loss; refusals to borrowers who then leave cost the hedge.

## Why Nobody Has Built This
Pricing engines record locks and changes but are built to quote, not to predict. Hedge advisors model pull-through at pipeline level for coverage, not at loan level for a negotiation. And the lender's own data on which concessions saved loans has never been captured: the request, the reason and the outcome sit in three different places.

## What to Build
A loan-level competing-risks model (fund, withdraw, renegotiate) using rate move since lock, days remaining, milestone status, purpose, channel and loan officer history, wired into the lock-change workflow. Each request arrives with the modelled probability of fallout with and without the concession, the expected cost to the hedge of each choice, and a recommended response. Every decision and outcome is logged so the model and the policy improve together.

## Target Customer
Capital markets heads and lock desk managers at independent mortgage banks closing $1B–$20B a year that hedge their own pipelines; hedge advisors who could embed it for their client base.

## Impact If Built
If concessions run at 5–10 basis points on a quarter of locks in a falling-rate month (estimate), targeting them at borrowers who would really leave is worth several basis points of margin across the pipeline, against production profits of 21 basis points in 2025 (MBA).
