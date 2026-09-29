# The Test That Healed Past the Regression

**Niche:** [[niches/qa-test-automation-vendors/ai-generated-and-self-healing/profile|AI-Generated & Self-Healing Tests]]
**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Self-healing repairs a test by finding the element that most resembles the one that disappeared, which repairs cosmetic changes and also conceals the regressions that removed the element deliberately.
**Tags:** #graph-theory #bert #large-language-models #bayesian-inference #confidence-intervals #evaluation-metrics #cross-validation #automation
**Contested on:** Every serious competitor here is fighting to make a test that writes and repairs itself trustworthy enough to rely on — and whoever does that takes quality engineering, because a suite that heals past a regression is worse than no suite and the category has already failed this promise twice.

## The Problem
A developer removes a confirmation step from a purchase flow by mistake. The test that verified the confirmation step can no longer find its element. Self-healing locates the element that most resembles it — the next button in the flow — binds to that, and the test passes. The regression ships. Nobody is alerted, because from the healing mechanism's perspective this is indistinguishable from a renamed element, which is what it was designed to handle. The suite has not merely failed to catch the defect; it has actively reported that the behaviour is correct.

## Why Nobody Has Built This
Healing was implemented on selector similarity because that is the information available at the moment of failure — the test knows what it was looking for and what is on the page, and nothing more. The information that would resolve it is the application change: whether the element was renamed or removed is answerable from the diff and is not consulted, because the test tool and the version control system are separate and nobody joined them. The failure mode is also invisible by construction: a healed test passes, and nothing records that it healed in a way it should not have.

## What to Build
Classify before healing, using the change. Join the test failure to the application change that preceded it, which is the input the current implementations lack and is available in every repository — an element renamed in a diff is a cosmetic change and an element deleted alongside the logic behind it is not. Reason about behaviour rather than about selectors: the question is whether the flow the test verifies still exists, which is answerable from the change and from the surrounding application structure. Heal only where the classification is confident, and fail loudly with the evidence where it is not, since the asymmetry is extreme — a false heal produces false assurance and a false failure produces five minutes of investigation. Record every heal with its classification and evidence, so the failure mode becomes auditable rather than invisible, which it currently is. Report the heal rate and the heal-then-defect rate, which is the honest measure of whether the mechanism is safe and no vendor publishes it. And validate against real regressions deliberately, by introducing changes known to be regressions and confirming the mechanism fails rather than heals, which is mutation testing applied to the healing mechanism itself and is the evaluation this capability needs and has never had.

## Target Customer
Quality engineering leadership evaluating these tools, and the vendors shipping self-healing, for whom a demonstrable safety property is the strongest available differentiator in a market with a history of disappointment.

## Impact If Built
The hazard is false assurance, which is the worst possible failure for a testing system and is invisible by construction. Joining to the application change is what makes classification possible, and auditing heals is what makes the failure mode detectable at all.
