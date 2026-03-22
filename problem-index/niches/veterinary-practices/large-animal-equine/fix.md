# Farm Call Invoicing Automation

**Niche:** [[niches/veterinary-practices/large-animal-equine/profile|Large Animal & Equine]]
**Industry:** [[industries/veterinary-practices|Veterinary Practices]]
**Type:** Fix (Pain Point)
**One-liner:** Farm call invoices involve travel fees calculated by mileage, after-hours premiums, multi-animal procedure bundles, and herd discounts — all manually calculated because no PMS supports ambulatory billing logic, resulting in $15K-30K/year in unbilled or underbilled services per practice.
**Tags:** #feature-engineering #automation #revenue-impact #worker-facing

## The Problem
A single farm call invoice for a large animal vet can include: a trip charge based on round-trip mileage ($2-4/mile), an after-hours or emergency premium (1.5-2x base fees), procedures performed on 3-12 individual animals (each with different charges), drugs dispensed from the truck pharmacy (marked up from wholesale), and optional herd health discounts for farms on annual wellness programs. Assembling this invoice requires the vet to remember every animal seen, every procedure performed, every drug administered, the exact mileage driven, and whether the call fell outside normal hours. Most vets scribble notes on paper during the call and reconstruct the invoice that evening or the next morning. Items are routinely forgotten: the sedation given to horse #3, the extra banamine left with the barn manager, the 15 miles of detour for a road closure. Industry estimates suggest large animal vets underbill by 10-20% on farm calls simply due to incomplete recall.

## Why It's Still Broken
PMS invoicing modules are designed for in-clinic visits where a receptionist enters charges in real time as the vet completes each procedure. In ambulatory practice, there is no receptionist — the vet is alone in the field, often with gloved hands, and cannot stop to enter charges between procedures. By the time invoicing happens (hours later), details are lost. Existing PMS platforms have no concept of mileage-based travel fees, after-hours multipliers, or multi-animal visit structures — these are all entered as manual line items or custom invoice templates that the vet must assemble from scratch for every call.

## What a Fix Looks Like
A mobile invoicing tool (standalone or PMS-integrated) that: (1) auto-calculates travel fees using GPS-tracked mileage from the practice to the farm and back, (2) lets the vet tap procedures and drugs on their phone as they work through each animal — building the invoice in real time rather than from memory, (3) auto-applies after-hours premiums based on the time of the call, (4) supports multi-animal visit structures with per-animal line items and shared call fees, (5) applies herd health contract discounts automatically for enrolled farms, and (6) generates a client-ready invoice on-site for immediate payment or email delivery. The key design requirement is speed — adding a procedure to the invoice must take under 5 seconds on a phone with one hand.

## Who Feels the Pain
The large animal vet who spends 30-60 minutes every evening reconstructing invoices from memory and handwritten notes, and the practice owner who loses $15K-30K/year in services that were performed but never billed.

## Impact If Fixed
Recovers 10-20% of currently unbilled farm call revenue ($15K-30K/year for a typical large animal practice). Eliminates the nightly 30-60 minute invoice reconstruction ritual, giving the vet that time back for rest or family. Reduces billing disputes with farm clients by providing itemized, GPS-verified invoices delivered at the time of service.
