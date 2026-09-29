# Shift-Left From Software Quality

**Niche:** [[niches/digital-accessibility-firms/build-regression-prevention/profile|Build Regression Prevention]]
**Industry:** [[industries/digital-accessibility-firms|Digital Accessibility Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software moved quality checks to the moment of change decades ago, and accessibility is still audited twice a year.
**Tags:** #automation #workflow-orchestration #compliance #evaluation-metrics #data-integration #descriptive-statistics #quick-win #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to stop new accessibility failures reaching production, because remediating them afterwards costs many times more — and whoever catches them in the build takes the account.

## The Problem
Software quality established that a defect costs progressively more the later it is found, and responded by moving checks to the moment of change: linting in the editor, tests on commit, security scanning in the pipeline, and a build that fails rather than a report that accumulates. The economics are well documented and the tooling is commodity. Accessibility is still assessed as a periodic audit, which is where software quality was before any of it.

## What Already Exists
Checks at commit and in the pipeline; baselines so legacy issues do not block; developer-facing feedback in the editor; build failure on regression; and trend reporting on new defects.

## The Customization Gap
The adaptation is to a property that is only partly decidable automatically. It requires: (1) automated checks covering a minority of the real failures, so a passing build must not be read as an accessible build — this is the substantive difference and is the misreading the whole field already struggles with; (2) component-level testing in a design system rather than only application-level, since that is where leverage is; (3) checks over rendered output and interaction rather than source; (4) a baseline problem so severe that naive adoption fails immediately; and (5) an engineering audience with no accessibility training, so the feedback must teach rather than cite.

## Target Customer
Engineering and platform teams, accessibility firms offering enablement, design system teams, and testing and quality tooling vendors.

## Impact If Solved
Software moved checks to the moment of change because late defects cost more, and the tooling is commodity. Automated coverage of only a minority of failures is why a passing build must be reported honestly rather than as accessibility.
