# Booth Operations: Content, Keys & Projection

**Parent Industry:** [[industries/movie-theaters|Movie Theaters]]
**Category:** Low Digitized
**Contested on:** Every serious competitor in this niche is fighting to have every scheduled show find its content ingested and its key valid on the right server, with the projector healthy, before the doors open, and whoever drives dark-screen incidents closest to zero takes the account.

## Profile
**Market Size:** ~$300M a year in projection service contracts, content delivery, theatre management systems and booth labour (estimate)
**Share of Parent Industry:** ~2% of receipts (estimate)
**Digital Adoption:** Low in practice — the equipment is digital, but key tracking, ingest checks and fault response run on email, memory and a manager's walk through the booth
**Target Buyer:** Director of technical operations at a circuit; owner at an independent
**Automation Potential:** High for key and content checks and fault prediction; physical repairs stay with technicians

## What Makes This a Distinct Niche
Digital projection removed the projectionist trade from most theatres: BLS counted ~1,720 projectionists in the industry in May 2023 against ~5,270 general and operations managers. Content arrives as encrypted Digital Cinema Packages that unlock only with a KDM addressed to one server for a set window. KDMs fail when they target the wrong server, reference an expired certificate or start after a preview showtime, and Film-Tech members name late delivery as the main problem. The work is now a checking job done by managers. Cinemark reports ~22% of its auditoriums moved to Barco laser, a hardware cycle that changes server certificates and keys at every swap.

## Current Tools & Gaps
Theatre management systems (Hollywood Software, GDC), projector and server vendors' remote monitoring (Christie, Barco, NEC, Sony; Dolby and GDC servers), integrators' network operations centres, distributors' key desks. Gaps: no single view of key coverage per show for the week, alerts written for technicians rather than managers, and failure history scattered across service tickets.

## Problems
- [[niches/movie-theaters/booth-content-and-projection/build|🔨 Build: Show-by-Show Key and Content Assurance]]
- [[niches/movie-theaters/booth-content-and-projection/buy|🛒 Buy: IT Monitoring Retargeted at Projection Booths]]
- [[niches/movie-theaters/booth-content-and-projection/fix|🔧 Fix: Keys Checked at Midnight on Thursday]]
