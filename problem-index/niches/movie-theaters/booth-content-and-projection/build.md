# Show-by-Show Key and Content Assurance

**Niche:** [[niches/movie-theaters/booth-content-and-projection/profile|Booth Operations: Content, Keys & Projection]]
**Industry:** [[industries/movie-theaters|Movie Theaters]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The schedule, the content library and the key inventory live in three places, so a missing key is found when a full auditorium won't start.
**Tags:** #autoencoders #change-point-detection #survival-analysis #workflow-orchestration #worker-facing #automation
**Contested on:** Every serious competitor in this niche is fighting to have every scheduled show find its content ingested and its key valid on the right server, with the projector healthy, before the doors open, and whoever drives dark-screen incidents closest to zero takes the account.

## The Problem
Each week brings new films, new trailers, new KDMs and schedule changes. A projector swap changes the server certificate and silently orphans keys issued to the old one. Thursday previews start before some keys' windows open. Nobody checks every show against every key until the show fails.

## Why Nobody Has Built This
Ticketing vendors own the schedule, theatre management vendors own the playlists, and distributors' key desks own the KDMs; each sees one piece. Integrators monitor hardware, not keys.

## What to Build
A service that reads the week's schedule, the ingested content and every KDM's target server and validity window, checks each show, and drafts key requests to the right distributor desk days ahead. It adds anomaly detection on projector and server telemetry to warn of failures before the show, and a remaining-life estimate for lasers and lamps.

## Target Customer
Technical operations directors at circuits of 20+ theatres; integrators offering managed booth services.

## Impact If Built
Most avoidable dark screens (key gaps, missing content, foreseeable hardware faults) caught days ahead, cutting refunds and the manager's Thursday-night audit.
