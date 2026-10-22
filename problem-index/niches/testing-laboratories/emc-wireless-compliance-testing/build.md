# Diagnosing a Failing Emissions Scan

**Niche:** [[niches/testing-laboratories/emc-wireless-compliance-testing/profile|EMC & Wireless Compliance Testing]]
**Industry:** [[industries/testing-laboratories|Testing Laboratories]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A senior EMC engineer looks at a failing radiated emissions plot and says "that's the switching regulator's harmonics coupling onto the USB cable" — a read nobody has written down, and the one that decides whether the client passes this week.
**Tags:** #tacit-knowledge-ml #cnns #gradient-boosting #k-nearest-neighbors #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this sub-niche is fighting to get a product through emissions, immunity and radio testing on the first chamber booking, and whoever turns a failing scan into a diagnosed fix fastest — in a lab the FCC still recognises — wins the launch.

## The Problem
When a product fails radiated or conducted emissions, the chamber booking turns into a debugging session. The experienced engineer reads the spectrum — the spacing of peaks, their bandwidth, whether they move with cable position or operating mode — and links it to a likely source: a clock harmonic, a switching power supply, a display interface, a poorly bonded shield. Juniors cannot, and the client's own engineers often cannot either. The difference between a two-hour fix and a two-week redesign is frequently this read.

## Why Nobody Has Built This
The labelled history is scattered: scans are saved, but what the engineer concluded, what fix was applied and whether the retest passed live in notes and emails. Each product is different, and engineers disagree on borderline causes. Any tool has to answer while the product is still in the chamber.

## What to Build
A diagnosis assistant trained on the lab's archive of failing scans paired with the confirmed cause and fix: it reads a new scan with the product's description (clock frequencies, power topology, interfaces, cable set), proposes ranked likely sources with similar past cases, and suggests the next diagnostic step. Engineers tag cause and fix in one click after each retest, which grows the archive.

## Target Customer
EMC lab managers who sell pre-compliance and debugging time; large manufacturers' in-house EMC labs.

## Impact If Built
Faster diagnosis converts failed bookings into passed retests sooner, raises chamber throughput, and keeps the senior engineer's pattern library when they leave.
