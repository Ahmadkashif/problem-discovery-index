# Cost Reported Per Request, Not Per Useful Record

**Niche:** [[niches/web-data-extraction-firms/collection-infrastructure/profile|Collection Infrastructure]]
**Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Customers are billed per request or per gigabyte and care about correct records delivered, and the ratio between the two varies by an order of magnitude across targets with nobody reporting it.
**Tags:** #revenue-impact #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #quick-win #automation #data-integration
**Contested on:** Not terminal — the contest differs by whether the problem is reaching the page or reading it, and the decomposition is recorded in the profile.

## The Problem
A customer is billed for requests. For one target, nine requests in ten succeed and yield a correct record. For another, defended by aggressive detection, it takes six requests to get one page, and one page in five parses correctly — thirty requests per useful record. Both appear on the invoice as requests at the same rate. The customer's actual cost per useful record differs thirtyfold between targets and nothing in the billing or the reporting tells them, so they cannot tell which targets are worth collecting and which are consuming their budget for almost nothing.

## Why It's Still Broken
Per-request billing is simple to meter and matches the firm's own cost structure for the access half. Reporting cost per useful record requires knowing which records were useful, which requires the validation the correctness niche describes. A hard target consuming thirty requests per record is more revenue, not less, so the incentive to surface it is negative. And customers accept the metering unit they are given.

## What a Fix Looks Like
Report the ratio the customer actually cares about. Publish cost per successfully extracted and validated record per target, which is computable from data the firm already has and immediately tells a customer where their budget goes — this is the disclosure and it is uncomfortable precisely because it is useful. Break the ratio into its stages, so a customer can see whether a target is expensive because of blocking or because of parse failure, which have different remedies. Alert when a target's ratio degrades, since a site deploying new defences shows up as a cost change before it shows up as a failure. Offer outcome-based pricing per validated record for targets where the firm is confident, which aligns the incentive and is a genuine differentiator. Recommend dropping targets whose ratio makes them uneconomic for the customer's stated value, which costs revenue and buys trust. Report the same ratio internally by target, since the firm's own margin varies as much as the customer's cost and is equally unmeasured. And show the cost of freshness explicitly, because much of the spend is re-fetching unchanged pages and a customer choosing a longer interval saves a lot for very little.

## Who Feels the Pain
Customers whose budget disappears into targets they cannot identify; firms whose margin varies wildly by target with nobody tracking it; and target sites absorbing thirty requests for every record somebody actually uses.

## Impact If Fixed
Cost per validated record varies thirtyfold across targets and nothing reports it. Breaking the ratio into blocking and parsing stages tells a customer which remedy applies, and showing the cost of freshness lets them buy a longer interval for a large saving.
