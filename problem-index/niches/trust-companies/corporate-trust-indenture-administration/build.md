# An Obligations Map Across the Trusteeship Book

**Niche:** [[niches/trust-companies/corporate-trust-indenture-administration/profile|Corporate Trust & Indenture Administration]]
**Industry:** [[industries/trust-companies|Trust Companies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A corporate trustee holds thousands of indentures and cannot query them: which deals require a notice within ten days of an event, which let 25% of holders direct the trustee, which require an annual certificate the issuer has not sent.
**Tags:** #large-language-models #transformers #bert #evaluation-metrics #compliance #workflow-orchestration
**Contested on:** *Not terminal as stated.* The honest partial sentence is that corporate trustees compete to administer indentures without taking on liability they did not price, but in performing structured deals that means computing every payment-date waterfall and report correctly on a fixed monthly clock, while in defaulted issues it means acting only on proper holder direction with indemnity and notice. Different teams, clocks and winners. Decomposed into contested sub-niches below.

## The Problem
Each trusteeship's duties sit in a long indenture plus supplements. Relationship managers know their own deals; nobody can answer a question across the book, such as which issues are affected by a new rule, which issuers owe compliance certificates this month, or which deals have unusual trustee duties that raise liability.

## Why Nobody Has Built This
Indentures look standard but vary in exactly the provisions that matter, and extracting them reliably was not feasible before long-document language models. Trustees also treat documents as legal records rather than data.

## What to Build
An extraction layer that turns every indenture and supplement into structured obligations — events of default, cure periods, notice timetables, holder direction and consent thresholds, indemnity conditions, reporting deliverables, payment mechanics — with citations, feeding a calendar and a queryable book. It serves both the structured reporting team and the default team described in the sub-niches.

## Target Customer
Heads of corporate trust and corporate trust risk at the large trustees.

## Impact If Built
Missed deliverables and notices are caught before they become liability, new-business acceptance can price unusual duties, and a question that now takes weeks of file review takes minutes.
