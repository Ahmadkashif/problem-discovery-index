# Quasi-Experimental Practice

**Niche:** [[niches/seo-tooling-vendors/causal-attribution-of-change/profile|Causal Attribution of Visibility Change]]
**Industry:** [[industries/seo-tooling-vendors|SEO Tooling Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Economics and epidemiology built a rigorous toolkit for causal inference from observational panels, and SEO overlays a vertical line on a chart.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #bayesian-inference #monte-carlo-methods #evaluation-metrics #descriptive-statistics #time-series-forecasting
**Contested on:** Every serious competitor in this niche is fighting to answer whether what a site did worked or whether the algorithm moved — and whoever does it owns the only dataset capable of settling the customer's recurring question.

## The Problem
Inferring causation from observational panel data is one of the best-developed areas of applied statistics. Difference-in-differences, synthetic controls, event studies, matching and instrumental variables are standard in economics, epidemiology and policy evaluation, with well-understood assumptions and diagnostics. They exist precisely for situations where you cannot randomise and must exploit natural variation. SEO has a large panel, frequent exogenous shocks, and heterogeneous treatment across millions of units, and it uses none of the toolkit.

## What Already Exists
Difference-in-differences and event study designs; synthetic control construction; matching and propensity methods; panel fixed-effects estimation; and sensitivity and placebo testing for assumption checking.

## The Customization Gap
The adaptation is to a panel of websites with unobserved treatment and an adversarial environment. It requires: (1) treatment inferred from crawl differences rather than recorded, since nobody tells the vendor what a site changed and the intervention must be detected — this detection step is the substantive addition to an otherwise standard method; (2) shocks that hit every unit simultaneously, since an algorithm update has no untreated group in the usual sense and the control must be constructed from sites whose characteristics made them unaffected; (3) a ranking system that is a zero-sum competition, so one site's gain is another's loss and the stable unit treatment assumption is plainly violated — this interference is the hardest methodological problem here; (4) heterogeneous effects by site type as the interesting result rather than as a nuisance; and (5) output for a marketer rather than a referee, which changes presentation without weakening the method.

## Target Customer
SEO tooling vendor data teams, enterprise SEO measurement, and applied econometrics practitioners for whom web panels are an unexploited domain.

## Impact If Solved
The toolkit exists for exactly this situation and the panel is large with frequent exogenous shocks. Inferring treatment from crawl differences and handling the zero-sum interference between competing sites are the two additions the standard methods need.
