# Adaptation Rules Learned From a Studio's Archive

**Niche:** [[niches/graphic-design-studios/artwork-versioning-and-adaptation/profile|Artwork Versioning & Adaptation]]
**Industry:** [[industries/graphic-design-studios|Graphic Design Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A studio's archive holds thousands of master layouts next to the variants its production artists built by hand, and no tool learns how that studio adapts.
**Tags:** #transformers #autoregressive-models #optimization-fundamentals #automation #worker-facing #feature-engineering
**Contested on:** Every serious competitor in this niche is fighting to produce every size, language and channel variant from an approved master with no manual touch and no brand or legal-copy error, and whoever delivers the most compliant variants per hour takes the account.

## The Problem
Generic resizing tools scale and reposition elements by fixed rules and produce variants a production artist then rebuilds. Each studio, and each client's brand, adapts in characteristic ways — which element yields first in a narrow banner, where the headline breaks, when the product shot crops — and those habits are visible in years of past work but written down nowhere.

## Why Nobody Has Built This
Template-based automation requires the template to be built in the platform from the start; studios' archives are free-form Illustrator, InDesign, Photoshop and Figma files with inconsistent layer naming. Learning layout from those files needs element roles inferred from the layers, which only recently became practical.

## What to Build
Ingest the studio's archive of masters and hand-built variants, infer each element's role (logo, headline, body, legal, product, background), and learn the studio's adaptation preferences per client and format. For a new master, generate every variant as a proposal, with hard constraints — logo clear space and minimum size, legal copy present and legible, platform safe zones — enforced by a solver rather than learned. The production artist reviews a contact sheet and fixes exceptions.

## Target Customer
Studios and production houses doing campaign and retail adaptation for several brand clients.

## Impact If Built
Most variants arrive ready for review rather than built from scratch, production hours per launch fall several-fold (estimate), and the studio's adaptation quality becomes a repeatable asset rather than one artist's habit.
