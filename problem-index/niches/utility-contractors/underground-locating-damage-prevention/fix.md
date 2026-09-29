# The Locator Knows the Map Is Wrong and Tells Nobody

**Niche:** [[niches/utility-contractors/underground-locating-damage-prevention/profile|Underground Utility Locating & Damage Prevention]]
**Industry:** [[industries/utility-contractors|Utility Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** A technician traces a line, finds it three metres from where the records put it, marks the ground correctly, and closes the ticket.
**Tags:** #tacit-knowledge-ml #data-integration #evaluation-metrics #automation #worker-facing

## The Problem
The locator's job is to find what is actually buried, not what the records say is buried. Every day, on a large fraction of tickets, those differ: a line is offset from its mapped position, deeper or shallower than recorded, made of a different material, or present when the map shows nothing at all.

The technician resolves it in the field. They trace the line electromagnetically, mark where it really is, and complete the ticket. The mark on the ground is correct, the excavation is safe, and the discrepancy — the fact that the record was wrong at this location, by this much, in this way — is not recorded anywhere that reaches the map.

Multiply by hundreds of millions of tickets a year and this is the largest continuously generated map-correction dataset imaginable, discarded at the moment of creation.

The consequences compound. The same wrong record misleads the next screen and the next locator. Screening buffers stay generous because nobody can say where the maps are reliable. Facility operators run expensive periodic records improvement programmes to learn what their locators established years ago. And when a damage does occur on an unmarked facility, the investigation discovers a records error that the field had already encountered.

The same loss applies to the technician's own knowledge. Experienced locators know which corridors are congested, which records vintages cannot be trusted, and which signals in a particular area mean something unusual. It stays with them.

## Why It's Still Broken
The contract is per ticket. A locating contractor is paid to mark and to respond on time, and time spent documenting a discrepancy is unpaid and slows the next job.

The parties are misaligned. The correction benefits the facility operator, who owns the map; the effort falls on the contractor's technician. Nothing in the commercial arrangement transfers value between them.

The capture tools are also poor. Recording a positional correction properly means capturing a measured position, a depth, a material and a confidence, on a phone, in the rain, on a shoulder. Anything that takes more than a few seconds will not be used.

And there is a quiet liability concern: a documented record that an operator was told its map was wrong, on a date, creates an obligation if nothing was done.

## What a Fix Looks Like
**Make discrepancy capture a two-second action.** A single control that says "found here, not there", capturing position and depth automatically from the locating equipment or the device. Anything more elaborate will be skipped.

**Instrument the equipment rather than the technician.** Modern locating receivers can record position and depth as the line is traced. Capturing that stream, rather than asking for manual entry, turns every trace into a survey at no marginal effort.

**Route corrections into records improvement with priority.** Discrepancies in congested corridors, on high-consequence facilities, or with large offsets are worth more than the rest and should be triaged, not queued.

**Compute per-area records confidence and publish it internally.** A map of where the maps are wrong is the most valuable derived asset in this business, and it falls out of the correction stream. It should feed screening buffers and ticket risk scoring directly.

**Pay for it.** The clean solution to the misalignment is commercial: facility operators pay for verified corrections, which is far cheaper than a records improvement programme and far cheaper than a damage. Someone has to price it.

**Capture the technician's judgment too.** A short structured note on unusual conditions — congestion, interference, unmarked facilities encountered — is the tacit layer, and it is the part that currently retires with the locator.

## Who Feels the Pain
Facility operators, whose maps stay wrong in places their own contractors have already corrected; locators, who rediscover the same discrepancy repeatedly and are paid to say nothing about it; excavators, who receive marks based on records nobody can characterise; and everyone living near a line whose recorded position is wrong.

## Impact If Fixed
Records accuracy is the root cause behind a large share of excavation damages, and the correction data is being generated continuously and thrown away. Capturing it turns every locate into a survey, feeds the screening and risk models above it, and replaces periodic records improvement programmes with a continuous one paid for by the party that benefits.
