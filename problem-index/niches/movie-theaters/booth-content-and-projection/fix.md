# Keys Checked at Midnight on Thursday

**Niche:** [[niches/movie-theaters/booth-content-and-projection/profile|Booth Operations: Content, Keys & Projection]]
**Industry:** [[industries/movie-theaters|Movie Theaters]]
**Type:** Fix (Pain Point)
**One-liner:** New films and their keys arrive late in the week, so the manager on the Thursday close checks them by hand hours before the first preview.
**Tags:** #large-language-models #workflow-orchestration #worker-facing #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to have every scheduled show find its content ingested and its key valid on the right server, with the projector healthy, before the doors open, and whoever drives dark-screen incidents closest to zero takes the account.

## The Problem
Content and KDMs for Friday's openers often land Wednesday or Thursday. The closing manager opens the theatre management system, compares the key list to the schedule screen by screen, and emails the distributor's key desk for anything missing, hoping for a reply before the preview.

## Why It's Still Broken
The check is manual because the key inventory and the ticketing schedule aren't joined, and late delivery is a distributor habit no exhibitor can change alone.

## What a Fix Looks Like
An automatic daily report comparing every scheduled show for the next seven days with the keys present, highlighting gaps by showtime and pre-filling the request email with the server serial and certificate. It needs read access to two systems, not a new platform.

## Who Feels the Pain
Closing managers on Thursday nights; audiences at sold-out previews; distributors' after-hours key desks.

## Impact If Fixed
A daily gap report removes the late-night audit and turns most key failures into routine emails sent days earlier.
