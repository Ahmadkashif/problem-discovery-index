# Predicting a Failed Test Pressing Before the Lacquer Is Cut

**Niche:** [[niches/recording-studios/vinyl-lacquer-cutting/profile|Vinyl Lacquer Cutting]]
**Industry:** [[industries/recording-studios|Recording Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A cutting engineer decides by ear how loud, long and bass-heavy a side can be, and learns weeks later from a test pressing whether the call was right.
**Tags:** #tacit-knowledge-ml #gradient-boosting #feature-engineering #cnns #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to cut lacquers that pass the test pressing first time, and whoever wastes the fewest scarce lacquers and plant-queue weeks on recuts keeps the label's vinyl work.

## The Problem
Failures have known causes: sibilance that distorts, out-of-phase bass that throws the stylus vertically, inner-groove distortion on a long side, a level too hot for the program's dynamics. An experienced engineer hears most of them in the master before cutting and adjusts. A less experienced one cuts, waits for the test pressing, and recuts. Each recut uses lacquers in short supply and sends the job to the back of a plant's queue.

## Why Nobody Has Built This
The labelled data has never been assembled. The cut settings are on the lathe or in a notebook, the master is on a drive, and the outcome is an email from a plant or a label. The engineers who could label failures are few and busy, and they disagree about what is acceptable for a given genre.

## What to Build
A pre-cut analyser trained on a cutting room's own history: features of the master (high-frequency energy in sibilant passages, low-frequency phase correlation, dynamic range, side duration and track positions) plus the planned cut settings, joined to test-pressing outcomes and defect categories. It flags risky passages with timestamps and estimates failure probability before the lacquer is touched. Pooled across rooms, it becomes a teaching tool for new cutting engineers.

## Target Customer
Owner-engineers of cutting rooms and the mastering studios that have added lathes, plus pressing plants that cut in-house.

## Impact If Built
Fewer recuts per title, lacquers saved in a single-supplier market, and weeks off the release schedule for labels whose vinyl ships after the digital release.
