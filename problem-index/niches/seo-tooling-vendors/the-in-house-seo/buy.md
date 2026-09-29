# Incident Diagnosis Practice

**Niche:** [[niches/seo-tooling-vendors/the-in-house-seo/profile|The In-House SEO]]
**Industry:** [[industries/seo-tooling-vendors|SEO Tooling Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Site reliability engineering built change correlation and blast radius analysis to answer what broke, and SEO answers the same question with four browser tabs.
**Tags:** #causal-inference #change-point-detection #worker-facing #evaluation-metrics #confidence-intervals #time-series-forecasting #hypothesis-testing #graph-theory
**Contested on:** Every serious competitor in this niche is fighting to give the in-house SEO an answer when traffic drops rather than four charts that correlate — and whoever does that changes whether the role can defend itself inside a business.

## The Problem
Diagnosing what caused a metric to move is a developed engineering discipline. Incident response tooling correlates a degradation with deployments, configuration changes and dependency events, establishes temporal precedence, estimates blast radius and presents ranked hypotheses to an on-call engineer under time pressure. The practice exists because guessing during an incident is expensive. SEO faces the same problem on a slower clock with higher stakes for the individual, and has no equivalent.

## What Already Exists
Change and deployment correlation with metric degradation; anomaly detection with seasonality handling; ranked hypothesis presentation under time pressure; blast radius estimation; and post-incident timeline assembly.

## The Customization Gap
The adaptation is to a metric moved by an external system nobody controls. It requires: (1) the dominant cause frequently being a third party's algorithm change, which has no equivalent in an owned system and means the tooling must incorporate a cross-customer view to detect it — this is why a vendor with a corpus can do this and a customer cannot; (2) effects that unfold over days and weeks rather than seconds, which changes detection from real-time anomaly to trend break; (3) competitor action as a first-class cause, which no engineering diagnosis model contemplates; (4) causes that are unobservable in principle, so the output must carry honest uncertainty rather than a root cause; and (5) an audience that is a marketing leadership meeting rather than an engineer, which changes the presentation entirely.

## Target Customer
In-house SEO teams, agencies, and observability vendors for whom externally-caused business metric diagnosis is an adjacent market.

## Impact If Solved
Incident tooling exists because guessing is expensive, and SEO guesses with a deadline. A third party's algorithm as the dominant cause requires the cross-customer view that only a vendor with a corpus has.
