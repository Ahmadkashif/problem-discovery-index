# The Corpus Discarded at the End of Every Engagement

**Niche:** [[niches/performance-marketing-agencies/portfolio-measurement-priors/profile|Portfolio Measurement Priors]]
**Industry:** [[industries/performance-marketing-agencies|Performance Marketing Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The same measurement question is answered across hundreds of advertisers with the clients' real revenue visible, and the answers are thrown away when each engagement ends.
**Tags:** #bayesian-inference #causal-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #monte-carlo-methods #revenue-impact #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to turn a portfolio of hundreds of advertisers into calibrated priors on how much each platform overstates — and whoever does that is selling the only thing in this market that cannot be copied from a platform's documentation.

## The Problem
An agency has run geographic holdouts for thirty clients over four years. Each produced a finding: this platform overstated by roughly this much, in this vertical, with this purchase cycle. Each finding was presented in a deck and then forgotten. A new client arrives in the same vertical and the plan is built from the platform's own reported numbers, because nobody has the thirty previous answers in a form that could inform it. The agency has assembled, expensively, the only cross-advertiser incrementality dataset outside the platforms, and stores it in slides.

## Why Nobody Has Built This
Agencies are organised around engagements rather than around an accumulating asset, so nothing persists past a client relationship — the organisational structure produces the data loss directly. Client confidentiality is assumed to prevent pooling, which is true of raw data and not of abstracted priors. Nobody is accountable for the firm's knowledge. And the value of a prior is invisible until someone tries to use one.

## What to Build
Turn the portfolio into a measurement asset. Retain every experiment and measurement result in a structured record — platform, vertical, purchase cycle, method, effect size, uncertainty — which is the fix and is the step that converts thirty decks into a dataset. Estimate priors on platform overstatement by vertical and cycle, which is the deliverable and is what lets a new engagement start from evidence rather than from the platform's number. Pool hierarchically, since each client's experiment is small and the whole point is that thirty small experiments together say something none of them says alone. Abstract sufficiently that no client's data is exposed, which resolves the confidentiality objection that has prevented this and is a design requirement rather than an obstacle. Use the priors to shorten new engagements, since a client can be given a defensible allocation in week one rather than after a six-month measurement programme — this is the commercial argument. Update continuously as new experiments complete, so the asset compounds. Publish selected findings, because credible published priors are the strongest new business asset available in a market where everyone claims measurement expertise. Detect platform behaviour changes across the portfolio, which no single advertiser can see and which is genuinely valuable in the first days. Price the priors as a product distinct from the hours, which is how an agency escapes selling time against a spend percentage. And validate priors against subsequent experiments, since an unchecked prior is folklore with a number.

## Target Customer
Agency leadership seeking a defensible asset, in-house teams buying measurement expertise, and the measurement vendors who lack a cross-advertiser experimental corpus.

## Impact If Built
Thirty expensive experiments live in slides because the firm is organised around engagements rather than an accumulating asset. Abstracted hierarchical priors resolve the confidentiality objection and let a new engagement start from evidence in week one rather than month six.
