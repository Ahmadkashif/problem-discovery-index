# Jurisdiction-Aware Claims Workflow Engine

**Niche:** [[niches/insurance-tpa/workers-comp-claims/profile|Workers' Comp Claims TPA]]
**Industry:** [[industries/insurance-tpa|Insurance TPA]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Generic BPM tools exist for workflow automation, but none encode the 50-state matrix of workers' comp benefit schedules, filing deadlines, and compensability rules.
**Tags:** #llm #text-classification #nlp #compliance #workflow-orchestration

## The Problem
Workers' comp examiners must track state-specific filing deadlines (3 days in California, 10 days in Texas), benefit calculation formulas (AWW caps, PPD schedules), and compensability determination criteria that vary by jurisdiction. Examiners currently maintain this knowledge through experience, reference binders, and manual lookups — leading to missed deadlines that trigger penalties averaging $2,000-$10,000 per violation.

## What Already Exists
Workflow tools like Pega, Appian, and ServiceNow offer configurable BPM platforms. Claims management systems like Guidewire ClaimCenter have basic jurisdiction rules. Neither provides a continuously updated, comprehensive rules engine that encodes all 50 states' workers' comp statutes with automatic deadline tracking relative to date-of-injury and filing events.

## The Customization Gap
The gap is a jurisdiction rules layer that sits atop any claims system — auto-populating state-specific deadlines, benefit formulas, required forms, and compensability criteria the moment a state is selected. This requires continuous legislative monitoring (states change rules annually) and mapping to examiner workflows, not just static reference tables.

## Target Customer
Multi-state TPAs handling claims across 10+ jurisdictions, particularly those that have expanded geographically through acquisition and now operate inconsistent state-specific processes.

## Impact If Solved
Eliminates 90% of jurisdiction-related compliance penalties (average $150K-$500K annually for mid-size TPAs) and reduces examiner time spent on regulatory lookups by 4-6 hours per week per examiner.
