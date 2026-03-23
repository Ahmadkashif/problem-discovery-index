# Subcontractor Coordination Failures on Complex Commercial Jobs

**Niche:** [[niches/insurance-restoration/commercial-industrial/profile|Commercial & Industrial Restoration]]
**Industry:** [[industries/insurance-restoration|Insurance Restoration]]
**Type:** Fix (Pain Point)
**One-liner:** Large commercial restoration jobs involve 5-15 specialty subcontractors (electrical, mechanical, roofing, flooring, painting) whose scheduling conflicts, scope overlaps, and documentation gaps delay projects by 30-60 days on average.
**Tags:** #workflow-orchestration #data-integration

## The Problem
A $2M commercial fire restoration might involve the restoration company (mitigation and project management), an electrician, a plumber, an HVAC contractor, a roofer, a drywall crew, painters, flooring installers, and specialty contractors (fire suppression, elevator repair, security systems). Each subcontractor has their own schedule, their own scope understanding, and their own documentation. The restorer/GC must coordinate sequencing (electrician must rough-in before drywall, HVAC before ceiling), prevent scope gaps (who is responsible for the fire-rated partition — drywall sub or fire suppression sub?), and ensure every sub's work is documented for the insurance estimate.

## Why It's Still Broken
Subcontractors on insurance restoration jobs work differently than on new construction — they're working from an insurance estimate (Xactimate line items), not a construction plan. The restorer assigns Xactimate line items to subs, but the mapping between Xactimate categories and trade responsibilities isn't always clear. Subs may complete work that isn't in the estimate (needing a supplement) or skip work they assumed another sub would handle. Communication happens through individual phone calls and texts — no shared project view exists for subs.

## What a Fix Looks Like
A subcontractor coordination platform designed for insurance restoration: maps Xactimate estimate line items to trade responsibilities (which sub handles which lines), creates a dependency-aware schedule that subs can view and update, tracks completion at the line-item level (not just trade-level), and flags scope gaps (line items not assigned to any sub) and scope overlaps (same line item assigned to multiple subs). Subs access their scope, schedule, and completion tracking via a mobile app without needing full access to the project management system.

## Who Feels the Pain
Restoration project managers who coordinate 5-15 subs through phone calls, spending 2-3 hours per day on scheduling and scope clarification. Subcontractors who arrive on-site to find their work can't proceed because the prerequisite trade hasn't completed.

## Impact If Fixed
Reduces average commercial restoration project duration by 20-30% through better sub coordination. Eliminates scope gaps that create $5,000-$20,000 in change orders per project. Saves the project manager 10-15 hours per week of coordination overhead.
