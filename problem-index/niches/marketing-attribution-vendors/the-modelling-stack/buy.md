# Causal Inference Practice

**Niche:** [[niches/marketing-attribution-vendors/the-modelling-stack/profile|The Modelling Stack]]
**Industry:** [[industries/marketing-attribution-vendors|Marketing Attribution Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Causal inference is a mature field with explicit assumption frameworks and sensitivity analysis, and marketing measurement states its assumptions in a footnote if at all.
**Tags:** #causal-inference #bayesian-inference #confidence-intervals #hypothesis-testing #monte-carlo-methods #evaluation-metrics #graph-theory #descriptive-statistics
**Contested on:** This niche is not terminal — path-based attribution and mix modelling are different disciplines with different failure modes and different winners, and they are stated separately in the sub-niches.

## The Problem
Causal inference from observational data is a developed field with a demanding intellectual standard: assumptions stated formally, identification argued explicitly, sensitivity analysis quantifying how much an unmeasured confounder would have to matter to overturn a finding, and bounds reported where point identification fails. Epidemiology and economics apply this seriously because wrong causal conclusions have consequences. Marketing measurement sells causal conclusions with the assumptions rarely written down and sensitivity analysis almost never performed.

## What Already Exists
Formal causal frameworks with identification conditions; sensitivity analysis for unmeasured confounding; partial identification and bounds; negative control and falsification testing; and transportability analysis across populations.

## The Customization Gap
The adaptation is to a commercial deliverable consumed by non-statisticians under time pressure. It requires: (1) assumptions expressed in business terms rather than in formal notation, since the person acting on the conclusion cannot read a causal diagram and an unstated assumption is functionally the same as no assumption — this translation is the substantive work; (2) sensitivity analysis presented as a decision-relevant range rather than as a technical appendix; (3) bounds rather than points where identification genuinely fails, which is commercially uncomfortable and intellectually correct; (4) falsification tests the client can understand and check, such as negative controls on channels known to be inactive, which are cheap and almost never run; and (5) continuous operation rather than a study, since the estimate is consumed weekly and the assumptions must be re-examined as the business changes.

## Target Customer
Measurement vendors, client measurement and finance functions, and applied causal inference practitioners for whom marketing is an underserved domain.

## Impact If Solved
The field states assumptions formally and tests sensitivity because wrong causal conclusions have consequences, and marketing states them in a footnote. Translating assumptions into business terms is the substantive work, and negative control tests are cheap and almost never run.
