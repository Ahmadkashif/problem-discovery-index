# Linting and Enforcement From Code Style

**Niche:** [[niches/technical-content-agencies/style-and-terminology/profile|Style & Terminology Consistency]]
**Industry:** [[industries/technical-content-agencies|Technical Content Agencies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Code style stopped being argued about when it became automatic, and documentation style is still reviewed by a person.
**Tags:** #automation #workflow-orchestration #evaluation-metrics #compliance #data-integration #word-embeddings #descriptive-statistics #quick-win
**Contested on:** Every serious competitor in this niche is fighting to keep one term meaning one thing across a corpus written by many people over many years, and whoever enforces that mechanically takes the account.

## The Problem
Software resolved the style argument by automating it: formatters apply the standard without discussion, linters enforce the rules at authoring, the whole repository is reformatted once, and style ceases to be a review topic. The effect was to remove an entire category of unproductive disagreement and free review for substance. Documentation review still spends attention on capitalisation, heading style and terminology that a tool could settle.

## What Already Exists
Automatic formatting applied without discussion; linting at authoring with editor integration; whole-repository normalisation; configurable rule sets with team-level agreement; and style removed from review entirely.

## The Customization Gap
The adaptation is to prose where some rules are semantic rather than syntactic. It requires: (1) terminology rules that depend on meaning rather than on form, so a formatter cannot simply rewrite and a suggestion must be judged — this is the substantive difference; (2) exceptions that are legitimate, since prose has context that code style does not; (3) a corpus whose older portions were written under different standards and cannot all be normalised safely; (4) writers who will reject a tool that changes their prose without asking; and (5) rules that must be agreed editorially rather than technically.

## Target Customer
Documentation teams and agencies, editorial leadership, documentation tooling vendors, and developer tooling providers.

## Impact If Solved
Automating code style removed a whole category of unproductive disagreement and freed review for substance. Rules that depend on meaning rather than form is why the documentation version suggests rather than rewrites.
