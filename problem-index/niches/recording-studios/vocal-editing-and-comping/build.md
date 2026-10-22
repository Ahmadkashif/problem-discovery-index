# A First Comp Built From the Producer's Past Choices

**Niche:** [[niches/recording-studios/vocal-editing-and-comping/profile|Vocal Editing, Tuning & Comping]]
**Industry:** [[industries/recording-studios|Recording Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every comp a producer has ever built is saved in their sessions as a labelled choice between takes, and no tool learns from them.
**Tags:** #tacit-knowledge-ml #cnns #contrastive-learning #transfer-learning #evaluation-metrics #automation
**Contested on:** Every serious competitor in this niche is fighting to turn a night of raw vocal takes into a tuned, timed comp the artist hears as their own performance by the next morning, and whoever's comps need the fewest artist overrides gets the producer's next session.

## The Problem
Comping a lead vocal takes one to three hours a song (estimate): listening to every take of every phrase and choosing by pitch, timing, tone and the hard-to-name "feel". Producers know which they prefer, often the less accurate take with more emotion, but the judgement is tacit and slow to pass on to an assistant or a freelance editor.

## Why Nobody Has Built This
Pitch and timing tools treat each take independently; selection between takes has been left to the ear. The labelled data, comp selections in session files, sits on producers' drives and has never been gathered. Producers fear tools that pick the "correct" take and lose the performance.

## What to Build
A comp assistant that aligns all takes to the lyric, segments them into phrases, and ranks the candidates for each phrase using a model of this producer's past choices, trained on their own sessions, where every comp lane is a labelled example. It proposes a first comp with confidence per phrase, highlights phrases where feel and accuracy disagree, and learns from every override. Per-artist adjustment covers singers whose best takes are the loose ones.

## Target Customer
Producers and production studios in vocal-heavy genres, freelance vocal editors working for several producers, and DAW makers who could ship it.

## Impact If Built
An hour or more saved per song (estimate) and comps that start close to what the producer would have picked, so overnight editing becomes a morning review.
