# Getting It Right at the Source

**Niche:** [[niches/music-distribution-platforms/metadata-capture-at-upload/profile|Metadata Capture at Upload]]
**Industry:** [[industries/music-distribution-platforms|Music Distribution Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The most consequential data entry in the music industry is performed by someone who has never heard the terms being asked of them.
**Tags:** #large-language-models #evaluation-metrics #workflow-orchestration #automation #confidence-intervals #worker-facing #data-integration #compliance
**Contested on:** Every serious competitor in this niche is fighting to get correct rights data out of an artist who does not know what a publisher is — and whoever designs that capture well prevents the matching problem instead of repairing it downstream.

## The Problem
The upload form asks for writer names, split percentages, publisher affiliations, performing rights organisation memberships and identifiers. A large share of uploaders are independent artists who wrote the song with a friend, have no publisher, do not know whether they are registered anywhere, and will type something plausible in order to proceed. The data they enter propagates into every downstream system and determines who gets paid for as long as the recording exists.

## Why Nobody Has Built This
The form was built to collect the fields the delivery specification requires, so it asks the industry's questions in the industry's language — a capture designed around a downstream schema will always speak the schema's vocabulary rather than the user's. Reducing friction at upload competes with data quality. The cost of bad data appears years later to someone else. And no distributor is judged on the quality of what it captures.

## What to Build
Design the capture around the person filling it in. Ask questions the artist can answer — who was in the room, who wrote the words, who wrote the music, is anyone signed to anything — and derive the industry fields from those, which is the core and is the difference between accurate data and plausible data. Explain the consequence at the point of entry, since an artist who understands that a missing writer means missing money will take the trouble. Validate against what is knowable, checking names against registries, splits against arithmetic and affiliations against membership data. Prefill from the artist's previous releases, as most uploaders repeat the same collaborators and re-entry is where errors enter. Detect the implausible — a hundred percent to one writer on a track with three credited performers — and ask rather than accept. Support the collaborator confirming their own details, which is both more accurate and resolves disputes before they exist. Handle the unregistered writer properly, since telling an artist their collaborator needs to register somewhere is more useful than accepting a blank. Provide a correction path after release that actually propagates, because errors are currently permanent in practice. Measure capture quality by downstream match rate, which is the only real test and is not currently connected. And report capture quality as a product metric, since a distributor with a better match rate has a genuine competitive claim.

## Target Customer
Product and rights leadership, independent artists and their collaborators, collecting organisations receiving the data, and publishing administration vendors.

## Impact If Built
A capture designed around a downstream schema speaks the schema's vocabulary rather than the user's, so the form asks questions its users cannot answer. Deriving the industry fields from questions an artist can answer is what turns plausible data into accurate data.
