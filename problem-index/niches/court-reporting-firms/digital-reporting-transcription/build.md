# Per-Passage Accuracy Evidence for Digital Transcripts

**Niche:** [[niches/court-reporting-firms/digital-reporting-transcription/profile|Digital Reporting Transcription Pools]]
**Industry:** [[industries/court-reporting-firms|Court Reporting Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** When opposing counsel or a legislature asks whether a digital transcript is as accurate as a stenographer's, the agency answers with marketing claims rather than evidence from its own transcripts.
**Tags:** #transformers #hidden-markov-models #evaluation-metrics #confidence-intervals #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to turn a digital reporter's multi-channel recording and annotations into a transcript that courts in that state will accept as certified, and whoever can certify digital transcripts in the most jurisdictions with evidence of their accuracy takes the account.

## The Problem
Digital and stenographic reporting are argued over with survey data and anecdotes. NCRA warns of unreliable recordings; AAERT's 2025 report cites users who value digital reporters' accuracy and on-time delivery. Neither side publishes measured error rates on real proceedings, and a court deciding whether to accept a digital transcript has nothing to examine.

## Why Nobody Has Built This
Measuring accuracy needs a verified reference for a sample of passages, which costs money. Publishing the result risks showing errors, and agencies have avoided the exposure while the licensing fight is open.

## What to Build
Per-transcript evidence. Align the transcript to the multi-channel audio, score each passage by recogniser confidence, overlap and channel quality, and send a random sample plus every low-confidence passage for blind verification. Record what was changed, and attach an accuracy statement with confidence intervals to the certification. Aggregated across thousands of jobs, this becomes the dataset a legislature or court study needs. Severity scoring of transcripts already exists as a QA function in [[niches/document-preparation-services/transcript-qa-accuracy-scoring/profile|Transcript QA & Accuracy Scoring]], where the score settles service credits and editor pay. Here the evidence has a different audience and burden: it supports a court certification and has to persuade a judge or legislature that a capture method yields a reliable record.

## Target Customer
VPs of digital reporting at national agencies; state court administrators evaluating digital recording.

## Impact If Built
Certification backed by evidence rather than assertion, the strongest available argument in states deciding acceptance, and an honest picture of where digital capture fails.
