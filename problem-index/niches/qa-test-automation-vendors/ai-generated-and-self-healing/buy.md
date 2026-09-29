# Oracle Generation Is the Hard Half

**Niche:** [[niches/qa-test-automation-vendors/ai-generated-and-self-healing/profile|AI-Generated & Self-Healing Tests]]
**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Automated test generation has decades of research and a well-known limitation — generating inputs is easy and knowing what the correct output should be is not — and the current commercial wave has rediscovered the easy half.
**Tags:** #large-language-models #monte-carlo-methods #evaluation-metrics #confidence-intervals #cross-validation #hypothesis-testing #transformers #automation
**Contested on:** Every serious competitor here is fighting to make a test that writes and repairs itself trustworthy enough to rely on — and whoever does that takes quality engineering, because a suite that heals past a regression is worse than no suite and the category has already failed this promise twice.

## The Problem
Automated test generation is a mature research area and its central difficulty has a name: the oracle problem. Generating inputs and exercising paths is tractable; knowing what the correct result should be is not, because the specification usually exists only in somebody's head. Commercial generated-test tooling mostly resolves this by asserting that the application should continue doing what it currently does, which produces a suite that detects change rather than defects and locks in whatever is already wrong.

## What Already Exists
Search-based and symbolic test generation with decades of research; property-based testing, which addresses the oracle problem by asserting invariants rather than outputs; metamorphic testing, which relates outputs to each other rather than to a known truth; differential testing against a reference implementation; and language models capable of inferring intent from code, documentation and naming.

## The Customization Gap
The adaptation is to a commercial setting with no specification. It requires: (1) taking the oracle problem seriously rather than sidestepping it, which means generating assertions from intent — documentation, requirements, issue text, naming, prior test suites — rather than from current behaviour, and being explicit when the assertion is merely a change detector; (2) property and invariant inference, since properties that should always hold are frequently stated in documentation and are a far stronger oracle than a recorded output; (3) labelling assertion strength, so a team can see which of their generated tests verify a requirement and which merely record the present, and can treat them differently; (4) generation targeted at what is not covered behaviourally rather than at what is not covered by line, which requires the behaviour coverage measurement from the other niche and is what makes generation useful rather than voluminous; and (5) honest evaluation against defect detection, since the category's previous failures with generated testing were failures of value rather than of volume and will repeat otherwise.

## Target Customer
Test generation vendors, quality engineering functions evaluating them, and the property-based testing tool communities whose approach addresses the central difficulty.

## Impact If Solved
The oracle problem is the known hard half and the commercial wave has solved the easy one, which is why generated suites detect change rather than defects. Intent-derived assertions and property inference are the two routes to a real oracle, and labelling assertion strength is the honesty that makes the output usable.
