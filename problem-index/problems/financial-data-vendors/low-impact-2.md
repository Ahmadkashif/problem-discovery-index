# Earnings Call Transcription for Finance

**Industry:** [[financial-data-vendors|Financial Data Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** General-purpose speech recognition is excellent and still mishears ticker symbols, misattributes the analyst from the third bank to ask a question, and cannot tell guidance from commentary.
**Tags:** #transformers #seq2seq #large-language-models #bert #evaluation-metrics #transfer-learning #automation #quick-win

## The Problem
During earnings season thousands of calls happen in a few weeks, clustered at the same hours. Clients — buy-side analysts, sell-side analysts, quant teams running NLP signals — expect a near-real-time transcript during the call and a corrected final transcript within hours, with every speaker identified by name, title and firm, the prepared remarks separated from Q&A, and numbers rendered exactly as spoken.

Vendors run mixed pipelines: automatic speech recognition for the live draft, human editors for the corrected version. The editing load spikes with the earnings calendar and is staffed accordingly.

## What Already Exists
Commodity ASR (Whisper-class open models, Deepgram, AssemblyAI, the cloud providers' services) produces strong general transcripts and basic diarisation. FactSet CallStreet, LSEG StreetEvents, S&P Global, Bloomberg, Aiera and Quartr all sell transcripts, and several have built custom models.

## The Customisation Gap
The finance-specific errors are the ones that matter. Company names, product names, drug compounds and non-GAAP metric names are out-of-vocabulary; "EBITDA" and "ARR" survive but a mid-cap's proprietary KPI does not. Numbers are spoken loosely ("one-two-five basis points," "a buck twenty") and must be normalised exactly. Diarisation must resolve to a named analyst at a named broker, which requires the call's participant list, the operator's introductions and a directory of covering analysts — none of which generic tools ingest. And the structural layer clients pay for — segmenting prepared remarks, Q&A turns, and statements of forward guidance — is a domain-specific classification task.

The customisation is a vocabulary built from the issuer's own filings and prior calls, a speaker-resolution model fed by the vendor's analyst directory, and a guidance and KPI tagger trained on the vendor's own edited-transcript archive, which is years of human corrections against machine drafts.

## Impact If Solved
Editor hours concentrated in the earnings peak are the cost line, and transcript latency and speaker accuracy are what clients compare vendors on. Domain adaptation of the recogniser and automatic speaker resolution move editors from correcting every line to reviewing flagged segments.
