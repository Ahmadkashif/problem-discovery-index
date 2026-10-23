# Uncertainty Marked Where the Audio Is Uncertain

**Niche:** [[niches/document-preparation-services/evidentiary-transcription/profile|Evidentiary & Investigative Transcription]]
**Industry:** [[industries/document-preparation-services|Document Preparation Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An evidentiary transcript presents contested words with the same certainty as clear ones, and cross-examination is where the difference comes out.
**Tags:** #transformers #bayesian-inference #evaluation-metrics #confidence-intervals #compliance #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to turn poor evidentiary audio into certified verbatim transcripts, speakers attributed and uncertainty marked, that hold up under cross-examination and arrive before the discovery or trial date, and whoever delivers the hardest recordings defensibly on that clock takes the account.

## The Problem
On a bodycam recording of a struggle or a jail call over a bad line, some words are clear, some are a best judgement and some are guesses. The transcript shows them all the same way, apart from the occasional [inaudible]. When a disputed phrase ("I have a gun" against "I don't have a gun") becomes central at trial, the transcriptionist may be called to explain, and nothing in the transcript records how sure they were or who else listened.

## Why Nobody Has Built This
Transcription firms are small and paid per minute. Recognisers produce word confidences, but those are uncalibrated on this audio and not what a court needs. The legal convention is a clean transcript, and nobody has offered a defensible alternative.

## What to Build
A transcript format and tool that carries calibrated confidence for every word and speaker label from the recogniser and the human pass together. It routes low-confidence passages to a second independent listener, records each passage's resolution (agreed, disputed, inaudible) and produces a certification page that documents the process, alongside the clean transcript the court expects. Calibration is fitted on double-transcribed evidentiary audio.

## Target Customer
Legal and law-enforcement transcription firms; prosecutors' and public defenders' offices that commission transcripts; insurers' special-investigation units.

## Impact If Built
Transcripts that admit uncertainty where it exists are harder to impeach. Disputed phrases are identified before trial rather than during it, and second-listener effort goes where it changes the outcome.
