# The Optic That Won't Come Up on Install Day

**Niche:** [[niches/it-value-added-resellers/complex-bom-configuration/profile|Complex BOM Configuration & Site Fit]]
**Industry:** [[industries/it-value-added-resellers|IT Distributors & Value-Added Resellers]]
**Type:** Fix (Pain Point)
**One-liner:** The most common install-day failure is a transceiver valid in the configurator and wrong for the customer's existing switches, and the reseller relearns it deal by deal.
**Tags:** #k-nearest-neighbors #feature-engineering #worker-facing #quick-win #data-integration
**Contested on:** Every serious competitor in this niche is fighting to send solution quotes whose bills of materials install as quoted at the customer's site, and whoever ships the lowest share of quoted lines needing a post-order change order or return takes the account.

## The Problem
Optics and cables are low-value lines on a high-value quote. A wrong speed, reach, connector or platform coding means links that won't come up, a field engineer waiting for replacements and an install that slips a week.

## Why It's Still Broken
Configurators validate optics against the new hardware, not against what sits at the other end of the cable. The reseller's record of which optics worked on which customer's core is a field engineer's notebook.

## What a Fix Looks Like
A per-customer list of the optics and cable types already in use, built from past orders and install notes, checked against every new BOM's transceiver lines; a flag when a quote's optics differ from what the far end accepts; and a short rule list maintained by the field team.

## Who Feels the Pain
Field engineers on site; pre-sales engineers who get the call; customers whose maintenance windows are wasted.

## Impact If Fixed
A single targeted check on transceiver lines could remove a large share of install-day slips (estimate: a few repeat visits a month at a mid-sized reseller, ~$1,000–3,000 each).
