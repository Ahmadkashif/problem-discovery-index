# The Merchant Who Was Never Warned

**Niche:** [[niches/print-on-demand-platforms/print-outcome-prediction/profile|Print Outcome Prediction]]
**Industry:** [[industries/print-on-demand-platforms|Print on Demand Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A merchant uploads artwork that will not print well, the platform accepts it, sells it for months, and the merchant learns about the problem through customer complaints and refunds.
**Tags:** #evaluation-metrics #worker-facing #confidence-intervals #revenue-impact #automation #descriptive-statistics #quick-win #cnns
**Contested on:** Every serious competitor in this niche is fighting to know before printing whether this artwork on this product at this facility will come out acceptably — and whoever does that takes the margin, because reprints and refunds are the margin and they are almost entirely predictable.

## The Problem
A merchant uploads a design and lists it across eleven products. The design has a subtle gradient that bands badly in direct-to-garment printing and text at a size that fills in on textured fabric. The platform accepts the upload, generates attractive mockups, and lists it. Over four months it sells two hundred times, generates thirty complaints, eighteen reprints and eleven refunds, and damages the merchant's store rating. The merchant never knew there was a problem with the file, could have fixed it in ten minutes at upload, and discovered it through a pattern in their support inbox.

## Why It's Still Broken
Warning a merchant at upload introduces friction into the moment the platform most wants to be frictionless, and the platform's growth metrics are designs uploaded and products listed. The mockup generator renders the design as an image, which looks fine, and nothing renders what the print will look like. The reprint cost is shared in a way that makes it nobody's clear loss. And the merchant, who would fix it instantly, is never told.

## What a Fix Looks Like
Tell the merchant at upload, specifically. Show the predicted issues at the moment of upload with the specific problem named — this gradient will band on this fabric, this text will fill in below this size — which is actionable where a risk score is not and which the merchant will act on because it is their revenue too. Show a predicted print appearance alongside the flattering mockup, since the mockup is the reason the merchant believes the design is fine and an honest preview is the most persuasive artefact available. Rank the warnings by expected impact, so a merchant fixes the one that matters. Offer the correction automatically where it is mechanical — raise the text size, adjust the colours into gamut, reposition away from a seam — with the merchant approving. Recommend which products the design will work on and which it will not, since the same file is fine on one substrate and poor on another and the merchant lists it everywhere by default. Warn on existing listings retrospectively, since the back catalogue contains the same problems and a one-time sweep is cheap. Report a design's realised complaint and reprint rate back to the merchant, so the feedback exists even where the prediction failed. And measure the merchant's fix rate, because a warning nobody acts on is a design problem in the warning.

## Who Feels the Pain
Merchants whose store ratings are damaged by a file they would have fixed; customers receiving poor prints; and platforms absorbing reprints for a problem they could have flagged at upload.

## Impact If Fixed
The merchant would fix the file in ten minutes and is never told, and the mockup is why they believe it is fine. An honest predicted-print preview alongside the mockup is the most persuasive artefact available, and a retrospective sweep of the back catalogue is cheap.
