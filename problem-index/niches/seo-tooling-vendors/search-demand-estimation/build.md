# Estimates Displayed as Facts

**Niche:** [[niches/seo-tooling-vendors/search-demand-estimation/profile|Search Demand Estimation]]
**Industry:** [[industries/seo-tooling-vendors|SEO Tooling Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Monthly search volume is an extrapolation from a clickstream panel with enormous tail error, displayed as an integer, and customers build annual content budgets on it.
**Tags:** #confidence-intervals #bayesian-inference #descriptive-statistics #hypothesis-testing #evaluation-metrics #time-series-forecasting #monte-carlo-methods #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to produce demand and difficulty numbers that are honest about their own error — and whoever does that displaces a market built on extrapolations displayed as integers.

## The Problem
A content team plans a year. They select four hundred topics from a tool that reports monthly search volume for each: 2,400, 880, 320, 90. Those numbers come from a clickstream panel covering a small fraction of users, extrapolated to the population. For the head terms the extrapolation is reasonable. For the tail — where most of the four hundred topics are — the panel may have seen the query a handful of times or not at all, and the reported figure is closer to a guess than a measurement. It is displayed with the same typography as the head terms. A year of investment is allocated on it.

## Why Nobody Has Built This
An integer sells better than an interval, and the first vendor to show error bars looks less capable than competitors who do not — a collective action problem that has held the market at false precision for fifteen years. Customers ask for a number and are unequipped to use a distribution. The error is known internally and disclosing it invites questions about the whole product. And nobody has been penalised for it, because the failures look like content that did not work.

## What to Build
Report the estimate as an estimate. Attach an uncertainty interval to every volume figure, derived from panel coverage for that query, which is the fix and is computable today from data the vendor already has — the error is known and simply not shown. Bucket rather than pretend, since a tail term is better described as somewhere between fifty and five hundred than as 90, and the bucket is honest where the integer is not. Report coverage explicitly, so a customer knows whether the panel saw this query at all. Model the tail with pooling across related queries rather than extrapolating each in isolation, which is a real statistical improvement and not merely a presentational one. Report seasonality and trend rather than a twelve-month average, since a term with all its volume in November is a different proposition and the average hides it. Replace difficulty composites with something externally meaningful, which is the fix note's subject. Give planning tools that propagate uncertainty into the forecast, so a content plan carries a range rather than a false total. Validate against ground truth where a customer's own data permits, which is the only external check available and which almost nobody runs. Educate the market deliberately, because the collective action problem means the first honest vendor must make honesty a selling point. And publish error properties openly, since a vendor that can defend its numbers under scrutiny is in a strong position when a competitor cannot.

## Target Customer
SEO tooling vendors, content and marketing teams building budgets on these figures, and the agencies whose recommendations rest on them.

## Impact If Built
The error is known internally and simply not shown, and an integer for a tail term is closer to a guess than a measurement. Intervals and buckets are computable today, and pooling across related queries is a real improvement to the tail rather than a presentational one.
