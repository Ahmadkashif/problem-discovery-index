# Custom Plate and Die Inventory Tracking

**Niche:** [[niches/printing-shops/letterpress-specialty-printers/profile|Letterpress & Specialty Printers]]
**Industry:** [[industries/printing-shops|Printing Shops]]
**Type:** Fix (Pain Point)
**One-liner:** Studios accumulate hundreds of custom letterpress plates and foil stamping dies that are stored in drawers and boxes with handwritten labels — when a client reorders or wants a matching piece, finding the right plate takes 15-45 minutes of searching, and 5-10% of plates are never found, requiring expensive re-creation.
**Tags:** #automation #data-integration #worker-facing

## The Problem
Every letterpress or foil stamping job creates a physical plate or die that the studio retains for potential reorders (a client returning for thank-you cards that match their wedding invitations needs the same plates). Over years, a studio accumulates 500-2,000+ plates and dies, stored in labeled envelopes in file cabinets or boxes. The labeling is inconsistent (client name? job name? date?), and plates for the same client's multi-piece suite may be stored in different locations. When a reorder arrives, the studio owner searches physically through storage, trying to locate the correct plate. If the plate is not found (damaged, mislabeled, or lost in the accumulated inventory), it must be re-created at $15-50 per plate — a cost the studio usually absorbs rather than charging the client.

## Why It's Still Broken
The plates are physical objects with no digital twin. Cataloging them would require the studio owner to stop production and photograph/barcode every plate — a project that never rises above higher-priority production work. New plates are added weekly but catalog maintenance is deferred indefinitely. The problem grows worse over time as inventory accumulates.

## What a Fix Looks Like
A simple catalog system: when a new plate is created, the operator photographs it with their phone, tags it with client name, job description, and creation date, and assigns a physical storage location (drawer A3, slot 12). The image and metadata are stored in a searchable database. When a reorder arrives, the operator searches by client name or job description, sees the plate image and storage location, and retrieves it directly. A periodic audit prompt helps the studio retire old plates for clients who are unlikely to reorder (wedding clients after 2+ years).

## Who Feels the Pain
Studio owners who spend 15-45 minutes searching for plates during reorder processing. Production staff who cannot start a reorder job because the plate search is ongoing. Clients who are charged plate re-creation fees or experience delays because their original plate could not be found.

## Impact If Fixed
Plate retrieval time drops from 15-45 minutes to under 2 minutes. Plate re-creation costs ($15-50 per plate, 10-20 reorders per year) are largely eliminated, saving $300-1,000 annually. Reorder turnaround time improves by 1-2 days because plate search is no longer a bottleneck.
