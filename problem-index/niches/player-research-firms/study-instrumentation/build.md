# A Session That Can Be Searched

**Niche:** [[niches/player-research-firms/study-instrumentation/profile|Study Instrumentation]]
**Industry:** [[industries/player-research-firms|Player Research Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The session leaves behind a video file, and everything downstream is limited by that.
**Tags:** #data-integration #automation #workflow-orchestration #evaluation-metrics #large-language-models #descriptive-statistics #object-detection #quick-win
**Contested on:** Every serious competitor in this niche is fighting to capture a session as a synchronised, searchable record rather than as a video file and some notes — and whoever builds that capture takes the account.

## The Problem
The record a session produces determines everything the analysis can do. Today it is a screen recording, a separate audio file, notes in a document with approximate timestamps, and sometimes a telemetry log aligned with nothing. Finding the moment a participant got confused means scrubbing video. The capture is set up per study by whoever is available, differs between studies, and quietly limits the quality of every finding that follows.

## Why Nobody Has Built This
Capture is treated as a logistics detail rather than as research infrastructure. Game builds do not emit telemetry for research by default. Each study's setup is improvised and thrown away. And nobody has connected capture quality to finding quality explicitly.

## What to Build
Capture everything on one timeline, by default, the same way every time. Synchronise screen, audio, observer notes and game telemetry onto a single timeline, which is the core and is what makes every downstream improvement possible. Provide a drop-in build integration that emits research events by default, so telemetry is present rather than negotiated per study. Let observers mark events live with one keystroke, which is the cheapest high-value capture there is. Transcribe and index audio automatically as the session runs rather than afterwards. Make the whole record searchable by utterance, event and time, since retrieval is what the analysis actually needs. Standardise the setup across studies so records are comparable and the firm's archive accumulates. Capture participant screen and face where consented, with the consent state recorded. Handle remote sessions with the same fidelity, as that is now a large share of studies. Store records with the study's metadata so they remain findable years later. And keep the capture unobtrusive, because a participant conscious of instrumentation behaves differently and the whole exercise depends on them not being.

## Target Customer
Games user research firms and platforms, in-house research functions, playtesting platforms, and research technology vendors.

## Impact If Built
The record a session produces sets a ceiling on every finding derived from it, and today that record is a video file. One synchronised searchable timeline is the precondition for every analysis improvement.
