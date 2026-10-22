# Photo-to-Fix-List for a Card Fixture

**Niche:** [[niches/greeting-card-publishers/the-card-merchandiser/profile|The Card Department Merchandiser]]
**Industry:** [[industries/greeting-card-publishers|Greeting Card Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A merchandiser spends most of a visit finding what is wrong with a fixture; a photo of each section could tell her in seconds, card by card.
**Tags:** #cnns #object-detection #transfer-learning #contrastive-learning #evaluation-metrics #worker-facing #automation
**Contested on:** Every serious competitor in this niche is fighting to keep every pocket full, correctly filed and on season with the fewest paid merchandiser hours per store, and whoever gives the merchandiser the fastest way to see and fix what is wrong with a fixture keeps the service contract.

## The Problem
A card fixture section holds dozens of pockets, each meant to hold one design. Shoppers misfile cards constantly, pockets empty unevenly, and off-season cards linger. The merchandiser checks each pocket against a planogram by eye, card by card, and is paid per assignment however long it takes.

## Why Nobody Has Built This
Shelf recognition vendors built their models for packaged goods with distinctive packaging and barcodes facing out. Card faces are partly hidden in pockets, many designs look alike, and the catalogue changes every season. The buyers, a few publishers and their merchandising services, are a small market.

## What to Build
An on-phone model that detects each visible card and pocket tag in a section photo, identifies each card against the publisher's design catalogue using image embeddings trained to match partial card faces, compares to the current planogram, and returns a fix list: misfiled cards and where they belong, empty and low pockets, off-season cards, wrong designs. It drafts the reorder and logs the visit with before-and-after photos.

## Target Customer
VPs of field operations at card publishers and the third-party merchandising services that maintain card departments under contract.

## Impact If Built
Visits that are shorter for the same or better fixture condition (estimate: an hour or more saved per store per week at high-volume stores), with proof of work the merchandiser no longer has to argue about.
