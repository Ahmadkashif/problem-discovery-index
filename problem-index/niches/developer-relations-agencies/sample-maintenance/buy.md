# Continuous Testing From Software Delivery

**Niche:** [[niches/developer-relations-agencies/sample-maintenance/profile|Sample & Tutorial Maintenance]]
**Industry:** [[industries/developer-relations-agencies|Developer Relations Agencies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Every product is tested continuously and the samples that demonstrate it are tested never.
**Tags:** #automation #workflow-orchestration #compliance #evaluation-metrics #data-integration #change-point-detection #descriptive-statistics #quick-win
**Contested on:** Every serious competitor in this niche is fighting to keep dozens of sample applications and tutorials working, because a developer's first experience of the product is running one — and whoever maintains them takes the account.

## The Problem
Continuous integration made it unremarkable that code is built and tested on every change, across dependency versions, with breakage caught immediately. The practice is universal inside product engineering. The sample applications that demonstrate the product to prospective users sit in separate repositories outside that pipeline, are tested by nobody, and break silently — which is a strange inversion given that they are what a new developer actually runs.

## What Already Exists
Continuous build and test on every change; dependency version matrix testing; scheduled runs catching upstream breakage; automated dependency updates with test verification; and visible build status.

## The Customization Gap
The adaptation is to samples that live outside the product's repository and depend on running services. It requires: (1) samples in separate repositories, frequently in several languages, owned by a function outside engineering, so the pipeline must be established rather than extended — this is the substantive difference; (2) samples that call live services and need credentials, environments and quotas to run; (3) tutorials whose steps are prose rather than code, needing a different verification approach; (4) breakage caused by the product's own releases as often as by dependencies; and (5) no owner in the engineering organisation to route a failure to.

## Target Customer
Developer relations agencies and in-house functions, engineering leadership, developer platform vendors, and testing tooling providers.

## Impact If Solved
Continuous testing made silent breakage unacceptable inside product engineering. Samples in separate repositories, calling live services, owned outside engineering, is why the same discipline has not reached them.
