# Continued-Stay Review Packet Drafter on Synthetic Notes

**Niche:** [[niches/psychiatric-hospitals/managed-care-concurrent-review/profile|Managed-Care Concurrent Review of Psychiatric Days]]
**Industry:** [[industries/psychiatric-hospitals|Psychiatric Hospitals]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool reads a psychiatric patient's day of notes and drafts a cited continued-stay argument against the payer's criteria, and a two-week MVP can show it on synthetic notes.
**Tags:** #large-language-models #transformers #evaluation-metrics #automation #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to win payer approval at each concurrent review for the psychiatric days the record supports, and whoever ends the year with the lowest share of reviewed patient days denied takes the account.

## The Problem
Before every call the coordinator reads 10–20 pages of notes. Evidence that would win the day, such as an overnight restraint, a refused dose or a failed pass, is often in a nursing or technician note she has no time to read.

## Why Nobody Has Built This
Behavioral necessity is written in prose, and the acute-care tools score structured data. Real notes cannot leave the hospital for a pilot, which slowed vendors down; synthetic notes remove that barrier for a first build.

## What to Build
The MVP: write 30–50 synthetic patients' 7–14-day stays (progress, nursing, technician, medication and social work notes) with seeded evidence and contradictions. Build a criteria schema from a published outline, extract cited spans with an LLM, check recency, and draft a 250-word packet with each sentence linked to its note. Evaluate span recall against 200 annotated patient-days with near-zero invented citations. Production adds EHR connectors, licensed payer criteria and a ledger of requested, approved and denied days by payer (ml entry 2).

## Target Customer
UR directors at freestanding hospitals and chains; revenue cycle AI vendors (AKASA, Candid Health) adding a behavioral module.

## Impact If Built
If cited packets cut prep from ~30 to ~10 minutes and keep 1–2% more of ~19,000 reviewed days paid in a 100-bed hospital, that is ~4 coordinator hours a day and ~$190,000–$380,000 a year (estimate).
