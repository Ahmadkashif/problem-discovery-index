# Fingerprints for the Formats Nobody Fingerprinted

**Niche:** [[niches/digital-goods-marketplaces/asset-fingerprinting-at-scale/profile|Asset Fingerprinting at Web Scale]]
**Industry:** [[industries/digital-goods-marketplaces|Digital Goods Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Fingerprinting is mature for music and video and absent for templates, fonts and design assets, which is why enforcement in this category has nothing to act on.
**Tags:** #contrastive-learning #transformers #graph-theory #evaluation-metrics #confidence-intervals #dimensionality-reduction #automation #transfer-learning
**Contested on:** Every serious competitor in this niche is fighting to recognise a modified copy of a template, font or plugin anywhere on the web — and whoever can do that for asset types nobody has fingerprinted makes enforcement possible at all.

## The Problem
A template is copied, opened, recoloured, re-exported to a different format, and posted. A font is subsetted to the characters someone needs and renamed. A plugin is decompiled, renamed and rebundled. None of these survive a file hash, and none are recognisable to perceptual image hashing, which sees only a preview picture and not the structure underneath. Every fingerprinting system that works well was built for audio and video streams, where the medium is a signal. These assets are structured documents, and nobody has built the equivalent for them — which is why the entire enforcement layer in this category rests on creators finding copies by hand.

## Why Nobody Has Built This
The commercially motivated fingerprinting investment went where the piracy losses were largest and most concentrated, which was music and film. Each asset type here needs its own structural treatment, so there is no single general solution and the work looks unrewarding. The rights holders are small and individually cannot fund it. And platforms have treated detection as a creator's problem, which removes the party best placed to build it.

## What to Build
Build structural fingerprints per asset family. Fingerprint the asset's structure rather than its rendered appearance — layer trees, style definitions, component hierarchies, glyph outlines and metrics, node graphs, parameter sets — which is what survives re-export and recolouring and is the central technical insight the category is missing. Design explicitly for the transformations that actually occur, since surviving a format conversion and a palette change is the requirement and generic similarity does not meet it. Support partial matching, because reuse of a portion within a larger work is the common case and whole-file matching misses most of it. Build an index that supports web-scale querying at acceptable cost, as detection that cannot be run continuously is a research result rather than a capability. Crawl where the material actually appears — aggregation sites, forums, file lockers, messaging channels and marketplaces — which is a coverage problem as much as a matching one. Embed per-purchase identifiers so a recovered copy can be traced to the buyer account that leaked it, which is the highest-leverage deterrent available and requires the delivery pipeline to participate. Calibrate false positives tightly, since an automated notice against innocent work is far more damaging than a missed copy and is what would discredit the whole system. Handle legitimate derivative use, because a licensed buyer's work will contain the asset and must not be flagged — this is where licence data makes detection usable. Share fingerprints across marketplaces, since the same works are sold in several places and the index is more valuable pooled. And report coverage and recall honestly, as an enforcement capability that never states its detection rate cannot be trusted by the creators depending on it.

## Target Customer
Digital goods marketplaces, creator collectives funding enforcement, anti-piracy vendors, and the creative tool vendors whose formats these are.

## Impact If Built
Fingerprinting went where the concentrated losses were and left structured creative formats untouched, which is why enforcement here rests on manual searching. Fingerprinting layer trees, glyph outlines and node graphs is what survives re-export, and per-purchase identifiers make a recovered copy traceable.
