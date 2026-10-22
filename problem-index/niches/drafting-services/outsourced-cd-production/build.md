# Outsourcing Readiness Scoring for a Markup Package

**Niche:** [[niches/drafting-services/outsourced-cd-production/profile|Outsourced Construction Document Production]]
**Industry:** [[industries/drafting-services|Drafting Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A design firm sends work out without knowing whether the package is clear enough to be drawn by someone who cannot ask questions, and finds out when it comes back wrong.
**Tags:** #transformers #large-language-models #gradient-boosting #object-detection #evaluation-metrics #workflow-orchestration
**Contested on:** *Not terminal as stated.* The honest partial sentence is "every serious competitor is fighting to produce an architect's or engineer's construction documents for less than the firm's own staff cost", but it yields two contests with different winners: one-off per-sheet overflow sets, won on turnaround and clarification rounds, and dedicated offshore production teams, won on retaining a trained team inside one firm's standards. Decomposed into contested sub-niches below.

## The Problem
Whether outsourcing saves money depends less on the bureau's rate than on the package. A clean, complete markup package on a firm template comes back right first time; an ambiguous one comes back wrong, takes two more rounds and costs the project architect more review time than drawing it themselves. Firms decide what to send out by habit, and nobody measures which packages are suitable.

## Why Nobody Has Built This
Bureaus have no incentive to tell clients a package is unready, and firms do not record how outsourced packages performed. The signal sits in the email trail between the two.

## What to Build
A pre-send check that reads the markup package — clouds, notes, referenced sheets, missing references, unresolved "coordinate with" notes — and scores how likely it is to come back right without questions, listing the items most likely to cause a round trip. It learns from the firm's own history of packages sent and rounds needed.

## Target Customer
Operations directors and BIM managers at architecture and engineering firms with 20 or more staff that outsource regularly.

## Impact If Built
Fewer wasted rounds, better choices about what to outsource, and a measurable outsourcing return instead of a rate comparison.
