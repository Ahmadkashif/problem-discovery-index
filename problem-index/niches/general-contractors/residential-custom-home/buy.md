# Selection & Allowance Management System

**Niche:** [[niches/general-contractors/residential-custom-home/profile|Residential Custom Home Builders]]
**Industry:** [[industries/general-contractors|General Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** General-purpose project budgeting tools exist, but none understand the custom home allowance model — where clients choose finishes against pre-set budgets, overages cascade through the contract, and missed deadlines delay construction.
**Tags:** #decision-trees #feature-engineering #automation #workflow-orchestration #data-integration

## The Problem
A typical custom home has 80-150 individual finish selections (tile patterns, countertop materials, cabinet styles, fixture models, paint colors, hardware finishes, appliance packages, lighting fixtures, flooring types). Each selection has an allowance budget in the contract, a deadline tied to the construction schedule, and a procurement lead time. When a client selects $18K in lighting against a $12K allowance, the $6K overage needs to flow into a change order, update the contract total, and adjust the draw schedule. Currently, builders track this in spreadsheets with manual formula updates — one mislinked cell means a $6K overage never gets billed.

## What Already Exists
Buildertrend and CoConstruct have basic selection tracking — they let clients view options and mark choices — but don't connect selections to allowance budgets, don't calculate overages automatically, and don't link selection deadlines to the construction schedule. General-purpose budgeting tools (QuickBooks, Sage) track costs but have no concept of "allowances" as a distinct budget type with client-facing visibility. Interior design tools (Studio Designer, Design Manager) track specifications but don't connect to construction scheduling or contractor accounting.

## The Customization Gap
The missing layer is allowance-aware budget logic that understands: (1) each selection category has a contract allowance amount; (2) when a client's selection exceeds the allowance, the difference is automatically calculated and staged as a change order; (3) selection deadlines are derived from the construction schedule (tile must be selected 6 weeks before bathroom rough-in to account for ordering lead time); (4) unselected items past deadline trigger alerts to both builder and client; (5) cumulative allowance overages roll up into a running contract adjustment visible to both parties. This requires construction-specific domain logic that no general budgeting or design tool provides.

## Target Customer
Custom home builders and their project coordinators who manage selections across multiple concurrent builds using spreadsheets, email threads, and physical binders of product samples.

## Impact If Solved
Eliminates the 3-5% of contract value that builders fail to collect due to untracked allowance overages (on a $1M home, that's $30-50K in lost revenue). Reduces selection-related schedule delays by 2-3 weeks per project by enforcing deadline visibility. Saves 4-6 hours per week of project coordinator time spent on manual allowance tracking and change order preparation.
