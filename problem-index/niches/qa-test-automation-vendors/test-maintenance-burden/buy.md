# Program Repair Research Applied to Tests

**Niche:** [[niches/qa-test-automation-vendors/test-maintenance-burden/profile|Test Maintenance Burden]]
**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Automated program repair and test repair have an active research literature with published techniques, and the commercial answer is heuristic selector matching.
**Tags:** #graph-theory #bert #large-language-models #gradient-boosting #evaluation-metrics #confidence-intervals #cross-validation #automation
**Contested on:** Every serious competitor in this niche is fighting to make a test suite survive two years of interface change without a permanent staffing commitment — and whoever does that takes the account, because the maintenance cost is where the entire economics of automated testing actually sits.

## The Problem
Repairing broken tests after a program change is a studied problem with published techniques: analysing the change, locating the affected test elements, and generating a repair that preserves the test's intent. There is a body of work on test repair specifically, alongside the broader automated program repair literature. The commercial implementations use similarity matching on selectors, which is the simplest possible approach and is the one most likely to repair a test past a real failure.

## What Already Exists
Automated test repair research with published algorithms and evaluation datasets; program repair techniques; abstract syntax tree differencing for change analysis; language models capable of understanding test intent from code; accessibility tree and semantic document representations; and record-and-compare visual techniques.

## The Customization Gap
The adaptation is to a repair that must not hide a defect. It requires: (1) the application change as an explicit input, since repair without knowing what changed is guesswork and the change is available in the version control history — this is the input the commercial implementations do not use and is why they cannot classify; (2) intent preservation as the correctness criterion, meaning the repaired test must still verify what the original verified, which requires representing the intent rather than the steps; (3) an explicit refusal path, because the safe behaviour when the change might be a regression is to fail and say so, and a system that always produces a repair is the hazardous design; (4) evaluation against real breakages with known causes, which requires a dataset of application changes paired with test failures and their correct dispositions — something the vendors could assemble from their fleet and the research community cannot; and (5) bulk repair, since the research typically addresses a single test and the practical problem is a hundred tests broken by one change.

## Target Customer
Test automation vendors, the self-healing feature teams within them, and the large quality engineering organisations building this internally.

## Impact If Solved
An active research literature addresses this and the commercial answer is the weakest available technique with a hazardous failure mode. Using the application change as an input is what makes classification possible, and an explicit refusal path is what makes automatic repair safe to trust.
