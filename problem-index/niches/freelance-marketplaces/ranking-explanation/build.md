# Build: Per-Account Placement Attribution

**Niche:** [[niches/freelance-marketplaces/ranking-explanation/profile|Ranking Explanation]]
**Industry:** [[industries/freelance-marketplaces|Freelance Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Attribute an individual freelancer's placement to the factors that produced it, separate the ones they control from the ones they do not, and say which are worth acting on.
**Tags:** #gradient-boosting #causal-inference #confidence-intervals #evaluation-metrics #large-language-models #hypothesis-testing #worker-facing #tacit-knowledge-ml
**Contested on:** Whether an attribution is specific enough to act on while remaining honest about the factors outside the person's control.

## The Problem

A freelancer's placement on a search page is the output of a model with hundreds of features, evaluated against a specific query, in competition with a specific set of other freelancers. Every quantity needed to explain that placement exists at the moment it is computed: the feature vector, the model, the score, the scores of everyone ranked above.

None of it is retained, and none of it is shown. The freelancer receives a position and, if they ask, a list of general best practices that applies equally to everyone on the platform and therefore explains nothing about them. They then act on guesses — rewriting a profile that was never the issue, dropping their rate when rate was not a factor, responding faster when they already responded fastest in their category.

## Why Nobody Has Built This

The stated reason is gaming, and it is a real reason — an attribution that names the top three levers names them to everyone, including the people who will manipulate rather than improve. But the stated reason covers a second one that is rarely said aloud: an explanation makes the ranking accountable. Once a platform tells someone their placement fell because their completion rate dropped, it has committed to that being true, has to defend it when it is wrong, and has to explain the next change as well.

There is also a genuine technical subtlety that makes naive attribution worse than nothing. Feature attribution explains a score, but placement is relative — a freelancer can improve every feature and still fall, because the people around them improved more or the query mix shifted. An attribution that says "your response rate contributed +0.3" to someone whose work halved is answering a question they did not ask. The useful explanation is of the *change in placement*, which requires comparing two model evaluations across two time points with the competitive set held in view, and that is a harder object than a single Shapley run.

## What to Build

An attribution service that explains placement changes rather than placement scores.

Log, for every ranked impression, the feature vector as of scoring time and the model version. This is the foundational and unglamorous part, and without it nothing downstream is possible retrospectively. Storage is manageable if sampled per account rather than per impression.

When a freelancer's placement in a category moves materially, decompose the change into three buckets. Own-feature movement: their completion rate, response time, recency, rating and price changed, with the direction and magnitude of each contribution. Competitive movement: the same features held constant, but the distribution of competitors shifted — more entrants, better-performing incumbents, price compression. Model movement: the ranker was retrained or reweighted between the two points. The decomposition is computable by holding each source fixed in turn and re-scoring, which is a counterfactual the platform is uniquely positioned to run because it owns both model versions.

Then generate the explanation in language, grounded strictly in the decomposition — a language model to phrase it, never to produce the content, with the numeric attribution as the only permitted source. Include an explicit actionability judgement: this factor is under your control and moving it by this much would move your placement by roughly this much; this factor is not under your control and no amount of effort will change it.

Report calibration. If the system says improving response time by two hours moves placement by four positions, measure whether it did for the people who acted on it. An uncalibrated explanation that sends people to work on the wrong thing is worse than the help article, because it is specific enough to be trusted.

## Target Customer

Platform leadership at marketplaces under pressure on supply-side transparency — which now includes regulatory pressure in the EU under platform-work transparency rules, and reputational pressure everywhere. Also the freelancer-side tooling market: third parties who could build a weaker version from observable rank data alone, without any platform cooperation.

## Impact If Built

A freelancer whose income moves gets a reason instead of a platitude, and the reason distinguishes effort that will pay from effort that will not — which is the single most valuable thing the platform could tell them and currently the one thing it will not. The support burden of "why did my work stop" collapses into a self-serve answer. And the platform is forced to look at its own attributions, which surfaces ranking behaviour nobody had cause to examine.
