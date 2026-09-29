# Checking the Prose Against the Product

**Niche:** [[niches/technical-content-agencies/content-drift/profile|Content Drift]]
**Industry:** [[industries/technical-content-agencies|Technical Content Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The product is a machine-readable source of truth and nothing checks the documentation against it.
**Tags:** #automation #data-integration #evaluation-metrics #compliance #change-point-detection #workflow-orchestration #descriptive-statistics #sets-and-logic
**Contested on:** Every serious competitor in this niche is fighting to keep prose true about software that ships weekly, and whoever detects the drift automatically takes the account.

## The Problem
Documentation describes software that changes weekly and is updated when someone notices or remembers. Examples stop compiling, parameters are renamed, defaults change, methods are removed, and screenshots show an interface that has been redesigned. Each individual instance is minor; collectively they teach readers that the documentation cannot be trusted, which is the most expensive thing a documentation corpus can lose.

## Why Nobody Has Built This
Documentation and code are maintained separately by different people with different cadences. Nobody has wired the product's own definitions into a check on the prose. Screenshots are treated as unverifiable. And the drift is found by readers, whose reports are treated as individual corrections.

## What to Build
Verify the documentation against the product automatically and continuously. Compile and run every code example against the current version in continuous integration, which is the core and eliminates the most damaging and most detectable class outright. Check named parameters, methods, endpoints and defaults against the product's own definitions, which is a comparison against machine-readable truth and is entirely mechanical. Detect screenshots showing interfaces that have changed, which is harder and is tractable with current tooling. Link documentation pages to the code they describe so a change flags the page, which is the structural fix. Flag pages whose subject changed and which have not been reviewed since, rather than reviewing everything periodically. Measure and report corpus staleness, which is the metric that makes drift a managed condition rather than an ambient one. Fail the documentation build on a broken example, which is what makes the check bite. Route drift alerts to the team that made the change, not only to the writers. Prioritise the most-read pages, since trust is lost fastest there. And treat a reader's drift report as a detection failure rather than as a useful contribution.

## Target Customer
Documentation teams and technical content agencies, engineering and developer experience leadership, documentation platform vendors, and testing tooling providers.

## Impact If Built
The product is a machine-readable source of truth and nothing checks the prose against it, so readers find the drift. Running every example in continuous integration eliminates the most damaging class outright.
