# Feature Flagging From Software Delivery

**Niche:** [[niches/conversion-optimization-firms/variant-implementation/profile|Variant Implementation Quality]]
**Industry:** [[industries/conversion-optimization-firms|Conversion Optimization Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software ships variants behind server-side flags as a matter of course, and optimisation injects them with a script.
**Tags:** #automation #workflow-orchestration #data-integration #evaluation-metrics #compliance #change-point-detection #descriptive-statistics #quick-win
**Contested on:** Every serious competitor in this niche is fighting to change a live page without introducing effects that have nothing to do with the hypothesis — and whoever implements variants cleanly takes the account.

## The Problem
Feature flagging solved the problem of serving different experiences to different users cleanly: the variant is part of the application, evaluated server-side or at build, with no flicker, no broken injection and consistent tracking. Product teams run experiments this way routinely. Conversion optimisation, which exists to run experiments, mostly does not, because client-side injection lets it operate without engineering involvement — which is a commercial convenience purchased with measurement quality.

## What Already Exists
Server-side flag evaluation; consistent assignment across sessions and devices; experiments as part of the application rather than injected; clean metric instrumentation; and gradual rollout from the same mechanism.

## The Customization Gap
The adaptation is to an agency working on a client's site without engineering access. It requires: (1) an external firm that cannot deploy code to the client's application, which is why client-side injection exists at all and is the substantive obstacle rather than a technical one; (2) tests on marketing pages owned by marketing rather than by engineering; (3) a commercial model built on speed without engineering dependency; (4) content management systems and page builders that are not application code; and (5) a hybrid reality where some tests must be client-side and the reporting should say which.

## Target Customer
Conversion optimisation firms and in-house teams, testing platform vendors, engineering leadership, and feature flagging providers.

## Impact If Solved
Feature flagging made clean variant delivery routine for product teams. An external firm with no deployment access is the commercial obstacle that keeps optimisation on client-side injection.
