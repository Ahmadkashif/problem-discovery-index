# Supplier Quality Software Adapted to Energetic Materials

**Niche:** [[niches/defense-systems-manufacturers/solid-rocket-motor-supply/profile|Solid Rocket Motor & Propellant Ingredient Supply]]
**Industry:** [[industries/defense-systems-manufacturers|Defense Systems Manufacturers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Aerospace supplier quality tools already manage first articles, APQP and production part approval; they don't understand energetic ingredient lots, shelf life or ageing.
**Tags:** #large-language-models #evaluation-metrics #feature-engineering #compliance #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to put qualified motors on missile lines at the contracted rate, and whoever delivers the most flight-qualified motors per month takes the account.

## The Problem
Motor makers manage dozens of energetic and inert ingredient suppliers, each delivering lots whose properties affect processing. Quality engineers track lot certificates, test results and supplier changes in spreadsheets and email, and decide by experience which lots to blend or reject.

## What Already Exists
Aerospace supplier quality and APQP/PPAP software (Net-Inspect, DISCUS for first articles, QMS suites such as ETQ and MasterControl) and LIMS for incoming test results (recalled; see [[niches/aerospace-parts-suppliers/first-article-inspection/profile|First Article Inspection & AS9102 Packages]] for the parts version).

## The Customization Gap
The energetics layer needs: lot genealogy from ingredient to batch to motor; property-based acceptance windows rather than dimensional characteristics; shelf life and storage hazard class; each lot's effect on batch outcomes, learned from batch history; change notification rules that trigger the prime's requalification review; and operation under ITAR on premises.

## Target Customer
Supplier quality managers at motor makers and at the primes' propulsion supply-chain teams.

## Impact If Solved
Lot-aware supplier quality lets a plant see an off-nominal ingredient lot before it reaches a mixer, avoiding a rejected batch or motor worth tens of thousands of dollars or more (estimate).
