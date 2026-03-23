# Cross-Advisor Client Knowledge Graph

**Niche:** [[niches/wealth-management-rias/multi-advisor-ria-firms/profile|Multi-Advisor Ensemble RIA Firms]]
**Industry:** [[industries/wealth-management-rias|Wealth Management RIAs]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product captures and structures the relationship context, investment rationale, and behavioral insights that advisors accumulate about each client — the knowledge that disappears when an advisor leaves.
**Tags:** #bert #text-classification #nlp #tacit-knowledge-ml #revenue-impact

## The Problem
When an advisor at a multi-advisor RIA departs, they take with them years of context about each client: why a particular asset allocation was chosen (the client's father lost everything in 2008), which communication style works (this client wants data, that client wants stories), and what behavioral triggers to watch for (this client panics when tech stocks drop 10%). CRM notes capture fragments, but the structured relationship intelligence that enables another advisor to seamlessly serve the client does not exist in any system.

## Why Nobody Has Built This
The knowledge is generated during conversations, not data entry sessions. Advisors do not naturally document "this client responds well to historical analogies about market recoveries" — they just know it and act on it. Building a knowledge graph requires passively capturing conversation content (meeting transcripts, email threads, call notes), extracting structured relationship attributes using NLP, and organizing them into a queryable format per client. The privacy and compliance constraints of recording client conversations add regulatory friction.

## What to Build
An NLP pipeline that ingests meeting transcripts (from Zoom/Teams recordings with client consent), email threads, and CRM notes, then extracts and maintains a structured client profile: communication preferences, investment rationale history, behavioral risk triggers, life event timeline, and relationship strength indicators. When a client is reassigned, the receiving advisor gets a comprehensive "client brief" that captures years of relationship context in a 10-minute read.

## Target Customer
COOs and managing partners at 5-20 advisor RIA firms who lose 5-15% of AUM during advisor transitions because the new advisor lacks relationship context.

## Impact If Built
Firms retain an additional 10-20% of at-risk AUM during advisor transitions — for a firm managing $500M, this translates to $50-100M in preserved assets and $500K-$1M in annual revenue per transition event.
