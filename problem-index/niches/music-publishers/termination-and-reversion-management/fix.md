# Publication Dates Nobody Recorded

**Niche:** [[niches/music-publishers/termination-and-reversion-management/profile|Termination & Reversion Management]]
**Industry:** [[industries/music-publishers|Music Publishers]]
**Type:** Fix (Pain Point)
**One-liner:** The termination window runs from each song's publication date, which is rarely in the agreement and often missing from the rights database.
**Tags:** #large-language-models #data-integration #compliance #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to know, for every grant in a catalogue, when it can be terminated or will revert, and to act inside the statutory window, and whoever finds the window first either keeps the song or gets it back.

## The Problem
An agreement may cover "all compositions written during the term." Each song's window depends on when that song was published, which has to be reconstructed from release dates, registration records and old label copy, song by song.

## Why It's Still Broken
Rights databases were built to collect royalties, which never needed a publication date. Acquired catalogues arrive with even less.

## What a Fix Looks Like
Backfill a publication date and its source for every work from release databases and Copyright Office registrations. Flag conflicting evidence for review and store the date as a sourced field that any termination calculation can rely on.

## Who Feels the Pain
Business affairs teams, estate lawyers and catalogue buyers' counsel.

## Impact If Fixed
A one-time data job that turns termination analysis from per-song research into a calculation.
