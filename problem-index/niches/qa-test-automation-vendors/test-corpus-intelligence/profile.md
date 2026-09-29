# Test Corpus Intelligence

**Parent Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor that gets here is fighting to use a fleet-wide record of tests, failures, repairs and the changes that caused them — and whoever does that can distinguish a cosmetic change from a regression, which is the capability the whole category is missing.

## Profile
**Market Size:** ~$380M US, largely latent
**Share of Parent Industry:** ~10% of category revenue
**Digital Adoption:** None — the corpus renders pass and fail
**Target Buyer:** The vendors themselves; secondarily quality engineering
**Automation Potential:** Very High — the corpus is large, structured and labelled by outcome

## What Makes This a Distinct Niche
These vendors observe test executions, failures, repairs and the application changes that caused them, across enormous numbers of applications. That is a labelled corpus of exactly the relationship the category cannot model within one organisation: which kinds of change break which kinds of test, whether a repair that was made turned out to be correct, and what a genuine regression looks like compared with a cosmetic break. The frameworks are shared, the change patterns recur, and the outcomes are recorded — which makes this an unusually favourable cross-customer learning problem and one where the structural representation contains no customer content. It is used to render pass and fail.

## Current Tools & Gaps
Execution history per customer, failure dashboards, and flakiness counters. The gaps: the cross-customer relationship between change patterns and test breakage is the category's missing model and is learnable only from a fleet; repair outcomes — whether a self-healed test was later found to have healed wrongly — are the label that would make healing safe and are not collected; flakiness patterns recur across customers using the same frameworks and are rediscovered individually; benchmarking a customer's suite health against comparable ones is a question customers ask and nobody answers; and no vendor has articulated a governance position, so the topic is avoided rather than designed.

## Problems
- [[niches/qa-test-automation-vendors/test-corpus-intelligence/build|🔨 Build: A Labelled Corpus, Used to Render Pass and Fail]]
- [[niches/qa-test-automation-vendors/test-corpus-intelligence/buy|🛒 Buy: Cross-Customer Learning With No Customer Content]]
- [[niches/qa-test-automation-vendors/test-corpus-intelligence/fix|🔧 Fix: The Same Flakiness Rediscovered Everywhere]]
