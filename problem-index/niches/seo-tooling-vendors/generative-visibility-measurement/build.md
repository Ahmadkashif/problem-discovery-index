# Estimating a Surface You Cannot Enumerate

**Niche:** [[niches/seo-tooling-vendors/generative-visibility-measurement/profile|Generative Visibility Measurement]]
**Industry:** [[industries/seo-tooling-vendors|SEO Tooling Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The answer is personalised, non-deterministic, generated fresh, and available through no interface, and the category is reporting a percentage derived from running forty prompts.
**Tags:** #monte-carlo-methods #confidence-intervals #bayesian-inference #descriptive-statistics #hypothesis-testing #large-language-models #evaluation-metrics #transformers
**Contested on:** Every serious competitor in this niche is fighting to produce a defensible estimate of how often a brand appears in generated answers across a surface that is personalised, non-deterministic and closed — and whoever establishes that method sets the category's next currency.

## The Problem
A vendor wants to tell a customer how visible their brand is in generated answers. There is no list to read. The same question asked twice returns different text citing different sources. Different users get different answers. The questions people ask are natural language, so the space is effectively unbounded, and the vendor's entire keyword taxonomy — built for a world of typed query strings — does not map onto it. The current industry response is to run a hand-picked set of prompts, count mentions, and present a percentage. Nobody can say what population that percentage estimates.

## Why Nobody Has Built This
The category has never needed sampling, because the search results page could be read directly — this absence of a statistical tradition is the real gap and it is cultural as much as technical. Constructing a sampling frame over natural-language questions requires deciding what the population is, which is a genuinely hard definitional problem nobody has taken on. Non-determinism is treated as noise to be averaged rather than as variance to be modelled. And a number with an interval looks weaker in a sales demonstration than one without.

## What to Build
Build the estimator properly. Define the population explicitly — the questions a brand's potential customers would actually ask, weighted by how often they are asked — which is the foundational decision and is what makes any resulting number mean something. Construct the sampling frame from real demand signals rather than from a hand-picked prompt list, using query data, customer support questions, community discussion and existing keyword demand mapped to natural phrasings. Sample the variance deliberately: repeat the same question, vary the phrasing, vary the context, and separate system non-determinism from genuine change, which is the core statistical work and is what lets a customer know whether something moved. Weight to demand, since an equal-weighted prompt set overstates the importance of rare questions. Report confidence intervals as standard, which is both honest and a durable differentiator in a market accustomed to unexplained integers. Measure the framing as well as the presence, because being cited as an alternative and being cited as the recommendation are different outcomes. Cover the several answer surfaces separately, as they draw on different sources and behave differently. Detect change against the measured variance rather than against the last reading, which is how a tracking study works and how this one should. Publish the methodology openly, since the first defensible method becomes the standard and standards are durable positions. And validate against whatever ground truth is obtainable, because a method nobody has checked is an assertion.

## Target Customer
SEO and visibility tooling vendors, enterprise brand measurement teams, and the market research firms with the sampling expertise this problem needs.

## Impact If Built
The category could always read the results page directly, so it has no sampling tradition and is now estimating an unbounded space from forty prompts. Defining the population and separating system variance from genuine change is what turns a percentage into a measurement.
