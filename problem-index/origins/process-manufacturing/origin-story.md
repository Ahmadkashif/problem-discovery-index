# Origin Story: The Data Hiway and the Fluid Catalytic Cracker

**Origin:** [[origins/process-manufacturing/profile|Process Manufacturing]]
**Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]]

## What Was True Before

A process plant before the mid-1970s was run from a **centralised panelboard** — a wall of analog gauges and pneumatic controllers, each wired or piped back to a single sensor and a single control valve, all converging on one control room. It worked, and it had a structural weakness: a fault in the central system, or simply the accumulating complexity of controlling more loops than one panel could sensibly display, threatened the whole unit at once.

Separately, controlling a process **well**, as opposed to merely stably, was limited by what a human operator or a single-loop analog controller could react to. Analog control reacted to what the process was doing right now. It could not look ahead.

## What They Built: Two Separate Inventions That Later Merged

**The platform.** Honeywell proposed the idea internally in 1969, filed the patent on **3 February 1975**, and publicly announced the **TDC 2000** on **11 November 1975** (granted January 1977). TDC 2000 was the first commercial **Distributed Control System** — control logic moved off the single panelboard and onto microprocessor-based modules connected by a proprietary network Honeywell called the "Data Hiway." A single module's failure no longer took down the whole unit, and — for the first time in a commercial product — direct digital control happened at the field level rather than as a supervisory layer bolted onto analog hardware.

**The algorithm.** **Charlie Cutler** joined Shell Oil in 1961. His **1967** doctoral dissertation formed the mathematical basis of what became **Dynamic Matrix Control (DMC)** — using a **step-response model** of the process to predict its future trajectory and compute the sequence of moves that optimises a performance objective over a horizon, not just the next instant. Cutler demonstrated it on a fluid catalytic cracking unit at Shell's **New Orleans refinery around 1973**, and it became Shell's standard advanced-control method through the late 1970s and early 1980s. He commercialised it through **DMC Corporation, founded in 1984**, sold to **AspenTech in 1996**.

## Why It Mattered, Together

Neither invention alone was the whole story. The DCS gave the plant a distributed, addressable, digital control platform. DMC gave that platform something worth running on it: a way to look ahead, using a model, rather than merely react. **The platform arrived in 1975. The algorithm that fully exploited it commercially had been demonstrated two years earlier at Shell and took another decade to become an industry-standard product** — the same infrastructure-before-weapon gap this series has already traced through SABRE-to-DINAMO and TOPS-to-PSR, in a third industry, on a different timescale.

## The Honest Correction

**Crediting DMC's invention solely to Shell and Cutler is the standard telling, and it is not the complete one.** Concurrent, independent work on model-predictive-control-family methods — model algorithmic control, IDCOM — was happening elsewhere in the same period. Cutler and Shell earned primacy for the dominant, commercially propagated version of the idea, not for sole invention of the underlying concept.

**Sources:** Honeywell corporate history and US patent records, TDC 2000 (filed Feb 3 1975, announced Nov 11 1975, granted Jan 1977); AspenTech corporate history, Charlie Cutler and DMC Corporation (founded 1984, acquired 1996); process-control industry accounts of Dynamic Matrix Control's demonstration at Shell's New Orleans refinery, c.1973; process-control literature noting the contemporaneous development of model algorithmic control and IDCOM.
