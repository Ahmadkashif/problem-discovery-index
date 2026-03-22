# Touch-Up vs. Repaint Decision Standardization

**Niche:** [[niches/painting-contractors/property-management-turns/profile|Property Management Turns]]
**Industry:** [[industries/painting-contractors|Painting Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** The decision to touch up a unit ($200-400) or fully repaint it ($800-1,200) is made subjectively by whoever walks the unit — producing inconsistent outcomes where identical conditions get different treatments depending on whether the PM, the painter, or the maintenance tech does the assessment.
**Tags:** #tacit-knowledge-ml #worker-facing #revenue-impact #cnns #gradient-boosting

## The Problem
When a tenant moves out, someone assesses the painting condition of each room: walls with a few nail holes and scuffs get touch-up; walls with heavy damage, multiple previous touch-up layers, smoke discoloration, or color changes get full repaint. This assessment drives a 3-4x cost difference per unit. The problem is that the assessment criteria are subjective and the assessor varies — sometimes it's the property manager (who defaults to touch-up to save money), sometimes the painter (who defaults to full repaint to make more money), and sometimes the maintenance tech (who has no painting expertise and guesses). Even when the same person assesses, their threshold shifts based on move-in urgency, budget pressure, and how many units they've already walked that day. The result: units in identical condition get different treatments across the portfolio, some touch-ups look terrible (visible patches where touch-up paint doesn't match the aged wall), and PMs lose trust in their painting contractors.

## Why It's Still Broken
There is no industry standard for the touch-up vs. repaint threshold. PDCA (Painting and Decorating Contractors of America) publishes surface prep standards for new work but nothing for maintenance/touch-up decisions. Paint manufacturers provide guidance on touch-up compatibility (same batch required for invisible touch-up) but don't address the condition assessment. The core challenge is that "this wall needs full repaint" depends on multiple interacting factors: number and size of damaged areas, age and condition of existing paint, color match between touch-up paint and aged wall paint, number of previous touch-up layers (each layer adds visible texture), surface sheen consistency, and the incoming tenant's expectations. Experienced turn painters integrate these factors instinctively; everyone else makes inconsistent calls.

## What a Fix Looks Like
A photo-based assessment tool where the assessor photographs each wall in the unit and the system classifies the recommended treatment: touch-up (isolated damage, recent paint, good color match expected), partial repaint (one or two walls need full coverage, others are fine), or full repaint (widespread damage, multiple touch-up layers, color change, or smoke/water discoloration). The CNN model is trained on thousands of before/after pairs — units where touch-up was performed and the result was acceptable vs. units where touch-up was performed and the result required a callback for full repaint. The key training signal is the callback: if a unit was touched up and then repainted within 30 days due to customer complaint, the original condition warranted full repaint. Over time, the model learns the threshold at which touch-up produces acceptable results vs. where it creates callbacks.

## Who Feels the Pain
Property managers who get tenant complaints about patchy touch-up jobs that looked "good enough" to the painter but not to the resident. Turn painters whose reputation suffers when PMs override their full-repaint recommendation and then blame them for the resulting poor touch-up. Maintenance techs who are asked to assess painting condition without the expertise to make the call.

## Impact If Fixed
Standardizes the touch-up/repaint decision across all assessors, reducing callbacks from touch-up failures by 50-70% ($200-500 per callback avoided). Optimizes painting spend by recommending touch-up where it will produce acceptable results and full repaint only where necessary — saving 15-25% of total turn painting costs through fewer unnecessary full repaints while avoiding callbacks from inappropriate touch-ups.
