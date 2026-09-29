# Self-Healing Automation and Program Repair

**Niche:** [[niches/web-data-extraction-firms/automated-extraction-repair/profile|Automated Extraction Repair]]
**Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Test automation built self-healing locators for exactly this problem and program repair research built the verification discipline, and extraction fleets use neither.
**Tags:** #large-language-models #automation #evaluation-metrics #transfer-learning #cross-validation #confidence-intervals #workflow-orchestration #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to repair a broken extractor without a person, verified, at fleet scale — and whoever does that takes the account, because repair is now mechanically feasible and is still being done by hand.

## The Problem
Browser test automation faced precisely this problem — selectors breaking when a page changes — and built self-healing locators that identify an element by multiple attributes and repair the reference automatically when the primary one fails. It is a standard feature in commercial test tooling. Separately, automated program repair research established the discipline that matters most: a generated patch must be validated, and a patch that passes a weak test is worse than no patch. Extraction repair uses neither the technique nor the discipline.

## What Already Exists
Self-healing element locators in test automation with multi-attribute identification and confidence scoring; visual and structural element matching across page versions; automated program repair with patch generation and validation; test oracles and regression suites as validation gates; and model-based code repair with verification loops.

## The Customization Gap
The adaptation is to a repair with no test suite to validate against. It requires: (1) a validation oracle built from the data's own history rather than from tests, since there is no assertion that the price is correct and the available evidence is that the new values should resemble the old distribution — constructing that oracle is the central adaptation and is what the program repair discipline insists on; (2) multi-attribute element identification carried over from test tooling, which is directly applicable and largely unused here; (3) repair across thousands of independent targets rather than one application, where the per-target cost must be near zero; (4) the patch-overfitting lesson from program repair, since a repair that satisfies a weak check and extracts the wrong field is exactly the overfitted patch that literature warns about and is the dominant risk here; and (5) cross-site generalisation, since many sites share layout patterns and a repair strategy that worked on one is evidence for another — an opportunity single-application repair never has.

## Target Customer
Extraction firms, test automation vendors for whom this is an adjacent market, and the automated program repair research community.

## Impact If Solved
Self-healing locators solve the technique and program repair supplies the discipline, and neither is used. Building a validation oracle from the data's own history is the central adaptation, and the patch-overfitting lesson is precisely the risk that makes unverified repair dangerous.
