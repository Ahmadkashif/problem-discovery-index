# Code Comprehension From Legacy Maintenance

**Niche:** [[niches/saas-implementation-partners/the-support-engineer/profile|The Post-Go-Live Support Engineer]]
**Industry:** [[industries/saas-implementation-partners|SaaS Implementation Partners]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Legacy software maintenance built comprehension and dependency tooling for inherited systems, and configured platforms have a slide deck.
**Tags:** #graph-theory #large-language-models #data-integration #worker-facing #evaluation-metrics #workflow-orchestration #automation #tacit-knowledge-ml
**Contested on:** Every serious competitor in this niche is fighting to let someone support a configuration built by people who have left, documented in a slide deck, with no record of why any of it is the way it is — and whoever supplies that context takes the account.

## The Problem
Maintaining systems whose authors are gone is a well-developed discipline in software. Static analysis maps dependencies, call graphs show what a change affects, history and issue tracking recover intent, and comprehension tooling explains unfamiliar code. Maintenance engineers expect these instruments because the alternative is guessing. Support engineers on configured enterprise platforms face the identical problem and have a metadata browser.

## What Already Exists
Dependency and impact analysis; call graph and reference tracing; intent recovery from commit and issue history; automated documentation generation from the system itself; and comprehension assistance for unfamiliar systems.

## The Customization Gap
The adaptation is to configuration metadata rather than source code. It requires: (1) the system being expressed as platform configuration with references across objects, workflows, rules and integrations rather than as code, so the dependency graph must be built from metadata the platform exposes inconsistently — this is the substantive difference; (2) no version history in most platforms, removing the richest source of intent; (3) a live production system that cannot be experimented on; (4) business intent that lives in requirements documents rather than in tickets; and (5) an engineer supporting several client systems rather than maintaining one.

## Target Customer
Implementation partners and managed services providers, support leadership, enterprise clients, and code comprehension and documentation vendors.

## Impact If Solved
Legacy maintenance built dependency analysis and intent recovery because the alternative is guessing. Configuration metadata with no version history is a poorer substrate than source code, which is what makes the intent capture matter more.
