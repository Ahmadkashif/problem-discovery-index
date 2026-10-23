# Allergen-Aware Line Sequencing for Multi-Brand Repackers

**Niche:** [[niches/contract-packagers/food-repacking-multipacks/profile|Food Repacking & Multipack Assembly]]
**Industry:** [[industries/contract-packagers|Contract Packagers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A repacker running several brands' foods on shared lines sequences jobs by gut feel, and every allergen-to-non-allergen changeover adds sanitation hours and recall risk.
**Tags:** #dynamic-programming #optimization-fundamentals #monte-carlo-methods #compliance #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to run many brands' foods through one set of lines with allergen and label control that a GFSI auditor and a retailer will accept, and whoever passes audits and changeovers with no undeclared-allergen hold takes the account.

## The Problem
A repacker's week might include tree nuts, peanut-free snacks, dairy-containing candy and a gluten-free brand on the same two lines. Running allergen-free products before allergen-containing ones avoids full washdowns, but ship dates, component arrivals and crew availability pull the sequence the other way. The scheduler balances it on a whiteboard.

## Why Nobody Has Built This
General production schedulers treat changeovers as times, not as food safety constraints. Food safety software records changeovers but does not plan them. The manufacturer's version of the problem is mapped as [[niches/food-manufacturing/sanitation-and-changeover-management/profile|Sanitation & Changeover Management]]: a plant sequencing its own recipes, under its own allergen statements. A repacker's shared lines run many brands' finished foods, each under the brand's allergen statement and label, so the constraints change with every client added. Repackers are small and their job mix changes weekly.

## What to Build
A sequencer that carries each job's allergen profile, each line's validated cleaning procedures and their times, ship windows and component readiness. It proposes the week's order with the fewest full washdowns, shows the cost of every exception, and generates the changeover verification steps for each transition.

## Target Customer
Owners and food safety managers at multi-brand food repackers and variety-pack co-packers.

## Impact If Built
Fewer sanitation hours lost to avoidable washdowns, fewer risky transitions, and a schedule an auditor can follow.
