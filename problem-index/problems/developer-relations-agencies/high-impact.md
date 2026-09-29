# The Function Cannot Prove It Works and Is Cut First Because of It

**Industry:** [[developer-relations-agencies|Developer Relations Agencies]]
**Type:** High Impact
**One-liner:** Developer advocacy plausibly drives a large share of adoption and reports talks given and community members, because the moment of influence carries no identifier and the conversion arrives months later.
**Tags:** #causal-inference #survival-analysis #bayesian-inference #confidence-intervals #hypothesis-testing #graph-neural-networks #evaluation-metrics #revenue-impact

## The Problem
A developer watches a conference talk, reads a tutorial, asks a question in a community channel and gets a helpful answer, tries the tool in a workshop, and eighteen months later specifies it at a new job where it becomes a six-figure contract. Every step of that chain is real and none of it is traceable: the talk had no tracking link, the community handle is pseudonymous, the eventual purchaser is an employer the advocate never met.

So developer relations reports what it can count — talks delivered, articles published, community members, event attendance, repository stars, workshop signups. The field is entirely candid that these are activity metrics, and has been arguing about replacements for a decade without converging, because the honest measurement requires linking diffuse influence to delayed conversion across identity boundaries.

The consequence is structural and predictable. When budgets tighten, functions that can demonstrate return keep their funding and functions that cannot do not, and developer relations is reliably in the second group. Practitioners describe the cycle: a downturn arrives, the team is cut, adoption declines a year later for reasons attributed to the market, and the function is rebuilt when conditions improve.

The attribution vacuum also distorts the work. Measured on activity, teams optimise activity — more talks, more posts, more events — which is not the same as more influence and is frequently the opposite, because the highest-value advocacy is often slow relationship work with a handful of people who become the internal champions of an adoption.

And agencies selling developer relations as a service inherit the problem at its worst, because they must justify a fee against outcomes their client cannot measure either.

## Why It's Unsolved
The identity join is genuinely hard. Developers participate pseudonymously, use personal accounts for community and corporate accounts for purchasing, move employers, and reasonably object to being tracked across those contexts. Any measurement design that depends on identifying individuals across surfaces is both technically fragile and ethically questionable, and the field's instinct to be careful about it is correct.

The timescales defeat ordinary attribution. Influence to adoption can take years, and no attribution window covers it. The most consequential advocacy — building a reputation that makes a tool a default choice — has no event to attribute at all.

Experiments are hard to run. Withholding advocacy from a region or a community to create a control group is possible in principle and unattractive in practice, and the effects are diffuse enough that the experiment needs to be large and long.

And there is a self-defeating dynamic in the field's own culture. Developer relations practitioners are frequently and rightly suspicious of measurement that would turn community relationships into a pipeline, because instrumenting a community in a way developers can feel destroys the trust the function depends on. That objection is legitimate and it has also been used to avoid measurement entirely, which is what leaves the budget undefended.

## What a Solution Looks Like
Measure cohorts, not people. Aggregate approaches — comparing adoption trajectories in regions, communities or segments with differing advocacy intensity — produce defensible estimates without tracking individuals across surfaces. This sacrifices precision for both ethics and durability, and it is dramatically better than counting talks.

Use the natural experiments that already exist. Advocacy is unevenly distributed by accident — a conference circuit covers some geographies and not others, a community programme launches in one region first, an advocate leaves and coverage drops. Those discontinuities are natural experiments, and comparing adoption before and after against unaffected comparators is the most credible evidence available without running anything deliberately.

Instrument what developers volunteer. Self-reported source at signup, community participation that a developer chooses to link to their account, and workshop attendance are all consented signals, and they are enough to establish relative rates without covert tracking.

Model the delay honestly. A survival framing over time from first touch to adoption, fit on the cohorts where both ends are observable, gives an estimate of how long influence takes to convert — which is the number that would justify a budget across a downturn, because it makes visible that this year's cuts show up in adoption eighteen months from now.

And distinguish influence from reach. A talk seen by two thousand people who forget it and a workshop with thirty who ship something are not equivalent, and outcome-weighted measurement would redirect the activity optimisation the current metrics produce.

## Impact If Solved
This determines whether a function that plausibly drives a large share of developer adoption survives budget cycles. Cohort-level and natural-experiment measurement gives it a defensible number without the covert tracking that would destroy the community trust it depends on, and modelling the conversion delay makes visible the specific dynamic — cut now, decline later, rebuild expensively — that this field has lived through repeatedly without ever being able to demonstrate.
