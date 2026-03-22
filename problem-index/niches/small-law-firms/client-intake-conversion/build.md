# AI Legal Intake Screening Agent

**Niche:** [[niches/small-law-firms/client-intake-conversion/profile|Client Intake & Lead Conversion]]
**Industry:** [[industries/small-law-firms|Small Law Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every call and web inquiry is answered instantly by an AI agent that qualifies the lead, captures case facts, checks for obvious conflicts, and schedules a consultation — so the attorney never loses a viable client to voicemail again.
**Tags:** #large-language-models #transformers #attention-mechanisms #bert #transfer-learning #evaluation-metrics #ai-agent #revenue-impact

## The Problem
Small firm attorneys miss 30-50% of incoming calls because they're in court, in meetings, or with other clients. Each missed call is a potential client who will call the next attorney on their list within minutes. Virtual receptionists answer the phone but can only take a message — they can't assess whether the caller has a viable legal matter, whether it's within the firm's practice areas and jurisdiction, or whether the statute of limitations is approaching. By the time the attorney returns the call hours later, the client has already retained someone else.

## Why Nobody Has Built This
Legal intake requires domain-specific qualification logic that varies by practice area (PI firms need to assess liability and injury severity; family law firms need to assess jurisdiction and conflict; criminal defense needs to assess charge severity and court date urgency). Building a general-purpose legal intake agent requires encoding qualification criteria across 10+ practice areas. LLM capability to handle nuanced legal conversations at intake quality is only recently achievable.

## What to Build
A voice and web AI agent that: answers calls/web inquiries 24/7, conducts a structured intake conversation (practice area identification, basic fact gathering, jurisdiction check, urgency assessment), scores the lead quality, checks for obvious conflicts against the firm's client list, schedules a consultation on the attorney's calendar, and delivers a structured intake summary to the attorney before the consultation. The agent is configured per firm with their practice areas, jurisdictions, and qualification criteria.

## Target Customer
Solo attorneys and small firms (2-5 attorneys) spending $2,000-$5,000/month on marketing who are losing 30-50% of leads to missed calls and slow follow-up.

## Impact If Built
Converts 15-25% more leads into consultations by eliminating response delay. Each additional retained client represents $3,000-$50,000 depending on practice area and fee structure. Pays for itself with 1-2 additional retained clients per month.
