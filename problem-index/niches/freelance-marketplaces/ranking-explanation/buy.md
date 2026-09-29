# Buy: Model Explainability Tooling Adapted to a Ranked Person

**Niche:** [[niches/freelance-marketplaces/ranking-explanation/profile|Ranking Explanation]]
**Industry:** [[industries/freelance-marketplaces|Freelance Marketplaces]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Explainability libraries produce feature attributions for a data scientist debugging a model; a freelancer needs an attribution for a relative outcome, addressed to them, that they can act on.
**Tags:** #gradient-boosting #evaluation-metrics #confidence-intervals #large-language-models #causal-inference #feature-engineering #worker-facing #automation
**Contested on:** Whether off-the-shelf attribution, built to explain a score to an engineer, can be made to explain a position to the person holding it.

## The Problem

Model explainability is a well-stocked toolbox. SHAP, integrated gradients, counterfactual explanation libraries and model cards are mature, widely used and cheap to run against a gradient-boosted ranker. A team asked to explain a ranking has everything it needs to produce attributions by the end of a sprint.

The output of that sprint will not be usable. It explains a score to someone who understands what a score is, in terms of features whose names are internal, for an absolute quantity when the freelancer's outcome is relative, with no statement about which factors are in their control and no measurement of whether acting on the explanation helps.

## What Already Exists

SHAP and its tree-optimised variants, which run efficiently over exactly the model classes marketplaces use for ranking. DiCE and related counterfactual-explanation libraries that generate "change these features by this much to cross this threshold". LIME for local surrogates. Model documentation tooling. On the delivery side, language models are entirely capable of turning a numeric attribution into a sentence a person can read.

## The Customization Gap

**Relative, not absolute.** Every library explains f(x) for one x. Placement is a position in a sorted list, and the same score means a different position depending on who else is in the query. The adaptation is to attribute the *rank*, which requires the competitive set as part of the explanation object — decomposing a position change into own-feature movement, competitor movement and model movement. No library expresses this; it has to be built around them.

**Controllability has to be a first-class feature attribute.** An attribution that ranks "category competition density" as the top contributor is technically correct and practically cruel. Every feature needs a control classification — directly controllable, indirectly influenceable, fixed — maintained as deliberate metadata, and the presentation has to lead with the controllable ones while still stating the fixed ones honestly rather than hiding them.

**Counterfactual generators need feasibility constraints from the domain.** DiCE will happily recommend a 40% rate reduction or a completion-rate improvement that would require rewriting history. The feasible action space for a freelancer — what can change this week, what takes three contracts, what is permanent — is domain knowledge the library has no way to hold.

**Gaming exposure needs a filter in the pipeline.** Some attributions are safe to surface because the only way to move the feature is to be better; others name a proxy that can be manipulated directly. The tooling has no concept of this distinction, and getting it wrong converts an explainability feature into an exploitation manual. The classification is per-feature, needs maintaining as the model changes, and is the piece that most often stops the project.

**Calibration measurement does not exist in any of these libraries.** SHAP will not tell you whether people who acted on its attribution improved. That loop — recommendation, action, observed outcome — has to be instrumented separately and is the only evidence that the explanation is worth anything.

## Target Customer

Marketplace ML teams told to ship transparency and reaching for SHAP first. Also platform-work compliance teams in jurisdictions where algorithmic transparency obligations now apply to work allocation, who are buying explainability tooling and discovering it does not answer the question the regulation asks.

## Impact If Solved

The mature tooling does the arithmetic and the five adaptations make it an answer a person can use. Practically: a freelancer gets "your position fell mostly because two new competitors in your category price below you and complete faster — your own metrics improved slightly," which is honest, specific, and tells them whether to work harder or work elsewhere.
