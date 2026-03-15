# Project Scoping and SOW Generation from Client Briefs

**Industry:** [[marketing-agencies-smb|SMB Marketing Agencies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic PM tools track tasks once scoped, but can't estimate that a "rebrand package" for a 3-location dental practice will take 47 hours across design, copy, and web — so agencies underbid by 20-30% and absorb the margin hit.
**Tags:** #gradient-boosting #regression #tabular-ml #workflow-orchestration

## The Problem
When a prospective client sends a brief — "We need a new website, SEO, and social media management" — the agency owner or strategist has to decompose that into specific deliverables, estimate hours per deliverable, assign appropriate team members, price the engagement, and generate a statement of work. This process takes 3-8 hours per proposal and relies almost entirely on the estimator's memory of similar past projects. Agencies that track time (fewer than half do consistently) have historical data but never analyze it systematically. The result is chronic under-scoping: 60% of agency owners report that scope creep is their top profitability problem, and the average agency operates at 10-15% net margins when 25-30% should be achievable.

## What Already Exists
Monday.com, Asana, ClickUp, and Teamwork handle task management and time tracking. Proposify and PandaDoc generate polished proposals and SOWs with e-signature. HubSpot CRM tracks the sales pipeline. Some agencies use Harvest or Toggl for time tracking that feeds into invoicing.

## The Customisation Gap
No existing tool connects historical time-tracking data to new project estimation. An agency-specific scoping engine would ingest past project data (deliverable type, client industry, client size, complexity indicators, actual hours logged vs. estimated), train a regression model on the agency's own history, and when a new brief arrives, decompose it into deliverables with confidence-weighted hour estimates. The SOW would auto-generate with line items, pricing tiers, and a risk flag for deliverables where the agency's historical variance is high ("Website redesign projects for multi-location businesses have ranged from 35-80 hours — consider a phased approach"). This turns a 6-hour guessing exercise into a 45-minute review-and-refine workflow.

## Impact If Solved
Agencies reduce under-scoping incidents by 40-50%, recovering 5-8 percentage points of net margin. Proposal turnaround drops from 5-7 days to 1-2 days, improving close rates by 15-20% since speed-to-proposal correlates strongly with SMB buying decisions.
