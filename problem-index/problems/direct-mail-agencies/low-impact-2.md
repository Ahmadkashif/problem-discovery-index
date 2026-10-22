# Proof of Distribution for Door-to-Door Routes

**Industry:** [[direct-mail-agencies|Direct Mail Agencies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Door-hanger and flyer distributors sell coverage by the door and prove it with GPS dots and photos that no tool turns into a street-by-street answer to the client's only question: did every paid door get one?
**Tags:** #hidden-markov-models #dbscan #cnns #object-detection #evaluation-metrics #data-integration #compliance

## The Problem
A distribution firm under NAICS 541870 sells a pizza chain, a roofer or a political campaign a set of neighbourhoods at a price per door, then sends crews of part-time walkers to hang pieces on doorknobs — not in mailboxes, which federal law reserves for stamped mail. Walkers are paid per piece or per route, often in cash or through a gig app, and the commonest failure is invisible at the time: a bundle dumped in a dumpster, a cul-de-sac skipped, an apartment complex where the walker couldn't get past the gate.

Clients discover the failure weeks later when response collapses on one route, and by then the firm cannot prove what happened. Many firms now equip walkers with phone GPS and require periodic photos, and send the client a map of dots. The map shows the walker moved through the area; it doesn't show which doors were covered, which were legitimately excluded (no-solicitation signs, gated entries, HOA rules) and which were missed.

## What Already Exists
Field-service and workforce GPS apps (generic fleet and mobile-workforce tracking), purpose-built walker apps such as FlyerBuddy, and distributors' own tracking portals advertised by national networks like FlyerNation USA and GPS Flyers. USPS's EDDM tools show carrier-route household counts for saturation mail, and parcel and address datasets give door locations.

## The Customisation Gap
Distribution needs a coverage model the generic trackers lack: GPS traces map-matched to street segments and address points, so a pass along a street counts the doors on the walked side only; route plans built from carrier-route or parcel geography with each door's expected placement; exclusion layers for gated communities, multi-unit buildings without door access, posted no-solicitation and local handbill ordinances; dwell-time and pace checks that flag "walking" at driving speed or long stops at a dumpster; and photo checks that confirm a hanger on a door rather than a pile on a lawn. The client report must state coverage as doors reached, doors legitimately excluded and doors missed, by street.

## Impact If Solved
A coverage-verified route report turns the distributor's weakest point — trust — into the thing it sells, lets crew leaders re-walk gaps the same day rather than refunding a route after a complaint, and gives clients a basis for comparing door-to-door with EDDM saturation mail on equal terms.
