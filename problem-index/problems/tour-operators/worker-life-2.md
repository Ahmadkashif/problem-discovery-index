# Rooming Lists and Manifests at Peak Season

**Industry:** [[tour-operators|Tour Operators]]
**Type:** Worker Life Changing
**One-liner:** An operations coordinator sends, corrects and re-sends the names, room types, flights and dietary needs for forty departures to two hundred suppliers by email. They find out about the mistake the day the group arrives.
**Tags:** #large-language-models #transformers #bert #worker-facing #automation #data-integration #quick-win

## The Problem
For each departure an operations coordinator assembles the final details every supplier needs:
- for each hotel, a rooming list with names, room types (twin, double, single, triple), bed requests, accessibility needs and late arrivals;
- for the coach company, a passenger manifest;
- for restaurants, numbers and dietary needs;
- for rail or ferry operators, named tickets;
- for the tour director, the full dossier.

The deadlines are the suppliers', typically a set number of days before arrival, and they fall on many departures at once at peak season.

The information changes until the last day. A traveller cancels. Two friends decide to share. A name is misspelt against the passport. An advisor sends a dietary note in the body of an email. The reservation system holds most of this, but suppliers receive spreadsheets or PDFs in their own formats. Confirmations come back as replies, in several languages, sometimes with the hotel's own changes buried in them. A coordinator handling a few dozen departures at peak is running hundreds of these threads (estimate).

Errors surface at the worst time. The group arrives and the hotel has the previous version of the list. A coeliac traveller's note never reached the restaurant. A single traveller has been put in a twin with a stranger. The tour director fixes it on site and the coordinator hears about it afterwards.

## Why It Matters to the Worker
The work is detail under pressure, and the coordinator owns every error even when the supplier caused it. Peak season means long hours of copying and checking, and the evening is spent rereading confirmation emails for the one line that changed. The job is often the entry point to an operations career. Done this way it teaches vigilance more than judgement, and turnover is high (estimate).

## What a Solution Looks Like
The coordinator works from one live departure record. Supplier documents are generated from it in each supplier's preferred format and sent on the supplier's deadline. Each confirmation that comes back is read automatically, whatever its language or layout, and compared field by field with what was sent. Differences are flagged: a missing name, a twin changed to a double, a date shifted. Changes after a document has gone out trigger a corrected version and a request for re-confirmation. The coordinator handles exceptions only, with each supplier's status for each departure on one screen.

## Impact If Solved
Cutting manual assembly and checking time per departure, plausibly from a few hours to under one (estimate), gives a coordinator back a large part of the peak-season evening. It would also cut the arrival-day errors that land on the tour director and the traveller.
