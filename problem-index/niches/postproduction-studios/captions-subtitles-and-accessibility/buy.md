# Speech Recognition Adapted to Timed-Text Specs

**Niche:** [[niches/postproduction-studios/captions-subtitles-and-accessibility/profile|Captions, Subtitles & Accessibility Files]]
**Industry:** [[industries/postproduction-studios|Postproduction Studios]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** General-purpose speech recognition produces accurate transcripts; a caption file needs line breaks, reading speeds, shot-change timing and sound tags that each platform defines differently.
**Tags:** #transformers #seq2seq #feature-engineering #evaluation-metrics #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to deliver caption, subtitle and audio-description files that pass a platform's timed-text spec and the FCC quality rules on first submission while machines do the first pass, and whoever spends the fewest human minutes per programme hour without a rejection takes the account.

## The Problem
Turning a transcript into a compliant caption file is most of the editor's work: splitting text into events of the right length, holding each on screen long enough to read, snapping in and out times to shot changes, adding speaker IDs and SDH tags such as [door slams], and following each platform's style rules on italics, numbers and line position.

## What Already Exists
Commercial and open-source speech recognition (including Whisper-class models) with word timestamps; subtitle editors (EZTitles, Ooona, Subtitle Edit) with spec checkers; platform timed-text style guides.

## The Customization Gap
The adaptation needs: segmentation into caption events driven by each platform's reading-speed and line-length limits; shot-change detection on picture so events don't straddle cuts; sound-event detection on the effects track to propose SDH tags; speaker diarisation tied to character names from the script; and style-guide rules per platform encoded as validators, not left to the editor's memory. Generic speech recognition stops at words and timestamps.

## Target Customer
Captioning operations at vendors and post houses delivering to several broadcasters and streamers.

## Impact If Solved
The editor starts from a near-compliant file and only corrects it, instead of building events by hand from a transcript.
