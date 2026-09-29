# Design of Experiments and Conjoint Analysis

**Niche:** [[niches/d2c-brand-operators/creative-decisioning/profile|Creative Decisioning]]
**Industry:** [[industries/d2c-brand-operators|D2C Brand Operators]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Market research built conjoint analysis to learn which attributes drive preference from a manageable number of tests, and creative testing varies everything at once.
**Tags:** #hypothesis-testing #confidence-intervals #logistic-regression #evaluation-metrics #causal-inference #monte-carlo-methods #feature-engineering #probability-distributions
**Contested on:** Every serious competitor in this niche is fighting to tell a brand what to make next rather than how to make it faster — and whoever does that takes the account, because production became cheap and the decision did not.

## The Problem
Learning which attributes of a thing drive a response, without testing every combination, is what experimental design and conjoint analysis were built for. Fractional factorial designs let a handful of tests identify the main effects across many attributes. Conjoint decomposes preference into attribute contributions and has been standard in product and packaging research for decades. Creative testing in this category varies whole assets against each other, which is the design experimental methodology exists to replace.

## What Already Exists
Fractional factorial and optimal experimental designs; conjoint analysis with attribute part-worth estimation; response surface methods for continuous attributes; multi-armed bandits for sequential allocation under testing; and the packaging and advertising research tradition of attribute-level creative testing.

## The Customization Gap
The adaptation is to a test run inside an advertising auction rather than in a panel. It requires: (1) designs that survive the platform's delivery algorithm, since the platform allocates impressions non-randomly and a factorial design executed through it is not the design you specified — handling this is the central methodological problem and it is soluble with the platform's own experiment tooling, which almost nobody uses for creative; (2) attributes extracted from the assets rather than specified in advance, since creative teams will not produce to a design matrix and the practical route is to tag what they made and analyse observationally with care; (3) sequential allocation, since letting a clearly-losing asset keep spending is a real cost that panel research does not have; (4) effects that decay, because creative fatigue means an attribute's measured effect has a shelf life and conjoint assumes stable preferences; and (5) outputs expressed as a creative brief rather than as part-worths, since the consumer of this analysis is a creative team.

## Target Customer
Growth and creative teams, creative testing vendors, and the market research profession whose methods transfer into a much larger volume setting.

## Impact If Solved
Attribute-level testing is a mature research discipline and creative testing varies everything at once. Designing around the platform's delivery algorithm is the central methodological problem, and expressing the output as a brief rather than as coefficients is what makes it usable.
