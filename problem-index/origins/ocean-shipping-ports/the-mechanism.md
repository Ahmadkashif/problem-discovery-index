# The Mechanism: What Standardisation Actually Made Computable

**Origin:** [[origins/ocean-shipping-ports/profile|Ocean Shipping & Ports]]
**Tags:** #data-integration #workflow-orchestration #automation #compliance #optimization-fundamentals #combinatorics-and-counting #graph-theory

> This file is the odd one out in the series, on purpose. There is no algorithm to walk through from 1956 — the mechanism here is a unit of measurement, and what it unlocked took decades to arrive. Read it as a lesson in sequencing: what has to become true before a data problem is even representable.

## The Problem With Loose Cargo, As a Data Problem

Before the container, a ship's cargo was a list of descriptions: 40 sacks of coffee, 12 crates of machine parts, 6 barrels of oil, each a different size, weight and shape, loaded wherever it would physically fit. **That list cannot be joined to anything.** It has no stable unit, no consistent identifier, and no guarantee that "12 crates of machine parts" means the same thing on two different manifests. A computer in 1956 could not have done anything useful with break-bulk cargo data even if one had been pointed at the problem, because the cargo itself was not yet expressed as data — it was expressed as prose.

## What the Container Actually Changed

The container's contribution was not computational. It was definitional: it converted cargo into a **fixed-size, stackable, uniquely identifiable unit**, agreed internationally under ISO/R 668 by 1968. That single change made several downstream problems representable as data for the first time:

**1. The container got an identity.** A box of a known, standard size can be given a number, looked up, tracked, and reconciled against a manifest — the precondition for everything now called supply-chain visibility.

**2. Loading became a combinatorial optimisation problem instead of a craft.** Deciding which container goes in which slot on which ship — to keep the vessel balanced, to avoid burying a container needed at an earlier port beneath one bound for a later port — is a structured **stowage-planning problem**: a discrete, countable set of identical-shaped units arranged against real constraints, fundamentally different from packing an unbounded variety of sacks and crates by eye, and eventually handed to an optimisation routine rather than a foreman's judgement.

**3. Routing became a network problem.** Once cargo moves in standard units between a fixed set of ports, the shipping network itself becomes a graph — ports as nodes, sailings as edges — reasoned about for cost and transit time, rather than point-to-point trade routes each priced on its own history.

**4. The paperwork became standardisable, and later electronic.** A bill of lading describing "12 crates of machine parts, condition unclear" cannot be machine-validated. A manifest listing standard container numbers against a fixed schema can be — the precondition later industries built electronic data interchange (EDI) and customs pre-clearance on top of.

## Why This Took Decades, Not Years

None of the above arrived in 1956, or even by 1968. Container-tracking systems, computerised stowage planning, and EDI-based customs filing are largely developments of the 1970s through 1990s, built by shipping lines, terminal operators and customs authorities **on top of** the standard, once it existed. The container is infrastructure the way SABRE's inventory system was infrastructure for airlines — necessary, and not itself the weapon; see [[origins/airlines/origin-story|Airlines' Origin Story]] for the direct parallel.

## The Trade-Offs Taken

Flexibility was traded for standardisation: a shipper with an oddly-shaped or oversized load no longer fits the system built for everyone else, and pays a premium or finds another mode. Local optimisation was traded for global interoperability — no single port or carrier chose the container dimensions best suited to its own equipment; everyone accepted a compromise size (agreed 1961–63, published 1968) in exchange for a box that worked everywhere. And the workforce that made loose cargo possible was traded for the workforce that makes standard cargo possible — see [[origins/ocean-shipping-ports/the-fight|The Fight]] for how that trade was priced.

## The Transferable Pattern

> **A data problem often cannot be solved, or even properly stated, until the thing being measured is first standardised into a discrete, identical, addressable unit. The standardisation is frequently the harder and more valuable achievement — and it usually looks like paperwork, not engineering, while it is happening.**

An FDE meeting an industry that still describes its core asset in free text — a "job," a "case," a "load," a "unit" with no fixed definition — is meeting an industry that has not yet had its container moment, and the opportunity is very often in defining the unit before touching the model.

**Sources:** Marc Levinson, *The Box* (2006, rev. 2016); ISO history of TC 104 and ISO/R 668 (1968); Port Authority of New York and New Jersey, *Our Port — History*; transportgeography.org, container-port and stowage-planning background.
