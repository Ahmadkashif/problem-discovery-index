# The Parts Counter With Six Catalogs

**Industry:** [[powersports-and-boat-dealers|Powersports & Boat Dealers]]
**Type:** Worker Life Changing
**One-liner:** The parts associate turns "the water pump thing for my 2009 Yamaha 150" into the right current part number across several OEM and aftermarket catalogs, while the phone rings and a technician waits, and owns every wrong part that comes back.
**Tags:** #cnns #contrastive-learning #k-nearest-neighbors #transformers #worker-facing #automation #quick-win

## The Problem
A powersports or marine parts counter serves three customers at once: the walk-in with a broken part in a plastic bag, the caller who knows only the year and roughly the model, and the technician who needs a part now to finish a flat-rate job. Each OEM line has its own electronic parts catalog: exploded diagrams, reference numbers and superseded part numbers. A multi-line store may look up the same job in several places: the OEM's catalog for the outboard, another for the hull's hardware, an aftermarket distributor's catalog for a cheaper equivalent, and the store's own inventory in the DMS. Serial-number breaks change the part mid-model-year. Supersession chains replace one number with another, sometimes two.

The associate's skill is matching a vague description or a worn part to the right diagram and the right number. When it's wrong, the special-order part arrives a week later, the customer's boat sits, the technician's job stalls, and the part goes back with a restocking fee or into the obsolete bin.

## Why It Matters to the Worker
It is constant, interrupted lookup work with little credit when it goes right and blame when it doesn't. Experienced counter people carry the supersessions, the serial breaks and the cross-references in their heads ("that impeller kit changed in 2012", "the aftermarket one fits but the seal is different"). New hires take months to get there, and in spring there is no time to train them. The job's pay is modest; the stress is out of proportion to it.

## What a Solution Looks Like
One lookup across the catalogs the store carries. The associate photographs the old part or types the customer's description; the system identifies the part family from the image, matches it against diagrams for the customer's model and serial range, resolves supersessions to the current number, shows stock on hand and at the distributor, and flags a serial-break risk before ordering. For phone and web customers it asks the one question that disambiguates (serial number, engine model plate photo) instead of guessing. Dealer Spike's PartSmart and the OEM catalogs already hold the diagrams; what's missing is the matching across them and the memory of which lookups went wrong.

## Impact If Solved
If an associate handles ~40 lookups a day in season and a third of them involve more than one catalog (estimate), cutting lookup time from minutes to seconds and halving wrong-part orders gives back an hour or more a day, and spares the associate most of the returns they currently answer for.
