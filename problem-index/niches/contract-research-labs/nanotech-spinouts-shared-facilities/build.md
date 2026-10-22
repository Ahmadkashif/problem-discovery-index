# A Portable Process Recipe and Run History

**Niche:** [[niches/contract-research-labs/nanotech-spinouts-shared-facilities/profile|Nanotech Spinouts on Shared Facilities]]
**Industry:** [[industries/contract-research-labs|Contract Research Labs]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A startup's real asset is its fabrication process, and it exists as run sheets spread across three facilities and one engineer's memory of how to tune each tool.
**Tags:** #tacit-knowledge-ml #gaussian-processes #bayesian-optimization #feature-engineering #transfer-learning #data-integration
**Contested on:** Every serious competitor serving these firms is fighting to give a nanotech startup production-grade fabrication and characterisation capability without its own cleanroom, and whoever turns rented tool time into reproducible process recipes the startup owns takes the account.

## The Problem
The process engineer knows that the deposition tool at one facility runs hot, that the etch at another needs ten extra seconds after maintenance, that a film looks right under the optical microscope before it measures right. When the engineer leaves, or a facility retires a tool, the startup restarts process development and loses months.

## Why Nobody Has Built This
Facilities own the tool logs and have no reason to make them portable; startups are too small to build process informatics; manufacturing execution systems assume one fab with fixed tools.

## What to Build
A startup-owned process record: each run's recipe, tool, facility, maintenance state, operator notes and characterisation results captured from run sheets and instrument files; a model of each step's response to settings, transferable across tools of the same class with a few calibration runs; and suggested settings when moving a step to a new tool, drawing on the engineer's past tuning decisions.

## Target Customer
Founder-CTOs and process engineers at nanotech spinouts using two or more shared facilities.

## Impact If Built
Moving a process to a new tool or a pilot line takes weeks rather than months (estimate), and the startup can show an investor a reproducible process it owns rather than an engineer it depends on.
