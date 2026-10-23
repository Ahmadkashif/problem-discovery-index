# Paid by the Minute for Audio the Machine Couldn't Hear

**Industry:** [[document-preparation-services|Document Preparation Services]]
**Type:** Worker Life Changing
**One-liner:** A home-based transcriptionist on a platform is paid the same per audio minute for a clean podcast as for a crosstalk-heavy focus group, and the QA score that decides which work they can see is a number they cannot audit.
**Tags:** #gradient-boosting #feature-engineering #evaluation-metrics #hypothesis-testing #worker-facing #automation

## The Problem
General transcription is now done mostly by independent contractors who log into a platform's work queue from home. The task is increasingly editing a machine draft rather than typing from scratch: listen, fix misrecognised words, attribute speakers, apply the style rules (clean verbatim or true verbatim, tags for crosstalk and inaudible passages, timestamps), and submit. Pay is per audio minute or per task, with a nominal rate that looks reasonable for clean audio and collapses for the files that actually need a human: a focus group with eight people talking over each other, an accented expert interview full of technical terms, a phone recording with a dog in the room.

The hard files are visible in the queue and experienced workers learn to avoid them. Those that are left sit unclaimed until the platform raises a bonus or assigns them to whoever is still online near the deadline. Meanwhile every submission is scored by a reviewer or a sample audit, and the score decides the worker's level: which queues they can see, how much work they get and whether they stay on the platform at all. The worker sees a number and a few marked errors. They cannot see how the reviewer weighed a disputed word, whether a second reviewer would agree, or why a score moved after a run of difficult files.

## Why It Matters to the Worker
Pay becomes unpredictable in a way the worker cannot plan around. An hour of work produces a decent wage on clean audio and a fraction of it on a bad file, and the decision to take a bad file is a decision to earn less. The skill the platform depends on, decoding hard audio, is the skill that pays worst. The QA score is the worker's livelihood, and it is opaque. A string of difficult files, or one strict reviewer, can drop a worker's level and cut their access to work without anything they could have done differently.

There is also the ear and the body: hours with headphones at volume, re-listening to the same three seconds, wrists on a keyboard and a foot on a pedal, alone at home with no colleague to ask whether that word was "affect" or "effect" in context.

## What a Solution Looks Like
Difficulty-adjusted pay set before the file is taken. The platform already knows the machine's confidence, the number of speakers, the noise level, the overlap and the domain vocabulary, so it can predict the editing effort per audio minute and post the rate accordingly, then settle against the actual effort afterwards. On quality, scores that are explained and contestable: every marked error shown with its severity and the audio, scores normalised for file difficulty, and periodic double-blind reviews that measure reviewer agreement and publish it to the workers it affects.

## Impact If Solved
A transcriptionist paid for difficulty would earn steadier hourly income and could take the hard files rather than dodging them. If hard audio takes ~3 times the editing minutes per audio minute of clean audio (estimate), a flat rate pays about a third as much per hour on it. Pricing by predicted effort would close most of that gap, worth ~$50–100 a week (estimate) to a contractor who spends ~10 hours a week on hard files. That improves the platform's turnaround on exactly the files customers pay a human for. A QA score that measures the work rather than the luck of the queue gives skilled workers a reason to stay, which matters in a trade where experience is the only thing a machine draft can't supply.
