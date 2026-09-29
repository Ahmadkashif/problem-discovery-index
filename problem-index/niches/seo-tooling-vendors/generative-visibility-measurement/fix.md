# The Share of Voice Number With No Method

**Niche:** [[niches/seo-tooling-vendors/generative-visibility-measurement/profile|Generative Visibility Measurement]]
**Industry:** [[industries/seo-tooling-vendors|SEO Tooling Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The dashboard says the brand has eleven percent share of generative visibility, and nobody at the vendor or the customer can say what that is eleven percent of.
**Tags:** #descriptive-statistics #confidence-intervals #evaluation-metrics #hypothesis-testing #compliance #quick-win #monte-carlo-methods #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to produce a defensible estimate of how often a brand appears in generated answers across a surface that is personalised, non-deterministic and closed — and whoever establishes that method sets the category's next currency.

## The Problem
A generative visibility figure appears in a dashboard. It moved from nine percent to eleven percent this month, and a team is discussing what they did that worked. The number comes from running a prompt set someone assembled, counting mentions, and dividing. The prompt set was not sampled from anything, is not weighted to demand, has been edited twice since last month, and the system's own run-to-run variance is larger than the movement being discussed. Everyone is treating it as a measurement. It is a count of a convenience sample, and the category is about to build a decade of reporting on it.

## Why It's Still Broken
The number was shipped quickly to meet demand for a generative metric, and provisional things become permanent once they appear in a report. Nobody asked what population it estimates, because the previous generation of metrics were enumerations and did not need one. Vendors competing to ship first have no incentive to be the one whose number carries a caveat. And the customer cannot evaluate a method that is not published.

## What a Fix Looks Like
State what the number is. Publish the prompt set, the sampling approach and the weighting with every figure, which is the fix, costs nothing, and immediately separates vendors doing this seriously from those who are not. Freeze the prompt set or version it explicitly, since a changing instrument makes a trend meaningless and this is the most common current error. Report run-to-run variance so a customer can tell whether a two-point move is real, which is a handful of repeated runs and is the single most useful addition available. Weight to actual demand rather than treating every prompt equally, and say how. Report a confidence interval, or at minimum a sample size. Distinguish presence from prominence and from framing, rather than collapsing them into one percentage. Separate the surfaces, since a blended figure across different answer systems is an average of unlike things. Provide the underlying observations so a customer can inspect what produced the number, which builds the trust the previous generation of unexplained integers eroded. Adopt a common method across the industry, because incomparable vendor-specific figures are how keyword difficulty ended up meaning nothing. And label the figure as an estimate wherever it appears, since a percentage in a dashboard reads as a fact and this one is not.

## Who Feels the Pain
Customers making decisions on run-to-run noise; vendors whose flagship new metric cannot survive a methodological question; and the category, which is repeating its keyword-difficulty mistake in real time.

## Impact If Fixed
A convenience sample with a changing instrument is being reported as a measurement, and the movement being discussed is smaller than the system's own variance. Publishing the prompt set, versioning it and reporting run-to-run variance costs nothing and separates real measurement from a count.
