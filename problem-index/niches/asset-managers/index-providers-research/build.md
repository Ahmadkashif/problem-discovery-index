# The Custom Index Factory

**Niche:** [[niches/asset-managers/index-providers-research/profile|Index Providers' Research & Methodology Teams]]
**Industry:** [[industries/asset-managers|Asset Managers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Demand for custom, thematic and factor indexes has outgrown a research process in which each new index is designed, back-tested, documented and approved largely by hand.
**Tags:** #large-language-models #monte-carlo-methods #convex-optimization #evaluation-metrics #hypothesis-testing #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this pocket is fighting to design, test, document and govern custom and thematic indexes faster than rivals without compromising methodology integrity — and whoever does that wins the ETF, separate-account and direct-indexing launches that drive licensing revenue.

## The Problem
An asset manager wants an index for a new ETF, a separately managed account or a direct-indexing programme: a theme, a factor tilt, an exclusion list, a capacity constraint. The index provider's researchers specify the methodology, build and back-test it, check turnover, capacity and concentration, write the methodology document, take it through index governance, and hand it to operations. Each request is similar in shape and still consumes weeks of researcher time, and the client's launch date does not move.

## Why Nobody Has Built This
Methodology is the provider's core intellectual property and its integrity is the brand, so automation has been resisted. Back-testing tools exist; methodology writing, governance review and the link between them do not.

## What to Build
A design pipeline in which the methodology is specified as structured rules from which the back-test, the capacity and turnover diagnostics and the methodology document are all generated, so they cannot diverge. Language models draft document sections from the rule specification and flag ambiguities that governance would catch; a library of prior approved designs supplies reusable components and precedent; and an overfitting check reports how many design variants were tried before the one presented, which is the integrity question clients and regulators should ask.

## Target Customer
Heads of custom and thematic index research at index providers.

## Impact If Built
Custom index turnaround falls from weeks to days with methodology integrity better evidenced than today, which is what wins launches.
