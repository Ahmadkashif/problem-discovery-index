# The Archive Researcher Logging Footage by Eye

**Industry:** [[film-distributors|Film Distributors]]
**Type:** Worker Life Changing
**One-liner:** The footage researcher at a stock and archival library gets back the hours spent scrubbing through reels to find a shot the catalogue can't describe, and the frustration of losing a licence because the clip existed but nobody could find it in time.
**Tags:** #contrastive-learning #transformers #cnns #transfer-learning #worker-facing #automation #quick-win

## The Problem
A documentary producer sends a research request at four in the afternoon. They want 1960s colour footage of a Detroit assembly line, a wide shot with workers visible, no logos, for a broadcast and streaming licence in North America and the UK, by tomorrow's edit. The library holds ~tens of thousands of hours of film and tape (estimate), digitised over years. Most of it is described at reel or story level with a few typed keywords from whoever logged it: "auto plant, 1964, B-roll". The researcher searches the keywords, pulls candidate reels, and scrubs through them at speed looking for the shot. They send screeners with timecodes, then check whether the clip has rights restrictions: identifiable people, music on the soundtrack, a news organisation's copyright, an underlying third-party licence.

Archival footage is licensed by the second. Rate cards run ~$40 to $80 a second with minimums (Producers Library lists $49 a second for regular documentary use). So the researcher's speed is the library's revenue: the first library to send a usable, clearable clip usually gets the licence.

## Why It Matters to the Worker
The job is a craft. Experienced archive researchers know their collection, know which reels from which decades hold what, and can recognise a period, a city or a make of car on sight. But most of the day is spent on mechanical scrubbing through footage the catalogue failed to describe, against a client's deadline that the researcher did not set. The collection knowledge is personal and unrecorded. A researcher who leaves takes the map of the archive with them, and a new hire takes years to build it.

## What a Solution Looks Like
Shot-level indexing of the digitised collection: every shot segmented and described, with searchable embeddings for objects, settings, period cues, camera framing, colour and on-screen text, and with transcripts of any speech. A researcher types the producer's request in plain language and gets ranked candidate shots with timecodes. They then refine by example ("more like this one, but wider"). Rights flags are attached from the catalogue record. Every time the researcher keeps or rejects a candidate, the system learns which shots match which requests.

## Impact If Solved
A request that took ~2 to 4 hours of scrubbing (estimate) takes minutes of review, so a researcher can answer several times as many requests a day. The library wins licences it currently loses to slower competitors. The researcher spends their time on what they are actually expert in: judging which clip tells the producer's story and is clearable.
