# The Evaluation Archive as a Prior on the Next Study

**Niche:** [[niches/energy-auditors/emv-evaluation-contractors/profile|Efficiency Programme Evaluation Contractors]]
**Industry:** [[industries/energy-auditors|Energy Auditors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The firm has evaluated the same measure in the same programme type dozens of times across jurisdictions and years, and every new study starts as though none of it happened.
**Tags:** #bayesian-inference #causal-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #gradient-boosting #feature-engineering #descriptive-statistics #data-integration #revenue-impact

## The Problem
Evaluation is commissioned study by study, jurisdiction by jurisdiction, and delivered as a report to the utility and the regulator. Each one estimates realization rates, net-to-gross ratios, and measure-level savings from a sample large enough to support the finding on its own. The firm has produced hundreds of such estimates for overlapping measures across states and years, and the accumulated evidence is used only as professional judgment — an evaluator remembering roughly what a heat pump study came out at last time. Nothing pools them formally. So each study pays full sampling cost to estimate a quantity the firm has strong prior information about, and the pooled evidence — which would be the most authoritative statement available about what these measures actually save — is never assembled or published.

## Why Nobody Has Built This
Studies are contracted deliverables for specific clients, and the underlying data arrives under utility agreements written for that engagement, so pooling across clients is a permissions question nobody has mapped. Regulators also expect jurisdiction-specific evidence and have historically been sceptical of borrowed estimates, which is a legitimate methodological position and has been read as prohibiting formal pooling rather than requiring it be done transparently. And the delivery model is project-based, with no role owning the archive.

## What to Build
An evaluation evidence base holding every prior study at the level a meta-analysis needs — measure, programme design, population, method, sample, estimate, and precision — with the reuse terms attached so any analysis can state which portion it may draw on. On that base, new studies are designed and estimated with pooled priors rather than from scratch, which is both more precise and cheaper at the same sample, and which is defensible to a regulator precisely because the prior is explicit and the jurisdiction-specific data still dominates where it is strong. Heterogeneity is modelled rather than assumed away: the useful output is not one national number but an understanding of how realization varies with programme design, climate, and population, which is what a utility designing next year's portfolio actually needs. And the pooled evidence base becomes a saleable product in its own right, since no single utility or regulator can assemble it.

## Target Customer
Practice leaders and principals at evaluation firms running 50-300 evaluators, and the programme administrators and commission staff who commission jurisdiction-specific studies to estimate quantities the industry has measured many times.

## Impact If Built
Lowers the cost of every study while raising its precision, in a business where sampling is the dominant cost and the regulator judges precision. It also converts a project archive into the field's authoritative evidence base — the one asset an evaluation firm can own that a competitor cannot bid against.
