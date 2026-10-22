# Alternate Mixes Re-Bounced by Hand After Every Change

**Niche:** [[niches/recording-studios/music-mixing/profile|Mixing for Artists & Labels]]
**Industry:** [[industries/recording-studios|Recording Studios]]
**Type:** Fix (Pain Point)
**One-liner:** Every revision means re-printing the main mix, instrumental, a cappella, TV mix, clean version and stems, and a forgotten mute in one of them reaches the label.
**Tags:** #automation #workflow-orchestration #evaluation-metrics #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to deliver a mix the artist signs off in the fewest revision rounds, and whoever translates an artist's notes and reference tracks into the right moves first time keeps that artist's next record.

## The Problem
A label delivery is not one file. It is the main mix plus five to ten alternates and a stem set, each named to the label's convention. After every revision the engineer prints them all again, often late at night, toggling mutes and sends by hand. Errors are common: an instrumental with a vocal reverb tail left in, a clean version with one word still uncensored, stems that don't sum to the mix.

## Why It's Still Broken
The list of required versions differs by label, distributor and sync library, and it lives in emails rather than in the session. DAWs can batch-export tracks, but they don't know what a "TV mix" means for a given client. Checking that the alternates match the approved main mix is done by listening.

## What a Fix Looks Like
A delivery template per client that defines each alternate as a set of mute and send states, prints them all from the approved session in one pass, names files to the label's convention, and automatically checks the results: stems that null against the main mix, an instrumental with no vocal energy, a clean version with the flagged words absent.

## Who Feels the Pain
Mix engineers printing deliverables after a long day; labels and sync teams who discover errors after release or placement.

## Impact If Fixed
An hour or more saved per song per revision on label projects (estimate), and the end of embarrassing delivery errors that cost a mixer the next job.
