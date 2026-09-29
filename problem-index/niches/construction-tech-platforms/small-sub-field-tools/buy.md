# Messaging as the Interface Instead of an App

**Niche:** [[niches/construction-tech-platforms/small-sub-field-tools/profile|Small Subcontractor Field Tools]]
**Industry:** [[industries/construction-tech-platforms|Construction Tech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Small construction crews already coordinate entirely through group text messages, which is a deployed, adopted, universally understood interface, and every vendor's response has been to ask them to install an app instead.
**Tags:** #large-language-models #bert #transformers #evaluation-metrics #confidence-intervals #workflow-orchestration #automation #worker-facing
**Contested on:** Every serious competitor selling to small subcontractors is fighting to let a foreman with dirty hands and a phone record what happened in under a minute, from a site with no signal — and whoever gets that interaction shortest takes the account.

## The Problem
A subcontractor's real project management system is a group message thread per job. Photos, material requests, schedule changes, questions, and end-of-day summaries all flow through it, from everyone, with no friction and total adoption. It has no structure, no search that works, no connection to job costing, and it disappears into a phone. Every vendor selling to this segment asks the crew to abandon a tool with 100% adoption for one with 30%, and then reports poor engagement.

## What Already Exists
Messaging infrastructure is a commodity: the business messaging APIs, WhatsApp Business, and SMS gateways are cheap, reliable and require no installation. Language models capable of reading an unstructured thread and extracting events, quantities, requests and issues are ordinary now and cheap at this volume. Photo handling through messaging is native. Every component needed to treat a message thread as a structured data source is purchasable off the shelf.

## The Customization Gap
The adaptation is to read the thread rather than replace it. It requires: (1) extraction tuned to how construction crews actually write — abbreviations, trade slang, partial sentences, photos with a two-word caption — which is where generic extraction underperforms badly and where a domain-tuned model earns its place; (2) resolving messages to job, area and crew from context rather than asking the sender to tag anything, since any tagging requirement recreates the friction the thread avoids; (3) confirming only what matters, by replying in-thread with a single question when an extracted quantity or a material request is ambiguous, which fits the medium instead of fighting it; (4) pushing structure outward — a material request becomes a purchase order draft, a schedule note becomes a calendar change, a quantity becomes a job cost entry — so the owner gets the system of record while the crew keeps the thread; and (5) treating the thread as the system of record for the crew and the database as the system of record for the office, rather than trying to make one serve both.

## Target Customer
Subcontractors of 5-50 people already coordinating by group message, and the vendors who have failed to displace that thread and could read it instead.

## Impact If Solved
Adoption stops being the problem, because there is nothing to adopt. The owner gets structured job data from a communication pattern that is already universal, at the cost of no behaviour change at all, which is the only path to data in this segment that has ever worked. The extraction quality is the risk and is measurable per message class, so the product can be honest about what it captures and what it misses.
