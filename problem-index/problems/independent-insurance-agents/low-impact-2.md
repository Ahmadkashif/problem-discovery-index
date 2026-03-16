# Renewal Review and Re-Marketing Trigger Identification

**Industry:** [[independent-insurance-agents|Independent Insurance Agents]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Account managers discover problematic renewals reactively when carrier notices arrive instead of proactively flagging accounts that need re-marketing 120+ days out.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #revenue-impact

## The Problem
Independent agencies manage hundreds to thousands of policies across dozens of carriers, each with different renewal timelines. Account managers currently rely on AMS renewal reports — a flat list of policies expiring in the next 60-90 days — to identify which accounts need attention. But this list treats every renewal equally: a loyal client with flat rates gets the same flag as an account where the carrier has been increasing rates 15% annually and is likely to non-renew. By the time the renewal notice arrives with a 25% rate increase or non-renewal, there are only 45-60 days to re-market — not enough time for complex commercial accounts that require multiple submissions and underwriting reviews.

## What Already Exists
Every AMS (Applied Epic, Vertafore, HawkSoft) generates basic renewal lists sorted by expiration date. Some agencies use spreadsheet-based workflows or Kanban boards (Trello, Monday.com) to track renewal status. Agency consulting firms recommend "120-day renewal workflows" but the trigger logic is manual: someone has to look at each account and decide if it needs re-marketing based on memory of past interactions and rate history.

## The Customisation Gap
The missing layer is predictive triage: a model that scores each upcoming renewal on re-marketing urgency based on rate trajectory (3-year premium trend), loss ratio with current carrier, carrier's recent appetite shifts in this class/geography, account profitability to the agency (commission vs. servicing cost), and client retention risk signals (complaints, coverage gaps, competitor quotes requested). Generic CRM scoring models don't understand insurance-specific signals like combined ratio trends, carrier market cycle positioning, or the relationship between loss history and renewal pricing. The model needs to ingest AMS policy data, carrier loss runs, and historical renewal outcomes to learn which accounts actually got re-marketed vs. renewed in place.

## Impact If Solved
Shifts re-marketing from a 60-day reactive scramble to a 120-day proactive pipeline. Agencies retain 5-10% more revenue by catching at-risk accounts early enough to find competitive alternatives, and account managers spend their time on the 20% of renewals that actually need intervention rather than reviewing 100% manually.
