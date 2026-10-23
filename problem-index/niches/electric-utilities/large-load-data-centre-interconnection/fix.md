# The Same Data Centre Counted at Three Utilities

**Niche:** [[niches/electric-utilities/large-load-data-centre-interconnection/profile|Large-Load & Data Centre Interconnection]]
**Industry:** [[industries/electric-utilities|Electric Distribution Utilities]]
**Type:** Fix (Pain Point)
**One-liner:** Developers shop one project to several utilities, each counts it in its forecast, and regional load projections inflate.
**Tags:** #k-nearest-neighbors #feature-engineering #descriptive-statistics #data-integration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to tell a data-centre or factory developer how many megawatts it can have, by when and for what upgrade, while screening out speculative requests, and whoever's answers still hold when the load energises takes the account.

## The Problem
A developer seeking power fast files similar requests with neighbouring utilities, sometimes under different project names. Each utility treats its request as live. Planners can't see the duplication, and regional reliability and resource assessments add the requests up.

## Why It's Still Broken
Request details are commercially confidential, utilities don't share pipelines, and nothing in the intake process asks applicants to disclose parallel requests or ties them to evidence of site control.

## What a Fix Looks Like
Inside each utility: require site-control evidence, a declaration of parallel requests and staged collateral, and score requests on signals of seriousness (land, fibre, permits, developer history). Across utilities, where a commission or regional planner convenes it: privacy-preserving matching of requests by location, size and developer entity, so double-counting is measured without revealing details.

## Who Feels the Pain
Planners sizing substations; forecasters cross-examined on inflated numbers; customers who pay for capacity built for loads that never arrive.

## Impact If Fixed
If ~20%–40% of large-load requests are duplicates or placeholders (estimate), removing them shrinks pipelines to the real projects and stops forecasts being discounted by every reader.
