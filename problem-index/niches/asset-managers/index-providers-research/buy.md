# Release Engineering for Index Methodology

**Niche:** [[niches/asset-managers/index-providers-research/profile|Index Providers' Research & Methodology Teams]]
**Industry:** [[industries/asset-managers|Asset Managers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Index methodologies are effectively software with trillions of dollars tracking them, and they are changed through document revisions and consultations rather than tested releases.
**Tags:** #evaluation-metrics #hypothesis-testing #descriptive-statistics #compliance #workflow-orchestration #automation
**Contested on:** Every serious competitor in this pocket is fighting to design, test, document and govern custom and thematic indexes faster than rivals without compromising methodology integrity — and whoever does that wins the ETF, separate-account and direct-indexing launches that drive licensing revenue.

## The Problem
A methodology change — a new free-float rule, a treatment for a corporate action, a sector reclassification — alters what passive funds must buy and sell. The change is consulted on, documented and implemented, but the link between the document and the calculation code is maintained by people.

## What Already Exists
Software release engineering: version control, automated test suites, staged rollout, change logs tied to code, and impact analysis before deployment.

## The Customization Gap
The adaptation needs: (1) methodology documents and calculation code versioned together, with tests that encode each rule; (2) impact analysis that estimates turnover and trading demand for tracking funds before a change is announced; (3) consultation records linked to the change; (4) governance approvals as release gates under benchmark-regulation oversight; and (5) corporate-action edge cases as regression tests.

## Target Customer
Heads of index methodology, governance and index operations.

## Impact If Solved
Methodology changes ship with evidence of their effect and a guarantee that the calculation matches the document.
