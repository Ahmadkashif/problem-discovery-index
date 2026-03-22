# Lightweight Mobile-First Electrical Service Management

**Niche:** [[niches/electrical-contractors/small-rural-electricians/profile|Small & Rural Electricians]]
**Industry:** [[industries/electrical-contractors|Electrical Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A phone-only business management tool — scheduling, estimates, invoices, customer records, and NEC code reference — built for a one-person electrical shop that does everything from the truck, priced at $50-100/month instead of $400+/month for enterprise field service platforms.
**Tags:** #large-language-models #automation #workflow-orchestration #worker-facing #revenue-impact

## The Problem
A rural electrician's day looks like this: wake up, check the spiral notebook for today's appointments, drive 30 minutes to the first job, diagnose the problem, write a handwritten estimate, do the work, write a handwritten invoice or tell the customer "I'll send you a bill," drive 45 minutes to the next job, repeat. At the end of the month, they sit at the kitchen table for 3-4 hours entering invoices into QuickBooks. They forget to bill for small jobs. They can't find the notes from a service call three months ago when the customer calls back. They don't know their actual revenue by job type. They carry a 2,000-page NEC codebook in the truck for reference. Every minute spent on paperwork is a minute not spent on billable work — and for a one-person shop, that administrative burden consumes 8-12 hours per week.

## Why Nobody Has Built This
The unit economics of serving one-person shops are challenging: at $50-100/month per user with minimal upsell potential, you need tens of thousands of users to build a viable business. ServiceTitan and Housecall Pro went upmarket for this reason — higher ARPU, larger accounts, more expansion revenue. The remaining tools (Jobber, Invoice2go, Joist) try to serve small shops but are designed around a dispatcher-technician separation that doesn't exist in a one-person operation. Building for this market requires extreme simplicity — the electrician must be able to create an estimate, convert it to an invoice, and collect payment in under 2 minutes on a phone screen while standing in a customer's garage.

## What to Build
A mobile-native app (no web dashboard needed, no desktop version) with five core functions: (1) Schedule — calendar view of upcoming jobs with customer name, address, and job notes, synced from text messages and phone calls via an LLM that parses incoming customer communications ("Can you come look at my panel next Tuesday?") into scheduled appointments; (2) Estimate — voice-to-estimate: the electrician describes the scope ("200A panel upgrade, new 50A circuit for EV charger, 6 new outlets in the garage") and the system generates a line-item estimate with material costs pulled from distributor pricing and labor calculated from configurable hourly rates; (3) Invoice — one-tap convert estimate to invoice, accept payment via integrated card reader or text-to-pay link; (4) Customer records — searchable history of every job, estimate, and invoice per customer, auto-generated from the estimate/invoice flow; (5) NEC reference — searchable NEC code with plain-language explanations, accessible offline for rural areas with no cell service.

## Target Customer
Owner-operator electricians in rural and small-town markets doing $100-400K in annual revenue, currently using paper + QuickBooks or no system at all. The US has approximately 25,000-30,000 one-person electrical shops, and fewer than 10% use any field service management software.

## Impact If Built
Recovers 8-12 hours per week of administrative time (estimate creation, invoice entry, record keeping), adding 4-6 billable hours at $75-150/hour — worth $15K-45K in additional annual revenue. Eliminates forgotten invoices (rural electricians estimate they fail to bill for 5-10% of small jobs). Provides the first-ever searchable job history for troubleshooting return visits.
