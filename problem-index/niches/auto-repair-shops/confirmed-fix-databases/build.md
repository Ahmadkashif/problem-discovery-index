# Hotline Transcripts as a Diagnostic Reasoning Corpus

**Niche:** [[niches/auto-repair-shops/confirmed-fix-databases/profile|Confirmed-Fix Diagnostic Knowledge Databases]]
**Industry:** [[industries/auto-repair-shops|Auto Repair Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Decades of recorded hotline calls contain master technicians reasoning aloud through diagnoses that beat everyone else in the trade, and the only thing extracted from each call is the final answer.
**Tags:** #large-language-models #transformers #bert #transfer-learning #word-embeddings #contrastive-learning #evaluation-metrics #tacit-knowledge-ml #data-integration #worker-facing

## The Problem
The database records outcomes: this symptom on this vehicle, root cause was this. That is valuable and it is the thin end of what the calls actually contain. On the call, a master technician takes a stuck technician's description, asks a specific sequence of questions, rules things out in a particular order, and explains why. The reasoning — which discriminating test to run first, which symptom combination makes a common cause unlikely, what to check before condemning an expensive part — is the expertise. It is spoken, recorded, and then reduced to a one-line fix record. What the subscriber gets is an answer with no path to it, which works when their vehicle matches the record and is useless when it nearly matches. Meanwhile the hotline specialists who hold the reasoning are a small, ageing, and irreplaceable group, and the company's succession plan for their knowledge is the same one-line records.

## Why Nobody Has Built This
Call audio was retained for quality assurance rather than as content, so it sits in telephony archives disconnected from the fix records it produced, often without reliable linkage to vehicle or case. Speech in a working shop environment is difficult — background noise, heavy trade shorthand, part names and codes spoken as fragments — and generic transcription degrades badly on exactly the technical terms that carry the meaning. And the organizational view has been that the database is the product and the call is the delivery mechanism, which gets the value backwards but has been true enough operationally that nobody challenged it.

## What to Build
An engine that treats the call archive as the primary corpus and the fix record as its index. Calls are transcribed with a domain-adapted model trained on trade vocabulary, part nomenclature, and code formats, then linked to the case and vehicle they concern. Each call is structured into its diagnostic elements: the presenting symptoms as described, the questions asked and what they ruled out, the tests recommended in order, the reasoning stated, and the confirmed outcome. That produces something the database has never contained — diagnostic paths rather than diagnostic answers. A subscriber whose vehicle nearly matches a prior case gets the sequence of discriminating tests rather than a conclusion that may not apply. Across the corpus, the accumulated paths make the specialists' method inspectable: which tests actually discriminate, where the trade's common assumptions are wrong, and which symptom presentations most often lead to a misdiagnosis and an unnecessary part.

## Target Customer
VPs of content and directors of diagnostic services at confirmed-fix publishers running 100-400 specialists, and the hotline managers who know their most valuable people are retiring and have no mechanism for transferring what they know.

## Impact If Built
Converts a retiring workforce's expertise into an asset that stays. It also changes the product's competitive position: any competitor can accumulate symptom-to-fix pairs given enough subscribers, but the reasoning corpus can only be built by whoever ran the hotline, and it is what makes the difference on the cases that do not match cleanly — which are precisely the cases a technician calls about.
