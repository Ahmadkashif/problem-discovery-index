# Test Selection & Pipeline Duration

**Parent Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor here is fighting to run only the tests a change could plausibly break, with evidence that nothing was missed — and whoever does that takes the platform account, because everyone runs everything and nobody has the evidence to stop.

## Profile
**Market Size:** ~$480M US attributable to test selection, impact analysis and pipeline optimisation
**Share of Parent Industry:** ~12% of category revenue
**Digital Adoption:** Low — the products exist and are used by a small minority
**Target Buyer:** Platform engineering
**Automation Potential:** Very High — the complete evidence is in the execution history

## What Makes This a Distinct Niche
Pipeline duration grows monotonically because every team adds steps and nobody removes them, and the cost of waiting is paid in engineer attention rather than in a budget line, so it is never prioritised. Parallelism, caching and test impact analysis all exist as products, and most organisations still run every test on every change — because deciding what to skip requires evidence that nothing important would be missed, and nobody has assembled it. That is what makes this a distinct contest: the technical capability is available and the adoption barrier is entirely about trust. A team will skip tests when they can see that the skipped tests have not caught anything in a year for changes of this shape, and not before. The platforms hold precisely that record.

## Current Tools & Gaps
Test impact analysis in a few products, parallelisation and sharding, caching, and manual pipeline splitting into fast and slow stages. The gaps: impact analysis requires coverage instrumentation that many stacks make impractical, which is why adoption is low; nothing reports the counterfactual — how often the skipped tests would have caught something — which is the evidence teams need; pipeline growth is unmonitored, so steps accumulate invisibly; the marginal value of each step is never computed, though the data exists; and the safety argument is made by assertion rather than by measurement, which is why cautious organisations refuse.

## Problems
- [[niches/ci-cd-platforms/test-selection-and-duration/build|🔨 Build: Everyone Runs Everything Because Nobody Has the Evidence]]
- [[niches/ci-cd-platforms/test-selection-and-duration/buy|🛒 Buy: Test Impact Analysis Without Coverage Instrumentation]]
- [[niches/ci-cd-platforms/test-selection-and-duration/fix|🔧 Fix: Steps Accumulate and Nothing Is Removed]]
