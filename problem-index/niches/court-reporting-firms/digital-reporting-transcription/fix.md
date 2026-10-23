# Annotations That Never Reach the Transcriptionist

**Niche:** [[niches/court-reporting-firms/digital-reporting-transcription/profile|Digital Reporting Transcription Pools]]
**Industry:** [[industries/court-reporting-firms|Court Reporting Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The digital reporter logs every speaker and spelling during the deposition, and the transcriptionist two days later works from the audio alone.
**Tags:** #large-language-models #data-integration #workflow-orchestration #quick-win #compliance
**Contested on:** Every serious competitor in this niche is fighting to turn a digital reporter's multi-channel recording and annotations into a transcript that courts in that state will accept as certified, and whoever can certify digital transcripts in the most jurisdictions with evidence of their accuracy takes the account.

## The Problem
Annotation software exports logs in its own format. Transcription tools cannot read them, so the transcriptionist re-identifies speakers by voice, guesses spellings the reporter already confirmed, and misses the passages the reporter flagged as unclear.

## Why It's Still Broken
Capture software and transcription software come from different vendors, and agencies have not specified an interchange format.

## What a Fix Looks Like
A simple shared format for speaker map, spellings, exhibits, flags and on/off times, converted from the major annotation tools and loaded into the transcription editor as timestamped hints and constraints.

## Who Feels the Pain
Transcriptionists; digital reporters whose work is wasted; certifying officers signing transcripts with avoidable errors.

## Impact If Fixed
Fewer speaker and spelling errors, faster turnaround, and a better case for digital transcripts in the states deciding whether to accept them.
