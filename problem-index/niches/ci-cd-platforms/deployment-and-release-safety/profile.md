# Deployment & Release Safety

**Parent Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Category:** Low Digitized
**Contested on:** Every serious competitor here is fighting to make a bad release stop itself before most users see it — and whoever does that takes the release account, because the alternative is that a human notices and reacts, which is what happens almost everywhere.

## Profile
**Market Size:** ~$840M US deployment, progressive delivery and release management
**Share of Parent Industry:** ~21% of category revenue
**Digital Adoption:** Low — most organisations deploy to everyone and watch
**Target Buyer:** Site reliability and release engineering
**Automation Potential:** Very High — the health signals exist and the decision is rule-based

## What Makes This a Distinct Niche
The continuous integration half of the category is mature and the delivery half is not. Most organisations still deploy a change to everybody at once and rely on someone noticing that something is wrong, which is a detection mechanism with a latency measured in minutes to hours and a coverage determined by who happens to be looking. Progressive delivery — releasing to a small population, evaluating health, and proceeding or reverting automatically — is mature, well documented and adopted by a minority. The gap is not capability but integration: it requires the deployment system to understand service health, which means joining delivery tooling to observability, and those are different products with different owners. The contest is an automatic, evidence-based stop, and the organisations that lack it discover the need during an incident.

## Current Tools & Gaps
Deployment tooling with rolling updates; progressive delivery controllers in the container ecosystem; feature flag platforms that provide a different route to the same outcome; and manual canary practices. The gaps: health evaluation is configured as a static threshold on one or two metrics, which is the same guessing problem the alerting niche describes; the comparison that matters — the canary population against the control population — is rarely made properly, so the evaluation is against a global baseline that includes the canary; rollback is available and slow enough that humans hesitate; feature flags and deployments are managed separately although they are the same decision; and nobody measures how long a bad release is live before it stops.

## Problems
- [[niches/ci-cd-platforms/deployment-and-release-safety/build|🔨 Build: Deploy to Everyone and Watch]]
- [[niches/ci-cd-platforms/deployment-and-release-safety/buy|🛒 Buy: Sequential Testing for the Canary Decision]]
- [[niches/ci-cd-platforms/deployment-and-release-safety/fix|🔧 Fix: Rollback That Nobody Trusts]]
