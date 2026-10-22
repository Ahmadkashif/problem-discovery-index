# Caption Review Routed by Error Risk

**Niche:** [[niches/postproduction-studios/captions-subtitles-and-accessibility/profile|Captions, Subtitles & Accessibility Files]]
**Industry:** [[industries/postproduction-studios|Postproduction Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Machine transcription is right on most lines and wrong on the ones that matter (names, overlapping speech, lyrics, jargon), and reviewers still read every line to find them.
**Tags:** #transformers #large-language-models #logistic-regression #evaluation-metrics #compliance #automation #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to deliver caption, subtitle and audio-description files that pass a platform's timed-text spec and the FCC quality rules on first submission while machines do the first pass, and whoever spends the fewest human minutes per programme hour without a rejection takes the account.

## The Problem
A captioning vendor runs speech recognition on a 44-minute episode, then a human editor reviews and corrects every line, fixes timing and adds SDH tags and speaker IDs. Most lines need no change. The errors cluster in predictable places: character and place names, overlapping dialogue, whispered or accented speech, song lyrics, technical jargon and anything under music. Review time per programme hour is the vendor's main cost and the platforms' error tolerance is low.

## Why Nobody Has Built This
Vendors have optimised the transcription engine rather than the review. The corrections editors make are kept as finished files, not as labelled examples of where the engine failed.

## What to Build
A line-level error-risk model trained on the vendor's own engine output versus final approved captions. It uses acoustic conditions (music bed, overlap, low signal-to-noise), lexical signals (rare words, names not in the show's glossary) and engine confidence. Editors see high-risk lines first and low-risk lines in a fast-confirm mode. Show glossaries are built automatically from scripts and earlier episodes.

## Target Customer
Captioning vendors and post houses' accessibility teams producing broadcast and streaming captions at volume.

## Impact If Built
If editors spend their time on the lines most likely to be wrong, review minutes per programme hour could fall by a third or more (estimate) at the same or lower rejection rate.
