# Client Emotional Communication Overload Triage

**Niche:** [[niches/small-law-firms/family-law-practices/profile|Family Law Practices]]
**Industry:** [[industries/small-law-firms|Small Law Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Family law clients in active divorce proceedings send 50+ emails and texts per week — no triage system exists to separate genuinely urgent legal matters from emotional venting, causing attorneys to spend 10-15 hours weekly on communications that don't advance the case.
**Tags:** #bert #transformers #attention-mechanisms #large-language-models #worker-facing #automation #tacit-knowledge-ml

## The Problem
A family law attorney with 15 active contested divorces receives 200-400 client communications per week. Most are emotionally charged messages about the opposing spouse's behavior, complaints about the pace of proceedings, anxiety about financial outcomes, or detailed accounts of conflicts during custody exchanges. Perhaps 10-15% contain information that is legally actionable or time-sensitive: "my spouse just moved assets to a new account," "I was served with an emergency motion," "my child told me about abuse during the last visit." The attorney must read every message because burying a genuine emergency in 40 emotional emails is the norm, not the exception. Experienced family law attorneys develop tacit pattern recognition — they can scan the first line of a message and know whether it requires action or acknowledgment — but this skill takes years to develop and fails under volume pressure.

## Why It's Still Broken
Generic email triage tools (SaneBox, priority inbox) classify by sender and metadata, not by legal content. A client's 47th email of the week might be the one that mentions the spouse hiding assets. The legal urgency of a message is embedded in its content, not its metadata. Building a family-law-specific triage system requires a model that understands legal concepts (emergency motions, asset dissipation, custody violations, domestic violence escalation) and can distinguish between a client expressing fear about a hypothetical outcome and a client reporting an event that requires immediate legal action. The training data challenge is significant: attorney-client communications are privileged, so labeled datasets don't exist in the public domain.

## What a Fix Looks Like
A communication triage layer that sits between client messages and the attorney's inbox, using a fine-tuned BERT model to classify each message on two dimensions: (1) legal urgency (action required / informational / emotional processing) and (2) topic category (financial, custody, procedural, personal). Urgent messages (mentions of court filings, asset movement, safety concerns, deadlines) are surfaced immediately with a summary of the actionable content. Informational messages are batched for daily review. Emotional processing messages receive an immediate acknowledgment ("received, reviewing") and are queued for weekly batch response. The attorney sees a prioritized dashboard instead of a chronological inbox. The model improves as the attorney's triage decisions (responded immediately vs. batched) become implicit labels.

## Who Feels the Pain
The family law attorney who answers emails at 11pm because they're afraid of missing an emergency buried in 50 emotional messages, and whose personal relationships and mental health suffer from the constant emotional absorption of client trauma.

## Impact If Fixed
Reduces attorney communication time from 10-15 hours/week to 3-5 hours/week by eliminating redundant reading of non-actionable messages. Eliminates the anxiety of potentially missing urgent client communications. Improves response time for genuinely urgent matters from hours (buried in queue) to minutes (surfaced by triage). Reduces family law attorney burnout — the #1 driver of attrition in family law practice.
