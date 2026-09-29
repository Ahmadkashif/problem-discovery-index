# Architecture Decision Practice

**Niche:** [[niches/headless-commerce-vendors/the-solutions-architect/profile|The Solutions Architect]]
**Industry:** [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software architecture developed decision records, evaluation methods and fitness functions to make design choices reviewable, and commerce compositions are designed from vendor slide decks.
**Tags:** #compliance #evaluation-metrics #graph-theory #confidence-intervals #worker-facing #workflow-orchestration #descriptive-statistics #automation
**Contested on:** Every serious competitor in this niche is fighting to let an architect find out whether a composition works before the programme commits to it — and whoever does that takes the delivery quality, because the failure modes currently appear in production eighteen months later.

## The Problem
Making architecture decisions reviewable and testable is a developed practice. Architecture decision records capture what was decided, why, and what was rejected. Scenario-based evaluation methods test a proposed architecture against the quality attributes that matter. Fitness functions turn architectural properties into automated tests that run continuously. Risk-driven architecture focuses effort where the uncertainty is. All of it exists, is taught, and is largely absent from commerce replatform programmes.

## What Already Exists
Architecture decision records with structured rationale; scenario-based architecture evaluation methods; architectural fitness functions as automated tests; risk-driven design prioritisation; quality attribute scenarios; and the trade-off analysis methods developed for exactly this kind of decision.

## The Customization Gap
The adaptation is to an architecture assembled from components you cannot inspect. It requires: (1) quality attribute scenarios written against vendor services whose internals are opaque, which means the scenarios must be expressed as observable behaviour and tested empirically rather than reasoned about — this empirical substitution is the adaptation and it is what the sandbox enables; (2) fitness functions that run against the composed production system, since the architectural properties that matter here are cross-service and cannot be tested in any single codebase; (3) risk prioritisation informed by what has actually gone wrong in comparable compositions, which requires the pattern library; (4) decision records that survive the integrator leaving, since the architect frequently does not stay with the system; and (5) trade-off analysis including commercial dimensions — vendor lock-in, contractual terms, exit cost — which software architecture methods do not model and which dominate here.

## Target Customer
Solutions architects, integrator and vendor delivery organisations, retail architecture functions, and the software architecture community.

## Impact If Solved
Architecture decision practice is mature and assumes components you can inspect and reason about. Expressing quality attributes as empirically testable observable behaviour is the adaptation, and fitness functions running against the composed production system are the only place these properties can be checked.
