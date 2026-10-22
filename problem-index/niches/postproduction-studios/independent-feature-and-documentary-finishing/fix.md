# The Festival DCP That Fails at the Venue

**Niche:** [[niches/postproduction-studios/independent-feature-and-documentary-finishing/profile|Independent Feature & Documentary Finishing]]
**Industry:** [[industries/postproduction-studios|Postproduction Studios]]
**Type:** Fix (Pain Point)
**One-liner:** An independent film's premiere DCP arrives with the wrong frame rate, an unreadable subtitle track or an expired key, and the problem is found at the festival's tech check.
**Tags:** #descriptive-statistics #feature-engineering #evaluation-metrics #compliance #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to take a locked independent cut to a deliverables package a distributor or streamer will accept, inside a finishing budget set before anyone read the delivery schedule, and whoever quotes the full deliverables cost up front and holds it takes the filmmaker.

## The Problem
Festivals require a Digital Cinema Package built to DCI and SMPTE specifications, often with encrypted content keys (KDMs) issued for the venue's projector. Filmmakers build DCPs themselves to save money, or a post house builds one in a rush. Common failures (Interop versus SMPTE packaging, subtitle format, audio channel mapping, a KDM issued for the wrong server or window) surface at the venue's technical check, days before the premiere.

## Why It's Still Broken
DCP tools create packages but do not validate them against each festival's stated requirements, and few filmmakers can test on a cinema server before shipping.

## What a Fix Looks Like
A validator that checks a DCP against DCI and SMPTE conformance and against the specific festival's technical requirements, plays a proxy of every reel, subtitle and audio channel, and checks KDM validity windows against screening times, with a plain-language report and fixes.

## Who Feels the Pain
Independent filmmakers at their most stressful week; festival technical staff; post houses fielding emergency rebuilds.

## Impact If Fixed
Failures get caught before shipping rather than at the venue, so no premiere screening is lost to a packaging error.
