# Captions That Cover the On-Screen Text

**Niche:** [[niches/postproduction-studios/captions-subtitles-and-accessibility/profile|Captions, Subtitles & Accessibility Files]]
**Industry:** [[industries/postproduction-studios|Postproduction Studios]]
**Type:** Fix (Pain Point)
**One-liner:** Captions sit at the bottom of the frame by default, on top of lower thirds, burned-in subtitles and on-screen graphics, which the FCC placement standard and every streamer spec forbid.
**Tags:** #object-detection #cnns #feature-engineering #evaluation-metrics #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to deliver caption, subtitle and audio-description files that pass a platform's timed-text spec and the FCC quality rules on first submission while machines do the first pass, and whoever spends the fewest human minutes per programme hour without a rejection takes the account.

## The Problem
Documentaries, news-style shows and reality series carry lower thirds, location cards, burned-in translations of foreign dialogue and graphics. A caption placed over them hides information from the viewer and fails QC. Editors reposition captions by eye while scrubbing through the programme.

## Why It's Still Broken
Caption tools know the caption's position, not what is in the frame underneath it. Burned-in text and faces are found by watching.

## What a Fix Looks Like
Detect on-screen text, graphics and faces per frame, check every caption event's position against them, and move conflicting events to the nearest clear position allowed by the platform's spec, flagging cases where no clear position exists.

## Who Feels the Pain
Caption editors scrubbing every programme; QC operators failing files; deaf and hard-of-hearing viewers who lose the information underneath.

## Impact If Fixed
Placement checks become automatic, a whole class of rejections disappears, and editors stop scrubbing every frame for conflicts.
