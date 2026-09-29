# Rating the Formatting

**Niche:** [[niches/ai-model-evaluation-firms/human-preference-operations/profile|Human Preference Operations]]
**Industry:** [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Preference collection infrastructure is solved and widely available, and the ratings it collects are shaped by presentation order, response length and formatting far more than anyone reporting the results acknowledges.
**Tags:** #logistic-regression #hypothesis-testing #confidence-intervals #causal-inference #evaluation-metrics #descriptive-statistics #bayesian-inference #probability-distributions
**Contested on:** Every serious competitor in this niche is fighting to collect preference ratings that measure the model rather than the presentation — and whoever does that takes the account, because the current ratings are substantially a measurement of length and formatting.

## The Problem
A rater sees two responses and picks one. The one on the left is picked more often than the one on the right. The longer one is picked more often than the shorter. The one with headings and bullet points is picked more often than the one in prose saying the same thing. The one that states its answer confidently is picked over the one that appropriately hedges. All four effects are documented, all four are substantial, and the resulting rating is published as a measure of model quality. A model tuned to produce long, formatted, confident answers climbs the leaderboard without getting better at anything.

## Why Nobody Has Built This
Correcting the confounds produces lower and less dramatic differences between models, which is unwelcome to everyone whose model is currently ranked well. The corrections require a model of what drives preference, which means taking a defensible position on how much of length preference is bias and how much is legitimate — a genuinely contestable question that is easier to avoid than to answer. The raw pairwise number is simple and the corrected one needs explaining. And the leaderboard's popularity depends partly on its simplicity.

## What to Build
Design the confounds out and adjust for what remains. Randomise and balance position within every rater, which eliminates order effects by construction and is the easiest fix available — it needs no statistics and is still not universal. Adjust preference for length and formatting explicitly, reporting both the raw and the adjusted rating so the reader can see how much of a model's standing is attributable to presentation, which is the headline finding this build produces. Normalise formatting in a parallel arm of collection, presenting both responses in identical styling, since that separates substance from presentation directly rather than by statistical adjustment and is the more convincing evidence. Characterise the rater population and report it, because a preference is always somebody's preference and publishing one without saying whose is the field's quietest omission. Model rater-specific effects rather than pooling, since raters differ systematically and pooling treats a consistent minority taste as noise. Report where preference is genuinely divided rather than forcing a winner, since two-thirds agreement and near-unanimity are different findings presented identically today. Collect the reason alongside the choice on a sample, which turns a preference into something diagnosable. And publish the adjustment methodology, because a corrected number the reader cannot interrogate replaces one problem with another.

## Target Customer
Labs consuming preference data for training and evaluation, leaderboard operators, evaluation firms running collection, and the enterprises making decisions on published preference rankings.

## Impact If Built
Reporting raw and presentation-adjusted ratings side by side shows how much of a model's standing is formatting, which is the finding the field discusses privately and never publishes. Position randomisation within rater is free and still not universal.
