# Service History That Tells the Tech What Failed Last Time

**Niche:** [[niches/industrial-distributors/equipment-service-technicians/profile|Equipment Service Technicians at Pump, Compressor & Lift-Truck Dealers]]
**Industry:** [[industries/industrial-distributors|Industrial Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A senior compressor technician hears the symptom on the phone and knows the likely cause; a junior drives out to find it, without the part.
**Tags:** #tacit-knowledge-ml #large-language-models #gradient-boosting #naive-bayes #evaluation-metrics #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to fix a down pump, compressor or lift truck on the first visit, and whoever sends the technician with the right diagnosis and the right parts already on the truck takes the account.

## The Problem
Dealer service records hold years of work orders: machine, symptom as reported, technician notes, parts used, labour hours. They are written in shorthand, mostly free text, and almost never searched. The diagnostic patterns — this model's unloader valve fails after this many hours, that symptom on that pump is almost always the mechanical seal — live with senior technicians.

## Why Nobody Has Built This
Service modules were built for billing, not learning. Notes are messy and inconsistent, and OEM diagnostic tools cover only the OEM's own newer equipment, while dealers service mixed fleets that include old machines.

## What to Build
A diagnostic assistant trained on the dealer's own work-order history: given the machine, hours and reported symptom, it ranks likely causes with the parts each would need, shows similar past jobs, and learns from every closed work order. Dispatchers use it on intake to load the truck; technicians use it on site.

## Target Customer
Service managers at compressor, pump and lift-truck dealers with ~10–100 field technicians (estimate).

## Impact If Built
Raising first-visit fix rates by even ~10 points (estimate) removes second trips, frees technician capacity in a trade that can't hire enough people, and lets juniors work like seniors sooner.
