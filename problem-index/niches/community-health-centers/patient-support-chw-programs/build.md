# An Outreach Queue That Learns From the Worker's Own Calls

**Niche:** [[niches/community-health-centers/patient-support-chw-programs/profile|Patient Support Services & Community Health Worker Programmes]]
**Industry:** [[industries/community-health-centers|Community Health Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Experienced community health workers know which patients are about to disappear, but their outreach lists are sorted by last visit date and their judgement leaves with them.
**Tags:** #tacit-knowledge-ml #gradient-boosting #survival-analysis #transformers #causal-inference #worker-facing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to keep a health center's high-risk patients in care through outreach, transport, interpretation and case management, and whoever keeps the largest share of a care team's high-risk panel with a kept visit inside its clinical interval takes the account.

## The Problem
A worker with ~100 high-risk patients (estimate) chooses whom to call each day by feel. The center cannot tell which choices paid off, and a new hire starts from a list.

## Why Nobody Has Built This
Gap-list vendors rank by measure status, not by drop-out risk. The worker's prioritisation is not captured as data, and her outreach prevents the very outcomes that would label it. Outcomes sit in pharmacy, eligibility and hospital feeds the center receives irregularly.

## What to Build
A structured outreach log drafted from call records and notes, with a one-tap worry rating. A survival and uplift model, trained on that log and on outcomes (kept visit within interval, next reading, coverage at renewal, emergency visits), puts each morning's three to five patients the worker would not have picked at the top of her queue, each with the reason. Detailed in the industry's high-impact problem and ml entry 1.

## Target Customer
Multi-site centers and FQHC-led networks with 10+ CHWs and case managers.

## Impact If Built
Keeping ~500 more chronic patients in care for three extra visits a year is ~1,500 visits, or ~$300,000–$450,000 of PPS revenue for a 20,000-patient center (estimate), plus measurable movement in hypertension and diabetes control.
