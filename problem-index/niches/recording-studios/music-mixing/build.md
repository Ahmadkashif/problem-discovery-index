# A Ledger of Every Note and the Move That Answered It

**Niche:** [[niches/recording-studios/music-mixing/profile|Mixing for Artists & Labels]]
**Industry:** [[industries/recording-studios|Recording Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A mixer answers thousands of notes a year and keeps no record of which move answered which note, so the skill that wins repeat clients can't be reviewed, reused or taught.
**Tags:** #tacit-knowledge-ml #transformers #contrastive-learning #large-language-models #feature-engineering #evaluation-metrics #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to deliver a mix the artist signs off in the fewest revision rounds, and whoever translates an artist's notes and reference tracks into the right moves first time keeps that artist's next record.

## The Problem
Each revision round leaves three traces: the client's note, the change in the session, and the client's response to the next bounce. They sit in three places, an email thread, a session file saved over itself, and a review link, and nobody joins them. A senior mixer's first-time hit rate on "warmer" or "more punch" is the most valuable thing about them, and it can't be measured, shown to a client or taught to an assistant.

## Why Nobody Has Built This
DAW makers build mixing tools, not records of mixing decisions. AI-mix vendors train on target curves and genre averages, which engineers distrust because they flatten a signature sound. Review-tool vendors capture notes but never see the session. And the session belongs to the artist's project, so nobody has asked permission to learn from it.

## What to Build
A DAW extension that snapshots parameter state at every bounce, computes the diff between bounces at the level of track, plug-in and parameter, and pulls the matching notes from the review tool or inbox. The engineer confirms with one click which change answered which note. On top: retrieval of the engineer's own past answers to similar notes from the same client or genre, then a ranking model that proposes candidate moves, and a clarifier that turns an ambiguous note into an A/B question for the client. Consent to learn from the session goes into the mix agreement.

## Target Customer
Freelance mixers doing 100–300 songs a year (estimate) and multi-room studios that run mix teams for labels and want to train juniors on how their senior engineers work.

## Impact If Built
Saving one revision round of ~2–3 hours on each of ~150 songs returns several hundred hours a year to a working mixer (estimate). It also gives a studio its first teachable record of the skill clients actually pay for.
