# A Transcribability Check While the Hearing Is Fresh

**Niche:** [[niches/court-reporting-firms/court-transcript-production/profile|Court and Appeal Transcript Production]]
**Industry:** [[industries/court-reporting-firms|Court Reporting Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Courts that record digitally learn that a microphone was off or two lawyers spoke over a ruling only when an appeal orders the transcript, months after anyone could fix it.
**Tags:** #transformers #gaussian-mixture-models #feature-engineering #evaluation-metrics #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to deliver certified transcripts of court proceedings, from an official reporter's notes or the court's own audio, inside the appellate record deadline at the statutory page rate, and whoever clears appeal transcripts without extension requests takes the account.

## The Problem
In a digitally recorded courtroom a clerk or monitor watches levels and logs speakers, but nobody listens back. When a notice of appeal arrives, the transcription company finds the inaudible passages: a witness off-microphone, crosstalk during a ruling, a sidebar recorded at the wrong volume. Then the parties must reconstruct the missing passages through a settled or agreed statement, which takes weeks and is weaker evidence than a transcript.

## Why Nobody Has Built This
Courts buy recording systems for capture, and transcription companies are paid per page once an order arrives, so nobody is paid to check audio that may never be transcribed. Most proceedings are never appealed.

## What to Build
An overnight pass over each day's court audio that diarises speakers by channel, estimates the share of speech a transcriber could not resolve, and flags passages where a ruling, a verdict or testimony overlaps other speech or drops below intelligibility. The judge's clerk gets a short morning report while memories are fresh, and recurring problems (a dead microphone, a courtroom that always clips) go to court IT. The same scores let transcription companies estimate edit effort and price before accepting an order.

## Target Customer
Court administrators and court reporting services managers in states with heavy digital recording; approved transcription companies.

## Impact If Built
Fewer settled statements and appeal delays, fewer disputed passages, and evidence of digital recording's real failure rate. That number matters in a policy fight where both sides currently argue without data.
