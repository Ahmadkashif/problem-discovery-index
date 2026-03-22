# OSP Design Tools with Make-Ready Tracking

**Niche:** [[niches/utility-contractors/telecom-fiber/profile|Telecom & Fiber]]
**Industry:** [[industries/utility-contractors|Utility Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** 3-GIS and Vetro FiberMap handle fiber network design but don't track the make-ready process that determines when each designed segment can actually be built — forcing project managers to maintain a parallel spreadsheet of thousands of pole attachment applications with their status across multiple pole owners.
**Tags:** #data-integration #workflow-orchestration #automation #quick-win

## The Problem
The fiber design tool shows the planned network. The make-ready spreadsheet shows which segments of that planned network can actually be built today (make-ready complete), which are pending (application submitted, waiting for engineering review), and which are blocked (pole replacement required, estimated 6 months). These two systems are disconnected. The project manager switches between the design tool (to understand what needs to be built) and the spreadsheet (to understand what can be built) and manually reconciles. For a deployment with 10,000 poles across 3 pole owners, the make-ready spreadsheet has 10,000 rows with status columns for each pole owner — a document so large it's difficult to maintain accurately.

## What Already Exists
3-GIS and Vetro FiberMap maintain the fiber network design with pole locations, span data, and construction method (aerial/underground). Katapult Engineering handles pole loading analysis and submits applications to pole owners. What's missing is a status tracking layer that connects pole-level make-ready status back to the construction-segment level in the design tool.

## The Customization Gap
A make-ready tracking module integrated into the fiber design platform that: (1) tracks every pole attachment application with status (submitted, engineering review, permit issued, make-ready construction scheduled, make-ready complete, inspected) per pole owner; (2) aggregates pole-level status to segment-level readiness — a construction segment is "ready" only when all poles in the segment have completed make-ready; (3) visualizes construction readiness on the fiber design map — color-coded segments showing ready (green), pending (yellow), blocked (red); (4) forecasts segment readiness dates based on pole owner processing time patterns — "Pole Owner A averages 45 days from application to completion, with 90th percentile at 90 days"; and (5) generates construction-ready segment lists that feed into the project manager's weekly construction planning.

## Target Customer
Fiber ISPs and construction contractors using 3-GIS or Vetro FiberMap for design who currently maintain separate make-ready tracking spreadsheets. 3-GIS and Vetro as platforms seeking to expand from design into construction management.

## Impact If Solved
Eliminates the 10,000-row make-ready tracking spreadsheet that is the bane of every fiber project manager's existence. Provides real-time visibility into construction readiness across the deployment area. Reduces construction delays caused by crews arriving at segments where make-ready is incomplete (currently 10-15% of scheduled work days). Enables predictive construction planning based on forecasted make-ready completion.
