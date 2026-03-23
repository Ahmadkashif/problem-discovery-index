# Accessibility Captioning and Multi-Language Compliance

**Niche:** [[niches/video-production-smb/corporate-training-video/profile|Corporate Training Video]]
**Industry:** [[industries/video-production-smb|Video Production SMB]]
**Type:** Fix (Pain Point)
**One-liner:** ADA and Section 508 require closed captions on all training videos, but production companies burn 2–4 hours per video manually correcting auto-generated captions that mangle technical terminology, and multi-language captioning multiplies the effort by the number of languages.
**Tags:** #transformer #speech-recognition #nlp #compliance #automation

## The Problem
Every training video delivered to a U.S. corporate client requires closed captions (ADA Title III, Section 508 for federal contractors). Auto-generated captions (YouTube, Descript, Rev AI) achieve 85–90% accuracy on general speech, but training videos contain domain-specific terminology — drug names, chemical compounds, regulatory citations, product names, acronyms — that ASR systems consistently misrecognize. An editor must manually review and correct every caption, a process taking 2–4 hours per hour of video. For clients with international workforces, captions are also needed in Spanish, French, Mandarin, and other languages — each requiring separate transcription and timing. A 10-video training series needing captions in 3 languages generates 30 captioning tasks, consuming 60–120 hours of production time.

## Why It's Still Broken
Auto-captioning accuracy has improved dramatically, but the "last 10%" of errors are concentrated in exactly the words that matter most in training content — the technical terms, proper nouns, and regulatory references that the learner must read correctly. Rev (human transcription) delivers 99% accuracy at $1.50/minute, but turnaround is 24–48 hours and doesn't cover multi-language. AI captioning services correct faster but still require domain-specific vocabulary training that resets for every client and industry. The production company ends up doing manual QA on every caption file regardless of the source, because a single captioning error in a compliance training video ("wear PAPR respirators" captioned as "wear paper respirators") creates a safety liability.

## What a Fix Looks Like
A captioning system purpose-built for training video where: (1) the production company uploads a client-specific glossary (technical terms, product names, acronyms, regulatory citations) that the ASR model uses during transcription, (2) captions are auto-generated with 98%+ accuracy on domain-specific terms, (3) a QA interface highlights low-confidence words for human review rather than requiring full read-through, (4) multi-language captioning uses the corrected English transcript as a source for translation, preserving technical term accuracy, (5) caption files are output in all standard formats (SRT, VTT, SCC, DFXP) for LMS compatibility, and (6) the glossary persists across projects for the same client, improving accuracy over time. The key innovation: the domain glossary pre-conditions the ASR model, solving the exact problem that generic captioning tools can't.

## Who Feels the Pain
Editors who spend 30% of post-production time on captioning QA instead of creative work, and production company owners who absorb the captioning cost because clients expect it as part of the delivery.

## Impact If Fixed
Reduces captioning time from 3 hours to 30 minutes per video through glossary-conditioned ASR and targeted QA. Enables the production company to offer multi-language captioning as a revenue add-on ($500–$1,500 per language) rather than absorbing it as a cost. Eliminates the compliance risk of caption errors in safety-critical training content.
