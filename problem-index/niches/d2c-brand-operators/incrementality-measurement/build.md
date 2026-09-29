# Every Channel Claims the Same Conversion

**Niche:** [[niches/d2c-brand-operators/incrementality-measurement/profile|Incrementality Measurement]]
**Industry:** [[industries/d2c-brand-operators|D2C Brand Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every channel claims the same conversions, the platform numbers exceed actual orders, and marketing budget is allocated by people who know the attribution is wrong and have no better basis.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #bayesian-inference #time-series-forecasting #revenue-impact #monte-carlo-methods #evaluation-metrics
**Contested on:** Every serious competitor in this niche is fighting to establish what a marketing dollar actually caused rather than what each channel claims — and whoever does that takes the account, because every budget decision in the category currently rests on numbers the people making them do not believe.

## The Problem
A brand ships four thousand orders in a month. Their paid social platform claims three thousand two hundred conversions, search claims fourteen hundred, their email tool claims nine hundred, affiliates claim six hundred and the analytics platform shows a different split again. The total claimed exceeds the total that happened by a factor. Every number is computed correctly by its own definition and no combination of them answers the question, which is how much of the four thousand would have happened with no spend at all and which channel produced the rest. The growth lead allocates next month's budget from these figures, knowing they are wrong, because the alternative is allocating from nothing.

## Why Nobody Has Built This
The platforms are both the seller of the advertising and the reporter of its effect, which is a conflict everyone accepts because no alternative measurement is on offer. Experimentation — the one method that establishes causation — costs money to run, since it means deliberately not spending in places to see what happens, and looks like giving up revenue. Media mix modelling requires more history and more spend variation than most brands have. And the attribution vendors sell reconciliation of the platforms' claims, which is a different and easier product than measuring causation.

## What to Build
Measure causation directly and model the rest. Run geographic and audience holdout experiments as a routine part of the budget rather than as an occasional project, since a small share of spend deliberately withheld produces a causal estimate nothing else can — and this discipline, rather than any model, is the core of the build. Calibrate the models to the experiments, so media mix modelling and attribution are fitted against measured incrementality rather than against platform claims, which is the specific correction the category needs and which turns an unfalsifiable model into a calibrated one. Estimate baseline demand explicitly, since the share that would have happened anyway is the largest single term and attributing it to whichever channel touched it last is the root error. Fit to the brand's own orders rather than to platform-reported conversions, which is the data the brand has and the platforms do not. Produce the marginal return curve per channel rather than an average return, because the decision is where the next dollar goes and an average return says nothing about it. Report uncertainty honestly, since a wide interval that is correct is more useful than a point estimate that is not. Measure the same way over time, so the trend is interpretable even when the level is uncertain. And make the experiment cadence a standing operating practice, because incrementality decays and a measurement from last year is describing a different auction.

## Target Customer
Brands allocating marketing budget, their investors, and the attribution vendors whose products currently rest on platform claims.

## Impact If Built
The platforms both sell the advertising and report its effect, and every brand accepts it for want of an alternative. Routine holdout experiments produce the causal estimate nothing else can, and calibrating the models to them is what turns an unfalsifiable attribution into a measurement.
