# Real-Time Speech and Assistance Infrastructure

**Niche:** [[niches/customer-support-platforms/voice-contact-centre/profile|Voice Contact Centre]]
**Industry:** [[industries/customer-support-platforms|Customer Support Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Real-time transcription, intent recognition and retrieval are commodity infrastructure priced in fractions of a cent, and a large share of contact centres still run an agent with a knowledge search box and a note pad.
**Tags:** #transformers #seq2seq #attention-mechanisms #large-language-models #evaluation-metrics #confidence-intervals #automation #worker-facing
**Contested on:** Every serious competitor in voice support is fighting to resolve a caller's issue without a human while they are on the line, and to make the agent faster when a human is needed — and whoever raises containment without raising repeat calls takes the account.

## The Problem
An agent takes a call, listens, forms an understanding, searches the knowledge base while the customer waits, reads, answers, and then spends two minutes after the call writing a summary. Streaming transcription, intent classification and grounded retrieval could have surfaced the relevant answer before the customer finished describing the problem, and the summary could have been drafted from the transcript. Both capabilities are commodity and unevenly deployed, and after-call work in particular is a substantial share of total handle time that nobody has attacked.

## What Already Exists
Streaming speech recognition at production quality is available from every major provider and as open weights, with latency suitable for real-time use. Intent classification, entity extraction and retrieval are commodity. Summarisation is trivial. Agent assist products from the platform vendors and specialists package all of it. Nothing in the stack requires development; the gap is deployment breadth and the quality of the adaptation.

## The Customization Gap
The adaptation is to a live call with a person waiting. It requires: (1) latency budgets that make assistance useful rather than distracting, since a suggestion arriving after the agent has already answered is noise and the interface must degrade gracefully rather than interrupt; (2) domain-adapted recognition for product names, account identifiers and the specific vocabulary of the business, which is where generic transcription fails and where the failures are on the words that matter; (3) after-call summarisation as the highest-value single application, since it is a large share of handle time, requires no real-time performance, and the agent reviews rather than writes — which is the fastest deployment with the clearest return; (4) grounding in the customer's own account state rather than only in the knowledge base, because most voice questions are about this customer's situation and a generic answer is why they called; and (5) an explicit position on recording, consent and retention, which in voice is a legal matter varying by jurisdiction and is the same issue the conversation intelligence niche in CRM describes.

## Target Customer
Contact centre platform vendors, agent assist specialists, and the operations leaders whose handle time is dominated by search and after-call work.

## Impact If Solved
After-call summarisation alone removes a substantial share of handle time with no real-time risk and is the obvious first deployment. Account-state grounding is the adaptation that makes real-time assistance genuinely useful rather than a knowledge search with extra steps, since the caller's question is nearly always about themselves.
