# Proposal Template Intelligence

**Niche:** [[niches/catering-companies/proposal-to-invoice-pipeline/profile|Proposal-to-Invoice Financial Pipeline]]
**Industry:** [[industries/catering-companies|Catering Companies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** CaterTrax and Better Cater offer proposal templates with static per-head pricing, but they do not learn from past event outcomes to suggest pricing adjustments or flag historically unprofitable configurations.
**Tags:** #gradient-boosting #regression #tabular-ml #revenue-impact #tacit-knowledge-ml

## The Problem
Catering sales managers build 20-40 proposals per month by copying and modifying previous proposals. The per-head pricing is set by a cost template that was calibrated once (often years ago) and never updated to reflect actual event costs. The result: some event configurations are systematically underpriced (outdoor events with complex logistics, events with heavy appetizer courses that cannibalize entree yield) while others are overpriced (simple buffet setups that cost less than the template assumes). The sales manager adjusts based on experience — but new sales managers use the template as-is.

## What Already Exists
CaterTrax, Better Cater, and Caterease provide proposal builders with customizable templates and per-head pricing. They allow the sales manager to adjust pricing manually but offer no data-driven guidance on whether the current pricing will be profitable for this specific event configuration.

## The Customization Gap
The tool must analyze historical proposal-vs-actual data (linking past proposals to post-event costs) and surface insights during proposal creation: "Events with this menu at this venue type have historically cost $52/head, not the $45/head template — consider adjusting." It should flag event configurations that have been unprofitable in the past, suggest pricing adjustments based on venue complexity, season, and service style, and pre-populate labor and rental estimates from similar past events.

## Target Customer
Catering sales managers who generate 15+ proposals per month and have no feedback loop between their quotes and actual event profitability.

## Impact If Solved
Data-driven proposal pricing reduces the 15-25% estimation error to under 5%, recovering $200K-$750K annually for a $3M caterer through elimination of systematic underquoting.
