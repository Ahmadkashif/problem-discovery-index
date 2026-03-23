# Poetry Contest and Reading Period Management Platform

**Niche:** [[niches/independent-publishers/poetry-chapbook-publishers/profile|Poetry & Chapbook Publishers]]
**Industry:** [[industries/independent-publishers|Independent Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No platform manages the full poetry contest lifecycle — submission intake with fee processing, anonymous first-round reading by rotating screeners, judge coordination, winner notification, and publication pipeline handoff.
**Tags:** #workflow-orchestration #automation #quick-win

## The Problem
Poetry contests are a primary revenue and acquisition channel for chapbook and full-length poetry publishers. A typical contest receives 300–1,500 entries at $20–$30 each, generating $6K–$45K in fees that subsidize publication costs. The management overhead is enormous: collect entries (Submittable handles this part), anonymize manuscripts for blind reading, assign first-round readers (often volunteers or interns), track reader progress, collect scores, advance finalists to the final judge, notify the winner, send personalized rejections to everyone else, and transition the winning manuscript into the production pipeline. Most presses manage this in a combination of Submittable, Google Sheets, and personal email — a 100+ hour process for a single contest.

## Why Nobody Has Built This
The market is too small for Submittable (which earns per-submission fees and has no incentive to reduce the downstream labor). Poetry-specific platforms would serve perhaps 200–500 presses with annual revenue under $5K per customer. The workflow involves unpaid volunteers (first readers) who need the simplest possible interface, and distinguished judges (often famous poets) who need white-glove communication — opposite ends of the user experience spectrum. And the editorial norms vary: some contests use blind reading, others don't; some have two rounds, others three; some contests are for chapbooks (20–40 pages), others for full-length collections (48–80 pages).

## What to Build
A contest management layer (could sit atop Submittable's API or as standalone) that: (1) auto-anonymizes submissions by stripping identifying information, (2) distributes manuscripts to first-round readers with configurable batches and scoring rubrics, (3) tracks reader progress with automatic reminders, (4) advances top-scoring manuscripts to the final round, (5) manages judge communication and timeline, (6) generates personalized result notifications (winner, finalists, general rejections) with customizable templates, and (7) transfers the winning manuscript metadata and file to the production workflow. Priced at $50–$100/month or per-contest at $200–$500.

## Target Customer
Editor-publishers at poetry and chapbook presses who run 1–4 contests per year receiving 300–1,500 submissions each.

## Impact If Built
Reduces contest management time from 100+ hours to 20 hours per contest. Enables presses to run additional contests (increasing revenue by $10K–$30K) without proportional time investment. Eliminates the 5–10% of submissions mishandled (lost in email, never read, anonymization failure) that damage the press's reputation.
