# The Inherited Report Nobody Can Reconcile

**Niche:** [[niches/security-alarm-integrators/fire-alarm-itm/profile|Fire Alarm Inspection, Testing & Maintenance]]
**Industry:** [[industries/security-alarm-integrators|Security Alarm Integrators]]
**Type:** Fix (Pain Point)
**One-liner:** Winning a building's inspection contract from another contractor means inheriting a device list in someone else's format, and the first annual test becomes an expensive survey.
**Tags:** #large-language-models #transformers #seq2seq #quick-win #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to hold a building's NFPA 72 inspection contract by delivering an AHJ-accepted report with every deficiency priced, and whoever turns the most deficiencies into approved repairs before the fire marshal's correction deadline takes the account.

## The Problem
The previous contractor's report lists every device by its own naming, its own addresses and its own location descriptions. The new crew finds a different count on site, with devices renamed after a renovation, some added and some missing. Reconciling the two takes a day of technician time, and until it's done nobody can say whether last year's deficiencies were fixed.

## Why It's Still Broken
Reports are PDFs in every vendor's layout, and there is no common device schema. AHJ portals store submissions but not structured device lists, and the outgoing contractor has no reason to help.

## What a Fix Looks Like
LLM extraction of the inherited report into a structured device list, matched against the panel's programmed points and the as-built drawings, with differences flagged for the crew to confirm on the first walk. Last year's open deficiencies carry forward as tasks.

## Who Feels the Pain
Inspection crews doing survey work they aren't paid for; service managers who can't price a takeover accurately; and building owners who assume continuity they don't have.

## Impact If Fixed
Takeovers start with a working inventory, the first inspection is priced correctly, and inherited deficiencies stop disappearing between contractors.
