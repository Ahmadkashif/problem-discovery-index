# Pipeline Execution Platforms

**Parent Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Category:** High Market Share
**Contested on:** Every serious competitor here is fighting to be where an organisation's pipelines actually run — and that contest is fought on economics in one market and on control in another, which is why this niche is not terminal and is decomposed below.

## Profile
**Market Size:** ~$1.7B US pipeline execution and build infrastructure
**Share of Parent Industry:** ~43% of category revenue
**Digital Adoption:** Universal — every software organisation runs pipelines somewhere
**Target Buyer:** Platform teams, buying on cost or on control depending on the market
**Automation Potential:** High — scheduling, caching and placement are all optimisable and mostly static

## What Makes This a Distinct Niche
This is the core of the category: somewhere, compute executes the build and the tests, and the choice of where has become one of the more consequential infrastructure decisions an engineering organisation makes. It determines how long developers wait, what the monthly bill is, what hardware is available, and how much of the platform team's time is spent operating rather than improving.

The filter fails here. "Pipeline execution" names the product rather than the contest, and the market has two halves that share almost nothing. One is a hosted commodity market competing on price per minute, queue time, cold start and cache locality, bought by a platform team with a spreadsheet. The other is a control market competing on auditability, air-gapped operation, specialised hardware and the ability to be operated by the customer, bought by organisations whose real alternative is running it themselves and who will do so if the product does not fit. Vendors strong in one are routinely irrelevant in the other. The two contested sub-niches below carry the terminal statements.

## Current Tools & Gaps
Hosted services from the repository platforms and specialist vendors; self-managed servers with deep customisation in large enterprises; cloud-native build services; and build systems providing caching and incrementality where adopted. The gaps: pricing is per minute of wall clock, which rewards slow builds and is misaligned with everyone's interests; cache behaviour is configured by copying a template and is rarely tuned, so most organisations pay repeatedly for work already done; runner placement ignores data locality, so builds pull dependencies across regions; and the platforms hold the complete record of which pipelines are worth their cost and compute none of it.

## Problems
- [[niches/ci-cd-platforms/pipeline-execution-platforms/build|🔨 Build: Paying by the Minute for Work Already Done]]
- [[niches/ci-cd-platforms/pipeline-execution-platforms/buy|🛒 Buy: Scheduling and Caching Are Solved Somewhere Else]]
- [[niches/ci-cd-platforms/pipeline-execution-platforms/fix|🔧 Fix: Pricing That Rewards a Slow Build]]
