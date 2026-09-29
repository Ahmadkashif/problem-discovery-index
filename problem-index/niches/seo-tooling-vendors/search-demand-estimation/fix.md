# The Difficulty Score That Means Nothing

**Niche:** [[niches/seo-tooling-vendors/search-demand-estimation/profile|Search Demand Estimation]]
**Industry:** [[industries/seo-tooling-vendors|SEO Tooling Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Keyword difficulty is a number out of a hundred, computed differently by every vendor, with no external referent and no stated meaning, and content plans are built by filtering on it.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #quick-win #compliance #revenue-impact #survival-analysis
**Contested on:** Every serious competitor in this niche is fighting to produce demand and difficulty numbers that are honest about their own error — and whoever does that displaces a market built on extrapolations displayed as integers.

## The Problem
Keyword difficulty is a composite of backlink metrics and page authority signals, scaled to a hundred, with the weighting chosen by each vendor. The same term scores forty-one at one vendor and sixty-eight at another. Neither number corresponds to anything measurable in the world — not the probability of ranking, not the time it would take, not the resource required. Practitioners filter their entire content strategy on it, targeting anything under thirty, because it is the only measure of competitiveness the tools offer. A number that predicts nothing is determining what gets written.

## Why It's Still Broken
The score was introduced as a convenience and became a planning input, and a convenience that becomes an input is never re-examined. Every vendor's version is different, which prevents any external referent from forming. Defining difficulty against an outcome would require the outcome data that sits on the customer's side. And the score is useful as a rough sort, which makes its misuse as a threshold easy to overlook.

## What a Fix Looks Like
Define difficulty against something real. Estimate the probability that a site with given characteristics ranks in a given period, rather than scoring the term in isolation, which is the fix — difficulty is a property of the pairing of a site and a term, and scoring the term alone is the error at the centre. Calibrate against observed outcomes from the vendor's own longitudinal corpus, connecting to the causal work, since millions of sites attempting to rank for millions of terms is exactly the training data required. Report an expected time and an expected effort, because those are the quantities a planner actually needs and a unitless score cannot supply. Express uncertainty, as an honest answer for many terms is that it depends heavily on factors the vendor cannot see. Publish the method, since incomparable proprietary composites are the reason the number means nothing across the market. Personalise to the customer's own site, which is both more useful and the only formulation that can be validated. Retire the unitless hundred-point scale, because its familiarity is what sustains the misuse. Show the competitive set explicitly rather than compressing it into a number, since a planner looking at who currently ranks learns more than the score tells them. Validate by predicting outcomes on held-out cases, which no vendor publishes. And warn where the score is being used as a threshold, because the filter-under-thirty habit is where the damage is done.

## Who Feels the Pain
Content teams filtering strategy on a number with no referent; customers comparing incompatible vendor scores; and the discipline, whose planning substrate is arbitrary.

## Impact If Fixed
Difficulty is a property of a site-and-term pairing and the score treats it as a property of the term alone. Calibrating against the vendor's own longitudinal record of millions of ranking attempts is exactly the data needed to make it mean something.
