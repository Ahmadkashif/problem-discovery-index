# Subcontractor Performance Scoring and Bid Analysis

**Industry:** [[general-contractors|General Contractors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic vendor management tools track contact information and certifications, but subcontractor performance in construction requires scoring based on field-specific outcomes — schedule compliance, change order rates, quality defect rates, and response time — that no generic vendor management tool is designed to capture.
**Tags:** #gradient-boosting #ranking #tabular-ml #automation

## The Problem
Subcontractor selection is one of the highest-stakes decisions in GC project management. A mechanical sub that underperforms — consistently late, generating excessive change orders, doing rework — can delay a project by weeks and erode an entire project's margin. Yet most GCs maintain subcontractor records informally: a list of contacts, perhaps some notes about past performance, and the collective memory of the senior project managers who have worked with those subs before. When a new project manager is assigned a project, they inherit relationships they didn't build and have no systematic way to evaluate which subs are actually the most reliable performers for the specific trade and project type.

## What Already Exists
Procore has a subcontractor directory and can log bid history. Vet the Sub and similar services provide subcontractor license, insurance, and bonding verification. BuildingConnected (now Autodesk) has a bid management platform that tracks which subs bid on which projects. None of these systems score subcontractors on actual performance metrics — schedule adherence, change order rates, quality outcomes, RFI response times — because that data lives in different parts of the project management system and isn't aggregated or scored.

## The Customisation Gap
A subcontractor performance scoring system for GCs needs to: aggregate performance signals from the project management system (on-time completion rates, change order ratio vs. original scope, punchlist item counts, documented deficiencies, RFI response time); weight these signals by the type of work (mechanical subs are evaluated differently than finishes subs) and project type (a sub excellent on residential may struggle on commercial); present a performance dashboard and a bid evaluation score that adjusts the bid price for historical performance risk (a sub bidding 5% under the next competitor but with a 15% historical change order rate is not actually cheaper). The construction-specific performance metrics and the trade-specific weighting are the customization that generic vendor management tools don't provide.

## Impact If Solved
Reduces subcontractor-related project overruns — estimated to contribute to 40-60% of GC margin leakage on complex projects. Enables data-driven subcontractor selection that outperforms relationship-based selection at scale, particularly as firms grow and project managers can't personally know every sub on the roster.
