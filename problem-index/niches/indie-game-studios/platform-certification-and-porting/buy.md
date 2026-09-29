# Compliance Automation From Regulated Software

**Niche:** [[niches/indie-game-studios/platform-certification-and-porting/profile|Platform Certification & Porting]]
**Industry:** [[industries/indie-game-studios|Indie Game Studios]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Regulated software turned compliance requirements into automated checks in the build, and game certification is a document and a hope.
**Tags:** #compliance #workflow-orchestration #automation #evaluation-metrics #sets-and-logic #data-integration #confidence-intervals #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to get a two-person team through four certification regimes written for studios with a compliance department — and whoever does it multiplies the reachable market without multiplying the team.

## The Problem
Industries where software must satisfy external requirements — medical devices, aviation, payments, accessibility — moved from reading documents to automated conformance: requirements expressed as testable rules, checks in the build pipeline, evidence generated automatically, and failures caught at commit rather than at audit. The shift happened because manual conformance does not scale and because a late failure is expensive. Game certification has the same structure and is still a reading exercise.

## What Already Exists
Requirements-as-code and automated conformance checking; continuous compliance in build pipelines; evidence generation for submission; deviation and exception tracking; and certification readiness reporting.

## The Customization Gap
The adaptation is to behavioural requirements about an interactive experience. It requires: (1) requirements about runtime behaviour — what happens on suspend, on disconnect, on low storage — which must be tested by exercising the game rather than by inspecting code, and that is the substantive technical problem; (2) four different regimes with no common structure, so the checks cannot share a specification; (3) requirements that change with platform updates and are not versioned in a machine-readable form; (4) teams with no build engineering capacity; and (5) an engine layer between the requirement and the implementation, so the check must know what the engine does by default.

## Target Customer
Technical leadership, porting houses, platform holders, and build and compliance tooling vendors.

## Impact If Solved
Regulated software moved from reading documents to automated conformance because late failures are expensive. Testing runtime behaviour rather than inspecting code is the technical adaptation, and the engine layer is what makes a shared check feasible.
