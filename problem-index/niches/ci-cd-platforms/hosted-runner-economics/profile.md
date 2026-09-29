# Hosted Runner Economics

**Parent Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in hosted execution is fighting to deliver a started, warm, cache-local runner in seconds at the lowest cost per change — and whoever does that takes the account, because this market is compared on a spreadsheet and switching is a configuration change.

## Profile
**Market Size:** ~$1.1B US hosted CI execution
**Share of Parent Industry:** ~28% of category revenue
**Digital Adoption:** Very High — the default for most organisations
**Target Buyer:** Platform teams comparing vendors on cost and queue time
**Automation Potential:** Very High — placement, warmth and sizing are all optimisable

## What Makes This a Distinct Niche
Hosted execution is close to a commodity market and behaves like one: the offerings are functionally similar, the comparison is made on a spreadsheet, and switching is a change to a configuration file rather than a migration. That makes the contest unusually sharp and unusually narrow. What actually differs between vendors is queue time before a runner is available, how cold the machine is when it starts, how far the cache and the dependency mirrors are from the compute, how well the instance size matches the workload, and the price per minute — and organisations discover all of this after adopting rather than during evaluation, because no vendor publishes it in comparable terms. The customers most affected are the ones with the highest volume, which is where the revenue is.

## Current Tools & Gaps
Hosted runners from every major vendor, machine size tiers, cached dependency mirrors of varying quality, and concurrency limits by plan. The gaps: queue time is rarely reported and is a large share of many organisations' elapsed pipeline time; cold start cost is paid on every job and is largely avoidable; instance sizing is chosen once by a human and is wrong for most jobs in both directions; cache proximity is not exposed, so a customer cannot tell that half their build is data transfer; and no vendor publishes comparable performance figures, so the market is compared on list price alone.

## Problems
- [[niches/ci-cd-platforms/hosted-runner-economics/build|🔨 Build: Queue Time Nobody Counts]]
- [[niches/ci-cd-platforms/hosted-runner-economics/buy|🛒 Buy: Autoscaling and Right-Sizing From Cloud Operations]]
- [[niches/ci-cd-platforms/hosted-runner-economics/fix|🔧 Fix: A Market Compared on List Price Alone]]
