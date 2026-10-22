# Doubles and Harmonies Aligned One Syllable at a Time

**Niche:** [[niches/recording-studios/vocal-editing-and-comping/profile|Vocal Editing, Tuning & Comping]]
**Industry:** [[industries/recording-studios|Recording Studios]]
**Type:** Fix (Pain Point)
**One-liner:** Alignment tools tighten stacked vocals to the lead automatically, then fail on breaths, consonants and held notes, and the editor fixes each one by hand.
**Tags:** #rnns #feature-engineering #automation #worker-facing #quick-win
**Contested on:** Every serious competitor in this niche is fighting to turn a night of raw vocal takes into a tuned, timed comp the artist hears as their own performance by the next morning, and whoever's comps need the fewest artist overrides gets the producer's next session.

## The Problem
A modern chorus may stack a dozen vocals: doubles, harmonies, ad-libs. Each must start and end with the lead, especially on consonants like "s" and "t" that flam audibly when misaligned. Alignment tools do most of it, but warp artefacts on held notes, misaligned breaths and doubled sibilants remain, and the editor zooms in and fixes them syllable by syllable.

## Why It's Still Broken
Alignment tools match each double to a guide track with signal processing and don't know where they've failed. They don't flag uncertain regions, so the editor must listen to everything. Different tools handle consonants differently, and none learns from the editor's corrections.

## What a Fix Looks Like
Alignment that reports its own confidence per syllable, flags the places likely to be audible (consonant onsets, phrase ends, breaths), offers alternative treatments for each, and learns from which ones the editor accepts. The editor reviews a list of flagged spots instead of the whole stack.

## Who Feels the Pain
Vocal editors and assistant engineers working overnight; producers waiting for stacks in the morning.

## Impact If Fixed
Stack alignment that takes minutes of review rather than an hour of manual repair per song (estimate).
