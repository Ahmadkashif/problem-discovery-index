# Answer-Date Extraction That Cannot Fail Silently

**Niche:** [[niches/legal-support-services/sop-receipt-forwarding/profile|Service-of-Process Receipt & Forwarding]]
**Industry:** [[industries/legal-support-services|Legal Support Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The one field that matters on a served document is the date a response is due, and it is computed by hand from the court, the service method and fifty states' rules.
**Tags:** #large-language-models #transformers #seq2seq #evaluation-metrics #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to read every served document correctly — entity, court, case type, answer date — and put it in front of the right lawyer the same day, and whoever never lets a served suit become a default takes the account.

## The Problem
Response periods differ by court, document type and how service was made; some run from service, some from mailing, some are stated on the face and some are not. Intake staff read each document and enter a date that the client then relies on.

## Why Nobody Has Built This
Generic extraction tools treat dates as fields to read, not to compute; the stakes of a wrong date make agents reluctant to automate; and the rules engine must be maintained jurisdiction by jurisdiction.

## What to Build
A pipeline that classifies each served document, extracts court, parties, case number, service method and stated deadlines, computes the response date from a maintained rules engine, and assigns a confidence; anything below threshold or in conflict with the face of the document goes to a person, and nothing is forwarded without a date.

## Target Customer
Registered agents' SOP operations; legal operations teams at companies served frequently.

## Impact If Built
Faster forwarding, consistent deadlines and an audit trail showing how every date was derived.
