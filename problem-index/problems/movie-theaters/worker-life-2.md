# The Manager Who Is Also the Projectionist

**Industry:** [[movie-theaters|Movie Theaters]]
**Type:** Worker Life Changing
**One-liner:** Since digital projection, the shift manager runs the booth between box office problems, and on a Thursday night they learn that a missing or mis-addressed decryption key will leave a sold-out preview dark.
**Tags:** #change-point-detection #autoencoders #large-language-models #evaluation-metrics #worker-facing #workflow-orchestration #automation

## The Problem
BLS counted only ~1,720 motion picture projectionists in the industry in May 2023, against ~5,270 general and operations managers and ~7,230 first-line supervisors. Digital projection removed the dedicated booth job at most theatres. Now the films arrive as Digital Cinema Packages on drives or by satellite and network delivery. Each is encrypted and unlocks only with a Key Delivery Message (KDM), issued by the distributor for a specific projector server and a set window of dates. A theatre management system schedules the playlists, but someone has to ingest the content, check that every KDM is present and valid for every screen and every show in the week, build the playlists with the right trailers and ads, and fix whatever fails.

That someone is usually the manager on duty. KDMs fail in ordinary ways. One targets the wrong server after a projector swap. Another references an expired certificate, or starts after a Thursday preview showtime, or ends before a late Sunday show. Film-Tech forum members name late KDM delivery by distributors as the main problem. A missing key is discovered when the show won't start, with the audience seated.

## Why It Matters to the Worker
The manager is already running the floor: cash drawers, a broken soda machine, a crew member who didn't show, a guest complaint. The booth is a second job they were trained for in a day, and its failures are the most visible thing that can happen in a theatre. A dark screen means refunds, an angry auditorium, a call to the distributor's after-hours line and a report to the district manager. Many managers check keys late on Thursday night because the next week's content arrived that afternoon.

The work also lacks a ladder. The skills that once made projection a trade (sound, lamp alignment, focus) now sit with a remote service vendor, and the manager gets the anxiety of the booth without the craft.

## What a Solution Looks Like
A booth assistant that reads the week's schedule from the ticketing system, the content and key inventory from the theatre management system, and the KDM files themselves. It checks every scheduled show against a present, valid key for the right server and window, and flags gaps days ahead with a drafted request to the distributor's key desk naming the server certificate and dates needed. It watches the projector and server logs for warnings that precede failures (lamp or laser hours, storage errors, rising temperatures) and tells the manager in plain language what to do, or calls the service vendor itself.

## Impact If Solved
Catching key and content gaps two or three days before showtime rather than at curtain could eliminate most avoidable dark-screen incidents, which are a recurring source of refunds and complaints (frequency not measured; estimate). For the manager it removes the Thursday-night audit and the dread of a preview going dark, and turns booth duty from an unpredictable second job into a checklist the system already ran.
