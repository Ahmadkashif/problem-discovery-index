# The Conform That Breaks on Reframes and Speed Ramps

**Niche:** [[niches/postproduction-studios/long-form-picture-finishing/profile|Long-Form Picture Finishing]]
**Industry:** [[industries/postproduction-studios|Postproduction Studios]]
**Type:** Fix (Pain Point)
**One-liner:** Repositions, speed ramps, nested sequences and temp effects don't survive the trip from the offline edit to the finishing system, and online editors rebuild them shot by shot.
**Tags:** #feature-engineering #seq2seq #evaluation-metrics #automation #worker-facing #quick-win
**Contested on:** Every serious competitor in this niche is fighting to carry a series' look consistently across every episode, colorist, HDR grade and SDR trim inside the streamer's delivery window, and whoever does it with the fewest supervised sessions and redeliveries takes the show.

## The Problem
The editor's Avid timeline is exported as an AAF or EDL and conformed in Resolve or Baselight against camera originals. Simple cuts translate. Reframes, variable speed changes, nested sequences, temp composites and timewarps often don't: the conform lands with wrong framing, wrong timing or missing effects. The online editor finds them by playing the conform against the offline reference and fixes them by hand, often the night before colour starts.

## Why It's Still Broken
Each editing and finishing system interprets effects differently, and the interchange formats carry them incompletely. The fix is human comparison, and nobody measures how many hours it takes per episode.

## What a Fix Looks Like
Automated comparison of the conform against the offline reference export, frame by frame, flagging shots where framing, timing or content differ beyond tolerance. A library of known translation failures by effect type and system pair proposes the correction for each flagged shot.

## Who Feels the Pain
Online editors and assistant editors working overnight; colorists whose session starts late; post producers whose schedule slips.

## Impact If Fixed
Conform checking could fall from hours of playback per episode to a list of the shots that actually differ (estimate), and errors stop reaching the supervised session.
