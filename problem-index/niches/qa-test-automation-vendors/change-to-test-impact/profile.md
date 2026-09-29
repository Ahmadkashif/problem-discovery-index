# Change-to-Test Impact

**Parent Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor here is fighting to model the relationship between an application change and the tests it affects — and whoever does that takes the category, because that relationship is its central object and is modelled nowhere.

## Profile
**Market Size:** ~$460M US attributable to test impact analysis and change-aware testing
**Share of Parent Industry:** ~12% of category revenue
**Digital Adoption:** None — the relationship is not modelled anywhere
**Target Buyer:** Platform and quality engineering
**Automation Potential:** Very High — both sides of the relationship are fully recorded

## What Makes This a Distinct Niche
The relationship between a code or interface change and the tests it breaks is the central object of the category and is not modelled anywhere. Every significant capability depends on it: selecting which tests to run depends on knowing which a change could affect; repairing a broken test safely depends on knowing what changed and whether the change was behavioural; classifying a failure as a regression or a maintenance break is the same question; and telling a developer whether their change is verified requires it too. The industry has instead built each capability on a weaker proxy — file proximity for selection, selector similarity for repair, re-run behaviour for flakiness — because the relationship itself was never constructed. Both sides of it are fully recorded in every organisation: the change is in version control and the test outcome is in the execution history.

## Current Tools & Gaps
Test impact analysis based on coverage instrumentation, file-based heuristics in some pipelines, and self-healing based on selector matching. The gaps: coverage-based impact analysis requires instrumentation many stacks cannot provide, which caps adoption; interface changes are outside code coverage entirely, although they cause most end-to-end test breakage; the historical relationship — which changes have broken which tests before — is free and is not used; nothing distinguishes a change that alters behaviour from one that alters presentation, which is the classification everything else needs; and no vendor has built the model despite holding the data across their whole fleet.

## Problems
- [[niches/qa-test-automation-vendors/change-to-test-impact/build|🔨 Build: The Category's Central Object, Unmodelled]]
- [[niches/qa-test-automation-vendors/change-to-test-impact/buy|🛒 Buy: Change Impact Analysis From Program Analysis]]
- [[niches/qa-test-automation-vendors/change-to-test-impact/fix|🔧 Fix: Interface Changes Are Invisible to Code Coverage]]
